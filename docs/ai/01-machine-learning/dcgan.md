---
layout: default
title: DCGAN (Deep Convolutional GAN)
parent: 1. 기계학습
grand_parent: AI (인공지능)
nav_order: 22
---

# DCGAN (Deep Convolutional GAN)
{: .fs-8 }

기계학습
{: .label .label-blue }

---

## 🎯 기술사 수준 설명

### 📌 핵심 암기 (Quick Reference)

{: .highlight }
> **DCGAN**: GAN에 CNN을 결합한 모델, 안정적인 고품질 이미지 생성
> - (구성) 합성곱 생성자, 합성곱 판별자
> - (핵심 기법) 스트라이드 합성곱, 배치 정규화, LeakyReLU
> - ⭐ **차별점**: 풀링 레이어 제거, 전치 합성곱 사용

---

## 핵심 키워드

`CNN` `GAN` `전치합성곱` `배치정규화` `스트라이드`

---

## 정의/개념

GAN에 CNN을 결합한 모델, 안정적인 고품질 이미지 생성

---

## 구성

| 구성 | 설명 |
|:-----|:-----|
| **생성자** | 전치 합성곱(Transposed Convolution)으로 이미지 업샘플링 |
| **판별자** | 스트라이드 합성곱으로 이미지 다운샘플링 |

---

## DCGAN 핵심 기법

| 기법 | 설명 |
|:-----|:-----|
| **풀링 제거** | 스트라이드 합성곱으로 대체 |
| **배치 정규화** | 학습 안정화 |
| **전치 합성곱** | 생성자에서 업샘플링 |
| **LeakyReLU** | 판별자에서 사용 |

---

## DCGAN 구조

```
생성자 (Generator)
┌──────┐   ┌──────┐   ┌──────┐   ┌──────┐
│ 노이즈 │ → │전치Conv│ → │전치Conv│ → │ 이미지 │
│ (z)  │   │ +BN   │   │ +BN   │   │      │
└──────┘   └──────┘   └──────┘   └──────┘

판별자 (Discriminator)
┌──────┐   ┌──────┐   ┌──────┐   ┌──────┐
│이미지 │ → │ Conv  │ → │ Conv  │ → │진짜/가짜│
│      │   │ +LReLU│   │ +LReLU│   │      │
└──────┘   └──────┘   └──────┘   └──────┘
```

---

## GAN vs DCGAN

| 항목 | GAN | DCGAN |
|:-----|:----|:------|
| **구조** | 완전연결층 | 합성곱층 |
| **이미지 품질** | 낮음 | 높음 |
| **학습 안정성** | 불안정 | 안정적 |

---

## 연계 토픽

- [GAN]({{ site.baseurl }}/docs/ai/01-machine-learning/gan)
- [CNN]({{ site.baseurl }}/docs/ai/01-machine-learning/cnn)

---

## 학습 체크리스트

- [ ] DCGAN 정의 암기
- [ ] 핵심 기법 4가지 설명
- [ ] GAN과의 차이점 설명
