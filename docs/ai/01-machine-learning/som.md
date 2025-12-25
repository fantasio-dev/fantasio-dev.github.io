---
layout: default
title: SOM
parent: 1. 기계학습
grand_parent: AI (인공지능)
nav_order: 20
---

<!-- CSV_APPLIED: 기술사_기본필수노트_AI - AI.csv | NO=21 | 중토픽=자기조직화지도 (Self-Organizing Map) -->
# SOM
{: .fs-8 }

1.3 비지도학습
{: .label .label-green }

---

## 🎯 기술사 수준 설명

### 📌 핵심 암기 (Quick Reference)

{: .highlight }
> **자기조직화지도 (Self-Organizing Map)**: 차원축소(dimensionality reduction)와 군집화(clustering)를 동시에 수행
> - 암기: `입가경노클` `거선수반`
> - 키워드: `자기조직화지도` `dimensionality reduction` `clustering`

---

<div class="exam-concept-block" markdown="1">

## 🧠 개념 영역

### 🔑 핵심 키워드 3개

| 키워드 | 설명 | 예시 |
|:--|:--|:--|
| **자기조직화지도** | 핵심 개념/대상 | - |
| **dimensionality reduction** | 주요 기법/구성요소 | - |
| **clustering** | 절차/평가/특징 | - |

---

### 📖 등장배경

| 구분 | 내용 |
|:--|:--|
| **문제/필요성** | 차원축소(dimensionality reduction)와 군집화(clustering)를 동시에 수행 |
| **활용/사례** | - |

---

### 📝 개념 정의

| 구분 | 정의 |
|:--|:--|
| **자기조직화지도 (Self-Organizing Map)** | 차원축소(dimensionality reduction)와 군집화(clustering)를 동시에 수행 |

</div>

---

<div class="exam-tech-block" markdown="1">

## 🏗️ 기술 영역

### 구성요소

#### 그룹 1: 구성요소
{: .highlight-purple }

| 항목 | 설명 |
|:--|:--|
| **입가경노클** | - |
| **> 입력층(input layer)** | 입력 벡터를 입력받는 층 |
| **> 가중치(weight)** | 입력 값의 연결강도 |
| **> 경쟁층(competitive layer)** | 가까운 거리 입력벡터 선택, 반복처리 |
| **> 노드(node)** | 경쟁층에서 입력 벡터 유사성에 의해 모이는 영역 |
| **> 클러스터링(clustering)** | 데이터의 유사성 기초 분류법 |


</div>

---

<details markdown="1">
<summary><h3 style="display:inline">📖 상세 설명 (클릭해서 펼치기)</h3></summary>

#### 내용

- 차원축소(dimensionality reduction)와 군집화(clustering)를 동시에 수행
- 대뇌피질의 시각피질의 학습 과정을 모델화한 인공신경망 알고리즘

#### 특징

- > 차원축소: Dimensionality Reduction
- > 군집화: Clustering
- > 승자독식: 반복을 통해서 입력 가중치와 유사한게 선택됨
- > 빠른속도: 전방으로 전달해서 즉시 분석, 실시간 학습 가능

#### 개념도

- 초기화, 입력, 가중치, 경쟁층, 노드, 출력층

#### 구성요소

- 입가경노클
- > 입력층(input layer): 입력 벡터를 입력받는 층
- > 가중치(weight): 입력 값의 연결강도
- > 경쟁층(competitive layer): 가까운 거리 입력벡터 선택, 반복처리
- > 노드(node): 경쟁층에서 입력 벡터 유사성에 의해 모이는 영역
- > 클러스터링(clustering): 데이터의 유사성 기초 분류법

#### 절차

- > 입력층: 연결강도 초기화
- > 경쟁층: 노드간거리계산 > 짧은노드선택 > 이웃간가중치수정 > 마지막벡터까지 반복
- > 확인: 마지막 벡터 > 최대회수 반복 > 학습률수정후 다시(노드간거리계산)

</details>

---

<details markdown="1">
<summary><h3 style="display:inline">🗂️ 기존 내용 (백업)</h3></summary>

# SOM(Self-Organizing Map)
{: .fs-8 }

1.3 비지도학습
{: .label .label-green }

---

## 핵심 키워드

`고차원 데이터` `저차원 격자 대응` `차원축소 군집화 동시 수행`

---

## 정의/개념

대뇌피질의 시각피질의 학습 과정을 모델화한 인공신경망으로써 자율 학습에 의한 클러스터링을 수행하는 알고리즘

---

## 개념도

```
    Input pattern    →    Cooperation    →    Adaption
   ┌─────────────┐      ┌─────────────┐    ┌─────────────┐
   │ ○ ○ ○ ○ ○  │      │   Time t₁   │    │   Winner    │
   │ ○ ○ ○ ○ ○  │  →   │   ───────   │ →  │   ───────   │
   │   Neurons   │      │   Time t₂   │    │  Neighbor   │
   └─────────────┘      └─────────────┘    └─────────────┘
   
   Competition         Cooperation          Adaption
```

---

## 프로세스/학습규칙

| # | 프로세스 | 핵심 |
|:--|:---------|:-----|
| 1 | 초기화 | 연결강도 초기화 |
| 2 | 입력 | 새로운 입력 벡터 입력 |
| 3 | 거리계산 | 입력 벡터와 모든 뉴런들간의 거리계산(Competition) |
| 4 | 출력 | 최소거리 있는 출력 뉴런 선택(Cooperation) |
| 5 | 가중치 조정 | 승자 뉴런과 이웃 뉴런 연결강도 조정(Adaption) |
| 6 | 반복 | 2단계 이동 반복 수행, 뉴런 변화 없을 시 종료 |

---

## 학습규칙

$$W_{new} = W_{old} + \alpha(X - W_{old})$$

- **W_new**: 조정된 후의 새로운 연결강도
- **W_old**: 조정되기 이전의 새로운 연결강도 벡터
- **α**: 학습률
- **X**: 입력패턴의 벡터

> 연결강도 벡터와 입력패턴의 차이에 일정한 비율을 곱하고 원래의 연결강도 벡터를 더하여 유사도를 조정함

---

## 연계 토픽

- [군집분석](/docs/ai/01-machine-learning/unsupervised-learning)
- [K-Means](/docs/ai/01-machine-learning/k-means)

---

## 학습 체크리스트

- [ ] SOM의 정의와 개념 이해
- [ ] 프로세스 6단계(초기화-입력-거리계산-출력-가중치조정-반복) 암기
- [ ] 학습규칙 수식 이해


</details>

