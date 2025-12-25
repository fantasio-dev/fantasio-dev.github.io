---
layout: default
title: ELECTRA
parent: 4. 자연어처리
grand_parent: AI (인공지능)
nav_order: 6
---

<!-- CSV_APPLIED: 기술사_기본필수노트_AI - AI.csv | NO=30 | 중토픽=ELECTRA (Efficiently Learning an Encoder that Classifies Token Replacements Accurately) -->
# ELECTRA
{: .fs-8 }

자연어처리
{: .label .label-purple }

---

## 🎯 기술사 수준 설명

### 📌 핵심 암기 (Quick Reference)

{: .highlight }
> **ELECTRA (Efficiently Learning an Encoder that Classifies Token Replacements Accurately)**: Generator가 문장에서 마스킹된 위치에 올수 있는 토큰을 예측하게 되고 Discriminator는 입력받은 문장이 Geneerator에 의해 대체되었는지 맞추며 학습하는 모델
> - 암기: `생성적` `GAN,` `제디제디`
> - 키워드: `ELECTRA` `빠름, 0이냐 1이냐, 맞냐 틀리냐` `Generator`

---

<div class="exam-concept-block" markdown="1">

## 🧠 개념 영역

### 🔑 핵심 키워드 3개

| 키워드 | 설명 | 예시 |
|:--|:--|:--|
| **ELECTRA** | 핵심 개념/대상 | - |
| **빠름, 0이냐 1이냐, 맞냐 틀리냐** | 주요 기법/구성요소 | - |
| **Generator** | 절차/평가/특징 | - |

---

### 📖 등장배경

| 구분 | 내용 |
|:--|:--|
| **문제/필요성** | Generator가 문장에서 마스킹된 위치에 올수 있는 토큰을 예측하게 되고 Discriminator는 입력받은 문장이 Geneerator에 의해 대체되었는지 맞추며 학습하는 모델 |
| **활용/사례** | - |

---

### 📝 개념 정의

| 구분 | 정의 |
|:--|:--|
| **ELECTRA (Efficiently Learning an Encoder that Classifies Token Replacements Accurately)** | Generator가 문장에서 마스킹된 위치에 올수 있는 토큰을 예측하게 되고 Discriminator는 입력받은 문장이 Geneerator에 의해 대체되었는지 맞추며 학습하는 모델 |

</div>

---

<div class="exam-tech-block" markdown="1">

## 🏗️ 기술 영역

### 구성요소

#### 그룹 1: 내용
{: .highlight-purple }

| 항목 | 설명 |
|:--|:--|
| **Generator가 문장에서 마스킹된 위치에 올수 있는 토큰을 예측하게 되고 Discriminator는 입력받은 문장이 Geneerator에 의해 대체되었는지 맞추며 학습하는 모델** | - |
| **> Generator** | 데이터 생성, Replace Token 수행 |
| **> Discriminator** | 모든 토큰 진위 판다 |
| **> Generator Loss** | 단독학습으로 구분할수 없는 값 생성 |
| **> Discriminator Loss** | 만들어낸 정답도 실제와 같다면 답으로 처리 |
| *** GAN 과의 차이점은 Generator가 적대적 학습을 하지 않고 생성적으로 학습** | - |
| *** 생성 모델이 원본 토큰을 생성하는데 성공, 그 토큰은 ‘fake’가 아닌 ‘real’로 간주** | - |
| *** 시그모이드만 사용(빠름, 0이냐 1이냐, 맞냐 틀리냐)** | - |


</div>

---

<details markdown="1">
<summary><h3 style="display:inline">📖 상세 설명 (클릭해서 펼치기)</h3></summary>

#### 내용

- Generator가 문장에서 마스킹된 위치에 올수 있는 토큰을 예측하게 되고 Discriminator는 입력받은 문장이 Geneerator에 의해 대체되었는지 맞추며 학습하는 모델
- > Generator: 데이터 생성, Replace Token 수행
- > Discriminator: 모든 토큰 진위 판다
- > Generator Loss: 단독학습으로 구분할수 없는 값 생성
- > Discriminator Loss: 만들어낸 정답도 실제와 같다면 답으로 처리
- * GAN 과의 차이점은 Generator가 적대적 학습을 하지 않고 생성적으로 학습
- * 생성 모델이 원본 토큰을 생성하는데 성공, 그 토큰은 ‘fake’가 아닌 ‘real’로 간주
- * 시그모이드만 사용(빠름, 0이냐 1이냐, 맞냐 틀리냐)

</details>

---

<details markdown="1">
<summary><h3 style="display:inline">🗂️ 기존 내용 (백업)</h3></summary>

# ELECTRA
{: .fs-8 }

자연어처리
{: .label .label-purple }

---

## 핵심 키워드

`ELECTRA` `사전학습` `토큰 대체` `효율적 학습` `언어 모델`

---

## 정의/개념

*(이미지 내용 추출 후 작성)*

---

## 학습 체크리스트

- [ ] 개념 이해
- [ ] 핵심 키워드 암기
- [ ] 실무 적용 사례 파악


</details>

