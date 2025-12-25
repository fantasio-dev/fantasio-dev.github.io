---
layout: default
title: Transformer
parent: 4. 자연어처리
grand_parent: AI (인공지능)
nav_order: 2
---

<!-- CSV_APPLIED: 기술사_기본필수노트_AI - AI.csv | NO=37 | 중토픽=트랜스포머 -->
# Transformer
{: .fs-8 }

자연어처리
{: .label .label-purple }

---

## 🎯 기술사 수준 설명

### 📌 핵심 암기 (Quick Reference)

{: .highlight }
> **트랜스포머**: 라벨링이 필요없는 빠른 AI, CNN, RNN 대체 > 트랜스포머
> - 암기: `입벡임` `인디셀멀정합` `출리소`
> - 키워드: `트랜스포머` `AI` `CNN`

---

<div class="exam-concept-block" markdown="1">

## 🧠 개념 영역

### 🔑 핵심 키워드 3개

| 키워드 | 설명 | 예시 |
|:--|:--|:--|
| **트랜스포머** | 핵심 개념/대상 | - |
| **AI** | 주요 기법/구성요소 | - |
| **CNN** | 절차/평가/특징 | - |

---

### 📖 등장배경

| 구분 | 내용 |
|:--|:--|
| **문제/필요성** | 라벨링이 필요없는 빠른 AI, CNN, RNN 대체 > 트랜스포머 |
| **활용/사례** | - |

---

### 📝 개념 정의

| 구분 | 정의 |
|:--|:--|
| **트랜스포머** | 라벨링이 필요없는 빠른 AI, CNN, RNN 대체 > 트랜스포머 |

</div>

---

<div class="exam-tech-block" markdown="1">

## 🏗️ 기술 영역

### 구성요소

#### 그룹 1: 구성요소
{: .highlight-purple }

| 항목 | 설명 |
|:--|:--|
| **> Input** | Word2Vec / Word Embedding |
| **> Encoder/Decoder Block** | - |
| **> Self > Attention** | 각 단어의 vector간 연관도 점수화, Query, Key, Value 벡터 생성 |
| **> Multi > Head Attention** | 가중치를 두어 다른 조건으로 학습, 더 많은 후보군 제공 |
| **> Add&Nomalization** | 추가 및 정규화 |
| **> Encoder/Decoder Attention** | - |
| **> Output** | Linear > Softmax |
| **> 계산편의 softmax를 적용해 합이 1이 되도록 한다** | - |


</div>

---

<details markdown="1">
<summary><h3 style="display:inline">📖 상세 설명 (클릭해서 펼치기)</h3></summary>

#### 내용

- 라벨링이 필요없는 빠른 AI, CNN, RNN 대체 > 트랜스포머
- > 라벨링 필요 없음: 행렬 병렬 연산처리
- > 의미기반: 의미를 찾는 셀프 어텐션

#### 구성요소

- > Input: Word2Vec / Word Embedding
- > Encoder/Decoder Block
- > Self > Attention: 각 단어의 vector간 연관도 점수화, Query, Key, Value 벡터 생성
- > Multi > Head Attention: 가중치를 두어 다른 조건으로 학습, 더 많은 후보군 제공
- > Add&Nomalization: 추가 및 정규화
- > Encoder/Decoder Attention
- > Output: Linear > Softmax
- > 계산편의 softmax를 적용해 합이 1이 되도록 한다
- * NLU의 한계 극복
- > 각 단어들의 query와 key vector 연산을 통해 관계를 유추하기에 단어의 거리는 무관
- > 행렬로 병렬연산하므로 속도 빠름

</details>

---

<details markdown="1">
<summary><h3 style="display:inline">🗂️ 기존 내용 (백업)</h3></summary>

# 트랜스포머(Transformer)
{: .fs-8 }

자연어처리
{: .label .label-purple }

---

## 핵심 키워드

`인코더` `디코더` `어텐션 메커니즘` `자연어 처리` `셀프 어텐션 레이어(self-attention layer)` `피드포워드(feedforward) 레이어` `마스크드 멀티-헤드 어텐션(multi-head attention) 레이어`

---

## 정의/개념

어텐션 메커니즘을 사용하여 입력된 문장을 병렬적으로 처리하여 문장 내 단어들의 위치 정보를 보존하면서 효율적으로 처리하는 자연어처리(NLP)를 위한 딥러닝 모델

