---
layout: default
title: 기계독해(MRC)
parent: 4. 자연어처리
grand_parent: AI (인공지능)
nav_order: 5
---

<!-- CSV_APPLIED: 기술사_기본필수노트_AI - AI.csv | NO=29 | 중토픽=기계독해 (Machine Reading Comprehension) -->
# 기계독해(MRC)
{: .fs-8 }

자연어처리
{: .label .label-purple }

---

## 🎯 기술사 수준 설명

### 📌 핵심 암기 (Quick Reference)

{: .highlight }
> **기계독해 (Machine Reading Comprehension)**: 주어진 지문에서 인공지능(AI) 알고리즘이 스스로 문제를 분석하고 질문에 최적화된 답안을 찾아내는 기술
> - 암기: `질매유답` `검독` `지생후`
> - 키워드: `기계독해` `AI` `Human Equivalence Score`

---

<div class="exam-concept-block" markdown="1">

## 🧠 개념 영역

### 🔑 핵심 키워드 3개

| 키워드 | 설명 | 예시 |
|:--|:--|:--|
| **기계독해** | 핵심 개념/대상 | - |
| **AI** | 주요 기법/구성요소 | - |
| **Human Equivalence Score** | 절차/평가/특징 | - |

---

### 📖 등장배경

| 구분 | 내용 |
|:--|:--|
| **문제/필요성** | 주어진 지문에서 인공지능(AI) 알고리즘이 스스로 문제를 분석하고 질문에 최적화된 답안을 찾아내는 기술 |
| **활용/사례** | - |

---

### 📝 개념 정의

| 구분 | 정의 |
|:--|:--|
| **기계독해 (Machine Reading Comprehension)** | 주어진 지문에서 인공지능(AI) 알고리즘이 스스로 문제를 분석하고 질문에 최적화된 답안을 찾아내는 기술 |

</div>

---

<div class="exam-tech-block" markdown="1">

## 🏗️ 기술 영역

### 구성요소

#### 그룹 1: 기계독해 과정
{: .highlight-purple }

| 항목 | 설명 |
|:--|:--|
| **> 사용자질문>문서에대한 매트릭스구성>유사도점수부여>답변생성** | - |
| **+ 검색단계** | - |
| **> TF > IDF** | 어떤 단어가 문서내에서 얼마나 중요한지 여부 |
| **> Term Frequency > Inverse Document Frequency** | - |
| **> TF > IDF 매트릭스구성** | - |
| **> BM25 Score** | 주어진 쿼리와 문서연관성 랭킹 함수 알고리즘 |
| **+ 독해단계** | - |
| **> 토큰화** | 텍스트를 작은 토큰단위로 나눔 |


</div>

---

<details markdown="1">
<summary><h3 style="display:inline">📖 상세 설명 (클릭해서 펼치기)</h3></summary>

#### 내용

- 주어진 지문에서 인공지능(AI) 알고리즘이 스스로 문제를 분석하고 질문에 최적화된 답안을 찾아내는 기술

#### 기계독해 과정

- > 사용자질문>문서에대한 매트릭스구성>유사도점수부여>답변생성
- + 검색단계
- > TF > IDF: 어떤 단어가 문서내에서 얼마나 중요한지 여부
- > Term Frequency > Inverse Document Frequency
- > TF > IDF 매트릭스구성
- > BM25 Score: 주어진 쿼리와 문서연관성 랭킹 함수 알고리즘
- + 독해단계
- > 토큰화: 텍스트를 작은 토큰단위로 나눔
- > Word Embedding: 단어를 기계가 이해하는 숫자로 변환
- > Character Embedding: 문자의 구성을 백터로 생성
- > Contextual Embedding: 문맥에 따라서 벡터로 생성
- > Self Attention: 문장 내의 다른 단어를 보고 힌트를 얻어서 현재단어 반영
- > Point Network: 결과 출력시 정답에 해당하는 부분 index 출력 네트워크

#### 기계독해유형

- EDM
- > Extractive Answer Datasets: 지문에 답변이 존재
- > Descriptive/Narrative Answer Datasets: 답변을 생성
- > Multiple > Choice Datasets: 답변 후보군 중 선택

#### 기계독해평가

- 정밀도 재현율 F1
- > Exact Match: 정확한샘플/전체샘플
- > F1 Score: 2*원래F1 / > ROUGE > L: 재현율 / > BLEU: 정밀도
- > HEQ(Human Equivalence Score): 대화식, 신뢰있는답변

</details>

---

<details markdown="1">
<summary><h3 style="display:inline">🗂️ 기존 내용 (백업)</h3></summary>

# 기계독해 (MRC)
{: .fs-8 }

자연어처리
{: .label .label-purple }

---

## 핵심 키워드

`MRC` `Machine Reading Comprehension` `질의응답` `문서 이해` `BERT`

---

## 정의/개념

*(이미지 내용 추출 후 작성)*

---

## 학습 체크리스트

- [ ] 개념 이해
- [ ] 핵심 키워드 암기
- [ ] 실무 적용 사례 파악


</details>

