---
layout: default
title: 과적합/과소적합
parent: 2. 딥러닝
grand_parent: AI (인공지능)
nav_order: 8
---

<!-- CSV_APPLIED: 기술사_기본필수노트_AI - AI.csv | NO=10 | 중토픽=과적합(overfitting)문제 -->
# 과적합/과소적합
{: .fs-8 }

2.2 딥러닝 문제/이슈
{: .label .label-yellow }

---

## 🎯 기술사 수준 설명

### 📌 핵심 암기 (Quick Reference)

{: .highlight }
> **과적합(overfitting)문제**: 과적합(overfitting)문제: 감독학습(Supervised Learning)에서 과거의 학습데이터에 대해서는 잘 예측하지만 새로 들어온 데이터에 대해서 성능이 떨어져서 일반화가 어려운 문제
> - 암기: `학튜분데복` `축제드감분`
> - 키워드: `과적합` `overfitting` `Supervised Learning`

---

<div class="exam-concept-block" markdown="1">

## 🧠 개념 영역

### 🔑 핵심 키워드 3개

| 키워드 | 설명 | 예시 |
|:--|:--|:--|
| **과적합** | 핵심 개념/대상 | - |
| **overfitting** | 주요 기법/구성요소 | - |
| **Supervised Learning** | 절차/평가/특징 | - |

---

### 📖 등장배경

| 구분 | 내용 |
|:--|:--|
| **문제/필요성** | 과적합(overfitting)문제: 감독학습(Supervised Learning)에서 과거의 학습데이터에 대해서는 잘 예측하지만 새로 들어온 데이터에 대해서 성능이 떨어져서 일반화가 어려운 문제 |
| **활용/사례** | - |

---

### 📝 개념 정의

| 구분 | 정의 |
|:--|:--|
| **과적합(overfitting)문제** | 과적합(overfitting)문제: 감독학습(Supervised Learning)에서 과거의 학습데이터에 대해서는 잘 예측하지만 새로 들어온 데이터에 대해서 성능이 떨어져서 일반화가 어려운 문제 |

</div>

---

<div class="exam-tech-block" markdown="1">

## 🏗️ 기술 영역

### 구성요소

#### 그룹 1: 발생원인
{: .highlight-purple }

| 암기 | 항목 | 설명 |
|:--|:--|:--|
| **학** | **> 지나친 학습** | Overtraining |
| **튜** | **> 지나친 튜닝** | Over > fitting due to Noise |
| **분** | **> 분류문제** | 범주 별 데이터셋을 잘 분류하지 못한 경우 |
| **데** | **> 데이터 부족** | Over > fitting due to Insufficient example |
| **복** | **> 복잡한 모형** | unnecessarily complex model |


</div>

---

<details markdown="1">
<summary><h3 style="display:inline">📖 상세 설명 (클릭해서 펼치기)</h3></summary>

#### 내용

- 과적합(overfitting)문제: 감독학습(Supervised Learning)에서 과거의 학습데이터에 대해서는 잘 예측하지만 새로 들어온 데이터에 대해서 성능이 떨어져서 일반화가 어려운 문제

#### 발생원인

- > 지나친 학습: Overtraining
- > 지나친 튜닝: Over > fitting due to Noise
- > 분류문제: 범주 별 데이터셋을 잘 분류하지 못한 경우
- > 데이터 부족: Over > fitting due to Insufficient example
- > 복잡한 모형: unnecessarily complex model

#### 해결방안

- > 차원축소: PCA(Principal Component Analysis): 주성분분석, 3차원 > 2차원
- > Regularization(제한): 람다항에 추가 페널티 부여, 출력층사용
- > DropOut: 특정 은닉층 제거 또는, 데이터 0으로 만들어 누락
- > 감소: 모수(parameter)의 수 감소, 은닉층 감소
- > 분석/검증: 앙상블/Cross Validation

#### 내용

- Overfitting과 Underfitting

</details>

---

<details markdown="1">
<summary><h3 style="display:inline">🗂️ 기존 내용 (백업)</h3></summary>

# 과적합/과소적합
{: .fs-8 }

2.2 딥러닝 문제/이슈
{: .label .label-yellow }

---

## 핵심 키워드

`과적합` `과소적합` `일반화` `정규화` `검증`

---

## 정의/개념

*(이미지 내용 추출 후 작성)*

---

## 학습 체크리스트

- [ ] 개념 이해
- [ ] 핵심 키워드 암기
- [ ] 실무 적용 사례 파악


</details>

