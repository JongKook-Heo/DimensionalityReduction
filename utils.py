import csv
from rdkit.Chem.Scaffolds.MurckoScaffold import MurckoScaffoldSmiles
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.DataStructs import TanimotoSimilarity

def read_pubchem_smiles(data_path: str):
    smiles_data = []
    with open(data_path) as f:
        csv_reader = csv.reader(f, delimiter=',')
        for idx, row in enumerate(csv_reader):
            smiles = row[-1]
            smiles_data.append(smiles)
    return smiles_data


def _generate_scaffold(smiles, include_chirality=False):
    mol = Chem.MolFromSmiles(smiles)
    scaffold = MurckoScaffoldSmiles(mol=mol, includeChirality=include_chirality)
    return scaffold


def generate_scaffolds(dataset, log_every_n=1000):
    scaffolds = {}
    data_len = len(dataset)
    print(f'Total Data Size {data_len}, about to generate scaffolds')
    for idx, smiles in enumerate(dataset):
        if idx % log_every_n == 0:
            print("Generating scaffold %d/%d"%(idx, data_len))
        scaffold = _generate_scaffold(smiles)
        if scaffold not in scaffolds:
            scaffolds[scaffold] = [idx]
        else:
            scaffolds[scaffold].append(idx)

    scaffolds = {k: sorted(v) for k, v in scaffolds.items()}
    scaffold_sets = [(s, s_set) for (s, s_set) in sorted(scaffolds.items(),
                                                         key=lambda x: (len(x[1]), x[1][0]), reverse=True)]
    return scaffold_sets

def molecular_distance(a: Chem.Mol, b:Chem.Mol, as_similarity=False):
    eps = 1e-4
    a, b = [AllChem.GetMorganFingerprint(Chem.AddHs(m), 2, useFeatures=True) for m in [a, b]]
    fp_similarity = TanimotoSimilarity(a, b)
    if as_similarity:
        return fp_similarity
    
    # distance = 1/(eps+fp_similarity)
    distance = 1- fp_similarity
    return distance