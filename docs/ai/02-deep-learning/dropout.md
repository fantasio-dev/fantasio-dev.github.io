---
layout: default
title: 드랍아웃
parent: 2. 딥러닝
grand_parent: AI (인공지능)
nav_order: 9
---

<!-- CSV_APPLIED: 기술사_기본필수노트_AI - AI.csv | NO=11 | 중토픽=드랍아웃 -->
# 드랍아웃
{: .fs-8 }

2.2 딥러닝 문제/이슈
{: .label .label-yellow }

---

## 🎯 기술사 수준 설명

### 📌 핵심 암기 (Quick Reference)

{: .highlight }
> **드랍아웃**: 심층신경망 학습을 위해 오류역전파(Back Propagation) 수행 시, 과적합(Overfitting)문제를 해결하기 위해 은닉층의 일부 노드를 무작위로 비활성화 하는 기법
> - 암기: `Back` `Progagation,` `Overfitting` `피백시하` `입비학역테`
> - 키워드: `드랍아웃` `Back Propagation` `Overfitting`

---

<div class="exam-concept-block" markdown="1">

## 🧠 개념 영역

### 🔑 핵심 키워드 3개

| 키워드 | 설명 | 예시 |
|:--|:--|:--|
| **드랍아웃** | 핵심 개념/대상 | - |
| **Back Propagation** | 주요 기법/구성요소 | - |
| **Overfitting** | 절차/평가/특징 | - |

---

### 📖 등장배경

| 구분 | 내용 |
|:--|:--|
| **문제/필요성** | 심층신경망 학습을 위해 오류역전파(Back Propagation) 수행 시, 과적합(Overfitting)문제를 해결하기 위해 은닉층의 일부 노드를 무작위로 비활성화 하는 기법 |
| **활용/사례** | - |

---

### 📝 개념 정의

| 구분 | 정의 |
|:--|:--|
| **드랍아웃** | 심층신경망 학습을 위해 오류역전파(Back Propagation) 수행 시, 과적합(Overfitting)문제를 해결하기 위해 은닉층의 일부 노드를 무작위로 비활성화 하는 기법 |

</div>

---

<div class="exam-tech-block" markdown="1">

## 🏗️ 기술 영역

### 구성요소

#### 그룹 1: 유형
{: .highlight-purple }

| 항목 | 설명 |
|:--|:--|
| **피백시하** | - |
| **> Feed Forward** | 은닉 초기 입력노드 대상 |
| **> Back Propagation** | 은닉 출력 노드 대상 |
| **> 시간/공간** | 드랍아웃 시간/공간적 연관성 고려 |
| **> Hybrid** | Feed + Back, 입력+출력 |


</div>

---

<details markdown="1">
<summary><h3 style="display:inline">📖 상세 설명 (클릭해서 펼치기)</h3></summary>

#### 내용

- 심층신경망 학습을 위해 오류역전파(Back Propagation) 수행 시, 과적합(Overfitting)문제를 해결하기 위해 은닉층의 일부 노드를 무작위로 비활성화 하는 기법

#### 유형

- 피백시하
- > Feed Forward : 은닉 초기 입력노드 대상
- > Back Propagation: 은닉 출력 노드 대상
- > 시간/공간: 드랍아웃 시간/공간적 연관성 고려
- > Hybrid: Feed + Back, 입력+출력

#### 작동원리

- 입비학역테
- > DropoutRate입력: 파라미터 입력, 0.5입력시 50%날림
- > 노드 비활성화: 은닉층 임의노드 선택해 확률기준 비활성
- > 신경망 학습: 비활성화 상태 학습
- > 오류역전파: 비활성화 반복하여 학습수행
- > 테스트: 비활성화 복구하여 테스트

#### 효과

- > 모델 복잡도 내림, 동조현상 회피(중복처리), 앙상블효과
- > 과적합방지

#### 고려사항

- > 속도지연: 무작위 제거발생, Batch Nomalization을 통한 드랍아웃 대체
- > 가중치활용: 레이어전달 데이터 미흡, 가중치값을 드랍되지 않는 노드에 추가적용

</details>

---

<details markdown="1">
<summary><h3 style="display:inline">🗂️ 기존 내용 (백업)</h3></summary>

# 드랍아웃 (Dropout)
{: .fs-8 }

2.2 딥러닝 문제/이슈
{: .label .label-yellow }

---

## 핵심 키워드

`드랍아웃` `정규화` `과적합 방지` `앙상블` `뉴런 비활성화`

---

## 정의/개념

*(이미지 내용 추출 후 작성)*

---

## 학습 체크리스트

- [ ] 개념 이해
- [ ] 핵심 키워드 암기
- [ ] 실무 적용 사례 파악


</details>

