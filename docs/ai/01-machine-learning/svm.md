---
layout: default
title: SVM
parent: 1. 기계학습
grand_parent: AI (인공지능)
nav_order: 14
---

<!-- CSV_APPLIED: 기술사_기본필수노트_AI - AI.csv | NO=16 | 중토픽=서포트 벡터 머신, SVM(Support Vector Machine) -->
# SVM
{: .fs-8 }

1.2 지도학습
{: .label .label-purple }

---

## 🎯 기술사 수준 설명

### 📌 핵심 암기 (Quick Reference)

{: .highlight }
> **서포트 벡터 머신, SVM(Support Vector Machine)**: 학습데이터를 두 개의 클래스로 나누는데 Margin을 최대로 하는 결정직선을 찾는 분류(classifier) 알고리즘
> - 암기: `하서마스` `커트하소`
> - 키워드: `서포트 벡터 머신, SVM` `classifier` `Hyperplane: 클래스를 구분하는 면/선/곡선`

---

<div class="exam-concept-block" markdown="1">

## 🧠 개념 영역

### 🔑 핵심 키워드 3개

| 키워드 | 설명 | 예시 |
|:--|:--|:--|
| **서포트 벡터 머신, SVM** | 핵심 개념/대상 | - |
| **classifier** | 주요 기법/구성요소 | - |
| **Hyperplane: 클래스를 구분하는 면/선/곡선** | 절차/평가/특징 | - |

---

### 📖 등장배경

| 구분 | 내용 |
|:--|:--|
| **문제/필요성** | 학습데이터를 두 개의 클래스로 나누는데 Margin을 최대로 하는 결정직선을 찾는 분류(classifier) 알고리즘 |
| **활용/사례** | - |

---

### 📝 개념 정의

| 구분 | 정의 |
|:--|:--|
| **서포트 벡터 머신, SVM(Support Vector Machine)** | 학습데이터를 두 개의 클래스로 나누는데 Margin을 최대로 하는 결정직선을 찾는 분류(classifier) 알고리즘 |

</div>

---

<div class="exam-tech-block" markdown="1">

## 🏗️ 기술 영역

### 구성요소

#### 그룹 1: 구성요소
{: .highlight-purple }

| 항목 | 설명 |
|:--|:--|
| **하서마스** | - |
| **> 초평면(Hyperplane** | 클래스를 구분하는 면/선/곡선), 분류, 회귀분석 |
| **> Support Vector** | 학습 데이터 중에서 분류 경계에 가장 가까운 곳에 위치한 데이터 |
| **> Margin** | 학습 데이터 중에서 분류 경계에 가장 가까운 데이터로부터 분류 경계까지의 거리 |
| **> Slack Variables** | 여유변수, 선형분류를 위해 허용하는 오차변수, Soft Margin SVM사용 |


</div>

---

<details markdown="1">
<summary><h3 style="display:inline">📖 상세 설명 (클릭해서 펼치기)</h3></summary>

#### 내용

- 학습데이터를 두 개의 클래스로 나누는데 Margin을 최대로 하는 결정직선을 찾는 분류(classifier) 알고리즘

#### 구성요소

- 하서마스
- > 초평면(Hyperplane: 클래스를 구분하는 면/선/곡선), 분류, 회귀분석
- > Support Vector: 학습 데이터 중에서 분류 경계에 가장 가까운 곳에 위치한 데이터
- > Margin: 학습 데이터 중에서 분류 경계에 가장 가까운 데이터로부터 분류 경계까지의 거리
- > Slack Variables: 여유변수, 선형분류를 위해 허용하는 오차변수, Soft Margin SVM사용

#### 기술요소

- 커트하소
- > 커널함수: 비선형패턴을 3차원공간으로 변환하여 경계면 찾기(2차원>3차원)
- > 커널트릭: 커널함수 사용시 연산부하를 해결하는 기법
- > 하드 마진 SVM(Hard Margin SVM): 오분류 허용안함, 경계오류 발생할수 있음.
- > 소프트 마진 SVM(Soft Margin SVM): 오분류 허용, 하드마진 적용 어려움으로 주로 이용
- *Support Vector Machine 은 선형으로 분리가 가능한지 불가능한지에 따라 적용하는 방식이 다름

#### 회귀 분석

- > 하나나 그 이상의 독립변수의 종속변수에 대한 영향의 추정을 할 수 있는 통계기법
- > regression analysis

</details>

---

<details markdown="1">
<summary><h3 style="display:inline">🗂️ 기존 내용 (백업)</h3></summary>

# SVM(Support Vector Machine)
{: .fs-8 }

1.2 지도학습
{: .label .label-purple }

---

## 핵심 키워드

`결정경계` `Support Vector` `Margin` `Hyperplane(초평면)` `Slack 변수` `OSH` `하드 마진` `소프트 마진`

---

## 정의/개념

데이터 사상된 공간 Support Vector간 거리가 가장 큰 경계 식별 지도학습 기반 알고리즘

---

## 개념도

```
  X₂ ↑  최대 마진
     │  ─────────────────  - 최대 마진을 위해 분류 수행
     │      Support Vectors
     │    ○       ○         - 마진이 클수록 훈련 외 데이터도 정확한 분류
     │  ○   ○               
     │    ○     ○           - 마진과 학습 오류는 Trade-off 관계
     │      ○ ●              
     │    ○     ●    OSH    - 선형적 분류 불가시 오차 허용을 위한 슬랙 변수 활용
     └───────────────────→ X₁
```

> 슬랙 변수(이상값 처리 목적)의 엄격한 적용시 오버피팅 발생하며, 반대의 경우 언더피팅 발생

---

## 구성요소

| 구분 | 핵심 |
|:-----|:-----|
| **결정경계** | 데이터 분류 기준 경계 |
| **Support Vector** | 훈련 데이터 중 결정경계 가장 근접 데이터 집합 |
| **Margin** | 결정 경계에서 서포트 벡터까지 거리 |
| **Hyperplane(초평면)** | 데이터 분류 위한 기준 |
| **Slack 변수** | 완벽한 분리 불가능시 허용된 오차 위한 변수 |
| **OSH** | Optimal Separating Hyperplane, 최적 경계선 |

---

## 기법

| 기법 | 핵심 |
|:-----|:-----|
| **Soft Margin** | 마진 안쪽 바깥쪽 이상값 허용 |
| **Hard Margin** | 마진 안쪽 바깥쪽 이상값 미허용 |
| **커널 기법** | 비선형 패턴 분리 |

---

## 연계 토픽

- [KNN](/docs/ai/01-machine-learning/knn)
- [지도학습](/docs/ai/01-machine-learning/supervised-learning)

---

## 학습 체크리스트

- [ ] SVM의 정의와 개념도 이해
- [ ] 구성요소(결정경계, Support Vector, Margin 등) 암기
- [ ] Soft Margin vs Hard Margin 차이점 이해


</details>

