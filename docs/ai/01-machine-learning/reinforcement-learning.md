---
layout: default
title: 강화학습
parent: 1. 기계학습
grand_parent: AI (인공지능)
nav_order: 22
---

<!-- CSV_APPLIED: 기술사_기본필수노트_AI - AI.csv | NO=3 | 중토픽=강화학습 (Reinforcement Learning) -->
# 강화학습
{: .fs-8 }

1.4 강화학습
{: .label .label-yellow }

---

## 🎯 기술사 수준 설명

### 📌 핵심 암기 (Quick Reference)

{: .highlight }
> **강화학습 (Reinforcement Learning)**: 어떤 환경 안에서 정의된 에이전트가 현재의 상태를 인식하여, 선택 가능한 행동들 중 보상을 최대화하는 행동 혹은 행동 순서를 선택
> - 암기: `Reward,` `의사결정` `큐딥` `역강화` `학습`
> - 키워드: `강화학습` `Reward` `신경망`

---

<div class="exam-concept-block" markdown="1">

## 🧠 개념 영역

### 🔑 핵심 키워드 3개

| 키워드 | 설명 | 예시 |
|:--|:--|:--|
| **강화학습** | 핵심 개념/대상 | - |
| **Reward** | 주요 기법/구성요소 | - |
| **신경망** | 절차/평가/특징 | - |

---

### 📖 등장배경

| 구분 | 내용 |
|:--|:--|
| **문제/필요성** | 어떤 환경 안에서 정의된 에이전트가 현재의 상태를 인식하여, 선택 가능한 행동들 중 보상을 최대화하는 행동 혹은 행동 순서를 선택 |
| **활용/사례** | - |

---

### 📝 개념 정의

| 구분 | 정의 |
|:--|:--|
| **강화학습 (Reinforcement Learning)** | 어떤 환경 안에서 정의된 에이전트가 현재의 상태를 인식하여, 선택 가능한 행동들 중 보상을 최대화하는 행동 혹은 행동 순서를 선택 |

</div>

---

<div class="exam-tech-block" markdown="1">

## 🏗️ 기술 영역

### 구성요소

#### 그룹 1: 역강화학습(Inverse Reinforcement Learning)
{: .highlight-purple }

| 항목 | 설명 |
|:--|:--|
| **> 보상함수를 구하는 학습** | 최적 선택을 할 경우를 감안하여 계산 |
| **> 보상함수구현 어려움** | 실세계에서 특정 모델에 대한 보상 함수를 구하는 것은 매우 복잡한 문제 |
| **> 보상함수다중속성** | 보상 함수는 단일 속성이 아닌 다속성으로 구성되는 경우가 대부분 |
| **> 미지보장추가고려** | 보상 함수를 정의할 때 미지의 보상 속성까지 추가적으로 고려 |


</div>

---

<details markdown="1">
<summary><h3 style="display:inline">📖 상세 설명 (클릭해서 펼치기)</h3></summary>

#### 내용

- 어떤 환경 안에서 정의된 에이전트가 현재의 상태를 인식하여, 선택 가능한 행동들 중 보상을 최대화하는 행동 혹은 행동 순서를 선택

#### 특징

- > Reward
- > 순차적의사결정: 관측순서에 따른 영향

#### 알고리즘

- > Q > Learning: state/action > Q Table > Q > Value(Reward)
- > Deep Q > Learning: state > Q Network(신경망) > 여러개 Q Value

#### 역강화학습(Inverse Reinforcement Learning)

- > 보상함수를 구하는 학습: 최적 선택을 할 경우를 감안하여 계산
- > 보상함수구현 어려움: 실세계에서 특정 모델에 대한 보상 함수를 구하는 것은 매우 복잡한 문제
- > 보상함수다중속성: 보상 함수는 단일 속성이 아닌 다속성으로 구성되는 경우가 대부분
- > 미지보장추가고려: 보상 함수를 정의할 때 미지의 보상 속성까지 추가적으로 고려

</details>

---

<details markdown="1">
<summary><h3 style="display:inline">🗂️ 기존 내용 (백업)</h3></summary>

# 강화학습(Reinforcement Learning)
{: .fs-8 }

1.4 강화학습
{: .label .label-yellow }

---

## 핵심 키워드

`Agent` `State` `Action` `Environment` `Reward 최대화`

---

## 정의/개념

에이전트가 환경과 상호작용하며 보상을 최대화하는 방법을 학습하는 기계 학습

---

## 개념도

```
                    ┌─────────┐
                    │  Agent  │
                    └────┬────┘
                         │
              ┌──────────┼──────────┐
              ↓          │          ↓
         State(s)     Reward(r)   Action(a)
              │          │          │
              └──────────┼──────────┘
                         │
                    ┌────┴────┐
                    │Environment│
                    └──────────┘
```

---

## 기법

| # | 기법 | 핵심 |
|:--|:-----|:-----|
| 1 | **MDP** | 강화학습 수식화 지원 알고리즘 |
| 2 | **Markov Chain** | 다음 단어가 나올 확률 예측 방식 |
| 3 | **Q-learning** | Q 함수 사용 |
| 4 | **DQN** | 딥러닝과 Q러닝 조합 |

---

## 연계 토픽

- [심층강화학습](/docs/ai/01-machine-learning/deep-reinforcement-learning)
- [Q-Learning](/docs/ai/01-machine-learning/q-learning)
- [MDP](/docs/ai/01-machine-learning/mdp)

---

## 학습 체크리스트

- [ ] 강화학습의 정의와 개념도 이해
- [ ] 구성요소(Agent, State, Action, Environment, Reward) 암기
- [ ] 주요 기법(MDP, Markov Chain, Q-learning, DQN) 파악


</details>

