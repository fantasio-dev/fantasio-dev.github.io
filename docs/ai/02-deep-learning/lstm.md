---
layout: default
title: LSTM
parent: 2. 딥러닝
grand_parent: AI (인공지능)
nav_order: 3
---

<!-- CSV_APPLIED: 기술사_기본필수노트_AI - AI.csv | NO=15 | 중토픽=LSTM (Long Shor Term Memory) -->
# LSTM
{: .fs-8 }

2.1 모델 구조
{: .label .label-purple }

---

## 🎯 기술사 수준 설명

### 📌 핵심 암기 (Quick Reference)

{: .highlight }
> **LSTM (Long Shor Term Memory)**: RNNs 의 Hidden Layer 를 Input Gate, Output Gate, Forget Gate 라는 세가지 게이트를 이용하여 장기 의존성 문제를 해결한 알고리즘
> - 암기: `정연` `게셀피모`
> - 키워드: `LSTM` `update, reset` `RNNs`

---

<div class="exam-concept-block" markdown="1">

## 🧠 개념 영역

### 🔑 핵심 키워드 3개

| 키워드 | 설명 | 예시 |
|:--|:--|:--|
| **LSTM** | 핵심 개념/대상 | - |
| **update, reset** | 주요 기법/구성요소 | - |
| **RNNs** | 절차/평가/특징 | - |

---

### 📖 등장배경

| 구분 | 내용 |
|:--|:--|
| **문제/필요성** | RNNs 의 Hidden Layer 를 Input Gate, Output Gate, Forget Gate 라는 세가지 게이트를 이용하여 장기 의존성 문제를 해결한 알고리즘 |
| **활용/사례** | - |

---

### 📝 개념 정의

| 구분 | 정의 |
|:--|:--|
| **LSTM (Long Shor Term Memory)** | RNNs 의 Hidden Layer 를 Input Gate, Output Gate, Forget Gate 라는 세가지 게이트를 이용하여 장기 의존성 문제를 해결한 알고리즘 |

</div>

---

<div class="exam-tech-block" markdown="1">

## 🏗️ 기술 영역

### 구성요소

#### 그룹 1: 구성요소
{: .highlight-purple }

| 항목 | 설명 |
|:--|:--|
| **정보저장삭제** | - |
| **> Gate** | - |
| **> Cell State에 정보 추가삭제** | - |
| **> 시그모이드 함수를 통한 3개 Gate, 정보 통과 여부 결정, 셀 상태 보호 및 제어** | - |
| **> Cell State** | - |
| **> 이전정보 + 선형연산 > 다음단계전달** | - |
| **> 메모리셀 전체 사슬 관통, 정보 전달** | - |
| **> 덧셈 연산, 기울기 소실문제 해결** | - |


</div>

---

<details markdown="1">
<summary><h3 style="display:inline">📖 상세 설명 (클릭해서 펼치기)</h3></summary>

#### 내용

- RNNs 의 Hidden Layer 를 Input Gate, Output Gate, Forget Gate 라는 세가지 게이트를 이용하여 장기 의존성 문제를 해결한 알고리즘

#### 특징

- > 단일 뉴럴 네트워크 레이어
- > 4 개의 상호작용 가능한 GATE 구조

#### 구성요소

- 정보저장삭제
- > Gate
- > Cell State에 정보 추가삭제
- > 시그모이드 함수를 통한 3개 Gate, 정보 통과 여부 결정, 셀 상태 보호 및 제어
- > Cell State
- > 이전정보 + 선형연산 > 다음단계전달
- > 메모리셀 전체 사슬 관통, 정보 전달
- > 덧셈 연산, 기울기 소실문제 해결
- 연산처리
- > Forget Gate: Cell State에서 어떤 정보를 제거할지 결정, 시그모이드 함수로 구성
- > Input Gate: 새로운 정보를 cell state에 저장할지 결정, tanh함수 사용
- > Memory Update: 과거 시점에 셀 상태 갱신
- > Output Gate: 최종출력값을 결정, cell state를 tanh 함수를 거쳐 > 1과 1사이 값을 생성

#### GRU

- Gated Recurrent Unit
- > LSTM의 간결한 구조
- > Gate 2개(update, reset), 빠름

</details>

---

<details markdown="1">
<summary><h3 style="display:inline">🗂️ 기존 내용 (백업)</h3></summary>

# LSTM (Long Short-Term Memory)
{: .fs-8 }

2.1 모델 구조
{: .label .label-purple }

---

## 핵심 키워드

`LSTM` `장단기 메모리` `게이트` `셀 상태` `장기 의존성`

---

## 정의/개념

*(이미지 내용 추출 후 작성)*

---

## 학습 체크리스트

- [ ] 개념 이해
- [ ] 핵심 키워드 암기
- [ ] 실무 적용 사례 파악


</details>

