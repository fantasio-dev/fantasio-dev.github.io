---
layout: default
title: 파괴적망각 (Catastrophic Forgetting)
parent: 2. 딥러닝
grand_parent: AI (인공지능)
nav_order: 1
---

# 파괴적망각 (Catastrophic Forgetting)
{: .fs-8 }

딥러닝
{: .label .label-green }

---

## 🎯 기술사 수준 설명

### 📌 핵심 암기 (Quick Reference)

{: .highlight }
> **파괴적망각**: 새로운 과제에 대한 학습을 할 때 기존에 배운 기억을 급격히 잊어버리는 현상
> - (해결방안) `리드지` 리허설(Rehearsal), 드롭아웃(Dropout), 지식증류(KnowledgeDistillation)

---

## 핵심 키워드

`망각` `연속학습` `리허설` `지식증류`

---

## 정의/개념

새로운 과제에 대한 학습을 할 때 기존에 배운 기억을 급격히 잊어버리는 현상

---

## 발생 원인

```
기존 학습 (Task A)
      ↓
가중치 최적화
      ↓
새 학습 (Task B)
      ↓
가중치 덮어쓰기 → Task A 성능 급격히 저하
```

---

## 해결방안 `리드지`

| 암기 | 방안 | 설명 |
|:-----|:-----|:-----|
| **리** | 리허설 (Rehearsal) | 기존 데이터를 새 데이터와 함께 학습 |
| **드** | 드롭아웃 (Dropout) | 일부 뉴런 비활성화로 과적합 방지 |
| **지** | 지식증류 (Knowledge Distillation) | 기존 모델 지식을 새 모델에 전달 |

---

## 추가 해결 방안

| 방안 | 설명 |
|:-----|:-----|
| **EWC (Elastic Weight Consolidation)** | 중요 가중치 변화 억제 |
| **Progressive Networks** | 새 과제마다 네트워크 추가 |
| **Memory Replay** | 메모리에 기존 경험 저장 후 재생 |

---

## 연계 토픽

- [전이학습]({{ site.baseurl }}/docs/ai/07-learning-techniques/transfer-learning)
- [드랍아웃]({{ site.baseurl }}/docs/ai/01-machine-learning/dropout)

---

## 학습 체크리스트

- [ ] 파괴적망각 정의 암기
- [ ] `리드지` 해결방안 3가지 설명
- [ ] 발생 원인 설명
