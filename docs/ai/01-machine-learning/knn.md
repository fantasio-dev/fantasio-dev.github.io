---
layout: default
title: KNN
parent: 1. 기계학습
grand_parent: AI (인공지능)
nav_order: 13
---

<!-- CSV_APPLIED: 기술사_기본필수노트_AI - AI.csv | NO=17 | 중토픽=KNN (K-Nearest Neighbor) -->
# KNN
{: .fs-8 }

1.2 지도학습
{: .label .label-purple }

---

## 🎯 기술사 수준 설명

### 📌 핵심 암기 (Quick Reference)

{: .highlight }
> **KNN (K-Nearest Neighbor)**: Sample에 주어진 x에서 가장 가까운 k개의 원소가 많이 속하는 class로 x를 분류하는 비모수적 확률밀도 추정 방법
> - 암기: `다유게단` `핑캐라다` `유마코`
> - 키워드: `KNN` `거리` `Nearest Neighbors`

---

<div class="exam-concept-block" markdown="1">

## 🧠 개념 영역

### 🔑 핵심 키워드 3개

| 키워드 | 설명 | 예시 |
|:--|:--|:--|
| **KNN** | 핵심 개념/대상 | - |
| **거리** | 주요 기법/구성요소 | - |
| **Nearest Neighbors** | 절차/평가/특징 | - |

---

### 📖 등장배경

| 구분 | 내용 |
|:--|:--|
| **문제/필요성** | Sample에 주어진 x에서 가장 가까운 k개의 원소가 많이 속하는 class로 x를 분류하는 비모수적 확률밀도 추정 방법 |
| **활용/사례** | - |

---

### 📝 개념 정의

| 구분 | 정의 |
|:--|:--|
| **KNN (K-Nearest Neighbor)** | Sample에 주어진 x에서 가장 가까운 k개의 원소가 많이 속하는 class로 x를 분류하는 비모수적 확률밀도 추정 방법 |

</div>

---

<div class="exam-tech-block" markdown="1">

## 🏗️ 기술 영역

### 구성요소

#### 그룹 1: 특징
{: .highlight-purple }

| 항목 | 설명 |
|:--|:--|
| **다유게단개** | - |
| **> 최고인접 다수결** | 기존 데이터 중 가장 유사한 k개의 데이터를 측정하여 분류 |
| **> 유사도(거리)기반** | 유클리디안 거리, 마할라노비스의 거리, 코사인 유사도 활용 |
| **> Lazy Learning기법** | 새로운 입력 값이 들어온 후 분류시작, 모델만들지 않음. |
| **> 단순유연성** | 모형이 단순하며 파라미터의 가정이 거의 없음 |
| **> NN(Nearest Neighbors) 개선** | - |
| **> KNN은 가장 근접한 k개의 데이터에 대한 다수결 내지 가중합계 방식으로 분류** | - |
| **> 가장 유사한 Instance를 찾아서 그와 같은 class에 일방적으로 분류, 잡음 데이터 성능 구림** | - |


</div>

---

<details markdown="1">
<summary><h3 style="display:inline">📖 상세 설명 (클릭해서 펼치기)</h3></summary>

#### 내용

- Sample에 주어진 x에서 가장 가까운 k개의 원소가 많이 속하는 class로 x를 분류하는 비모수적 확률밀도 추정 방법

#### 특징

- 다유게단개
- > 최고인접 다수결: 기존 데이터 중 가장 유사한 k개의 데이터를 측정하여 분류
- > 유사도(거리)기반: 유클리디안 거리, 마할라노비스의 거리, 코사인 유사도 활용
- > Lazy Learning기법: 새로운 입력 값이 들어온 후 분류시작, 모델만들지 않음.
- > 단순유연성: 모형이 단순하며 파라미터의 가정이 거의 없음
- > NN(Nearest Neighbors) 개선
- > KNN은 가장 근접한 k개의 데이터에 대한 다수결 내지 가중합계 방식으로 분류
- > 가장 유사한 Instance를 찾아서 그와 같은 class에 일방적으로 분류, 잡음 데이터 성능 구림

#### 추출방식

- 핑케라다
- ①새로운 fingerprint 입력(물음표, 동그라미) 확인
- ②거리기반 k개 데이터를 training set에서 추출
- ③추출데이터들의 클러스터 및 label 확인
- ④다수결(Majority Voting)에 의한 클러스터 매칭

#### 거리기반알고리즘

- 유마코
- > 유클리디안거리: 점과 점간 최단거리
- > 마할라노비스의 거리: 두 모집단들을 판별하는 문제에서 두 집단 사이의 거리
- > 코사인 유사도: 코사인사용 측정된 벡터간 유사한 정도

#### 장단점

- 간단하고 효율적, 성능자원 필요
- > 장점:효율성/결과일관성/간단한학습/유연한경계/모델의 유연성/높은 정확도
- > 단점: 성능가변성/높은 자원요구량/고비용/공간예측 부정확/거리계산 복잡성/노이즈에 약함

</details>

---

<details markdown="1">
<summary><h3 style="display:inline">🗂️ 기존 내용 (백업)</h3></summary>

# KNN(K Near Neighborhood)
{: .fs-8 }

1.2 지도학습
{: .label .label-purple }

---

## 핵심 키워드

`Fingerprint` `유클라디안` `맨하튼 거리`

---

## 정의/개념

Fingerprint 내 거리기반 K개 데이터 추출, 유클리디안, 맨하튼 거리 사용 분류 알고리즘

---

## 개념도

```
        Y-Axis
           │
           │     ★ ★        Class A (★)
           │   ★ ★ ★        Class B (▲)
           │     ★ ★
           │      ⬜ ← New example to classify
           │  K=3 ○───┐
           │   K=7 ○───┼─▲ ▲ ▲ ▲
           │         ▲ ▲ ▲
           └──────────────────── X-Axis
```

---

## 프로세스

| # | 프로세스 |
|:--|:--------|
| 1 | 새로운 Fingerprint 확인 |
| 2 | 거리 기반 K개 데이터를 Training Set에서 추출 |
| 3 | 추출 데이터 분류 확인 |
| 4 | 다수결로 분류 매핑 |

---

## 구성요소

| 구분 | 설명 |
|:-----|:-----|
| **K 의미** | 다수결 이후 완료 |
| **거리측정** | 유클리디안 거리, 마할라노비스 거리 |

---

## 연계 토픽

- [K-Means](/docs/ai/01-machine-learning/k-means)
- [SVM](/docs/ai/01-machine-learning/svm)

---

## 학습 체크리스트

- [ ] KNN 알고리즘의 정의와 프로세스 이해
- [ ] K 값의 의미와 선택 방법 파악
- [ ] 거리 측정 방법(유클리디안, 맨하튼) 이해


</details>

