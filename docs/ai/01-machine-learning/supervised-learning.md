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
> **지도학습**: 훈련데이터(Training Data)로부터 하나의 함수를 유추해내기 위한 기계학습 방법
> - (분류) `스케씨알` SVM, KNN, CNN, RNN
> - (회귀) `선신` 선형회귀분석, 신경망분석

---

<div class="exam-concept-block" markdown="1">

## 🧠 개념 영역

### 🔑 핵심 키워드 3개

| 키워드 | 설명 | 예시 |
|:------|:-----|:-----|
| **훈련데이터** | 레이블(정답)이 있는 학습 데이터 | 고양이 이미지 + "고양이" 레이블 |
| **분류(Classification)** | 데이터를 정해진 클래스로 분류 | 스팸메일 필터링 |
| **회귀(Regression)** | 입력에 대한 출력값 예측 | 주가 예측 |

---

### 📖 등장배경

| 구분 | 내용 |
|:-----|:-----|
| **데이터 활용** | 레이블이 있는 훈련데이터로부터 패턴을 학습하여 새로운 데이터 예측 필요 |
| **활용 사례** | 고양이 모습의 특징을 학습시키고 유투브에서 고양이 영상 찾기, 스팸메일 분류 |

---

### 📝 개념 정의

| 구분 | 정의 |
|:-----|:-----|
| **지도학습** | 훈련데이터로부터 함수를 유추하는 기계학습 방법 |

</div>

---

<div class="exam-tech-block" markdown="1">

## 🏗️ 기술 영역

### 구성요소 `분회` / `스케씨알` / `선신`

#### 그룹 1: 분류(Classification) 알고리즘 `스케씨알`
{: .highlight-purple }

| 암기 | 항목 | 설명 |
|:-----|:-----|:-----|
| **스** | SVM(Support Vector Machines) | 경계선 근접데이터(SV) 분석 |
| **케** | KNN(K-Nearest Neighbor) | 거리기반 많은 속성을 가진 클러스터 할당 |
| **씨** | CNN(Convolutional Neural) | Convolution, Pooling layer, Fully connected layer |
| **알** | RNN(Recurrent) | 셀에 정보저장, 은닉층 |

#### 그룹 2: 회귀(Regression) 알고리즘 `선신`
{: .highlight-purple }

| 암기 | 항목 | 설명 |
|:-----|:-----|:-----|
| **선** | 선형회귀분석 | 종속변수와 한개이상의 독립변수 관계 모델링 |
| **신** | 신경망(Neural networks) 분석 | 다층 퍼셉트론 기반 비선형 회귀 |

#### 평가(Evaluation)
{: .highlight-purple }

| 항목 | 설명 |
|:-----|:-----|
| **교차검증(Cross Validation)** | 훈련/검증 데이터 분리 반복 검증 |
| **정밀도(Precision)** | 예측 True 중 실제 True 비율 |
| **재현율(Recall)** | 실제 True 중 예측 True 비율 |

</div>

---

<div class="exam-bonus-block" markdown="1">

## ⭐ 차별점 키워드 (가산점 포인트)

{: .important }
> **지도학습 vs 비지도학습**
> - **레이블**: 지도학습은 정답(Label) 존재 / 비지도학습은 정답 없음
> - **목적**: 예측(Prediction) vs 구조 발견(Discovery)

</div>

---

<details markdown="1">
<summary><h3 style="display:inline">📖 상세 설명 (클릭해서 펼치기)</h3></summary>

#### 📊 분류 vs 군집 vs 회귀 비교

| 비교 | 분류 | 군집 | 회귀 |
|:-----|:-----|:-----|:-----|
| **목적** | Label 기반 그룹 예측 | 데이터 특성 군집화 | 함수식으로 값 예측 |
| **학습유형** | 지도 학습 | 비지도 학습 | 지도 학습 |
| **레이블** | 있음 | 없음 | 있음 |
| **사례** | 필기체 인식, 스팸필터 | 구매자 분류, 환자군 | 투자예측, 수요예측 |
| **알고리즘** | KNN, SVM | K-means, Clustering | 선형회귀, 로지스틱 |

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

- [ ] 지도학습 개념 정의 말할 수 있다
- [ ] `스케씨알` 분류 알고리즘 4개 설명 가능
- [ ] `선신` 회귀 알고리즘 2개 설명 가능
- [ ] Precision, Recall 정의 설명 가능

</details>

---

## 연계 토픽

- [SVM(서포트 벡터 머신)]({{ site.baseurl }}/docs/ai/01-machine-learning/svm)
- [KNN]({{ site.baseurl }}/docs/ai/01-machine-learning/knn)
- [CNN]({{ site.baseurl }}/docs/ai/02-deep-learning/cnn)
- [RNN]({{ site.baseurl }}/docs/ai/02-deep-learning/rnn)
- [비지도학습]({{ site.baseurl }}/docs/ai/01-machine-learning/unsupervised-learning)
