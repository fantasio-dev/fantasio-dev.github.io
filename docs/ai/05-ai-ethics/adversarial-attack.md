---
layout: default
title: 적대적 공격(Adversarial Attack)
parent: 5. AI 윤리/보안
grand_parent: AI (인공지능)
nav_order: 5
---

# 적대적 공격(Adversarial Attack)
{: .fs-8 }

AI공격
{: .label .label-purple }

---

## 🎯 기술사 수준 설명

### 📌 핵심 암기 (Quick Reference)

{: .highlight }
> **적대적 공격**: AI 모델을 속이거나 공격하는 기법
> - (공격유형) `오회전추` 오염공격, 회피공격, 전도공격, 추출공격

---

<div class="exam-concept-block" markdown="1">

## 🧠 개념 영역

### 🔑 핵심 키워드 3개

| 키워드 | 설명 | 예시 |
|:------|:-----|:-----|
| **Perturbation** | 입력에 작은 변화 추가 | 노이즈 추가 |
| **Poisoning** | 학습 데이터 오염 | 악성 데이터 주입 |
| **Model Extraction** | 모델 자체를 알아냄 | 모델 복사 |

---

### 📖 등장배경

| 구분 | 내용 |
|:-----|:-----|
| **AI 취약점** | AI 모델의 보안 취약점 발견 |
| **보안 필요성** | AI 시스템 보안 강화 필요 |

---

### 📝 개념 정의

| 구분 | 정의 |
|:-----|:-----|
| **적대적 공격** | AI 모델을 속이거나 공격하여 오작동을 유도하는 기법 |

</div>

---

<div class="exam-tech-block" markdown="1">

## 🏗️ 기술 영역

### 공격유형 `오회전추`

#### 공격유형 `오회전추`
{: .highlight-purple }

| 암기 | 항목 | 설명 |
|:-----|:-----|:-----|
| **오** | 오염공격(Poisoning) | 학습데이터 악의적인 데이터 주입, 학습과정 공격 |
| **회** | 회피공격(Evasion) | 입력데이터에 perturbation(작은변화) 추가, 모델이 정답을 피해가게 만듬 |
| **전** | 전도공격(Inversion) | 모델에 쿼리를 계속 던져서 학습데이터 유추 복원 |
| **추** | 추출공격(Extraction) | 모델에 쿼리를 던져 모델 자체를 알아냄, 모델복사 |

#### 공격 분류
{: .highlight-purple }

| 분류 | 공격 | 설명 |
|:-----|:-----|:-----|
| **무결성 측면** | Poisoning, Evasion | 모델 동작 방해 |
| **기밀성 측면** | Inversion, Extraction | 정보 유출 |

</div>

---

<div class="exam-bonus-block" markdown="1">

## ⭐ 차별점 키워드 (가산점 포인트)

{: .important }
> **적대적 공격 핵심**
> - **Poisoning vs Evasion**: 학습 과정 공격 vs 추론 과정 공격
> - **Inversion vs Extraction**: 데이터 복원 vs 모델 복사
> - **활용**: 주행 오인식, 표지판 변형, 보험 사기

</div>

---

<details markdown="1">
<summary><h3 style="display:inline">📖 상세 설명 (클릭해서 펼치기)</h3></summary>

#### ✅ 학습 체크리스트

- [ ] 적대적 공격 정의 말할 수 있다
- [ ] `오회전추` 공격유형 4개 설명 가능
- [ ] 무결성 vs 기밀성 측면 분류 설명 가능
