---
layout: default
title: 경사하강법(Gradient Descent)
parent: 1. 기계학습
grand_parent: AI (인공지능)
nav_order: 15
---

# 경사하강법(Gradient Descent)
{: .fs-8 }

6. 퍼셉트론
{: .label .label-purple }

---

## 🎯 기술사 수준 설명

### 📌 핵심 암기 (Quick Reference)

{: .highlight }
> **경사하강법**: 함수의 기울기(경사)를 구하여 기울기가 낮은 쪽으로 계속 이동시켜 극 값에 이를 때까지 반복시키는 1차 근사값 발견을 위한 최적화 알고리즘
> - (알고리즘) `확배미` 확률적(SGD), 배치(BGD), 미니배치
> - ⭐ **차별점**: Local Minimum 문제 - initial point를 다양하게 변경하여 global minimum 찾음

---

## 핵심 키워드

`Initial Weight` `Gradient` `Global Cost Minimum` `Stop Condition` `SGD` `BGD`

---

## 정의/개념

함수의 기울기(경사)를 구하여 기울기가 낮은 쪽으로 계속 이동시켜 극 값에 이를 때까지 반복시키는 1차 근사값 발견을 위한 최적화 알고리즘

---

## 구성요소

### 데이터

| 항목 | 설명 |
|:-----|:-----|
| **Initial Weight** | 초기 가중치 |
| **Gradient** | 기울기(경사) |
| **Global Cost Minimum** | 최저값 |
| **Stop Condition** | 학습 완료 조건 |

---

## 알고리즘 `확배미`

| 암기 | 항목 | 설명 |
|:-----|:-----|:-----|
| **확** | 확률적 경사하강법 (SGD) | 하강변화 심함, 랜덤하게 하강, 데이터 학습시마다 갱신, 지역최저점 빠질 수 있음 |
| **배** | 배치 경사하강법 (BGD) | 하나의 배치로 묶어서 하강, 전체데이터 학습 후 하강, 수렴이 안정적 |
| **미** | 미니배치 경사하강법 | 전체 배치를 사이즈로 나누고 각 배치로 학습, BGD보다 적은 계산 |

---

## 개념도

```
    Loss
      │
      │  ●                    Local Minimum
      │   ╲
      │    ╲  ●               ← 경사가 높은 곳
      │     ╲  ╲
      │      ●──●             ← 경사를 따라 이동
      │          ╲
      │           ●
      │            ╲
      │             ●         Global Minimum
      └───────────────────→ Weight
```

---

## Local/Global Minimum 문제

| 문제 | 설명 | 해결방안 |
|:-----|:-----|:---------|
| **Local Minimum** | 국소 최저점에 수렴 | initial point를 다양하게 변경 |
| **Gradient Vanishing** | MLP 적용시 학습 layer가 깊어질수록 기울기 소멸 | ReLU, LSTM 활용 |

---

## 연계 토픽

- [기울기 소실]({{ site.baseurl }}/docs/ai/01-machine-learning/vanishing-gradient)
- [활성화 함수]({{ site.baseurl }}/docs/ai/01-machine-learning/activation-function)
- [역전파]({{ site.baseurl }}/docs/ai/01-machine-learning/perceptron)

---

## 학습 체크리스트

- [ ] 경사하강법 정의 암기
- [ ] `확배미` 알고리즘 3가지 차이 설명
- [ ] Local/Global Minimum 문제와 해결방안 설명

