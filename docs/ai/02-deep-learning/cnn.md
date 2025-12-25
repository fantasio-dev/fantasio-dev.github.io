---
layout: default
title: CNN
parent: 2. 딥러닝
grand_parent: AI (인공지능)
nav_order: 28
---

<!-- CSV_APPLIED: 기술사_기본필수노트_AI - AI.csv | NO=12 | 중토픽=CNN -->
# CNN
{: .fs-8 }

2.1 딥러닝
{: .label .label-blue }

---

## 🎯 기술사 수준 설명

### 📌 핵심 암기 (Quick Reference)

{: .highlight }
> **CNN**: 데이터의 대비를 높여서 특징 추출 분석
> - 암기: `CPF` `RDB`
> - 키워드: `CNN` `feature` `Convolution`

---

<div class="exam-concept-block" markdown="1">

## 🧠 개념 영역

### 🔑 핵심 키워드 3개

| 키워드 | 설명 | 예시 |
|:--|:--|:--|
| **CNN** | 핵심 개념/대상 | - |
| **feature** | 주요 기법/구성요소 | - |
| **Convolution** | 절차/평가/특징 | - |

---

### 📖 등장배경

| 구분 | 내용 |
|:--|:--|
| **문제/필요성** | 데이터의 대비를 높여서 특징 추출 분석 |
| **활용/사례** | - |

---

### 📝 개념 정의

| 구분 | 정의 |
|:--|:--|
| **CNN** | 데이터의 대비를 높여서 특징 추출 분석 |

</div>

---

<div class="exam-tech-block" markdown="1">

## 🏗️ 기술 영역

### 구성요소

#### 그룹 1: Layer 구성
{: .highlight-purple }

| 항목 | 설명 |
|:--|:--|
| **> Convolution Layer** | - |
| **> 합성곱(Convolution) 연산을 통해 Feature를 추출하는 레이어** | - |
| **> Pooling Layer** | - |
| **> Sub Sampling을 통한 차원의 축소** | - |
| **> Fully Connected Layer** | - |
| **> Convolution, Pooling 처리결과** | - |


</div>

---

<details markdown="1">
<summary><h3 style="display:inline">📖 상세 설명 (클릭해서 펼치기)</h3></summary>

#### 내용

- 데이터의 대비를 높여서 특징 추출 분석

#### 동작방식

- > Convolution Layer를 통한 특징(feature) 추출
- > Pooling Layer를 통한 차원 축소
- > Fully Connected Layer를 통한 최종 분류

#### Layer 구성

- > Convolution Layer
- > 합성곱(Convolution) 연산을 통해 Feature를 추출하는 레이어
- > Pooling Layer
- > Sub Sampling을 통한 차원의 축소
- > Fully Connected Layer
- > Convolution, Pooling 처리결과

#### 성능 개선

- > ReLU: 0 > 1 활성화 함수, 기울기소실 해결
- > Dropout: 인공 신경망의 Overfitting 방지 위해 특정 뉴런 미동작 학습 수행
- > Bigdata: 과적합(Overfitting) 문제 해결, 여러 데이터의 경험 누적"

</details>

---

<details markdown="1">
<summary><h3 style="display:inline">🗂️ 기존 내용 (백업)</h3></summary>

# CNN(Convolutional Neural Network)
{: .fs-8 }

2.1 딥러닝
{: .label .label-blue }

---

## 핵심 키워드

`Convolution` `Pooling` `Fully Connected Layer`

---

## 정의/개념

영상, 이미지 처리 목적 Convolution, Pooling, Fully Connected Layer 구성 신경망 알고리즘

---

## 개념도

```
                                           ┌─── bird    Pbird
                                           │
  ┌──────┐    ┌──────┐    ┌──────┐        │─── sunset  Psunset
  │ 🦅   │    │      │    │      │        │
  │ 이미지 │ → │ conv │ → │ pool │ → ... → │─── dog     Pdog
  │      │    │      │    │      │        │
  └──────┘    └──────┘    └──────┘        │─── cat     Pcat
              convolution  max pooling     └─────────────────
              + nonlinearity              fully connected layers
                                          Nx binary classification
```

---

## 계층(Layer) 구성요소

| 계층(Layer) | 특징 | 설명 |
|:------------|:-----|:-----|
| **Convolution** | Feature Map<br>Filter | 이미지를 분류하기 위한 특징을 추출<br>Filter에서 추출한 각각의 Feature 집합<br>Edge filter, Convolution Filter |
| **Pooling** | Max Pooling<br>Down Sampling | Feature Map 대표값 추출<br>기존 이미지 축소 및 형태 유지 |
| **Fully Connected** | Dropout<br>flatten<br>Classification | 오버피팅을 막기 위한 정규화 작업<br>각 Layer를 1차원 벡터로 변환하는 평탄화 작업<br>Softmax 함수 등을 사용하여 Output 분류 |

> CNN 각 Layer의 성능 향상을 위해 하이퍼파라미터 사용자 조정 필요

---

## 연계 토픽

- [RNN](/docs/ai/02-deep-learning/rnn)
- [YOLO](/docs/ai/01-machine-learning/yolo)
- [Pooling Layer](/docs/ai/01-machine-learning/pooling-layer)

---

## 학습 체크리스트

- [ ] CNN의 정의와 구조 이해
- [ ] 3가지 계층(Convolution, Pooling, Fully Connected) 역할 암기
- [ ] 각 계층의 특징과 설명 파악


</details>

