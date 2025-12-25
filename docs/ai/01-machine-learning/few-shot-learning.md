---
layout: default
title: 퓨샷러닝(Few-Shot Learning)
parent: 1. 기계학습
grand_parent: AI (인공지능)
nav_order: 25
---

# 퓨샷러닝(Few-Shot Learning)
{: .fs-8 }

학습용데이터
{: .label .label-purple }

---

## 🎯 기술사 수준 설명

### 📌 핵심 암기 (Quick Reference)

{: .highlight }
> **퓨샷러닝**: 소량의 데이터로 효과적인 학습을 하는 학습 방식
> - (유형) `제원퓨` 제로샷, 원샷, 퓨샷

---

<div class="exam-concept-block" markdown="1">

## 🧠 개념 영역

### 🔑 핵심 키워드 3개

| 키워드 | 설명 | 예시 |
|:------|:-----|:-----|
| **Zero-shot** | 한번도 본 적 없는 클래스 학습 | 호랑이→사자→라이거 |
| **One-shot** | 하나의 샘플만 주어짐 | 한 개의 호랑이 |
| **Few-shot** | 클래스별 소수 샘플 | 적은 수의 호랑이 |

---

### 📖 등장배경

| 구분 | 내용 |
|:-----|:-----|
| **데이터 부족** | 레이블 데이터가 충분하지 않은 상황 |
| **인간처럼 학습** | 인간은 적은 예시로도 새로운 것을 학습 |

---

### 📝 개념 정의

| 구분 | 정의 |
|:-----|:-----|
| **퓨샷러닝** | 소량의 데이터로 효과적인 학습을 하는 방식 |

</div>

---

<div class="exam-tech-block" markdown="1">

## 🏗️ 기술 영역

### 유형 `제원퓨`

#### 유형 `제원퓨`
{: .highlight-purple }

| 암기 | 항목 | 설명 |
|:-----|:-----|:-----|
| **제** | 제로샷러닝 | 한번도 관측되지 않은 클래스 학습, 호랑이>사자>라이거 |
| **원** | 원샷러닝 | 하나의 샘플만 주어짐, 한개의 호랑이, 두번째는 맞춤 |
| **퓨** | 퓨샷러닝 | 클래스별 소수 샘플, 적은 수의 호랑이, 다음부터 맞춤 |

#### 비교
{: .highlight-purple }

| 유형 | 샘플 수 | 특징 |
|:-----|:--------|:-----|
| **Zero-shot** | 0개 | 관측되지 않은 클래스 추론 |
| **One-shot** | 1개 | 하나의 예시로 학습 |
| **Few-shot** | 2~5개 | 소수의 예시로 학습 |

</div>

---

<div class="exam-bonus-block" markdown="1">

## ⭐ 차별점 키워드 (가산점 포인트)

{: .important }
> **퓨샷러닝 핵심**
> - **N-way K-shot**: N개 클래스, 클래스당 K개 샘플
> - **Support Set**: 학습에 사용되는 소량의 샘플
> - **Query Set**: 예측 대상 샘플

</div>

---

<details markdown="1">
<summary><h3 style="display:inline">📖 상세 설명 (클릭해서 펼치기)</h3></summary>

#### ✅ 학습 체크리스트

- [ ] 퓨샷러닝 정의 말할 수 있다
- [ ] `제원퓨` 유형 3가지 차이 설명 가능
- [ ] N-way K-shot 개념 설명 가능

</details>

---

## 연계 토픽

- [메타학습](/docs/ai/01-machine-learning/meta-learning)
- [전이학습](/docs/ai/01-machine-learning/transfer-learning)

