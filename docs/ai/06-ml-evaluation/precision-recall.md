---
layout: default
title: 정밀도(Precision)/재현율(Recall)
parent: 6. ML 평가
grand_parent: AI (인공지능)
nav_order: 2
---

# 정밀도(Precision)/재현율(Recall)
{: .fs-8 }

ML 평가
{: .label .label-red }

---

## 🎯 기술사 수준 설명

### 📌 핵심 암기 (Quick Reference)

{: .highlight }
> - **정밀도 (Precision)**: 예측에서 참이라고 예측한 것 중 실제 참인 비율
> - **재현율 (Recall)**: 실제 참 값 중 참으로 예측한 비율 (민감도 = Recall)

---

## 핵심 키워드

`Precision` `Recall` `F1 Score` `Trade-off`

---

## 정의/개념

| 지표 | 정의 |
|:-----|:-----|
| **정밀도 (Precision)** | 예측에서 참이라고 예측한 것 중 실제 참인 비율 |
| **재현율 (Recall)** | 실제 참 값 중 참으로 예측한 비율 (민감도) |

---

## 수식

$$
\text{Precision} = \frac{TP}{TP + FP}
$$

$$
\text{Recall} = \frac{TP}{TP + FN}
$$

$$
\text{F1 Score} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}
$$

---

## 정밀도 vs 재현율

| 항목 | 정밀도 (Precision) | 재현율 (Recall) |
|:-----|:-------------------|:----------------|
| **초점** | 예측의 정확성 | 놓치지 않는 것 |
| **수식** | TP/(TP+FP) | TP/(TP+FN) |
| **중요 케이스** | 스팸 필터링 | 암 진단 |

---

## Trade-off

```
정밀도 ↑ → 재현율 ↓
재현율 ↑ → 정밀도 ↓

균형점: F1 Score (조화평균)
```

---

## 활용 사례

| 상황 | 중요 지표 | 이유 |
|:-----|:----------|:-----|
| **암 진단** | 재현율 | 놓치면 안 됨 |
| **스팸 필터** | 정밀도 | 중요 메일 오분류 방지 |
| **균형 필요** | F1 Score | 두 지표 균형 |

---

## 연계 토픽

- [혼동 행렬]({{ site.baseurl }}/docs/ai/06-ml-evaluation/confusion-matrix)
- [ROC Curve]({{ site.baseurl }}/docs/ai/06-ml-evaluation/roc-curve)

---

## 학습 체크리스트

- [ ] 정밀도/재현율 정의 암기
- [ ] 수식 암기
- [ ] Trade-off 관계 설명
