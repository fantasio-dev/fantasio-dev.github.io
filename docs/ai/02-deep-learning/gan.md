---
layout: default
title: GAN
parent: 2. 딥러닝
grand_parent: AI (인공지능)
nav_order: 11
---

<!-- CSV_APPLIED: 기술사_기본필수노트_AI - AI.csv | NO=23 | 중토픽=GAN (Generative Adversarial Network) -->
# GAN
{: .fs-8 }

7. 신경망 알고리즘
{: .label .label-green }

---

## 🎯 기술사 수준 설명

### 📌 핵심 암기 (Quick Reference)

{: .highlight }
> **GAN (Generative Adversarial Network)**: 생성자(Generator)와 판별자(Discriminator)가 서로 경쟁(적대적)하는 과정을 통해 정보를 학습하는 대표적 비지도학습
> - 암기: `제디파트` `편진븡`
> - 키워드: `GAN` `Generator` `Discriminator`

---

<div class="exam-concept-block" markdown="1">

## 🧠 개념 영역

### 🔑 핵심 키워드 3개

| 키워드 | 설명 | 예시 |
|:--|:--|:--|
| **GAN** | 핵심 개념/대상 | - |
| **Generator** | 주요 기법/구성요소 | - |
| **Discriminator** | 절차/평가/특징 | - |

---

### 📖 등장배경

| 구분 | 내용 |
|:--|:--|
| **문제/필요성** | 생성자(Generator)와 판별자(Discriminator)가 서로 경쟁(적대적)하는 과정을 통해 정보를 학습하는 대표적 비지도학습 |
| **활용/사례** | - |

---

### 📝 개념 정의

| 구분 | 정의 |
|:--|:--|
| **GAN (Generative Adversarial Network)** | 생성자(Generator)와 판별자(Discriminator)가 서로 경쟁(적대적)하는 과정을 통해 정보를 학습하는 대표적 비지도학습 |

</div>

---

<div class="exam-tech-block" markdown="1">

## 🏗️ 기술 영역

### 구성요소

#### 그룹 1: 구성요소
{: .highlight-purple }

| 암기 | 항목 | 설명 |
|:--|:--|:--|
| **제** | **> Generator** | Zero > Mean Gaussian 노이즈 기반 Fake Sample 생성 |
| **디** | **> Discriminator** | Real Sample과 Fake Sample 구분, 각 확률 Estimate |
| **파** | **> Fine Tune Training** | Generator, Discriminator 학습 오차 보정 |
| **트** | **> Training Data** | 학습데이터 |


</div>

---

<details markdown="1">
<summary><h3 style="display:inline">📖 상세 설명 (클릭해서 펼치기)</h3></summary>

#### 내용

- 생성자(Generator)와 판별자(Discriminator)가 서로 경쟁(적대적)하는 과정을 통해 정보를 학습하는 대표적 비지도학습

#### 특징

- > 적대적모델: 2개 모델을 통한, 새로운 학습을 만드는 프레임워크
- > Min > Max문제: 한쪽은 속이고, 한쪽은 구분하는 확률을 높이는 과정

#### 구성요소

- > Generator: Zero > Mean Gaussian 노이즈 기반 Fake Sample 생성
- > Discriminator: Real Sample과 Fake Sample 구분, 각 확률 Estimate
- > Fine Tune Training: Generator, Discriminator 학습 오차 보정
- > Training Data: 학습데이터

#### GAN문제점

- > 성능편차: Generator와 Discriminator 성능차이, DCGAN활용
- > 모드진동: 속고 속이는 학습만 진행, 학습 기억 사용
- > 모드붕괴: Generator가 Discriminator를 속이는것만 집중

</details>

---

<details markdown="1">
<summary><h3 style="display:inline">🗂️ 기존 내용 (백업)</h3></summary>

# GAN(Generative Adversarial Networks)
{: .fs-8 }

7. 신경망 알고리즘
{: .label .label-green }

---

## 핵심 키워드

`Generator` `Discriminator` `적대적 학습` `내쉬균형 적용`

---

## 정의/개념

Generator, Discriminator, 적대적 학습, 내쉬균형 적용, Fake Data 생성 신경망 알고리즘

---

## 아키텍처

```
                   Generator
                      │
           ┌─────────┴─────────┐
           │                   │
    (z)    │      Fake         │
    Latent ├───→  G(z)  ───────┤
    Vector │                   │          Discriminator
           │                   │              │
           │      Real         │              │      → Fake
           │───→  (x)  ────────┴──────→ [▷] ──┤
           │                                  │      → Real
           │                                  │
           └──────────────────────────────────┘
                    Fine Tune Training
```

---

## 학습원리

| 구분 | 설명 |
|:-----|:-----|
| **목적함수** | $min_G max_D V(D,G) = E_{x \sim P_{data}(x)}[logD(x)] + E_{z \sim P_z(z)}[log(1 - D(G(z)))]$ |
| **활성함수** | Sigmoid function 통한 이진분류, Real 또는 Fake 판별 |
| **Generator** | Zero-Mean 가우시안 노이즈 기반 Fake Sample 생성<br>Real Data와 유사한 특성을 가지도록 학습 |
| **Discriminator** | Real Data와 Fake Data 구별을 위한 확률 계산<br>판별 정확도 향상을 위해 학습 |

### 학습 목표

| 구분 | 설명 |
|:-----|:-----|
| **$max_D V(D)$** | D(x)=1, D(G(z))=0이 되도록 학습, V(D,G) 최대값 |
| **$min_G V(G)$** | D(G(z))=1, V(D,G) 최소값 |

> 학습 불안정, 성능 한계가 존재, 고해상도 이미지 생성불가

---

## 연계 토픽

- [DCGAN](/docs/ai/02-deep-learning/dcgan)
- [딥페이크](/docs/ai/02-deep-learning/gan)
- [VAE](/docs/ai/02-deep-learning/vae)

---

## 학습 체크리스트

- [ ] GAN의 정의와 아키텍처 이해
- [ ] Generator, Discriminator 역할 파악
- [ ] 목적함수 수식 이해
- [ ] 학습 불안정성 문제 인식


</details>

