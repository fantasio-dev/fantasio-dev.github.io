---
layout: default
title: K-Means
parent: 1. 기계학습
grand_parent: AI (인공지능)
nav_order: 17
---

<!-- CSV_APPLIED: 기술사_기본필수노트_AI - AI.csv | NO=20 | 중토픽=K-Means -->
# K-Means
{: .fs-8 }

1.3 비지도학습
{: .label .label-green }

---

## 🎯 기술사 수준 설명

### 📌 핵심 암기 (Quick Reference)

{: .highlight }
> **K-Means**: n개의 데이터를 K개의 군집으로 분류하기 위해 거리 기반으로 반복적으로 계산해 나가는 Clustering 알고리즘
> - 암기: `거리기반,` `KCentroid`
> - 키워드: `K-Means` `Clustering` `Centroid`

---

<div class="exam-concept-block" markdown="1">

## 🧠 개념 영역

### 🔑 핵심 키워드 3개

| 키워드 | 설명 | 예시 |
|:--|:--|:--|
| **K-Means** | 핵심 개념/대상 | - |
| **Clustering** | 주요 기법/구성요소 | - |
| **Centroid** | 절차/평가/특징 | - |

---

### 📖 등장배경

| 구분 | 내용 |
|:--|:--|
| **문제/필요성** | n개의 데이터를 K개의 군집으로 분류하기 위해 거리 기반으로 반복적으로 계산해 나가는 Clustering 알고리즘 |
| **활용/사례** | - |

---

### 📝 개념 정의

| 구분 | 정의 |
|:--|:--|
| **K-Means** | n개의 데이터를 K개의 군집으로 분류하기 위해 거리 기반으로 반복적으로 계산해 나가는 Clustering 알고리즘 |

</div>

---

<div class="exam-tech-block" markdown="1">

## 🏗️ 기술 영역

### 구성요소

#### 그룹 1: 핵심 항목
{: .highlight-purple }

| 항목 | 설명 |
|:--|:--|
| - | - |


</div>

---

<details markdown="1">
<summary><h3 style="display:inline">📖 상세 설명 (클릭해서 펼치기)</h3></summary>

#### 내용

- n개의 데이터를 K개의 군집으로 분류하기 위해 거리 기반으로 반복적으로 계산해 나가는 Clustering 알고리즘

#### 구성요소

- > K값: 클러스터링하여 묶을 클러스터의 개수
- > Centroid: 클러스터링 중심값

#### 장단점

- > 간단해서 빠름, 대용량적합, 다양성
- > 가중치 정의 어려움, 초기클러스터링 어려움, 결과난해

</details>

---

<details markdown="1">
<summary><h3 style="display:inline">🗂️ 기존 내용 (백업)</h3></summary>

# k-평균 군집(k-means clustering)
{: .fs-8 }

1.3 비지도학습
{: .label .label-green }

---

## 핵심 키워드

`K개 Centroid` `유클라디안 거리`

---

## 정의/개념

K개 군집, Centroid 설정, 좌표기반, 유클리디안 거리 사용 비지도 학습 알고리즘

---

## 메커니즘

```
Unlabelled Data              Labelled Clusters

    ● ●                      ⭕ ● ●
  ●   ● ●    ──K-means──→    ● ● ●    ← Cluster 1
    ● ● ●                    
  ● ●   ●                    ⭕ ● ●
    ● ●                      ● ● ●    ← Cluster 2
                               
                             ⭕ ● ●
                             ● ● ●    ← Cluster 3
                             
                             ⭕ = Centroid
```

---

## 프로세스

| # | 프로세스 | 핵심 |
|:--|:--------|:-----|
| 1 | K개 객체 선택 | K개 객체 임의 선택 |
| 2 | 할당 | 자료 가까운 군집 중심 할당 |
| 3 | 중심 갱신 | 군집 내 자료 평균 계산 군집 중심 갱신 |
| 4 | 반복 | 반복 |

---

## K값 식별 기법

- **엘보우 (Elbow Method)**: 군집 수에 따른 분산 감소율 확인
- **실루엣 (Silhouette Method)**: 군집 내 응집도와 군집 간 분리도 측정
- **덴드로그램**: 계층적 군집화 결과 시각화

---

## 연계 토픽

- [KNN](/docs/ai/01-machine-learning/knn)
- [군집분석](/docs/ai/01-machine-learning/unsupervised-learning)
- [DBSCAN](/docs/ai/01-machine-learning/dbscan)

---

## 학습 체크리스트

- [ ] K-Means 알고리즘의 정의와 메커니즘 이해
- [ ] 프로세스(선택-할당-갱신-반복) 암기
- [ ] K값 식별 기법(엘보우, 실루엣, 덴드로그램) 파악


</details>

