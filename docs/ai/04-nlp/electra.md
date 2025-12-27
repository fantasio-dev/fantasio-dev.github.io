---
layout: default
title: ELECTRA
parent: 4. 자연어처리
grand_parent: AI (인공지능)
nav_order: 5
---

# ELECTRA
{: .fs-8 }

자연어처리
{: .label .label-purple }

---

## 🎯 기술사 수준 설명

### 📌 핵심 암기 (Quick Reference)

{: .highlight }
> **ELECTRA**: Efficiently Learning an Encoder that Classifies Token Replacements Accurately
> - BERT 학습 비효율성을 개선하는 Pre-Train 언어 모델
> - 모든 토큰에 대해 학습하여 효율성 개선
> - (구성) 생성기, 판별기
> - ⭐ **차별점**: 마스킹 대신 대체 토큰 탐지 방식으로 효율적 학습

---

## 핵심 키워드

`사전학습` `토큰 대체` `생성기` `판별기` `효율성`

---

## 정의/개념

BERT 학습 비효율성을 개선하는 Pre-Train 언어 모델, 모든 토큰에 대해 학습하여 효율성 개선

---

## 구성

| 구성 | 역할 |
|:-----|:-----|
| **생성기 (Generator)** | 마스킹된 토큰을 대체 토큰으로 생성 |
| **판별기 (Discriminator)** | 각 토큰이 원본인지 대체된 것인지 판별 |

---

## ELECTRA vs BERT

| 항목 | BERT | ELECTRA |
|:-----|:-----|:--------|
| **학습 방식** | 마스킹된 토큰만 예측 | 모든 토큰에 대해 판별 |
| **학습 효율** | 15% 토큰만 학습 | 100% 토큰 학습 |
| **학습 속도** | 느림 | 빠름 |

---

## 동작 방식

```
원본: "The chef cooked the meal"
      ↓
마스킹: "The [MASK] cooked the [MASK]"
      ↓
생성기: "The artist cooked the fish"
      ↓
판별기: [원본, 대체됨, 원본, 원본, 대체됨]
```

---

## 연계 토픽

- [트랜스포머]({{ site.baseurl }}/docs/ai/04-nlp/transformer)
- [기계독해 (MRC)]({{ site.baseurl }}/docs/ai/04-nlp/mrc)
- [워드 임베딩]({{ site.baseurl }}/docs/ai/04-nlp/word-embedding)

---

## 학습 체크리스트

- [ ] ELECTRA 정의 암기
- [ ] BERT와의 차이점 설명
- [ ] 생성기와 판별기 역할 설명
