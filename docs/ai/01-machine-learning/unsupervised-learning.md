---
layout: default
title: 군집분석
parent: 1. 기계학습
grand_parent: AI (인공지능)
nav_order: 16
---

<!-- CSV_APPLIED: 기술사_기본필수노트_AI - AI.csv | NO=2 | 중토픽=무감독학습 -->
# 군집분석
{: .fs-8 }

1.3 비지도학습
{: .label .label-green }

---

## 🎯 기술사 수준 설명

### 📌 핵심 암기 (Quick Reference)

{: .highlight }
> **무감독학습**: 입력값에 대한 목표치가 주어지지 않는 기계학습
> - 암기: `군축` `민디핸섬` `피카` `적간`
> - 키워드: `무감독학습` `Principal Component Analysis` `Generator`

---

<div class="exam-concept-block" markdown="1">

## 🧠 개념 영역

### 🔑 핵심 키워드 3개

| 키워드 | 설명 | 예시 |
|:--|:--|:--|
| **무감독학습** | 핵심 개념/대상 | - |
| **Principal Component Analysis** | 주요 기법/구성요소 | - |
| **Generator** | 절차/평가/특징 | - |

---

### 📖 등장배경

| 구분 | 내용 |
|:--|:--|
| **문제/필요성** | 입력값에 대한 목표치가 주어지지 않는 기계학습 |
| **활용/사례** | - |

---

### 📝 개념 정의

| 구분 | 정의 |
|:--|:--|
| **무감독학습** | 입력값에 대한 목표치가 주어지지 않는 기계학습 |

</div>

---

<div class="exam-tech-block" markdown="1">

## 🏗️ 기술 영역

### 구성요소

#### 그룹 1: 군집화
{: .highlight-purple }

| 항목 | 설명 |
|:--|:--|
| **Clustering** | - |
| **- K > means** | n개의 데이터를 K개의 군집으로 분류하기 위해 거리 기반 반복 계산 |
| **> 중심점이 변하지 않을때까지 계속 반복, K개수설정 > 초기중심점, 군집, 중심재설정, 재할당, 반복** | - |
| **- DBSCAN** | 중심이동, 밀도기반 군집화, 밀도 |
| **- EM Clustering** | 정규분포 기반 E > Step, M > Step 반복 군집화, 최적파라미터 찾기 |
| **- SOM** | 자기조직학습, 차원축소, 클러스터링 동시수행 |


</div>

---

<details markdown="1">
<summary><h3 style="display:inline">📖 상세 설명 (클릭해서 펼치기)</h3></summary>

#### 내용

- 입력값에 대한 목표치가 주어지지 않는 기계학습

#### 군집화

- Clustering
- - K > means: n개의 데이터를 K개의 군집으로 분류하기 위해 거리 기반 반복 계산
- > 중심점이 변하지 않을때까지 계속 반복, K개수설정 > 초기중심점, 군집, 중심재설정, 재할당, 반복
- - DBSCAN: 중심이동, 밀도기반 군집화, 밀도
- - EM Clustering: 정규분포 기반 E > Step, M > Step 반복 군집화, 최적파라미터 찾기
- - SOM: 자기조직학습, 차원축소, 클러스터링 동시수행

#### 차원축소

- Reduce Dimension
- - PCA(Principal Component Analysis): 주성분분석, 3차원 > 2차원
- - ICA(Independent Component Analysis) : 주어진 특징에서 새로운 특징 추출

#### 적대적학습

- - GAN: 생성자(Generator)와 판별자(Discriminator)가 서로 경쟁하는 과정을 통해 정보를 학습
- - DCGAN: Deep Convolutional GAN

</details>

---

<details markdown="1">
<summary><h3 style="display:inline">🗂️ 기존 내용 (백업)</h3></summary>

# 군집분석(Cluster Analysis)
{: .fs-8 }

1.3 비지도학습
{: .label .label-green }

---

## 핵심 키워드

`계층적 군집분석` `비계층적 군집분석` `중복 비계층적 군집분석`

---

## 정의/개념

개체 유사성 측정, 군집 개체 상이성, 계층, 비계층, 중복군집 비지도 학습 기법

---

## 유형

```
                    군 집 분 석
                        │
            ┌───────────┼───────────┐
            ↓           ↓           ↓
    군집대상의 중복여부   ?           ?
            │
    ┌───────┼───────┐
    ↓               ↓
   작음          제약없음
    │               │
 자료의 크기      자료의 크기
    │               │
┌───┴───┐       ┌───┴───┐
↓       ↓       ↓       ↓
계층적   비계층적  중복 비계층적
군집분석  군집분석    군집분석

최단 연결법    K-Means 알고리즘   프림(PRIM)
최장 연결법    DBSCAN 알고리즘
평균 연결법
Ward 연결법
```

---

## 알고리즘

| 유형 | 알고리즘 | 설명 |
|:-----|:---------|:-----|
| **계층적 군집분석** | 최단 연결법 | n*n 거리 행렬에서 거리가 가장 가까운 데이터를 묶어서 군집형성 |
| | 최장연결법 | 최단연결법과 같은 방법이나 거리가 먼 데이터나 군집을 묶어서 형성 |
| | 평균연결법 | 최단연결법으로 군집을 수행하는데 그 거리를 구하는 방식이 평균을 이용 |
| | Ward 연결법 | 군집 내 편차들의 제곱합을 최소화하는 방식으로 군집 수행 |
| **비계층적 군집분석** | K-Means 알고리즘 | K개의 중심값을 선정하고, 중심값과 다른 **데이터 간의 거리를 이용**하여 분류를 수행하는 비지도학습 |
| | DBSCAN 알고리즘 | 임의의 클러스터 중심을 이동, 중심으로부터 정해진 반경 거리 내에 최소 데이터 포인트 개수를 확인하여 **밀도 기반**으로 군집화를 수행하는 알고리즘 |
| **중복군집 분석** | 프림(PRIM) | Patient Rule Induction Method<br>규칙에 의한 군집화(Clustering)와 목적함수(object function) 값의 최적화를 동시에 실시하면서 오차를 최소화 시킬 알고리즘 |

> 군집분석의 경우 빅데이터 기반의 집단을 분류하는 용도로 사용되어 비계층적 군집분석을 주로 활용

---

## 연계 토픽

- [K-Means](/docs/ai/01-machine-learning/k-means)
- [DBSCAN](/docs/ai/01-machine-learning/dbscan)

---

## 학습 체크리스트

- [ ] 군집분석의 정의와 유형 이해
- [ ] 계층적 vs 비계층적 군집분석 차이점 파악
- [ ] 주요 알고리즘(K-Means, DBSCAN) 특징 암기


</details>

