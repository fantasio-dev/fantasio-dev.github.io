---
layout: default
title: 워드 임베딩(Word Embedding)
parent: 4. 자연어처리
grand_parent: AI (인공지능)
nav_order: 3
---

<!-- CSV_APPLIED: 기술사_기본필수노트_AI - AI.csv | NO=41 | 중토픽=워드 임베딩 -->
# 워드 임베딩(Word Embedding)
{: .fs-8 }

자연어
{: .label .label-purple }

---

## 🎯 기술사 수준 설명

### 📌 핵심 암기 (Quick Reference)

{: .highlight }
> **워드 임베딩**: 전체 단어들 간의 관계에 맞춰 해당 단어의 특성을 갖는 벡터로 바꿔주므로 단어들 사이의 유사도를 계산하는 기법
> - 암기: `통텀핫` `신워벗`
> - 키워드: `워드 임베딩` `Term > Document Matrix` `TDM`

---

<div class="exam-concept-block" markdown="1">

## 🧠 개념 영역

### 🔑 핵심 키워드 3개

| 키워드 | 설명 | 예시 |
|:--|:--|:--|
| **워드 임베딩** | 핵심 개념/대상 | - |
| **Term > Document Matrix** | 주요 기법/구성요소 | - |
| **TDM** | 절차/평가/특징 | - |

---

### 📖 등장배경

| 구분 | 내용 |
|:--|:--|
| **문제/필요성** | 전체 단어들 간의 관계에 맞춰 해당 단어의 특성을 갖는 벡터로 바꿔주므로 단어들 사이의 유사도를 계산하는 기법 |
| **활용/사례** | - |

---

### 📝 개념 정의

| 구분 | 정의 |
|:--|:--|
| **워드 임베딩** | 전체 단어들 간의 관계에 맞춰 해당 단어의 특성을 갖는 벡터로 바꿔주므로 단어들 사이의 유사도를 계산하는 기법 |

</div>

---

<div class="exam-tech-block" markdown="1">

## 🏗️ 기술 영역

### 구성요소

#### 그룹 1: 기술의 발전 측면 기술유형
{: .highlight-purple }

| 암기 | 항목 | 설명 |
|:--|:--|:--|
| **통** | **통텀핫 신워벗** | - |
| **텀** | **> 통계적 기반** | TDM(Term > Document Matrix), TF > IDF, One > hot Encoding |
| **핫** | **> 신경망 기반** | Word2Vec, BERT |


</div>

---

<details markdown="1">
<summary><h3 style="display:inline">📖 상세 설명 (클릭해서 펼치기)</h3></summary>

#### 내용

- 전체 단어들 간의 관계에 맞춰 해당 단어의 특성을 갖는 벡터로 바꿔주므로 단어들 사이의 유사도를 계산하는 기법

#### 기술의 발전 측면 기술유형

- 통텀핫 신워벗
- > 통계적 기반: TDM(Term > Document Matrix), TF > IDF, One > hot Encoding
- > 신경망 기반: Word2Vec, BERT

#### 임베딩 수준 측면 기술유형

- > 단어 수준의 임베딩: Word2Vec, FastText, ELMo(Embedding from Language Models)
- > 문장 수준의 임베딩: BERT, GPT

</details>

---

<details markdown="1">
<summary><h3 style="display:inline">🗂️ 기존 내용 (백업)</h3></summary>

# 워드 임베딩(Word Embedding)
{: .fs-8 }

자연어
{: .label .label-purple }

---

## 🎯 기술사 수준 설명

### 📌 핵심 암기 (Quick Reference)

{: .highlight }
> **워드 임베딩**: 단어들 간의 관계에 맞춰 해당 단어를 벡터로 변환하는 기법
> - (통계적 기반) `통텀핫` TDM, TF-IDF, One-hot Encoding
> - (신경망 기반) `신워벗` Word2Vec, BERT

---

<div class="exam-concept-block" markdown="1">

## 🧠 개념 영역

### 🔑 핵심 키워드 3개

| 키워드 | 설명 | 예시 |
|:------|:-----|:-----|
| **벡터 변환** | 단어를 숫자 벡터로 변환 | [0.2, 0.5, 0.3] |
| **유사도 계산** | 단어 간 유사도 측정 | 코사인 유사도 |
| **의미 표현** | 단어의 의미를 벡터로 표현 | 유사 단어 근접 |

---

### 📖 등장배경

| 구분 | 내용 |
|:-----|:-----|
| **컴퓨터 이해** | 컴퓨터가 단어를 이해하려면 숫자로 변환 필요 |
| **의미 반영** | 단어의 의미를 반영한 표현 필요 |

---

### 📝 개념 정의

| 구분 | 정의 |
|:-----|:-----|
| **워드 임베딩** | 단어들 간의 관계에 맞춰 특성을 갖는 벡터로 변환하는 기법 |

</div>

---

<div class="exam-tech-block" markdown="1">

## 🏗️ 기술 영역

### 통계적 기반 `통텀핫` / 신경망 기반 `신워벗`

#### 통계적 기반 `통텀핫`
{: .highlight-purple }

| 암기 | 항목 | 설명 |
|:-----|:-----|:-----|
| **통** | TDM(Term-Document Matrix) | 용어-문서 행렬 |
| **텀** | TF-IDF | 단어 중요도 측정 |
| **핫** | One-hot Encoding | 단어를 희소 벡터로 표현 |

#### 신경망 기반 `신워벗`
{: .highlight-purple }

| 암기 | 항목 | 설명 |
|:-----|:-----|:-----|
| **신** | 신경망 기반 | 딥러닝 활용 |
| **워** | Word2Vec | CBOW, Skip-gram |
| **벗** | BERT | 양방향 트랜스포머 |

#### 임베딩 수준
{: .highlight-purple }

| 수준 | 기법 |
|:-----|:-----|
| **단어 수준** | Word2Vec, FastText, ELMo |
| **문장 수준** | BERT, GPT |

</div>

---

<div class="exam-bonus-block" markdown="1">

## ⭐ 차별점 키워드 (가산점 포인트)

{: .important }
> **워드 임베딩 핵심**
> - **유사도 계산**: 벡터 간 거리/각도로 유사도 측정
> - **밀집 벡터**: One-hot(희소) → Word2Vec(밀집)
> - **문맥 반영**: ELMo, BERT는 문맥에 따라 다른 벡터

</div>

---

<details markdown="1">
<summary><h3 style="display:inline">📖 상세 설명 (클릭해서 펼치기)</h3></summary>

#### ✅ 학습 체크리스트

- [ ] 워드 임베딩 정의 말할 수 있다
- [ ] `통텀핫` 통계적 기반 3가지 설명 가능
- [ ] `신워벗` 신경망 기반 설명 가능
- [ ] 단어 수준 vs 문장 수준 차이 설명 가능

</details>

---

## 연계 토픽

- [BERT](/docs/ai/04-nlp/bert)
- [트랜스포머](/docs/ai/04-nlp/transformer)
- [TF-IDF](/docs/ai/04-nlp/tf-idf)

</details>

