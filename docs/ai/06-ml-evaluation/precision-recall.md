---
layout: default
title: 정밀도/재현율
parent: 6. 머신러닝 검증·평가
grand_parent: AI (인공지능)
nav_order: 4
---

<!-- CSV_APPLIED: 기술사_기본필수노트_AI - AI.csv | NO=27 | 중토픽=정밀도(Precision) / 재현율(Recall) -->
# 정밀도/재현율
{: .fs-8 }

머신러닝 검증·평가
{: .label .label-yellow }

---

## 🎯 기술사 수준 설명

### 📌 핵심 암기 (Quick Reference)

{: .highlight }
> **정밀도(Precision) / 재현율(Recall)**: [정밀도 > Precision] TP/ TP+FP
> - 암기: `정재정`
> - 키워드: `정밀도` `TP, FP` `TP`

---

<div class="exam-concept-block" markdown="1">

## 🧠 개념 영역

### 🔑 핵심 키워드 3개

| 키워드 | 설명 | 예시 |
|:--|:--|:--|
| **정밀도** | 핵심 개념/대상 | - |
| **TP, FP** | 주요 기법/구성요소 | - |
| **TP** | 절차/평가/특징 | - |

---

### 📖 등장배경

| 구분 | 내용 |
|:--|:--|
| **문제/필요성** | [정밀도 > Precision] TP/ TP+FP |
| **활용/사례** | 정보 검색 분야에서 정밀도(precision)는 검색된 문서들 중 관련 있는 문서들의 비율. |

---

### 📝 개념 정의

| 구분 | 정의 |
|:--|:--|
| **정밀도(Precision) / 재현율(Recall)** | [정밀도 > Precision] TP/ TP+FP |

</div>

---

<div class="exam-tech-block" markdown="1">

## 🏗️ 기술 영역

### 구성요소

#### 그룹 1: 정밀도 > Precision
{: .highlight-purple }

| 항목 | 설명 |
|:--|:--|
| **TP/ TP+FP** | - |
| **> 모델이 True라고 예측한 것 중에서 실제 True인 것의 비율** | - |
| **> 정답이 맞는 것을 예측한 경우(TP, FP)에 대한, 정답을 올바르게 예측한 경우(TP)의 비율** | - |
| **> 정답이라고 예상했던 것들 중 진짜 정답인 것들의 비율** | - |
| **ex) 정보 검색 분야에서 정밀도(precision)는 검색된 문서들 중 관련 있는 문서들의 비율.** | - |


</div>

---

<details markdown="1">
<summary><h3 style="display:inline">📖 상세 설명 (클릭해서 펼치기)</h3></summary>

#### 정밀도 > Precision

- TP/ TP+FP
- > 모델이 True라고 예측한 것 중에서 실제 True인 것의 비율
- > 정답이 맞는 것을 예측한 경우(TP, FP)에 대한, 정답을 올바르게 예측한 경우(TP)의 비율
- > 정답이라고 예상했던 것들 중 진짜 정답인 것들의 비율
- ex) 정보 검색 분야에서 정밀도(precision)는 검색된 문서들 중 관련 있는 문서들의 비율.

#### 재현률 > Recall

- TP/TP+FN
- > 실제 True인 것 중에서 모델이 True라고 예측한 것의 비율
- > 실제 정답이 맞는 것들에 대해(TP, FN), 정답을 올바르게 예측한 경우(TP)의 비율
- > 진짜 정답 중에 모델이 정답이라고 예측한 것들의 비율
- ex)정보 검색 분야에서 재현율(recall)은 관련 있는 문서들 중 실제로 검색된 문서들의 비율

#### 정확도 Accuracy

- Baseline TP+TN / (전체)
- > 직관적 모델 성능 지표

#### F1 Score

- 정밀도 정확도 한번에
- > (정밀도*정확도) / (정밀도 + 정확도)
- > 높을수록 좋음

</details>

---

<details markdown="1">
<summary><h3 style="display:inline">🗂️ 기존 내용 (백업)</h3></summary>

# 정밀도/재현율
{: .fs-8 }

머신러닝 검증·평가
{: .label .label-yellow }

---

## 핵심 키워드

`정밀도` `재현율` `F1 Score` `Trade-off` `임계값`

---

## 정의/개념

*(이미지 내용 추출 후 작성)*

---

## 학습 체크리스트

- [ ] 개념 이해
- [ ] 핵심 키워드 암기
- [ ] 실무 적용 사례 파악


</details>

