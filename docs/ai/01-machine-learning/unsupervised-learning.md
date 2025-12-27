---
layout: default
title: 비지도학습(Unsupervised Learning)
parent: 1. 기계학습
grand_parent: AI (인공지능)
nav_order: 10
---

# 비지도학습(Unsupervised Learning)
{: .fs-8 }

1.3 비지도학습
{: .label .label-green }

---

## 🎯 기술사 수준 설명

### 📌 핵심 암기 (Quick Reference)

{: .highlight }
> **비지도학습**: 입력값에 대한 목표치가 주어지지 않는 기계학습
> - (군집화) `케디이솜` K-means, DBSCAN, EM Clustering, SOM
> - (차원축소) `피아` PCA, ICA
> - (적대적학습) `갠디` GAN, DCGAN
> - ⭐ **차별점**: 레이블 유무 - 비지도학습은 정답(Label) 없음, 지도학습은 정답 존재

---

## 핵심 키워드

`군집화(Clustering)` `차원축소(Reduce Dimension)` `적대적학습` `K-means` `PCA` `GAN`

---

## 정의/개념

입력값에 대한 목표치가 주어지지 않는 기계학습

---

## 개념도

```
비지도학습 (Unsupervised Learning)
├── 군집화 (Clustering)
│   ├── K-means: 거리 기반 반복 계산
│   ├── DBSCAN: 밀도 기반 군집화
│   ├── EM Clustering: 정규분포 기반
│   └── SOM: 자기조직학습
├── 차원축소 (Reduce Dimension)
│   ├── PCA: 주성분분석
│   └── ICA: 독립 성분 분석
└── 적대적학습
    ├── GAN: 생성자-판별자 경쟁
    └── DCGAN: Deep Convolutional GAN
```

---

## 구성요소 `군차적` / `케디이솜` / `피아` / `갠디`

### 그룹 1: 군집화(Clustering) `케디이솜`
{: .highlight-purple }

| 암기 | 항목 | 설명 |
|:-----|:-----|:-----|
| **케** | K-means | n개의 데이터를 K개의 군집으로 분류하기 위해 거리 기반 반복 계산<br>중심점이 변하지 않을때까지 계속 반복 |
| **디** | DBSCAN | 중심이동, 밀도기반 군집화 |
| **이** | EM Clustering | 정규분포 기반 E-Step, M-Step 반복 군집화, 최적파라미터 찾기 |
| **솜** | SOM | 자기조직학습, 차원축소, 클러스터링 동시수행 |

### 그룹 2: 차원축소(Reduce Dimension) `피아`
{: .highlight-purple }

| 암기 | 항목 | 설명 |
|:-----|:-----|:-----|
| **피** | PCA(Principal Component Analysis) | 주성분분석, 3차원 → 2차원 |
| **아** | ICA(Independent Component Analysis) | 주어진 특징에서 새로운 특징 추출 |

### 그룹 3: 적대적학습 `갠디`
{: .highlight-purple }

| 암기 | 항목 | 설명 |
|:-----|:-----|:-----|
| **갠** | GAN | 생성자(Generator)와 판별자(Discriminator)가 서로 경쟁하는 과정을 통해 정보를 학습 |
| **디** | DCGAN | Deep Convolutional GAN |

---

## 연계 토픽

- [K-Means]({{ site.baseurl }}/docs/ai/01-machine-learning/k-means)
- [DBSCAN]({{ site.baseurl }}/docs/ai/01-machine-learning/dbscan)
- [PCA]({{ site.baseurl }}/docs/ai/01-machine-learning/pca)
- [SOM]({{ site.baseurl }}/docs/ai/01-machine-learning/som)
- [GAN]({{ site.baseurl }}/docs/ai/01-machine-learning/gan)

---

## 학습 체크리스트

- [ ] 비지도학습 정의 암기
- [ ] `케디이솜` 군집화 알고리즘 4개 설명
- [ ] `피아` 차원축소 알고리즘 2개 설명
- [ ] `갠디` 적대적학습 2개 설명
