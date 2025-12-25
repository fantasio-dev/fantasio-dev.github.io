---
layout: default
title: 지도학습(Supervised Learning)
parent: 1. 기계학습
grand_parent: AI (인공지능)
nav_order: 9
---

# 지도학습(Supervised Learning)
{: .fs-8 }

1.2 지도학습
{: .label .label-purple }

---

## 🎯 기술사 수준 설명

### 📌 핵심 암기 (Quick Reference)

{: .highlight }
> **지도학습**: 분류, 회귀, 평가 → 훈련데이터로부터 함수를 유추하는 기계학습
> - (분류 알고리즘) `스케씨알` SVM, KNN, CNN, RNN
> - (회귀 알고리즘) `선신` 선형회귀분석, 신경망분석
> - (평가) 교차검증, Precision, Recall

---

<div class="exam-concept-block" markdown="1">

## 🧠 개념 영역

### 🔑 핵심 키워드 3개

| 키워드 | 설명 | 예시 |
|:------|:-----|:-----|
| **분류(Classification)** | 정해진 클래스로 데이터 분류 | 스팸메일 필터링, 고양이 영상 탐지 |
| **회귀(Regression)** | 입력→출력 관계를 함수로 예측 | 주가 예측, 수요 예측 |
| **레이블(Label)** | 학습 데이터에 부여된 정답값 | Positive/Negative, 가격값 |

---

### 📖 등장배경

| 구분 | 내용 |
|:-----|:-----|
| **데이터 활용** | 레이블이 있는 훈련데이터로부터 패턴을 학습하여 새로운 데이터 예측 필요 |
| **비즈니스 요구** | 스팸메일 분류, 이미지 인식, 가격 예측 등 실무 문제 해결 요구 증가 |

---

### 📝 개념 정의

| 구분 | 정의 (22자 이내) |
|:-----|:----------------|
| **지도학습** | 레이블 기반 함수 유추 학습 |

</div>

---

<div class="exam-tech-block" markdown="1">

## 🏗️ 기술 영역

### 구성요소 (핵심 암기법 상세) `분회` / `스케씨알` / `선신`

#### 그룹 1: 분류(Classification) 알고리즘 `스케씨알`
{: .highlight-purple }

| 암기 | 항목 | 설명 | 예시 |
|:-----|:-----|:-----|:-----|
| **스** | SVM | 경계선 근접데이터(Support Vector) 분석 | 이진 분류, 다중 분류 |
| **케** | KNN | 거리 기반 K개 이웃 클러스터 할당 | 추천 시스템, 패턴 인식 |
| **씨** | CNN | Convolution, Pooling, FC Layer 구조 | 이미지 인식, 객체 탐지 |
| **알** | RNN | 셀에 정보 저장, 은닉층 순환 구조 | 시계열 분석, 자연어 처리 |

#### 그룹 2: 회귀(Regression) 알고리즘 `선신`
{: .highlight-purple }

| 암기 | 항목 | 설명 | 예시 |
|:-----|:-----|:-----|:-----|
| **선** | 선형회귀분석 | 종속변수와 독립변수 관계 모델링 | 가격 예측, 수요 예측 |
| **신** | 신경망 분석 | 다층 퍼셉트론 기반 비선형 회귀 | 복잡한 패턴 예측 |

#### 그룹 3: 평가(Evaluation)
{: .highlight-purple }

| 항목 | 설명 | 수식/특징 |
|:-----|:-----|:-----|
| **교차검증** | Cross Validation | 훈련/검증 데이터 분리 반복 검증 |
| **정밀도(Precision)** | 예측 True 중 실제 True 비율 | TP / (TP + FP) |
| **재현율(Recall)** | 실제 True 중 예측 True 비율 | TP / (TP + FN) |

</div>

---

<div class="exam-bonus-block" markdown="1">

## ⭐ 차별점 키워드 (가산점 포인트)

{: .important }
> **지도학습 vs 비지도학습 핵심 차이**
> - **레이블 유무**: 지도학습은 정답(Label)이 존재, 비지도학습은 정답 없음
> - **목적**: 지도학습은 예측(Prediction), 비지도학습은 구조 발견(Discovery)
> - **대표 기법**: 분류/회귀 vs 군집/차원축소

</div>

---

<details markdown="1">
<summary><h3 style="display:inline">📖 상세 설명 (클릭해서 펼치기)</h3></summary>

#### 📊 분류 vs 군집 vs 회귀 비교

| 비교 | 분류 | 군집 | 회귀 |
|:-----|:-----|:-----|:-----|
| **개념도** | +/- 그룹 분리선 | ○ 그룹핑 | 데이터 추세선 |
| **목적** | 새로운 데이터 그룹 예측 | 데이터 특성 군집화 | 함수식으로 값 예측 |
| **학습유형** | 지도 학습 | 비지도 학습 | 지도 학습 |
| **레이블** | 있음 | 없음 | 있음 |
| **사례** | 필기체 인식, 스팸필터 | 구매자 분류, 환자군 | 투자예측, 수요예측 |

#### 🔄 지도학습 프로세스

```
[훈련데이터] → [특징추출] → [모델학습] → [검증] → [예측]
     ↑                                    ↓
  레이블 O ←────── 정답 비교 ───────────→ 오차 계산
```

#### 📈 상위 토픽 계층도

```
기계학습 (Machine Learning)
├── 지도학습 (Supervised Learning) ⭐
│   ├── 분류: SVM, KNN, CNN, RNN
│   └── 회귀: 선형회귀, 신경망
├── 비지도학습 (Unsupervised Learning)
│   ├── 군집화: K-means, DBSCAN
│   └── 차원축소: PCA, ICA
└── 강화학습 (Reinforcement Learning)
    └── Q-Learning, Deep Q-Learning
```

#### ✅ 학습 체크리스트

- [ ] 지도학습 개념 정의 22자로 말할 수 있다
- [ ] `스케씨알` 분류 알고리즘 4개 설명 가능
- [ ] `선신` 회귀 알고리즘 2개 설명 가능
- [ ] 분류 vs 군집 vs 회귀 차이점 설명 가능
- [ ] Precision, Recall 정의 및 수식 설명 가능

</details>

---

## 🧠 암기법 / 핵심 구문

{: .highlight }
> 지도학습 암기: **`분회 스케씨알 선신`**
> - **분**류: `스케씨알` (SVM, KNN, CNN, RNN)
> - **회**귀: `선신` (선형회귀, 신경망)

---

## 연계 토픽

- [SVM(서포트 벡터 머신)](/docs/ai/01-machine-learning/svm)
- [KNN](/docs/ai/01-machine-learning/knn)
- [CNN](/docs/ai/01-machine-learning/cnn)
- [RNN](/docs/ai/01-machine-learning/rnn)
- [선형 회귀](/docs/ai/01-machine-learning/linear-regression)
- [비지도학습](/docs/ai/01-machine-learning/unsupervised-learning)

---

## 참고자료

- 정보관리기술사 AI 학습자료
- 기술사 기본필수노트 AI
