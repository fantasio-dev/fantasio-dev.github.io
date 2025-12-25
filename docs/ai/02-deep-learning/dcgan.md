---
layout: default
title: DCGAN
parent: 2. 딥러닝
grand_parent: AI (인공지능)
nav_order: 12
---

<!-- CSV_APPLIED: 기술사_기본필수노트_AI - AI.csv | NO=24 | 중토픽=DCGAN (Deep Convolutional GAN) -->
# DCGAN
{: .fs-8 }

7. 신경망 알고리즘
{: .label .label-green }

---

## 🎯 기술사 수준 설명

### 📌 핵심 암기 (Quick Reference)

{: .highlight }
> **DCGAN (Deep Convolutional GAN)**: GAN의 Fully Connected Layer를 제거하고 Convolution Layer와 배치정규화 구조를 사용하여 안정적인 학습이 가능한 알고리즘
> - 암기: `컨배풀풀` `RLT`
> - 키워드: `DCGAN` `평균 0, 분산 1` `Rectified Linear Unit`

---

<div class="exam-concept-block" markdown="1">

## 🧠 개념 영역

### 🔑 핵심 키워드 3개

| 키워드 | 설명 | 예시 |
|:--|:--|:--|
| **DCGAN** | 핵심 개념/대상 | - |
| **평균 0, 분산 1** | 주요 기법/구성요소 | - |
| **Rectified Linear Unit** | 절차/평가/특징 | - |

---

### 📖 등장배경

| 구분 | 내용 |
|:--|:--|
| **문제/필요성** | GAN의 Fully Connected Layer를 제거하고 Convolution Layer와 배치정규화 구조를 사용하여 안정적인 학습이 가능한 알고리즘 |
| **활용/사례** | - |

---

### 📝 개념 정의

| 구분 | 정의 |
|:--|:--|
| **DCGAN (Deep Convolutional GAN)** | GAN의 Fully Connected Layer를 제거하고 Convolution Layer와 배치정규화 구조를 사용하여 안정적인 학습이 가능한 알고리즘 |

</div>

---

<div class="exam-tech-block" markdown="1">

## 🏗️ 기술 영역

### 구성요소

#### 그룹 1: 구성요소
{: .highlight-purple }

| 항목 | 설명 |
|:--|:--|
| **> 네트워크구조** | - |
| **> Convolution** | Filter > Feature Map |
| **> 배치정규화** | 활성화 함수 값의 정규분포화(평균 0, 분산 1), 기울기감소 해결 |
| **> Fully > connected hidden layers 삭제** | - |
| **> Pooling Layer 사용안함** | - |
| **> 활성화 함수** | - |
| **> ReLU(Rectified Linear Unit)** | 생성자층 사용 |
| **> Tanh** | 출력층 사용 |


</div>

---

<details markdown="1">
<summary><h3 style="display:inline">📖 상세 설명 (클릭해서 펼치기)</h3></summary>

#### 내용

- GAN의 Fully Connected Layer를 제거하고 Convolution Layer와 배치정규화 구조를 사용하여 안정적인 학습이 가능한 알고리즘
- > Convolution 적용, Pooling 적용 X

#### 구성요소

- > 네트워크구조
- > Convolution: Filter > Feature Map
- > 배치정규화: 활성화 함수 값의 정규분포화(평균 0, 분산 1), 기울기감소 해결
- > Fully > connected hidden layers 삭제
- > Pooling Layer 사용안함
- > 활성화 함수
- > ReLU(Rectified Linear Unit): 생성자층 사용
- > Tanh: 출력층 사용
- > Leaky ReLU: 판별자층 사용, 음수 ReLU

</details>

---

<details markdown="1">
<summary><h3 style="display:inline">🗂️ 기존 내용 (백업)</h3></summary>

# DCGAN(Deep Convolution GAN)
{: .fs-8 }

7. 신경망 알고리즘
{: .label .label-green }

---

## 핵심 키워드

`GAN Fully Connected Layer 제거` `배치 정규화 구조 사용` `Fractional-Strided Convolution`

---

## 정의/개념

GAN Fully Connected Layer 제거, 배치 정규화 구조 사용 GAN 알고리즘

---

## 아키텍처

```
Generator:
┌─────┐    ┌─────┐    ┌─────┐    ┌─────┐    ┌─────┐
│  In │ →  │DeConv1│ → │DeConv2│ → │DeConv3│ → │DeConv4│
└─────┘    └─────┘    └─────┘    └─────┘    └─────┘
4x4x512    8x8x256    16x16x128  32x32x64   64x64x3
(Random)   (BN,ReLU)  (BN,ReLU)  (BN,ReLU)  (BN,tanh)

Discriminator:
┌─────┐    ┌─────┐    ┌─────┐    ┌─────┐    ┌─────┐
│  In │ →  │Conv1 │ → │Conv2 │ → │Conv3 │ → │Conv4 │
└─────┘    └─────┘    └─────┘    └─────┘    └─────┘
64x64x3    32x32x32   16x16x64   8x8x128    4x4x256
           (BN,ReLU)  (BN,ReLU)  (BN,ReLU)  (ReLU)

                    Image generated
```

---

## 기술 구성요소

| 구분 | 구성요소 | 핵심 |
|:-----|:---------|:-----|
| **네트워크 구조** | Convolution | Feature Map, Filter, Stride, Padding |
| | Fractional-Strided Convolution | 이미지 업스케일링 수행 |
| | 배치정규화 | 활성화 함수 값의 정규분포화(평균0, 분산1) |
| **활성화 함수** | ReLU | 생성자 모든 층 ReLU사용 |
| | Tanh | 마지막 결과 도출 시 Tanh 사용 |
| | Leaky ReLU | 판별자 모든 층 Leaky ReLU 사용 |

---

## GAN vs DCGAN 비교

| 구분 | GAN | DCGAN |
|:-----|:----|:------|
| **구조** | Fully Connected Layer 사용 | Fully Connected Layer 제거 |
| **정규화** | 없음 | 배치 정규화 사용 |
| **활성화 함수** | 단순 | 층별 다른 활성화 함수 사용 |
| **이미지 품질** | 저품질 | 고품질 |

---

## 연계 토픽

- [GAN](/docs/ai/02-deep-learning/gan)
- [CNN](/docs/ai/02-deep-learning/cnn)

---

## 학습 체크리스트

- [ ] DCGAN의 정의와 아키텍처 이해
- [ ] GAN과의 차이점(FC Layer 제거, 배치정규화) 파악
- [ ] 네트워크 구조 및 활성화 함수 특징 암기


</details>

