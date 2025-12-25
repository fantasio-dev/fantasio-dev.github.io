---
layout: default
title: 경사하강법
parent: 1. 기계학습
grand_parent: AI (인공지능)
nav_order: 15
---

<!-- CSV_APPLIED: 기술사_기본필수노트_AI - AI.csv | NO=8 | 중토픽=경사 하강법 (Gradient decent) -->
# 경사하강법
{: .fs-8 }

6. 퍼셉트론
{: .label .label-purple }

---

## 🎯 기술사 수준 설명

### 📌 핵심 암기 (Quick Reference)

{: .highlight }
> **경사 하강법 (Gradient decent)**: 함수의 기울기(경사)를 구하여 기울기가 낮은 쪽으로 계속 이동시켜 극 값에 이를 때까지 반복시키는 1차 근사값 발견을 위한 최적화 알고리즘
> - 암기: `확배미`
> - 키워드: `경사 하강법` `경사` `Stochastic Gradient Descent`

---

<div class="exam-concept-block" markdown="1">

## 🧠 개념 영역

### 🔑 핵심 키워드 3개

| 키워드 | 설명 | 예시 |
|:--|:--|:--|
| **경사 하강법** | 핵심 개념/대상 | - |
| **경사** | 주요 기법/구성요소 | - |
| **Stochastic Gradient Descent** | 절차/평가/특징 | - |

---

### 📖 등장배경

| 구분 | 내용 |
|:--|:--|
| **문제/필요성** | 함수의 기울기(경사)를 구하여 기울기가 낮은 쪽으로 계속 이동시켜 극 값에 이를 때까지 반복시키는 1차 근사값 발견을 위한 최적화 알고리즘 |
| **활용/사례** | - |

---

### 📝 개념 정의

| 구분 | 정의 |
|:--|:--|
| **경사 하강법 (Gradient decent)** | 함수의 기울기(경사)를 구하여 기울기가 낮은 쪽으로 계속 이동시켜 극 값에 이를 때까지 반복시키는 1차 근사값 발견을 위한 최적화 알고리즘 |

</div>

---

<div class="exam-tech-block" markdown="1">

## 🏗️ 기술 영역

### 구성요소

#### 그룹 1: 구성요소
{: .highlight-purple }

| 항목 | 설명 |
|:--|:--|
| **+ 데이터** | - |
| **> Initial Weight** | 초기가중치 |
| **> Gradient** | 기울기(경사) |
| **> Grobal Cost Minimum** | 최저값 |
| **> Stop Condition** | 학습완료조건 |
| **+ 알고리즘** | - |
| **> 확률적 경사하강법 (Stochastic Gradient Descent)** | 하강변화심함 |
| **> 랜덤하게 하강, 데이터학습시마다 갱신, 지역최저점 빠질수 있음** | - |


</div>

---

<details markdown="1">
<summary><h3 style="display:inline">📖 상세 설명 (클릭해서 펼치기)</h3></summary>

#### 내용

- 함수의 기울기(경사)를 구하여 기울기가 낮은 쪽으로 계속 이동시켜 극 값에 이를 때까지 반복시키는 1차 근사값 발견을 위한 최적화 알고리즘

#### 구성요소

- + 데이터
- > Initial Weight: 초기가중치
- > Gradient: 기울기(경사)
- > Grobal Cost Minimum: 최저값
- > Stop Condition: 학습완료조건
- + 알고리즘
- > 확률적 경사하강법 (Stochastic Gradient Descent): 하강변화심함
- > 랜덤하게 하강, 데이터학습시마다 갱신, 지역최저점 빠질수 있음
- > 배치 경사하강법 (Batch Gradient Descent)
- > 하나의 배치로 묶어서 하강, 전체데이터 학습후 하강, 수렴이 안정적
- > 미니배치 경사하강법 (Mini > Batch Gradient Descent)
- > 전체 배치를 사이즈(사용자임의)로 나누고, 각 배치로 학습, BGD보다 적은 계산
- * Local Maximum/Minimum & Global Maximum/Minimum 문제
- > local minimum문제 대응 위해 initial point 를 다양하게 변경하여 global minimum 찾음.
- > Gradient Decent는 MLP(Multi Layer Perceptron) 적용시, 학습 layer가 깊어질수록 기울기가 소멸, 학습 효과가 사라지는 Gradient Vanishing Problem발생

</details>

---

<details markdown="1">
<summary><h3 style="display:inline">🗂️ 기존 내용 (백업)</h3></summary>

# 경사하강법(Gradient Descent)
{: .fs-8 }

6. 퍼셉트론
{: .label .label-purple }

---

## 핵심 키워드

`학습률` `최적의 파라미터`

---

## 정의/개념

주어진 함수의 최소값 위치를 찾기 위해 비용함수의 가중치 반대 방향으로 정의한 학습률을 가지고 조금씩 움직여 가면서 최적의 파라미터를 찾으려는 기법

---

## 경사하강법의 개념

- 주어진 함수의 최소값 위치를 찾기 위해 비용 함수(Cost Function)의 Gradient 반대 방향으로 정의한 Learning Rate(step size)를 가지고 조금씩 움직여 가면서 최적의 파라미터를 찾으려는 방법
- 머신 러닝 기법 등에서 오차항의 최소값을 찾기 위해 사용되는 기법

---

## 매커니즘

```
    J(w)
      │
      │ Initial      Gradient
      │ weight  ╲  ╱
      │         ─●─
      │          ╲
      │           ╲
      │            ╲        Global cost minimum
      │             ╲          Jmin(w)
      │              ●─────────────────────────
      │
      └──────────────────────────────────────── w
```

### Formal definition

$$cost(W) = \frac{1}{2n}\sum_{i=1}^{n}(Wx^{(i)} - y^{(i)})^2$$

$$W := W - α\frac{∂}{∂W}cost(W)$$

---

## 프로세스

| # | 단계 | 설명 |
|:--|:-----|:-----|
| 1 | 임의의 변수 초기값 선택 | 시작점 설정 |
| 2 | 변수 값에 해당하는 경사도(기울기) 계산 | Gradient 계산 |
| 3 | 변수를 경사방향으로 움직여 다음 기울기 계산 | 이동 및 재계산 |
| 4 | 1),2),3)을 반복하여 함수의 최소값이 되는 값을 찾음 | 반복 수행 |

---

## 주의사항

- 머신 러닝에서 예측 값과 실제 값의 오차를 설명하는 오차함수의 최소값을 찾기 위해 사용
- 적절한 Learning Rate 지정 문제로 인해 오버슈팅 문제를 지니며 이를 해결하기 위한 경사하강법 최적화 알고리즘 존재

---

## 연계 토픽

- [오류역전파](/docs/ai/01-machine-learning/perceptron)
- [옵티마이저](/docs/ai/02-deep-learning/optimizer)

---

## 학습 체크리스트

- [ ] 경사하강법의 정의와 수식 이해
- [ ] 프로세스 4단계 암기
- [ ] Learning Rate와 오버슈팅 문제 이해


</details>

