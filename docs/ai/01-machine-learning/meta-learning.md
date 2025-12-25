---
layout: default
title: 메타학습(Meta Learning)
parent: 1. 기계학습
grand_parent: AI (인공지능)
nav_order: 24
---

# 메타학습(Meta Learning)
{: .fs-8 }

학습용데이터
{: .label .label-purple }

---

## 🎯 기술사 수준 설명

### 📌 핵심 암기 (Quick Reference)

{: .highlight }
> **메타학습**: 아는 것과 모르는 것을 즉각 구분하는 메타인지로부터 시작, 적은 양의 데이터로 스스로 학습하는 방식
> - (유형) `거모최` 거리기반, 모델기반, 최적화기반
> - (적용) 퓨샷러닝

---

<div class="exam-concept-block" markdown="1">

## 🧠 개념 영역

### 🔑 핵심 키워드 3개

| 키워드 | 설명 | 예시 |
|:------|:-----|:-----|
| **메타인지** | 아는 것과 모르는 것을 구분 | 학습 능력 학습 |
| **적은 데이터** | 소량의 데이터로 학습 | Few-shot |
| **일반화** | 새로운 문제에 적용 | 전이 학습 |

---

### 📖 등장배경

| 구분 | 내용 |
|:-----|:-----|
| **데이터 부족** | 레이블 데이터가 부족한 상황 |
| **빠른 적응** | 새로운 Task에 빠르게 적응해야 하는 요구 |

---

### 📝 개념 정의

| 구분 | 정의 |
|:-----|:-----|
| **메타학습** | 적은 데이터로도 스스로 학습하고 문제에 적용하는 학습방식 |

</div>

---

<div class="exam-tech-block" markdown="1">

## 🏗️ 기술 영역

### 유형 `거모최`

#### 유형 `거모최`
{: .highlight-purple }

| 암기 | 항목 | 설명 |
|:-----|:-----|:-----|
| **거** | 거리기반학습방식 | Prototypical Network, Relational Network |
| **모** | 모델기반학습방식 | Memory 이용, RNN |
| **최** | 최적화학습방식 | Model Parameter 최적화 |

#### 적용
{: .highlight-purple }

| 항목 | 설명 |
|:-----|:-----|
| **퓨샷러닝** | 소량의 데이터로 효과적인 학습 |
| **MAML** | Model-Agnostic Meta-Learning |

</div>

---

<div class="exam-bonus-block" markdown="1">

## ⭐ 차별점 키워드 (가산점 포인트)

{: .important }
> **메타학습 핵심**
> - **Learning to Learn**: 학습하는 방법을 학습
> - **Few-shot 적용**: 소량 데이터로 효과적 학습
> - **메타인지**: 아는 것과 모르는 것을 즉각 구분

</div>

---

<details markdown="1">
<summary><h3 style="display:inline">📖 상세 설명 (클릭해서 펼치기)</h3></summary>

#### ✅ 학습 체크리스트

- [ ] 메타학습 정의 말할 수 있다
- [ ] `거모최` 유형 3가지 설명 가능
- [ ] 퓨샷러닝과의 관계 설명 가능

</details>

---

## 연계 토픽

- [퓨샷러닝](/docs/ai/01-machine-learning/few-shot-learning)
- [전이학습](/docs/ai/01-machine-learning/transfer-learning)

