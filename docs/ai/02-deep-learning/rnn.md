---
layout: default
title: RNN
parent: 2. 딥러닝
grand_parent: AI (인공지능)
nav_order: 2
---

<!-- CSV_APPLIED: 기술사_기본필수노트_AI - AI.csv | NO=14 | 중토픽=RNN (Recurrent Neural Networks) -->
# RNN
{: .fs-8 }

2.1 모델 구조
{: .label .label-purple }

---

## 🎯 기술사 수준 설명

### 📌 핵심 암기 (Quick Reference)

{: .highlight }
> **RNN (Recurrent Neural Networks)**: 내부에 순환 구조를 가진 입력과 출력을 시퀀스 단위로 처리하고 BPTT(Backpropagation Through Time) 이용하는 인공 신경망 모델
> - 암기: `순환구조` `셀리역시`
> - 키워드: `RNN` `Backpropagation Through Time` `BackPropagation Through Time`

---

<div class="exam-concept-block" markdown="1">

## 🧠 개념 영역

### 🔑 핵심 키워드 3개

| 키워드 | 설명 | 예시 |
|:--|:--|:--|
| **RNN** | 핵심 개념/대상 | - |
| **Backpropagation Through Time** | 주요 기법/구성요소 | - |
| **BackPropagation Through Time** | 절차/평가/특징 | - |

---

### 📖 등장배경

| 구분 | 내용 |
|:--|:--|
| **문제/필요성** | 내부에 순환 구조를 가진 입력과 출력을 시퀀스 단위로 처리하고 BPTT(Backpropagation Through Time) 이용하는 인공 신경망 모델 |
| **활용/사례** | - |

---

### 📝 개념 정의

| 구분 | 정의 |
|:--|:--|
| **RNN (Recurrent Neural Networks)** | 내부에 순환 구조를 가진 입력과 출력을 시퀀스 단위로 처리하고 BPTT(Backpropagation Through Time) 이용하는 인공 신경망 모델 |

</div>

---

<div class="exam-tech-block" markdown="1">

## 🏗️ 기술 영역

### 구성요소

#### 그룹 1: 특징
{: .highlight-purple }

| 암기 | 항목 | 설명 |
|:--|:--|:--|
| **순** | **> 유닛간의 연결이 Directed Cycle을 형성해 자신을 가리키며 Recurrent Weight을 포함** | - |
| **환** | **> 입력/출력을 시퀀스 단위로 처리하는 신경망 알고리즘** | - |
| **구** | **> Cell** | 이전 값을 기억하는 메모리 역할 |
| **조** | **> 은닉층** | 처리후 출력보내고 다시 가중치 값으로 사용 |


</div>

---

<details markdown="1">
<summary><h3 style="display:inline">📖 상세 설명 (클릭해서 펼치기)</h3></summary>

#### 내용

- 내부에 순환 구조를 가진 입력과 출력을 시퀀스 단위로 처리하고 BPTT(Backpropagation Through Time) 이용하는 인공 신경망 모델

#### 특징

- > 유닛간의 연결이 Directed Cycle을 형성해 자신을 가리키며 Recurrent Weight을 포함
- > 입력/출력을 시퀀스 단위로 처리하는 신경망 알고리즘
- > Cell: 이전 값을 기억하는 메모리 역할
- > 은닉층: 처리후 출력보내고 다시 가중치 값으로 사용

#### 학습형태

- > Cell 저장: 이전값을 기억함.
- > Recurrent Weight: 반복가중치 구조
- > BPTT: 오류역전파. 모든 시점에 대한 가중치 공유함, 기울기소실 LSTM으로 개선
- > Sequential Data: 시계열의 내용과 함께 문맥 이해, 길어질수록 전달 한계 발생

#### 역전파 + 시간, LSTM개선

- > 기존의 역전파 방법에 시간이 추가되어 BPTT(BackPropagation Through Time)이라는 변형된 학습 방법을 이용
- > 다만, 역전파의 거리가 늘어나면 gradient 값이 폭증하거나 사라지는 현상이 발생하는 문제점이 발생(이를 개선한 구조가 LSTM과 GRU임)

#### 구조

- 입력 > 은닉 > 출력
- > one to one > 기본 NN 구조
- > one to many > 이미지 캡션 (이미지 > > 문장)
- > many to one > 감정분류 (문장 > > 호/불호)
- > many to many > 기계번역 (문장 > > 문장), 비디오 캡션 (비디오 > > 문장)

</details>

---

<details markdown="1">
<summary><h3 style="display:inline">🗂️ 기존 내용 (백업)</h3></summary>

# RNN (Recurrent Neural Network)
{: .fs-8 }

2.1 모델 구조
{: .label .label-purple }

---

## 핵심 키워드

`RNN` `순환 신경망` `시퀀스` `시계열` `은닉 상태`

---

## 정의/개념

*(이미지 내용 추출 후 작성)*

---

## 학습 체크리스트

- [ ] 개념 이해
- [ ] 핵심 키워드 암기
- [ ] 실무 적용 사례 파악


</details>

