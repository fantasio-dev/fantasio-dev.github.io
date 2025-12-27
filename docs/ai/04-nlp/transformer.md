---
layout: default
title: 트랜스포머(Transformer)
parent: 4. 자연어처리
grand_parent: AI (인공지능)
nav_order: 2
---

# 트랜스포머(Transformer)
{: .fs-8 }

자연어처리
{: .label .label-purple }

---

## 🎯 기술사 수준 설명

### 📌 핵심 암기 (Quick Reference)

{: .highlight }
> **트랜스포머**: 라벨링이 필요없는 빠른 AI, CNN, RNN 대체
> - 라벨링 필요 없음: 행렬 병렬 연산처리
> - 의미기반: 의미를 찾는 셀프 어텐션
> - (구성) Input, Encoder/Decoder Block, Self-Attention, Multi-Head Attention, Output
> - ⭐ **차별점**: NLU의 한계 극복 - 각 단어들의 query와 key vector 연산을 통해 관계를 유추, 단어의 거리 무관, 행렬 병렬연산으로 속도 빠름

---

## 핵심 키워드

`Self-Attention` `Multi-Head Attention` `Encoder` `Decoder` `Query` `Key` `Value`

---

## 정의/개념

라벨링이 필요없는 빠른 AI, CNN, RNN 대체
- 라벨링 필요 없음: 행렬 병렬 연산처리
- 의미기반: 의미를 찾는 셀프 어텐션

---

## 구성요소

### Input

| 항목 | 설명 |
|:-----|:-----|
| **Word2Vec / Word Embedding** | 단어를 벡터로 변환 |
| **Positional Encoding** | 위치 정보 추가 |

### Encoder/Decoder Block

| 항목 | 설명 |
|:-----|:-----|
| **Self-Attention** | 각 단어의 vector간 연관도 점수화, Query, Key, Value 벡터 생성 |
| **Multi-Head Attention** | 가중치를 두어 다른 조건으로 학습, 더 많은 후보군 제공 |
| **Add&Normalization** | 추가 및 정규화 |
| **Encoder/Decoder Attention** | 인코더-디코더 간 연결 |

### Output

| 항목 | 설명 |
|:-----|:-----|
| **Linear** | 선형 변환 |
| **Softmax** | 계산편의 softmax를 적용해 합이 1이 되도록 함 |

---

## NLU의 한계 극복

| 항목 | 설명 |
|:-----|:-----|
| **거리 무관** | 각 단어들의 query와 key vector 연산을 통해 관계를 유추하기에 단어의 거리는 무관 |
| **속도 빠름** | 행렬로 병렬연산하므로 속도 빠름 |

---

## Self-Attention 수식

$$
\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V
$$

| 기호 | 설명 |
|:-----|:-----|
| Q | Query (질의) |
| K | Key (키) |
| V | Value (값) |
| d_k | Key 차원 (스케일링) |

---

## 연계 토픽

- [ChatGPT]({{ site.baseurl }}/docs/ai/04-nlp/chatgpt)
- [워드 임베딩]({{ site.baseurl }}/docs/ai/04-nlp/word-embedding)
- [ELECTRA]({{ site.baseurl }}/docs/ai/04-nlp/electra)

---

## 학습 체크리스트

- [ ] 트랜스포머 정의와 특징 암기
- [ ] 구성요소(Input, Encoder/Decoder, Output) 설명
- [ ] Self-Attention 수식 암기
- [ ] NLU 한계 극복 방법 설명
