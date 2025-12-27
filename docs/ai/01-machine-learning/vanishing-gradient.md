---
layout: default
title: 기울기소실 문제(Vanishing Gradient)
parent: 1. 기계학습
grand_parent: AI (인공지능)
nav_order: 7
---

# 기울기소실 문제(Vanishing Gradient)
{: .fs-8 }

기계학습
{: .label .label-blue }

---

## 🎯 기술사 수준 설명

### 📌 핵심 암기 (Quick Reference)

{: .highlight }
> **기울기소실 문제**: 역전파(Backpropagation) 학습에서 입력층으로 갈수록 기울기가 0으로 수렴하여 학습이 잘 안되는 문제
> - (해결방안) `활배잔` 활성화함수변경(ReLU), 배치정규화, 잔차학습

---

## 핵심 키워드

`역전파` `Backpropagation` `Sigmoid` `ReLU` `배치정규화` `잔차학습`

---

## 정의/개념

역전파(Backpropagation) 학습에서 입력층으로 갈수록 기울기가 0으로 수렴하여 학습이 잘 안되는 문제

---

## 발생 원인

```
출력층 → 은닉층 → 은닉층 → 입력층
  ↓         ↓         ↓
기울기    기울기     기울기
 큼       작음      매우 작음 → 0 수렴
```

- Sigmoid/Tanh의 기울기 범위: 0~0.25
- 층이 깊을수록 기울기가 곱해져 0에 수렴

---

## 해결방안 `활배잔`

| 암기 | 방안 | 설명 |
|:-----|:-----|:-----|
| **활** | 활성화함수변경 | ReLU 사용 (기울기 1 유지) |
| **배** | 배치정규화 | Batch Normalization으로 분포 안정화 |
| **잔** | 잔차학습 | Residual Connection (Skip Connection) |

---

## ReLU가 해결하는 이유

| 함수 | 기울기 범위 | 문제 |
|:-----|:-----------|:-----|
| **Sigmoid** | 0~0.25 | 곱해질수록 0 수렴 |
| **ReLU** | 0 또는 1 | 양수 영역에서 기울기 1 유지 |

---

## 연계 토픽

- [활성화 함수]({{ site.baseurl }}/docs/ai/01-machine-learning/activation-function)
- [경사 하강법]({{ site.baseurl }}/docs/ai/01-machine-learning/gradient-descent)
- [드랍아웃]({{ site.baseurl }}/docs/ai/01-machine-learning/dropout)

---

## 학습 체크리스트

- [ ] 기울기소실 문제 정의 암기
- [ ] 발생 원인 설명
- [ ] `활배잔` 해결방안 3가지 설명