---

## 아키텍처

```
                              ┌─────────┐
                              │ Softmax │
                              └────┬────┘
                              ┌────┴────┐
                              │ Linear  │
                              └────┬────┘
                         ┌─────────┴─────────┐
                         │   피드포워드 신경망   │
                         └─────────┬─────────┘
            ┌────────────────────┐ │
            │     <인코더>        │ │
       Nx   │  ┌───────────────┐ │ │  ┌───────────────┐   Nx
      (6회) │  │피드포워드 신경망│ │ │  │  인코더-디코더  │  (6회)
            │  └───────────────┘ │ │  │    어텐션     │
            │  ┌───────────────┐ │ │  └───────────────┘
            │  │  인코더 셀프   │ │ │  ┌───────────────┐
            │  │    어텐션     │ │──▶│  마스크드 셀프   │
            │  └───────────────┘ │    │    어텐션     │
            └────────────────────┘    └───────────────┘
                      │                       │
            ┌─────────┴─────────┐ ┌───────────┴───────────┐
            │  포지셔널 인코딩   │ │    포지셔널 인코딩     │
            └─────────┬─────────┘ └───────────┬───────────┘
            ┌─────────┴─────────┐ ┌───────────┴───────────┐
            │      임베딩       │ │        임베딩         │
            └─────────┬─────────┘ └───────────┬───────────┘
                      │                       │
                   <입력>                  <출력>
```

---

## 구성요소

### 입력 (Input)

| 구성요소 | 설명 |
|:---------|:-----|
| **포지셔널 인코딩 (Positional Encoding)** | 입력단어의 위치 값 추가<br>- 사인, 코사인 함수 이용<br>- RNN 미 적용으로 인한 단어 위치 문제해결 |

### 인코더 (Encoder)

| 구성요소 | 설명 |
|:---------|:-----|
| **인코더 셀프 어텐션 (Encoder Self-Attention)** | 멀티 헤드 셀프 어텐션: 입력 토큰 병렬처리<br>- Query=Key=Value<br>- 6개의 인코더가 이전 인코더의 어텐션 참조 |
| **피드 포워드 신경망 (Feed Forward NN)** | Position-Wise 완전 연결망<br>- 잔차(Residual) 연결이용 및 정규화 수행 |

### 디코더 (Decoder)

| 구성요소 | 설명 |
|:---------|:-----|
| **마스크드 셀프 어텐션 (Masked Self-Attention)** | 멀티 헤드 셀프 어텐션: 입력 토큰 병렬처리<br>- Query=Key=Value<br>- 현재 이후 단어 마스킹 처리 |
| **인코더-디코더 어텐션** | 셀프 어텐션 아님<br>- 인코더 어텐션과 디코더 어텐션 결합 사용<br>- 인코더 셀프 어텐션=Key=Value<br>- 디코더 셀프 어텐션=Query |
| **피드 포워드 신경망** | 인코더 구조와 동일 |

### 출력 (Output)

| 구성요소 | 설명 |
|:---------|:-----|
| **Linear Layer (Fully Connected Layer)** | 디코더 출력을 벡터화하여 신경망 연결 |
| **Softmax** | 출력단어 예측 |

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
| $d_k$ | Key 차원 (스케일링) |

---

## Transformer vs RNN 비교

| 구분 | Transformer | RNN |
|:-----|:------------|:----|
| **처리 방식** | 병렬 처리 | 순차 처리 |
| **장거리 의존성** | 강함 (Self-Attention) | 약함 (Vanishing Gradient) |
| **학습 속도** | 빠름 | 느림 |
| **위치 정보** | Positional Encoding | 순서대로 처리 |

---

## 연계 토픽

- [NLP 기초](/docs/ai/04-nlp/nlp-basics)
- [ChatGPT](/docs/ai/04-nlp/chatgpt)
- [생성형AI](/docs/ai/04-nlp/chatgpt)

---

## 학습 체크리스트

- [ ] Transformer 아키텍처의 인코더-디코더 구조 이해
- [ ] Self-Attention 메커니즘 수식 암기
- [ ] 구성요소별 역할 파악 (포지셔널 인코딩, 멀티헤드 어텐션 등)


</details>

