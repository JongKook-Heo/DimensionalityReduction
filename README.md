# DimensionalityReduction with Molecules
__2021020636 허종국__

특정한 화학 분자의 용해도, 전기 음성도, 혈관장벽 투과도 등의 물성을 예측하는 것을 __물성예측__ 이라고 합니다. 물성 예측은 신약 개발, 반응 예측 등 다양한 화학 정보학 분야의 태스크에 앞서 가장 먼저 해결해야될 태스크입니다. 화학 분자의 물성은 화학 분자가 가지고 있는 특정한 구조인 __작용기(functional group)__ 나 __스캐폴드(Scaffold)__ 에 의해 결정됩니다. 이번 튜토리얼에서는 rdkit 패키지를 통해 화학 분자를 시각화하고 MDS와 ISOMAP을 활용하여 공통된 Scaffold를 가진 분자들이 어떻게 매핑되는지 알아보겠습니다.

## Table of Contents:
- [Requirements](#requirements)
- [Download Data](#download-data)
- [Dimensionality Reduction Tutorial](#dimensionality-reduction-tutorial)
  * [Multi-Dimensional Scaling](#multi-dimensional-scaling)
  * [ISOMAP](#isomap)
- [References](#references)

# Requirements
rdkit 패키지는 python 3.8이상에서 작동하지 않습니다. 본 튜토리얼을 사용하기 적합한 가상환경을 올려두었으니 아래 명령어를 통해 환경을 구축해주시기 바랍니다.

```
conda env create --file environment.yaml
```

# Download Data
본 튜토리얼에서 사용하는 data는 PubChem에서 수집된 약 1000만개의 화학분자 데이터입니다. 데이터의 용량과 라이센스 문제로 __./data__ 라는 폴더를 생성한 후 해당 폴더에 [링크](https://drive.google.com/file/d/1aDtN6Qqddwwn2x612kWz9g0xQcuAtzDE/view)를 통해 데이터를 다운받으시길 바랍니다. 

# Dimensionality Reduction

## Multi Dimensional Scaling
MDS는 원본 좌표계의 위치 없이 유사도/거리만을 가지고 저차원의 좌표계를 찾을 때 사용됩니다. 본 튜토리얼에서는 분자를 일련의 문자열로 해싱하는 __MorganFingerPrint__ 를 통해 분자를 해싱하고, __Tanimoto Similarity__ 를 통해 분자의 유사도를 구하여 거리 행렬로 사용하였습니다.
- [CODE IMPLEMENTATION](https://github.com/JongKook-Heo/DimensionalityReduction/blob/main/1.Multi%20Dimensional%20Scaling.ipynb)

## ISOMAP
ISOMAP은 MDS와 달리 원본 좌표계가 필요합니다. 본 튜토리얼에서는 rdkit에서 제공하는 122개의 __Molecular Descriptor__ 를 활용하여 분자의 특징에 대한 DataFrame을 구축한 후, ISOMAP을 적용하였습니다.
- [CODE IMPLEMENTATION](https://github.com/JongKook-Heo/DimensionalityReduction/blob/main/2.ISOMAP.ipynb)

# References
## code
- MolCLR : https://github.com/yuyangw/MolCLR
## images
- https://github.com/pilsung-kang/Business-Analytics-IME654-
