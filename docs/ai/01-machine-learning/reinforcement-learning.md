---
layout: default
title: 강화학습(Reinforcement Learning)
parent: 1. 기계학습
grand_parent: AI (인공지능)
nav_order: 22
---

# 강화학습(Reinforcement Learning)
{: .fs-8 }

1.4 강화학습
{: .label .label-yellow }

---

## 🎯 기술사 수준 설명

### 📌 핵심 암기 (Quick Reference)

{: .highlight }
> **강화학습**: 어떤 환경 안에서 정의된 에이전트가 현재의 상태를 인식하여, 선택 가능한 행동들 중 보상을 최대화하는 행동 혹은 행동 순서를 선택
> - (알고리즘) `큐딥` Q-Learning, Deep Q-Learning
> - (역강화학습) 보상함수를 구하는 학습
> - ⭐ **차별점**: Reward 기반 순차적 의사결정, 관측순서에 따른 영향

---

## 핵심 키워드

`Agent` `State` `Action` `Environment` `Reward` `Q-Learning` `Deep Q-Learning`

---

## 정의/개념

어떤 환경 안에서 정의된 에이전트가 현재의 상태를 인식하여, 선택 가능한 행동들 중 보상을 최대화하는 행동 혹은 행동 순서를 선택

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

## 특징

| 특징 | 설명 |
|:-----|:-----|
| **Reward** | 보상 기반 학습 |
| **순차적 의사결정** | 관측 순서에 따른 영향 |

---

## 알고리즘 `큐딥`

| 암기 | 항목 | 설명 |
|:-----|:-----|:-----|
| **큐** | Q-Learning | state/action → Q Table → Q-Value(Reward) |
| **딥** | Deep Q-Learning | state → Q Network(신경망) → 여러개 Q Value |

---

## 역강화학습(Inverse Reinforcement Learning)

| 항목 | 설명 |
|:-----|:-----|
| **보상함수를 구하는 학습** | 최적 선택을 할 경우를 감안하여 계산 |
| **보상함수구현 어려움** | 실세계에서 특정 모델에 대한 보상 함수를 구하는 것은 매우 복잡한 문제 |
| **보상함수 다중속성** | 보상 함수는 단일 속성이 아닌 다속성으로 구성되는 경우가 대부분 |
| **미지보장 추가고려** | 보상 함수를 정의할 때 미지의 보상 속성까지 추가적으로 고려 |

---

## 연계 토픽

- [Q-Learning]({{ site.baseurl }}/docs/ai/01-machine-learning/q-learning)
- [심층강화학습]({{ site.baseurl }}/docs/ai/01-machine-learning/deep-reinforcement-learning)
- [MDP]({{ site.baseurl }}/docs/ai/01-machine-learning/mdp)

---

## 학습 체크리스트

- [ ] 강화학습 정의와 개념도 이해
- [ ] 구성요소(Agent, State, Action, Environment, Reward) 암기
- [ ] Q-Learning vs Deep Q-Learning 차이 설명
- [ ] 역강화학습 개념 이해
