---
layout: default
title: 파괴적 망각
parent: 2. 딥러닝
grand_parent: AI (인공지능)
nav_order: 10
---

<!-- CSV_APPLIED: 기술사_기본필수노트_AI - AI.csv | NO=28 | 중토픽=파괴적망각 (Catastrophic Forgetting) -->
# 파괴적 망각
{: .fs-8 }

2.2 딥러닝 문제/이슈
{: .label .label-yellow }

---

## 🎯 기술사 수준 설명

### 📌 핵심 암기 (Quick Reference)

{: .highlight }
> **파괴적망각 (Catastrophic Forgetting)**: Single Task(단일 과제) 성능우수, 다른 종류의 Task를 학습하면 이전에 학습했던 Task에 대한 성능이 현저하게 떨어지는 문제(이전학습망각)
> - 암기: `정증동`
> - 키워드: `파괴적망각` `단일 과제` `이전학습망각`

---

<div class="exam-concept-block" markdown="1">

## 🧠 개념 영역

### 🔑 핵심 키워드 3개

| 키워드 | 설명 | 예시 |
|:--|:--|:--|
| **파괴적망각** | 핵심 개념/대상 | - |
| **단일 과제** | 주요 기법/구성요소 | - |
| **이전학습망각** | 절차/평가/특징 | - |

---

### 📖 등장배경

| 구분 | 내용 |
|:--|:--|
| **문제/필요성** | Single Task(단일 과제) 성능우수, 다른 종류의 Task를 학습하면 이전에 학습했던 Task에 대한 성능이 현저하게 떨어지는 문제(이전학습망각) |
| **활용/사례** | - |

---

### 📝 개념 정의

| 구분 | 정의 |
|:--|:--|
| **파괴적망각 (Catastrophic Forgetting)** | Single Task(단일 과제) 성능우수, 다른 종류의 Task를 학습하면 이전에 학습했던 Task에 대한 성능이 현저하게 떨어지는 문제(이전학습망각) |

</div>

---

<div class="exam-tech-block" markdown="1">

## 🏗️ 기술 영역

### 구성요소

#### 그룹 1: 개선알고리즘
{: .highlight-purple }

| 항목 | 설명 |
|:--|:--|
| **정증동** | - |
| **> 정규화** | 기존 학습 파라미터 최대한 유지, 평균과 분산 |
| **> 증류(Distillation)** | 이전파라미터 압축전달, 네트워크전달, 메모리 기법 등 |
| **> 동적구조** | Pruning/Masking 기법, Task별 파라미터 지정, 네트워크 지정, 노드/Layer추가 |
| ***현 시점에서는 레이어의 개수가 파괴적 망각에 영향이 크다고 알려져 있어 Drop** | Out 방식 효율적 |


</div>

---

<details markdown="1">
<summary><h3 style="display:inline">📖 상세 설명 (클릭해서 펼치기)</h3></summary>

#### 내용

- Single Task(단일 과제) 성능우수, 다른 종류의 Task를 학습하면 이전에 학습했던 Task에 대한 성능이 현저하게 떨어지는 문제(이전학습망각)

#### 개선알고리즘

- 정증동
- > 정규화: 기존 학습 파라미터 최대한 유지, 평균과 분산
- > 증류(Distillation): 이전파라미터 압축전달, 네트워크전달, 메모리 기법 등
- > 동적구조: Pruning/Masking 기법, Task별 파라미터 지정, 네트워크 지정, 노드/Layer추가
- *현 시점에서는 레이어의 개수가 파괴적 망각에 영향이 크다고 알려져 있어 Drop > Out 방식 효율적

</details>

---

<details markdown="1">
<summary><h3 style="display:inline">🗂️ 기존 내용 (백업)</h3></summary>

# 파괴적 망각 (Catastrophic Forgetting)
{: .fs-8 }

2.2 딥러닝 문제/이슈
{: .label .label-yellow }

---

## 핵심 키워드

`파괴적 망각` `연속 학습` `지식 보존` `신경망 가소성` `Elastic Weight`

---

## 정의/개념

*(이미지 내용 추출 후 작성)*

---

## 학습 체크리스트

- [ ] 개념 이해
- [ ] 핵심 키워드 암기
- [ ] 실무 적용 사례 파악


</details>

