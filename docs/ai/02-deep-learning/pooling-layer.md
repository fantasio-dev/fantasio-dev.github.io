---
layout: default
title: Pooling Layer
parent: 2. 딥러닝
grand_parent: AI (인공지능)
nav_order: 2
---

<!-- CSV_APPLIED: 기술사_기본필수노트_AI - AI.csv | NO=13 | 중토픽=Pooling Layer -->
# Pooling Layer
{: .fs-8 }

3.2 분류(Classification)
{: .label .label-purple }

---

## 🎯 기술사 수준 설명

### 📌 핵심 암기 (Quick Reference)

{: .highlight }
> **Pooling Layer**: Convolution Layer에서 출력 데이터를 입력으로 받아서 Sub > Sampling을 통해 출력 데이터(Activation Map)의 크기를 줄이거나 특정 데이터를 강조하는 레이어
> - 암기: `입영연이반결` `평최혼확`
> - 키워드: `Pooling Layer` `Activation Map` `Convolution`

---

<div class="exam-concept-block" markdown="1">

## 🧠 개념 영역

### 🔑 핵심 키워드 3개

| 키워드 | 설명 | 예시 |
|:--|:--|:--|
| **Pooling Layer** | 핵심 개념/대상 | - |
| **Activation Map** | 주요 기법/구성요소 | - |
| **Convolution** | 절차/평가/특징 | - |

---

### 📖 등장배경

| 구분 | 내용 |
|:--|:--|
| **문제/필요성** | Convolution Layer에서 출력 데이터를 입력으로 받아서 Sub > Sampling을 통해 출력 데이터(Activation Map)의 크기를 줄이거나 특정 데이터를 강조하는 레이어 |
| **활용/사례** | - |

---

### 📝 개념 정의

| 구분 | 정의 |
|:--|:--|
| **Pooling Layer** | Convolution Layer에서 출력 데이터를 입력으로 받아서 Sub > Sampling을 통해 출력 데이터(Activation Map)의 크기를 줄이거나 특정 데이터를 강조하는 레이어 |

</div>

---

<div class="exam-tech-block" markdown="1">

## 🏗️ 기술 영역

### 구성요소

#### 그룹 1: 유형
{: .highlight-purple }

| 항목 | 설명 |
|:--|:--|
| **> Average** | 평균, 특징이 약함, 결과가 안좋음. |
| **> Max** | 특징이 강하지만 overfitting 되기 쉬움 |
| *** 약점 보완하기 위해 두 기법 응용** | - |
| **> Mix** | 랜덤하고 평균/최대 반복 |
| **> Stochastic** | 임의값 선택 |


</div>

---

<details markdown="1">
<summary><h3 style="display:inline">📖 상세 설명 (클릭해서 펼치기)</h3></summary>

#### 내용

- Convolution Layer에서 출력 데이터를 입력으로 받아서 Sub > Sampling을 통해 출력 데이터(Activation Map)의 크기를 줄이거나 특정 데이터를 강조하는 레이어

#### 특징

- > 파라미터감소: 과적합억제, 연산감소
- > 출력: 채널 수 유지, 특징추출, 변화적음

#### 동작

- 1. Feature Map 입력: Convolution Layer의 출력 값인 Feature Map을 채널 개수
- 2. Pooling 영역 설정: 커널사이즈 만큼
- 3. Pooling 연산: Pooling Average, Max
- 4. Pooing 영역 이동: Stride 값 만큼 window를 이동해 Pooling 영역을 재설정
- 5. 반복 : 2 ~ 4를 반복해 채널 별 Activation 출력을 생성
- 6. 결과 출력 > 채널별로 생성된 Activation을 FC Layer 의 입력으로 출력

#### 유형

- > Average: 평균, 특징이 약함, 결과가 안좋음.
- > Max: 특징이 강하지만 overfitting 되기 쉬움
- * 약점 보완하기 위해 두 기법 응용
- > Mix: 랜덤하고 평균/최대 반복
- > Stochastic: 임의값 선택

