---
layout: default
title: Pooling Layer
parent: 2. 딥러닝
grand_parent: AI (인공지능)
nav_order: 2
---

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
> - ⭐ **차별점**: Pooling Layer 특징: > - **파라미터 감소**: 과적합 억제, 연산 감소

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
