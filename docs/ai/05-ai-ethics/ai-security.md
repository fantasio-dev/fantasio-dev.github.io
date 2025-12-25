---
layout: default
title: 인공지능 보안
parent: 5. AI 윤리/보안
grand_parent: AI (인공지능)
nav_order: 3
---

<!-- CSV_APPLIED: 기술사_기본필수노트_AI - AI.csv | NO=44 | 중토픽=인공지능 보안 -->
# 인공지능 보안
{: .fs-8 }

인공지능 문제
{: .label .label-purple }

---

## 🎯 기술사 수준 설명

### 📌 핵심 암기 (Quick Reference)

{: .highlight }
> **인공지능 보안**: [공격기법] 무기 오회전추
> - 암기: `무기` `오회전추`
> - 키워드: `인공지능 보안` `중독 공격, 오염 공격` `회피 공격`

---

<div class="exam-concept-block" markdown="1">

## 🧠 개념 영역

### 🔑 핵심 키워드 3개

| 키워드 | 설명 | 예시 |
|:--|:--|:--|
| **인공지능 보안** | 핵심 개념/대상 | - |
| **중독 공격, 오염 공격** | 주요 기법/구성요소 | - |
| **회피 공격** | 절차/평가/특징 | - |

---

### 📖 등장배경

| 구분 | 내용 |
|:--|:--|
| **문제/필요성** | [공격기법] 무기 오회전추 |
| **활용/사례** | - |

---

### 📝 개념 정의

| 구분 | 정의 |
|:--|:--|
| **인공지능 보안** | [공격기법] 무기 오회전추 |

</div>

---

<div class="exam-tech-block" markdown="1">

## 🏗️ 기술 영역

### 구성요소

#### 그룹 1: 공격기법
{: .highlight-purple }

| 항목 | 설명 |
|:--|:--|
| **무기 오회전추** | - |
| **> 무결성 측면** | Poisoning attack(중독 공격, 오염 공격), Evasion attack(회피 공격) |
| **> 기밀성 측면** | Inversion attack(전도 공격, 학습 데이터 추출 공격), Model extraction attack(모델 추출 공격) |


</div>

---

<details markdown="1">
<summary><h3 style="display:inline">📖 상세 설명 (클릭해서 펼치기)</h3></summary>

#### 공격기법

- 무기 오회전추
- > 무결성 측면 : Poisoning attack(중독 공격, 오염 공격), Evasion attack(회피 공격)
- > 기밀성 측면 : Inversion attack(전도 공격, 학습 데이터 추출 공격), Model extraction attack(모델 추출 공격)

#### 유형별 방어

- > 무결성 취약점 공격 방어기법
- > 공통: Defence > GAN
- > Poisoning Attack: 적대적 훈련 (Adeverarial Training), 입력값 제한
- > Evasion Attack: 이진 분류기 판별
- > 기밀성 취약점 공격 방어기법
- > 공통 : Feature Squeezing
- > Model Inversion Attack : Gradient Masking
- > Model Extraction Attack : 쿼리 횟수 제한, Distillation

#### 공격사례

- > 부정적 이용 : 주행 오인식, 표지판 변형, 보험 사기, 임상 실험 회피
- > 긍정적 이용 : 모델 평가, 일반화 검증

</details>

---

<details markdown="1">
<summary><h3 style="display:inline">🗂️ 기존 내용 (백업)</h3></summary>

# 인공지능 보안
{: .fs-8 }

인공지능 문제
{: .label .label-purple }

---

## 🎯 기술사 수준 설명

### 📌 핵심 암기 (Quick Reference)

{: .highlight }
> **인공지능 보안**: AI 시스템에 대한 공격과 방어 기술
> - (공격) `무기 오회전추` 무결성(Poisoning, Evasion), 기밀성(Inversion, Extraction)
> - (방어) Defence-GAN, Adversarial Training, Feature Squeezing

---

<div class="exam-concept-block" markdown="1">

## 🧠 개념 영역

### 🔑 핵심 키워드 3개

| 키워드 | 설명 | 예시 |
|:------|:-----|:-----|
| **무결성 공격** | 모델 동작 방해 | Poisoning, Evasion |
| **기밀성 공격** | 정보 유출 | Inversion, Extraction |
| **적대적 방어** | 공격에 대한 방어 | Adversarial Training |

---

### 📖 등장배경

| 구분 | 내용 |
|:-----|:-----|
| **AI 취약점** | AI 모델의 다양한 보안 취약점 발견 |
| **보안 필요성** | AI 시스템 보안 강화 필요 |

---

### 📝 개념 정의

| 구분 | 정의 |
|:-----|:-----|
| **인공지능 보안** | AI 시스템에 대한 공격 방어 및 보안 강화 기술 |

</div>

---

<div class="exam-tech-block" markdown="1">

## 🏗️ 기술 영역

### 공격기법 `무기 오회전추` / 방어기법

#### 공격기법 `무기 오회전추`
{: .highlight-purple }

| 측면 | 공격 | 설명 |
|:-----|:-----|:-----|
| **무결성** | Poisoning attack | 중독 공격, 오염 공격 |
| **무결성** | Evasion attack | 회피 공격 |
| **기밀성** | Inversion attack | 전도 공격, 학습 데이터 추출 공격 |
| **기밀성** | Model extraction attack | 모델 추출 공격 |

#### 무결성 취약점 방어기법
{: .highlight-purple }

| 공격 | 방어 |
|:-----|:-----|
| **공통** | Defence-GAN |
| **Poisoning Attack** | 적대적 훈련(Adversarial Training), 입력값 제한 |
| **Evasion Attack** | 이진 분류기 판별 |

#### 기밀성 취약점 방어기법
{: .highlight-purple }

| 공격 | 방어 |
|:-----|:-----|
| **공통** | Feature Squeezing |
| **Model Inversion** | Gradient Masking |
| **Model Extraction** | 쿼리 횟수 제한, Distillation |

#### 공격 사례
{: .highlight-purple }

| 구분 | 사례 |
|:-----|:-----|
| **부정적 이용** | 주행 오인식, 표지판 변형, 보험 사기, 임상 실험 회피 |
| **긍정적 이용** | 모델 평가, 일반화 검증 |

</div>

---

<div class="exam-bonus-block" markdown="1">

## ⭐ 차별점 키워드 (가산점 포인트)

{: .important }
> **AI 보안 핵심**
> - **Adversarial Training**: 적대적 샘플로 학습
> - **Feature Squeezing**: 입력 특성 압축
> - **쿼리 제한**: 모델 추출 방지

</div>

---

<details markdown="1">
<summary><h3 style="display:inline">📖 상세 설명 (클릭해서 펼치기)</h3></summary>

#### ✅ 학습 체크리스트

- [ ] AI 보안 정의 말할 수 있다
- [ ] `오회전추` 공격기법 4가지 설명 가능
- [ ] 무결성/기밀성 방어기법 설명 가능

</details>

---

## 연계 토픽

- [적대적 공격](/docs/ai/05-ai-ethics/adversarial-attack)
- [GAN](/docs/ai/02-deep-learning/gan)

</details>

