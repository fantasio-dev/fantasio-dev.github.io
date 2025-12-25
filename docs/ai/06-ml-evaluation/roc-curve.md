---
layout: default
title: ROC Curve / PR Curve
parent: 6. 검증/평가/운영
grand_parent: AI (인공지능)
nav_order: 3
---

# ROC Curve / Precision-Recall Curve
{: .fs-8 }

인공지능 평가
{: .label .label-purple }

---

## 🎯 기술사 수준 설명

### 📌 핵심 암기 (Quick Reference)

{: .highlight }
> **ROC Curve / PR Curve**: 분류 모델의 성능을 시각화하는 그래프
> - (ROC) `알특민` X축:특이도(Specificity), Y축:민감도(Sensitivity)
> - (PR) `정재정` X축:정밀도(Precision), Y축:재현율(Recall)

---

<div class="exam-concept-block" markdown="1">

## 🧠 개념 영역

### 🔑 핵심 키워드 3개

| 키워드 | 설명 | 예시 |
|:------|:-----|:-----|
| **ROC Curve** | 민감도와 특이도의 관계 | TPR vs FPR |
| **PR Curve** | 정밀도와 재현율의 관계 | 불균형 데이터 적합 |
| **AUC** | 커브 아래 면적 | 1에 가까울수록 좋음 |

---

### 📖 등장배경

| 구분 | 내용 |
|:-----|:-----|
| **모델 비교** | 여러 분류 모델의 성능을 시각적으로 비교 |
| **임계값 분석** | 다양한 임계값에서의 성능 확인 |

---

### 📝 개념 정의

| 구분 | 정의 |
|:-----|:-----|
| **ROC Curve** | 모든 분류 임계값에서 민감도와 특이도를 표시한 그래프 |
| **PR Curve** | 정밀도와 재현율을 기준으로 불균형 데이터 성능 평가 그래프 |

</div>

---

<div class="exam-tech-block" markdown="1">

## 🏗️ 기술 영역

### ROC Curve `알특민` / PR Curve `정재정`

#### ROC Curve `알특민`
{: .highlight-purple }

| 암기 | 항목 | 설명 |
|:-----|:-----|:-----|
| **알** | AUC | ROC Curve 아래의 면적으로 환산하여 평가 |
| **특** | 특이도(Specificity) | X축: FP / (FP+TN) |
| **민** | 민감도(Sensitivity) | Y축: TP / (TP+FN) |

#### PR Curve `정재정`
{: .highlight-purple }

| 암기 | 항목 | 설명 |
|:-----|:-----|:-----|
| **정** | 정밀도(Precision) | X축: TP / (TP + FP) |
| **재** | 재현율(Recall) | Y축: TP / (TP + FN) |
| **정** | 정확도와 다름 | 불균형 데이터셋일 때 성능 평가에 유리 |

#### 사용 상황
{: .highlight-purple }

| 상황 | 권장 커브 |
|:-----|:---------|
| **균형 데이터** | ROC Curve |
| **불균형 데이터** | PR Curve |
| **Positive 중요** | PR Curve |

</div>

---

<div class="exam-bonus-block" markdown="1">

## ⭐ 차별점 키워드 (가산점 포인트)

{: .important }
> **ROC vs PR Curve**
> - **ROC**: 균형 데이터에 적합, TN도 고려
> - **PR**: 불균형 데이터에 적합, Positive 클래스에 집중
> - **AUC**: 1에 가까울수록 좋은 모델

</div>

---

<details markdown="1">
<summary><h3 style="display:inline">📖 상세 설명 (클릭해서 펼치기)</h3></summary>

#### ✅ 학습 체크리스트

- [ ] ROC Curve 정의와 축 설명 가능
- [ ] PR Curve 정의와 축 설명 가능
- [ ] AUC 개념 설명 가능
- [ ] 균형/불균형 데이터에서 선택 기준 설명 가능

</details>

---

## 연계 토픽

- [혼동행렬](/docs/ai/06-ml-evaluation/confusion-matrix)
- [정밀도/재현율](/docs/ai/06-ml-evaluation/precision-recall)
