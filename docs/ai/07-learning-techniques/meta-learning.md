---
layout: default
title: 메타학습(Meta Learning)
parent: 7. 학습 기법
grand_parent: AI (인공지능)
nav_order: 7
---

# 메타학습(Meta Learning)
{: .fs-8 }

학습 기법
{: .label .label-green }

---

## 🎯 기술사 수준 설명

### 📌 핵심 암기 (Quick Reference)

{: .highlight }
> **메타학습**: 아는 것과 모르는 것을 즉각적으로 구분하는 메타인지로부터 시작한 개념, 적은 양의 데이터로도 스스로 학습하고 문제에 적용하는 학습방식
> - (유형) 거리기반, 모델기반, 최적화기반
> - ⭐ **차별점**: 퓨샷러닝 적용 - 적은 데이터로 빠른 학습 가능

---

## 핵심 키워드

`메타인지` `퓨샷러닝` `Prototypical Network` `MAML` `적은 데이터`

---

## 정의/개념

아는 것과 모르는 것을 즉각적으로 구분하는 메타인지로부터 시작한 개념, 적은 양의 데이터로도 스스로 학습하고 문제에 적용하는 학습방식

---

## 유형

| 유형 | 설명 | 대표 기법 |
|:-----|:-----|:---------|
| **거리기반 학습방식** | 거리 측정을 통한 유사도 기반 분류 | Prototypical Network, Relational Network |
| **모델기반 학습방식** | Memory 이용 | RNN |
| **최적화 학습방식** | Model Parameter 최적화 | MAML |

---

## 메타학습 vs 일반 학습

| 비교 | 메타학습 | 일반 학습 |
|:-----|:---------|:---------|
| **데이터 양** | 소량 | 대량 |
| **학습 방식** | 학습하는 방법을 학습 | 직접 학습 |
| **적응력** | 빠른 적응 | 느린 적응 |

---

## 연계 토픽

- [퓨샷러닝]({{ site.baseurl }}/docs/ai/07-learning-techniques/few-shot-learning)
- [전이학습]({{ site.baseurl }}/docs/ai/07-learning-techniques/transfer-learning)

---

## 학습 체크리스트

- [ ] 메타학습 정의 암기
- [ ] 유형 3가지 설명
- [ ] 퓨샷러닝과의 관계 설명
