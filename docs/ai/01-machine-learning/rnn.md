---
layout: default
title: RNN (Recurrent Neural Networks)
parent: 1. 기계학습
grand_parent: AI (인공지능)
nav_order: 12
---

# RNN (Recurrent Neural Networks)
{: .fs-8 }

기계학습
{: .label .label-blue }

---

## 🎯 기술사 수준 설명

### 📌 핵심 암기 (Quick Reference)

{: .highlight }
> **RNN**: 순환신경망 순서가 있는 순차적 데이터(시계열) 처리를 위해 재귀적으로 연결한 신경망 구조
> - (장단점) 이전 출력이 현재의 입력에 영향 / 역전파 학습 중 기울기 소실, 장기 의존성(Long-Term Dependency) 문제
> - (발전) LSTM, GRU로 발전

---

## 핵심 키워드

`순환신경망` `시계열` `재귀` `기울기소실` `LSTM`

---

## 정의/개념

순환신경망 순서가 있는 순차적 데이터(시계열) 처리를 위해 재귀적으로 연결한 신경망 구조

---

## 구조

```
      ┌─────────────────────────────┐
      │                             │
      ▼                             │
┌─────────┐   ┌─────────┐   ┌─────────┐
│  h(t-1) │ → │   h(t)  │ → │  h(t+1) │
└─────────┘   └─────────┘   └─────────┘
      ▲             ▲             ▲
      │             │             │
┌─────────┐   ┌─────────┐   ┌─────────┐
│  x(t-1) │   │   x(t)  │   │  x(t+1) │
└─────────┘   └─────────┘   └─────────┘
```

---

## 장점과 한계

| 항목 | 설명 |
|:-----|:-----|
| **장점** | 이전 출력이 현재의 입력에 영향 (순서 정보 유지) |
| **한계** | 역전파 학습 중 기울기 소실 문제 |
| **한계** | 장기 의존성(Long-Term Dependency) 문제 |

---

## RNN 발전 계보

```
RNN (기본)
  ↓ 기울기 소실 해결
LSTM (Long Short-Term Memory)
  ↓ 경량화
GRU (Gated Recurrent Unit)
```

---

## 활용 분야

| 분야 | 설명 |
|:-----|:-----|
| **자연어처리** | 텍스트 생성, 번역 |
| **시계열 예측** | 주가, 날씨 예측 |
| **음성인식** | 음성→텍스트 변환 |

---

## 연계 토픽

- [LSTM]({{ site.baseurl }}/docs/ai/01-machine-learning/lstm)
- [CNN]({{ site.baseurl }}/docs/ai/01-machine-learning/cnn)
- [기울기소실 문제]({{ site.baseurl }}/docs/ai/01-machine-learning/vanishing-gradient)

---

## 학습 체크리스트

- [ ] RNN 정의 암기
- [ ] 장점과 한계 설명
- [ ] LSTM과의 관계 설명
