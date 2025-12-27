---
layout: default
title: GNN (Graph Neural Network)
parent: 3. 신경망
grand_parent: AI (인공지능)
nav_order: 2
---

# GNN (Graph Neural Network)
{: .fs-8 }

신경망
{: .label .label-yellow }

---

## 🎯 기술사 수준 설명

### 📌 핵심 암기 (Quick Reference)

{: .highlight }
> **GNN (Graph Neural Network)**: 데이터를 노드와 엣지로 관계를 표현하는 그래프 신경망
> - (구성) 노드, 엣지, 메시지 전달
> - (유형) GCN, GraphSAGE, GAT
> - ⭐ **차별점**: 비유클리드 데이터(그래프) 처리 가능

---

## 핵심 키워드

`그래프` `노드` `엣지` `메시지 전달` `집계`

---

## 정의/개념

데이터를 노드와 엣지로 관계를 표현하는 그래프 신경망

---

## 구성요소

| 구성요소 | 설명 |
|:---------|:-----|
| **노드 (Node)** | 개체 표현 |
| **엣지 (Edge)** | 관계 표현 |
| **특성 (Feature)** | 노드/엣지 속성 |

---

## 메시지 전달 (Message Passing)

```
1. 이웃 노드 정보 수집
      ↓
2. 메시지 집계 (Aggregation)
      ↓
3. 노드 상태 업데이트
      ↓
4. 반복
```

---

## GNN 유형

| 유형 | 설명 |
|:-----|:-----|
| **GCN (Graph Convolutional Network)** | 합성곱 적용 |
| **GraphSAGE** | 샘플링 기반 집계 |
| **GAT (Graph Attention Network)** | 어텐션 메커니즘 적용 |

---

## 활용 분야

| 분야 | 활용 |
|:-----|:-----|
| **소셜 네트워크** | 친구 추천, 커뮤니티 탐지 |
| **분자 구조** | 신약 개발 |
| **추천 시스템** | 아이템 관계 모델링 |
| **지식 그래프** | 관계 추론 |

---

## 연계 토픽

- [CNN]({{ site.baseurl }}/docs/ai/01-machine-learning/cnn)
- [추천 시스템]({{ site.baseurl }}/docs/ai/07-ai-service/recommendation-system)

---

## 학습 체크리스트

- [ ] GNN 정의 암기
- [ ] 구성요소 3가지 설명
- [ ] 메시지 전달 개념 설명
- [ ] GNN 유형 3가지 나열
