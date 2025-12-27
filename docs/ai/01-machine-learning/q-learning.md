---
layout: default
title: Q-러닝 (Q-Learning)
parent: 1. 기계학습
grand_parent: AI (인공지능)
nav_order: 23
---

# Q-러닝 (Q-Learning)
{: .fs-8 }

기계학습
{: .label .label-blue }

---

## 🎯 기술사 수준 설명

### 📌 핵심 암기 (Quick Reference)

{: .highlight }
> **Q-러닝**: 행동선택 가치 함수를 기반으로 강화학습 알고리즘
> - (Q) 상태와 행동에 대한 품질값
> - (프로세스) 상태→행동→보상→Q값 업데이트→반복

---

## 핵심 키워드

`Q값` `상태` `행동` `보상` `강화학습`

---

## 정의/개념

행동선택 가치 함수를 기반으로 강화학습 알고리즘

---

## Q 테이블

```
        행동1    행동2    행동3
상태1   Q(s1,a1) Q(s1,a2) Q(s1,a3)
상태2   Q(s2,a1) Q(s2,a2) Q(s2,a3)
상태3   Q(s3,a1) Q(s3,a2) Q(s3,a3)
```

---

## Q값 업데이트 수식

$$
Q(s,a) \leftarrow Q(s,a) + \alpha [R + \gamma \max_{a'} Q(s',a') - Q(s,a)]
$$

| 기호 | 설명 |
|:-----|:-----|
| Q(s,a) | 상태 s에서 행동 a의 가치 |
| α | 학습률 (Learning Rate) |
| R | 보상 (Reward) |
| γ | 할인율 (Discount Factor) |
| s' | 다음 상태 |

---

## 프로세스

```
1. 현재 상태 s 관측
      ↓
2. ε-greedy로 행동 a 선택
      ↓
3. 행동 실행, 보상 R과 다음 상태 s' 관측
      ↓
4. Q값 업데이트
      ↓
5. s = s'로 갱신, 반복
```

---

## 탐색 vs 활용

| 전략 | 설명 |
|:-----|:-----|
| **탐색 (Exploration)** | 새로운 행동 시도 |
| **활용 (Exploitation)** | 현재 최적 행동 선택 |
| **ε-greedy** | ε 확률로 탐색, (1-ε) 확률로 활용 |

---

## 연계 토픽

- [강화학습]({{ site.baseurl }}/docs/ai/01-machine-learning/reinforcement-learning)
- [딥러닝]({{ site.baseurl }}/docs/ai/01-machine-learning/deep-learning)

---

## 학습 체크리스트

- [ ] Q-러닝 정의 암기
- [ ] Q값 업데이트 수식 암기
- [ ] 탐색과 활용 개념 설명
