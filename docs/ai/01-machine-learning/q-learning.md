---
layout: default
title: Q-Learning
parent: 1. 기계학습
grand_parent: AI (인공지능)
nav_order: 25
---

<!-- CSV_APPLIED: 기술사_기본필수노트_AI - AI.csv | NO=25 | 중토픽=Q-러닝 -->
# Q-Learning
{: .fs-8 }

1.4 강화학습
{: .label .label-yellow }

---

## 🎯 기술사 수준 설명

### 📌 핵심 암기 (Quick Reference)

{: .highlight }
> **Q-러닝**: Q > Learning은 Model이 없이(Model > Free) 학습하는 강화학습 알고리즘
> - 암기: `Model` `Free,` `Q` `정벨큐` `최미` `반재` `테근` `초액관업반`
> - 키워드: `Q-러닝` `Model > Free` `Quality`

---

<div class="exam-concept-block" markdown="1">

## 🧠 개념 영역

### 🔑 핵심 키워드 3개

| 키워드 | 설명 | 예시 |
|:--|:--|:--|
| **Q-러닝** | 핵심 개념/대상 | - |
| **Model > Free** | 주요 기법/구성요소 | - |
| **Quality** | 절차/평가/특징 | - |

---

### 📖 등장배경

| 구분 | 내용 |
|:--|:--|
| **문제/필요성** | Q > Learning은 Model이 없이(Model > Free) 학습하는 강화학습 알고리즘 |
| **활용/사례** | - |

---

### 📝 개념 정의

| 구분 | 정의 |
|:--|:--|
| **Q-러닝** | Q > Learning은 Model이 없이(Model > Free) 학습하는 강화학습 알고리즘 |

</div>

---

<div class="exam-tech-block" markdown="1">

## 🏗️ 기술 영역

### 구성요소

#### 그룹 1: 구성요소
{: .highlight-purple }

| 항목 | 설명 |
|:--|:--|
| **> 정책** | 최대보상(최고 Q값에 따른 액션), 미래보상관찰(미래 기대) |
| **> 벨만방정식** | 정책반복(최적 보상 찾기), 재귀함수(현재최고보상, 미래보상) |
| **> Q러닝** | 테이블 기반(벨만방적식 반복), 반복적 근사(반복을 통한 Q근사) |
| ***벨만 기대 방정식은 현재 상태의 가치함수와 다음 상태의 가치함수 사이의 관계** | - |


</div>

---

<details markdown="1">
<summary><h3 style="display:inline">📖 상세 설명 (클릭해서 펼치기)</h3></summary>

#### 내용

- Q > Learning은 Model이 없이(Model > Free) 학습하는 강화학습 알고리즘

#### 특징

- > 강화학습, Model > Free
- > Q: 현재 상태에서 취한 행동의 보상에 대한 미래의 보상들의 종합적인 품질(Quality) 기대값.

#### 구성요소

- > 정책: 최대보상(최고 Q값에 따른 액션), 미래보상관찰(미래 기대)
- > 벨만방정식:정책반복(최적 보상 찾기), 재귀함수(현재최고보상, 미래보상)
- > Q러닝:테이블 기반(벨만방적식 반복), 반복적 근사(반복을 통한 Q근사)
- *벨만 기대 방정식은 현재 상태의 가치함수와 다음 상태의 가치함수 사이의 관계

#### 절차

- ① value table Q 초기화
- ②정책 기반 Action 선택/수행
- ③새로운 상태 및 보상 관찰
- ④다음상태 최대보상 업데이트
- ⑤새로운 상태 설정, 반복수행

#### 강화학습

- > Deep Q > Learning: 기존 Q > 러닝에서 Q테이블을 딥러닝 CNN으로 변경한 것임.
- > Markov Chain: 마르코프 성질( 특정 미래 상태의 확률은 오직 과거의 상태에 의존)

</details>

---

<details markdown="1">
<summary><h3 style="display:inline">🗂️ 기존 내용 (백업)</h3></summary>

# Q-Learning
{: .fs-8 }

1.4 강화학습
{: .label .label-yellow }

---

## 핵심 키워드

`Q함수 사용` `최적의 정책 학습` `Q-Table` `Agent` `Reward 구성`

---

## 정의/개념

에이전트가 특정 상태에서 특정 행동을 취했을 때 얻을 수 있는 기대 보상을 학습하는 강화학습 기법

---

## 프로세스

| # | 프로세스 |
|:--|:--------|
| 1 | Q 테이블 초기화 |
| 2 | 현재 상태 관찰 |
| 3 | Action 선택 |
| 4 | Reward 확인 |
| 5 | 새로운 상태 관찰 |
| 6 | Q 테이블 갱신 |

---

## 구성요소

| 구분 | 기술요소 | 설명 |
|:-----|:---------|:-----|
| **Q 함수** | 벨만 방정식 | 현재 상태의 가치함수와 다음 상태의 가치함수 사이의 관계를 표현한 방정식<br>Q(s,a) = r + lr * max(Q(s',a')) |
| | Q 함수 | 입력값이 state(현재상태), action(동작)이고, 출력이 reward(보상값)인 함수<br>Q(state, action) = reward |
| | MAX Q | 임의의 상태 s(state)에서 Q 가 가질 수 있는 최대 보상값<br>Q(state, action) = reward |
| | 정책(π) | 임의의 상태 s(state)에서 Q 가 최대값을 가지게 하는 a(action)값<br>π*(s) = argmax Q(s, a) |
| **Q Learning 알고리즘** | Q-Table | 각각의 state-s 에서 각각의 action-a 이가지는 Q(s,a)값을 모두 포함하는 테이블 |
| | 학습률 | Q 값의 갱신 완급을 결정하는 파라미터 |
| | Agent | Q-Table 을 기준으로 매 state 에서 가장 적절한 action 을 선택 |
| | Rewards | Agent 의 Action 에 따른 보상값<br>최대 보상값을 탐색하여 선택 |

---

## 연계 토픽

- [DQN](/docs/ai/01-machine-learning/deep-reinforcement-learning)
- [강화학습](/docs/ai/01-machine-learning/reinforcement-learning)
- [MDP](/docs/ai/01-machine-learning/mdp)

---

## 학습 체크리스트

- [ ] Q-Learning의 정의와 프로세스 이해
- [ ] 벨만 방정식과 Q 함수 개념 파악
- [ ] Q-Table의 역할 이해


</details>

