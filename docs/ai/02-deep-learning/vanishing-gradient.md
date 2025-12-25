---
layout: default
title: 기울기 소실 문제
parent: 2. 딥러닝
grand_parent: AI (인공지능)
nav_order: 7
---

<!-- CSV_APPLIED: 기술사_기본필수노트_AI - AI.csv | NO=9 | 중토픽=기울기소실 문제 (Vanishing Gradient Problem) -->
# 기울기 소실 문제
{: .fs-8 }

2.2 딥러닝 문제/이슈
{: .label .label-yellow }

---

## 🎯 기술사 수준 설명

### 📌 핵심 암기 (Quick Reference)

{: .highlight }
> **기울기소실 문제 (Vanishing Gradient Problem)**: MLP에서 Hidden Layer의 하단에서는 학습 layer가 깊어질수록 기울기가 소멸, 학습 효과가 사라지는
> - 암기: `활가` `학활가` `기가배`
> - 키워드: `기울기소실 문제` `Multi Layer Perceptron` `시그모이드사용`

---

<div class="exam-concept-block" markdown="1">

## 🧠 개념 영역

### 🔑 핵심 키워드 3개

| 키워드 | 설명 | 예시 |
|:--|:--|:--|
| **기울기소실 문제** | 핵심 개념/대상 | - |
| **Multi Layer Perceptron** | 주요 기법/구성요소 | - |
| **시그모이드사용** | 절차/평가/특징 | - |

---

### 📖 등장배경

| 구분 | 내용 |
|:--|:--|
| **문제/필요성** | MLP에서 Hidden Layer의 하단에서는 학습 layer가 깊어질수록 기울기가 소멸, 학습 효과가 사라지는 |
| **활용/사례** | - |

---

### 📝 개념 정의

| 구분 | 정의 |
|:--|:--|
| **기울기소실 문제 (Vanishing Gradient Problem)** | MLP에서 Hidden Layer의 하단에서는 학습 layer가 깊어질수록 기울기가 소멸, 학습 효과가 사라지는 |

</div>

---

<div class="exam-tech-block" markdown="1">

## 🏗️ 기술 영역

### 구성요소

#### 그룹 1: 해결방안
{: .highlight-purple }

| 항목 | 설명 |
|:--|:--|
| **> 학습효율** | - |
| **> 메모리기반 LSTM활용** | Long Short > Term Memory 통한 장기의존성 문제 해결, Forget Gate |
| **> 사전학습기반 DBN(Deep Belief Network)활용** | 심층신뢰신경망, Pre > Training 수행, 예측 값 정확성 개선 |
| **> 활성함수개선** | - |
| **> 미분값보전 ReLU함수 활용** | - |
| **> 음의 값 활용, Leaky ReLU사용** | - |
| **> 은닉층에서 시그모이드 함수 지양** | - |
| **> 가중치측면** | - |


</div>

---

<details markdown="1">
<summary><h3 style="display:inline">📖 상세 설명 (클릭해서 펼치기)</h3></summary>

#### 내용

- MLP에서 Hidden Layer의 하단에서는 학습 layer가 깊어질수록 기울기가 소멸, 학습 효과가 사라지는
- > MLP(Multi Layer Perceptron)

#### 원인

- > 활성화함수(시그모이드사용): 소실(0또는 1에 수렴) / 폭주(임계값을 넘어간 기울기)
- > 가중치측면(가중치영향): 역전파중 가중치폭주 / 모델에적합하지 않는 가중치

#### 해결방안

- > 학습효율
- > 메모리기반 LSTM활용: Long Short > Term Memory 통한 장기의존성 문제 해결, Forget Gate
- > 사전학습기반 DBN(Deep Belief Network)활용: 심층신뢰신경망, Pre > Training 수행, 예측 값 정확성 개선
- > 활성함수개선
- > 미분값보전 ReLU함수 활용
- > 음의 값 활용, Leaky ReLU사용
- > 은닉층에서 시그모이드 함수 지양
- > 가중치측면
- > 기울기자름(Gradient Clipping): 임계값 넘지 않도록
- > 가중치초기화: 모델의 적합한 가중치 적용
- > 배치정규화: 입력을 평균과 분산으로 정규화

</details>

---

<details markdown="1">
<summary><h3 style="display:inline">🗂️ 기존 내용 (백업)</h3></summary>

# 기울기 소실 문제 (Vanishing Gradient)
{: .fs-8 }

2.2 딥러닝 문제/이슈
{: .label .label-yellow }

---

## 핵심 키워드

`기울기 소실` `역전파` `심층 신경망` `ReLU` `배치 정규화`

---

## 정의/개념

*(이미지 내용 추출 후 작성)*

---

## 학습 체크리스트

- [ ] 개념 이해
- [ ] 핵심 키워드 암기
- [ ] 실무 적용 사례 파악


</details>

