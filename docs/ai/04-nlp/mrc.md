---
layout: default
title: 기계독해 (MRC)
parent: 4. 자연어처리
grand_parent: AI (인공지능)
nav_order: 4
---

# 기계독해 (MRC)
{: .fs-8 }

자연어처리
{: .label .label-purple }

---

## 🎯 기술사 수준 설명

### 📌 핵심 암기 (Quick Reference)

{: .highlight }
> **기계독해 (Machine Reading Comprehension)**: 주어진 지문을 이해하고 질문에 대한 정답을 찾는 자연어 처리 기술
> - (유형) `추불다다` 추출형, 불가능형, 다중선택형, 다중문서
> - ⭐ **차별점**: 질의응답(QA) 시스템의 핵심 기술

---

## 핵심 키워드

`지문 이해` `질의응답` `QA` `BERT` `추출형`

---

## 정의/개념

주어진 지문을 이해하고 질문에 대한 정답을 찾는 자연어 처리 기술

---

## 유형 `추불다다`

| 암기 | 유형 | 설명 |
|:-----|:-----|:-----|
| **추** | 추출형 (Extractive) | 지문에서 정답 구간 추출 |
| **불** | 불가능형 (Unanswerable) | 답변 불가 여부 판단 포함 |
| **다** | 다중선택형 (Multi-choice) | 보기 중 정답 선택 |
| **다** | 다중문서 (Multi-passage) | 여러 문서에서 정답 탐색 |

---

## MRC 프로세스

```
1. 지문 (Context) 입력
      ↓
2. 질문 (Question) 입력
      ↓
3. 지문-질문 인코딩 (BERT 등)
      ↓
4. 정답 위치/내용 예측
      ↓
5. 정답 (Answer) 출력
```

---

## 대표 데이터셋

| 데이터셋 | 특징 |
|:---------|:-----|
| **SQuAD** | 위키피디아 기반 추출형 |
| **KorQuAD** | 한국어 기계독해 |
| **CoQA** | 대화형 질의응답 |

---

## 연계 토픽

- [트랜스포머]({{ site.baseurl }}/docs/ai/04-nlp/transformer)
- [ELECTRA]({{ site.baseurl }}/docs/ai/04-nlp/electra)
- [워드 임베딩]({{ site.baseurl }}/docs/ai/04-nlp/word-embedding)

---

## 학습 체크리스트

- [ ] MRC 정의 암기
- [ ] `추불다다` 유형 4가지 설명
- [ ] 프로세스 설명
