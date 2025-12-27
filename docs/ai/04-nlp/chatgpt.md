---
layout: default
title: ChatGPT
parent: 4. 자연어처리
grand_parent: AI (인공지능)
nav_order: 3
---

# ChatGPT
{: .fs-8 }

자연어처리
{: .label .label-purple }

---

## 🎯 기술사 수준 설명

### 📌 핵심 암기 (Quick Reference)

{: .highlight }
> **ChatGPT**: 사전학습(Pre-Trained) Transformer를 활용한 텍스트 생성 언어모델
> - (기술요소) `RLHF`: 인간 피드백 강화학습
> - (구성) Base LLM, RLHF
> - (활용) 검색엔진, 챗봇, 코딩, 가상비서

---

## 핵심 키워드

`GPT` `Pre-Trained` `RLHF` `LLM` `인간 피드백`

---

## 정의/개념

사전학습(Pre-Trained) Transformer를 활용한 텍스트 생성 언어모델

---

## 구성

| 구성 | 설명 |
|:-----|:-----|
| **Base LLM** | 기본 대규모 언어 모델, 텍스트 데이터 학습 |
| **RLHF** | Reinforcement Learning from Human Feedback, 인간 피드백 강화학습 |

---

## RLHF 프로세스

```
1. 초기 모델 학습 (Supervised Learning)
   ↓
2. Reward 모델 학습 (인간 평가 기반)
   ↓
3. 강화학습으로 최적화 (PPO)
```

---

## 활용 분야

| 분야 | 설명 |
|:-----|:-----|
| **검색엔진** | 질문-답변 형태 검색 |
| **챗봇** | 대화형 AI 서비스 |
| **코딩** | 코드 생성 및 설명 |
| **가상비서** | 개인화 서비스 |

---

## GPT 모델 발전

| 버전 | 파라미터 수 | 특징 |
|:-----|:-----------|:-----|
| **GPT-1** | 1.17억 | 기초 모델 |
| **GPT-2** | 15억 | 텍스트 생성 능력 향상 |
| **GPT-3** | 1,750억 | 퓨샷 러닝 |
| **GPT-4** | 비공개 | 멀티모달, 향상된 추론 |

---

## 연계 토픽

- [트랜스포머]({{ site.baseurl }}/docs/ai/04-nlp/transformer)
- [강화학습]({{ site.baseurl }}/docs/ai/01-machine-learning/reinforcement-learning)

---

## 학습 체크리스트

- [ ] ChatGPT 정의 암기
- [ ] RLHF 개념 설명
- [ ] 구성(Base LLM, RLHF) 설명
- [ ] 활용 분야 4가지 나열
