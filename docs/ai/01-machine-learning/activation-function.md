---
layout: default
title: 활성화 함수
parent: 1. 기계학습
grand_parent: AI (인공지능)
nav_order: 16
---

<!-- CSV_APPLIED: 기술사_기본필수노트_AI - AI.csv | NO=7 | 중토픽=활성화 함수 -->
# 활성화 함수
{: .fs-8 }

6. 퍼셉트론
{: .label .label-purple }

---

## 🎯 기술사 수준 설명

### 📌 핵심 암기 (Quick Reference)

{: .highlight }
> **활성화 함수**: [활성화함수] 일정 범위값 변환 전달, 단조 증가 함수
> - 암기: `항시렐계` `핫소`
> - 키워드: `활성화 함수` `x` `NET`

---

<div class="exam-concept-block" markdown="1">

## 🧠 개념 영역

### 🔑 핵심 키워드 3개

| 키워드 | 설명 | 예시 |
|:--|:--|:--|
| **활성화 함수** | 핵심 개념/대상 | - |
| **x** | 주요 기법/구성요소 | - |
| **NET** | 절차/평가/특징 | - |

---

### 📖 등장배경

| 구분 | 내용 |
|:--|:--|
| **문제/필요성** | [활성화함수] 일정 범위값 변환 전달, 단조 증가 함수 |
| **활용/사례** | - |

---

### 📝 개념 정의

| 구분 | 정의 |
|:--|:--|
| **활성화 함수** | [활성화함수] 일정 범위값 변환 전달, 단조 증가 함수 |

</div>

---

<div class="exam-tech-block" markdown="1">

## 🏗️ 기술 영역

### 구성요소

#### 그룹 1: 활성화함수
{: .highlight-purple }

| 항목 | 설명 |
|:--|:--|
| **일정 범위값 변환 전달, 단조 증가 함수** | - |
| **> 항등함수** | f(x) = x, 선형출력 |
| **> 시그모이드함수** | y=1/1+e^ > x, 0과 1사이, 0.5기준 |
| **> ReLU함수** | ReLU(x) = { 0 if x < 0, x if x >= 0 }, 0보다 크면 x |
| **> 계단함수** | f(NET) = { 1 if NET >= T, 0 if NET < T, 기준값 T기준 0 아니면 1 |
| **> tanh 함수** | > 1과 1사이 값을 생성 |


</div>

---

<details markdown="1">
<summary><h3 style="display:inline">📖 상세 설명 (클릭해서 펼치기)</h3></summary>

#### 활성화함수

- 일정 범위값 변환 전달, 단조 증가 함수
- > 항등함수: f(x) = x, 선형출력
- > 시그모이드함수: y=1/1+e^ > x, 0과 1사이, 0.5기준
- > ReLU함수: ReLU(x) = { 0 if x < 0, x if x >= 0 }, 0보다 크면 x
- > 계단함수: f(NET) = { 1 if NET >= T, 0 if NET < T, 기준값 T기준 0 아니면 1
- > tanh 함수: > 1과 1사이 값을 생성

#### 원핫인코딩과 소프트맥스

- > 범주형 데이터를 수치형 데이터로 변경, 원핫 인코딩(One > hot Encoding)
- > 피처값의 유형에 따라서 새로은 고유값 추가, 해당하는 컬럼 1로 처리
- > 색상값 수치화, 수학적 희소벡터
- > 차원의 저주문제: 차원이 증가할수록 학습데이터 줄어들고 성능 떨어짐
- > 출력층에서 정규화(0 > 1로 처리)처리 소프트맥스
- > 0 > 1사이의 실수, 확률값
- >출력의 총합은 항상 1

</details>

---

<details markdown="1">
<summary><h3 style="display:inline">🗂️ 기존 내용 (백업)</h3></summary>

# 활성화 함수(Activation function)
{: .fs-8 }

6. 퍼셉트론
{: .label .label-purple }

---

## 핵심 키워드

`Sigmoid Function` `Step Function` `ReLU Function` `Tanh Function` `Leaky ReLU Function` `Identity Function`

---

## 정의/개념

인공신경망에서 현재 레이어(Layer)의 입력 신호와 가중치의 총합을 비선형적 출력 신호로 변환하여 활성화 여부를 결정하는 함수

---

## 활성화 함수 유형

### 단극성 활성화 함수

| 활성화 함수 | 개념도 | 설명 |
|:-----------|:------|:-----|
| **Sigmoid Function** (시그모이드 함수) | $h(x) = \frac{1}{1 + e^{-x}}$ | 로지스틱 함수라고도 하며 x값의 변화에 따라 0에서 1까지의 값을 출력하는 S자형 함수 |
| **Step Function** (계단 함수) | $y = 1$ (when $x≥0$)<br>$y = 0$ (when $x<0$) | 특정 값 이하는 0, 이상은 1로 출력하도록 만들어진 함수<br>함수식: y = 1 (when x≥0), 0 (when x<0) |
| **ReLU Function** (Rectified Linear Unit 경사 함수) | $f(x) = max(0, x)$ | Gradient Vanishing 문제(layer가 늘어날 때 값이 사라지는 현상)을 해결하기 위한 함수<br>x값이 음수일 경우 0을 출력 |

### 양극성 활성화 함수

| 활성화 함수 | 개념도 | 설명 |
|:-----------|:------|:-----|
| **Tanh Function** (쌍곡 탄젠트 함수) | $tanh(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}}$ | Sigmoid Function을 재활용하여 -1 ~ 1의 범위를 갖는 함수 |
| **Leaky ReLU Function** | $f(x) = max(αx, x)$ | x값이 음수일 때 입력 값의 10분의 1만을 출력하는 ReLU의 변형 |
| **Identity Function** (항등 함수) | $f(x) = x$ | 양극성이며 입력 값의 가중 합이 그대로 출력 |

---

## 활성화 함수 비교

| 함수 | 출력 범위 | 장점 | 단점 |
|:-----|:---------|:-----|:-----|
| **Sigmoid** | 0 ~ 1 | 확률 해석 가능 | 기울기 소실, 계산 비용 |
| **Tanh** | -1 ~ 1 | 0 중심 | 기울기 소실 |
| **ReLU** | 0 ~ ∞ | 빠른 학습, 기울기 소실 해결 | Dead ReLU |
| **Leaky ReLU** | -∞ ~ ∞ | Dead ReLU 해결 | α 하이퍼파라미터 필요 |

---

## 연계 토픽

- [기울기 소실](/docs/ai/01-machine-learning/vanishing-gradient)
- [역전파](/docs/ai/01-machine-learning/perceptron)

---

## 학습 체크리스트

- [ ] 활성화 함수의 정의와 목적 이해
- [ ] 6가지 활성화 함수 특징 암기
- [ ] 단극성 vs 양극성 활성화 함수 차이 파악


</details>

