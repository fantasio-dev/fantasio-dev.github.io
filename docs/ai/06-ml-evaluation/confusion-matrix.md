---
layout: default
title: 혼동 행렬 (Confusion Matrix)
parent: 6. ML 평가
grand_parent: AI (인공지능)
nav_order: 1
---

# 혼동 행렬 (Confusion Matrix)
{: .fs-8 }

ML 평가
{: .label .label-red }

---

## 🎯 기술사 수준 설명

### 📌 핵심 암기 (Quick Reference)

{: .highlight }
> **혼동 행렬**: 2개 이상 유목 자료에서 한 유목을 기준으로 다른 유목 결합 분류 판정 행렬
> - (구성) `참참거거` TP, TN, FP, FN

---

## 핵심 키워드

`TP` `TN` `FP` `FN` `정확도` `정밀도` `재현율`

---

## 정의/개념

2개 이상 유목 자료에서 한 유목을 기준으로 다른 유목 결합 분류 판정 행렬

---

## 혼동 행렬 구조

|  | 예측: Positive | 예측: Negative |
|:-----|:--------------|:--------------|
| **실제: Positive** | TP (True Positive) | FN (False Negative) |
| **실제: Negative** | FP (False Positive) | TN (True Negative) |

---

## 구성 요소 `참참거거`

| 암기 | 요소 | 설명 | 의미 |
|:-----|:-----|:-----|:-----|
| **참** | TP | 참을 참으로 예측 | 정답 |
| **참** | TN | 거짓을 거짓으로 예측 | 정답 |
| **거** | FP | 거짓을 참으로 예측 | 오답 (1종 오류) |
| **거** | FN | 참을 거짓으로 예측 | 오답 (2종 오류) |

---

## 평가 지표

| 지표 | 수식 | 의미 |
|:-----|:-----|:-----|
| **정확도 (Accuracy)** | (TP+TN)/(TP+TN+FP+FN) | 전체 정답률 |
| **정밀도 (Precision)** | TP/(TP+FP) | 예측 Positive 중 정답 |
| **재현율 (Recall)** | TP/(TP+FN) | 실제 Positive 중 정답 |
| **F1 Score** | 2×(P×R)/(P+R) | 정밀도와 재현율의 조화평균 |

---

## 연계 토픽

- [정밀도/재현율]({{ site.baseurl }}/docs/ai/06-ml-evaluation/precision-recall)
- [ROC Curve]({{ site.baseurl }}/docs/ai/06-ml-evaluation/roc-curve)

---

## 학습 체크리스트

- [ ] 혼동 행렬 정의 암기
- [ ] TP, TN, FP, FN 구분 설명
- [ ] 평가 지표 수식 암기