</details>

---

<details markdown="1">
<summary><h3 style="display:inline">🗂️ 기존 내용 (백업)</h3></summary>

# Pooling Layer
{: .fs-8 }

3.2 분류(Classification)
{: .label .label-purple }

---

## 🎯 기술사 수준 설명

### 📌 핵심 암기 (Quick Reference)

{: .highlight }
> **Pooling Layer**: Convolution Layer 출력을 Sub-Sampling하여 차원을 축소하는 레이어
> - (동작) `입영연이반결` 입력→영역설정→연산→이동→반복→결과출력
> - (유형) `평최혼확` Average, Max, Mix, Stochastic

---

<div class="exam-concept-block" markdown="1">

## 🧠 개념 영역

### 🔑 핵심 키워드 3개

| 키워드 | 설명 | 예시 |
|:------|:-----|:-----|
| **Sub-Sampling** | 데이터 크기 축소 | 4x4 → 2x2 |
| **Stride** | 이동 간격 | 2칸씩 이동 |
| **Feature Map** | Convolution 출력 | 특징 맵 |

---

### 📖 등장배경

| 구분 | 내용 |
|:-----|:-----|
| **파라미터 감소** | 과적합 억제, 연산량 감소 필요 |
| **특징 강조** | 중요한 특징을 강조하고 노이즈 제거 |

---

### 📝 개념 정의

| 구분 | 정의 |
|:-----|:-----|
| **Pooling Layer** | Sub-Sampling으로 출력 데이터 크기를 줄이거나 특징을 강조하는 레이어 |

</div>

---

<div class="exam-tech-block" markdown="1">

## 🏗️ 기술 영역

### 동작 `입영연이반결` / 유형 `평최혼확`

#### 동작 과정 `입영연이반결`
{: .highlight-purple }

| 암기 | 항목 | 설명 |
|:-----|:-----|:-----|
| **입** | Feature Map 입력 | Convolution Layer 출력 값을 채널 개수만큼 입력 |
| **영** | Pooling 영역 설정 | 커널사이즈 만큼 영역 설정 |
| **연** | Pooling 연산 | Average, Max 등 연산 수행 |
| **이** | Pooling 영역 이동 | Stride 값만큼 window 이동 |
| **반** | 반복 | 영역설정→연산→이동 반복 |
| **결** | 결과 출력 | FC Layer 입력으로 출력 |

#### Pooling 유형 `평최혼확`
{: .highlight-purple }

| 암기 | 항목 | 설명 |
|:-----|:-----|:-----|
| **평** | Average Pooling | 평균값, 특징이 약함, 결과가 안좋음 |
| **최** | Max Pooling | 최대값, 특징이 강하지만 overfitting 되기 쉬움 |
| **혼** | Mix Pooling | 랜덤하게 평균/최대 반복 (약점 보완) |
| **확** | Stochastic Pooling | 임의값 선택 |

</div>

---

<div class="exam-bonus-block" markdown="1">

## ⭐ 차별점 키워드 (가산점 포인트)

{: .important }
> **Pooling Layer 특징**
> - **파라미터 감소**: 과적합 억제, 연산 감소
> - **출력**: 채널 수 유지, 특징 추출, 변화 적음
> - **Average vs Max**: 서로 약점 보완하기 위해 Mix, Stochastic 사용

</div>

---

<details markdown="1">
<summary><h3 style="display:inline">📖 상세 설명 (클릭해서 펼치기)</h3></summary>

#### ✅ 학습 체크리스트

- [ ] Pooling Layer 정의 말할 수 있다
- [ ] `입영연이반결` 동작 6단계 설명 가능
- [ ] `평최혼확` 유형 4가지 차이 설명 가능
- [ ] Max vs Average Pooling 비교 설명 가능

</details>

---

## 연계 토픽

- [CNN](/docs/ai/02-deep-learning/cnn)
- [과적합 문제](/docs/ai/02-deep-learning/overfitting-underfitting)

</details>

