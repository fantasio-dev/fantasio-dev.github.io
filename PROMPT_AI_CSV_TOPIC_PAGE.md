# AI 토픽(CSV 1행) → 블로그 페이지 반영 프롬프트 (개별 적용용)

## 목적

`{다운로드_폴더}/기술사_기본필수노트_AI - AI.csv`의 **단일 행(1개 토픽)**을 근거로, `docs/ai/**`(기출 제외)의 해당 토픽 마크다운 페이지를 **1교시형 양식**으로 작성/갱신한다.

---

## 입력

- CSV 행 필드: `NO`, `토픽`, `중토픽`, `암기법`, `기술요소`, `매커니즘`
- 대상 마크다운 파일(1개): 아래 매핑표의 경로

---

## 작업 규칙 (핵심)

- **CSV 내용 우선**: 서술/표/절차는 가능한 한 CSV의 `기술요소`, `매커니즘`을 그대로 구조화한다.
- **참고자료 섹션 금지**: `## 참고자료` / 외부 출처 섹션을 만들지 않는다.
- **데일리 덱 호환**:
  - 페이지에 반드시 다음 제목(헤딩)을 포함한다:
    - `### 📝 개념 정의` (또는 텍스트에 `개념 정의`가 포함된 헤딩)
    - `### 구성요소` (또는 `구성요소`가 포함된 헤딩)
    - `### 📌 핵심 암기 (Quick Reference)` (헤딩 텍스트에 `암기` 포함)
  - `### 구성요소` 직후에 **표(table)**가 최소 1개는 오도록 한다. (데일리 덱이 표를 추출함)
- **기존 내용 보존(안전장치)**:
  - 기존 본문이 있으면 맨 아래에 `<details>`로 `기존 내용 (백업)` 섹션으로 감싼다.
  - 단, 이미 `<!-- CSV_APPLIED:` 마커가 있는 파일은 **재백업하지 않고** 본문을 교체한다.
- **스타일**:
  - 구성요소/기술요소 표 블록은 가능하면 보라색 강조를 적용한다.
    - 예: `{: .highlight-purple }` + 표

---

## 출력 양식 (1교시형)

아래 구조를 준수한다:

1. `## 🎯 기술사 수준 설명`
2. `### 📌 핵심 암기 (Quick Reference)` + `{: .highlight }` 블록
3. `<div class="exam-concept-block" markdown="1">` (핵심 키워드/등장배경/개념정의)
4. `<div class="exam-tech-block" markdown="1">` (구성요소 표 중심)
5. (선택) `<div class="exam-bonus-block" markdown="1">` (차별점/가산점 포인트)
6. `<details>` “📖 상세 설명 (클릭해서 펼치기)” (CSV 원문을 섹션별로 정리)
7. (선택) `## 연계 토픽`
8. (선택) `## 학습 체크리스트`

---

## CSV → 마크다운 변환 가이드

- CSV 텍스트 내 섹션 표기:
  - `[구성요소]`, `[알고리즘]`, `[절차]`, `[특징]`, `[평가]` 등은 `####` 소제목으로 변환
- 항목 나열:
  - `A: 설명` / `A = 설명` / `A > 설명` 형태는 표로 변환 (항목/설명)
- 암기법:
  - `암기법`의 토큰은 Quick Reference에 백틱 코드로 표시: 예) `스케씨알` `선신`
  - 가능하면 구성요소 표의 첫 컬럼에 `암기`(글자) 컬럼을 추가해 매핑

---

## NO → 대상 파일 매핑 (AI)

> 이 매핑은 **현재 AI 블로그의 디렉토리 구조**를 기준으로 한다. 파일이 없으면 생성하되, 기존 구조(상위 폴더/parent/nav_order)는 유지/추정한다.

| NO | 중토픽(요약) | 대상 파일 |
|---:|---|---|
| 1 | 지도학습 | `docs/ai/01-machine-learning/supervised-learning.md` |
| 2 | 무감독학습 | `docs/ai/01-machine-learning/unsupervised-learning.md` |
| 3 | 강화학습 | `docs/ai/01-machine-learning/reinforcement-learning.md` |
| 4 | 딥러닝 | `docs/ai/01-machine-learning/deep-learning-concept.md` |
| 5 | 퍼셉트론 | `docs/ai/01-machine-learning/perceptron.md` |
| 6 | 파라미터/하이퍼파라미터 | `docs/ai/08-ml-process/hyperparameters.md` |
| 7 | 활성화 함수 | `docs/ai/01-machine-learning/activation-function.md` |
| 8 | 경사 하강법 | `docs/ai/01-machine-learning/parameters.md` |
| 9 | 기울기 소실 | `docs/ai/02-deep-learning/vanishing-gradient.md` |
| 10 | 과적합 | `docs/ai/02-deep-learning/overfitting-underfitting.md` |
| 11 | 드랍아웃 | `docs/ai/02-deep-learning/dropout.md` |
| 12 | CNN | `docs/ai/02-deep-learning/cnn.md` |
| 13 | Pooling Layer | `docs/ai/02-deep-learning/pooling-layer.md` |
| 14 | RNN | `docs/ai/02-deep-learning/rnn.md` |
| 15 | LSTM | `docs/ai/02-deep-learning/lstm.md` |
| 16 | SVM | `docs/ai/01-machine-learning/svm.md` |
| 17 | KNN | `docs/ai/01-machine-learning/knn.md` |
| 18 | 데이터 레이블링 | `docs/ai/01-machine-learning/data-labeling.md` |
| 19 | DBSCAN | `docs/ai/01-machine-learning/dbscan.md` |
| 20 | K-Means | `docs/ai/01-machine-learning/k-means.md` |
| 21 | SOM | `docs/ai/01-machine-learning/som.md` |
| 22 | PCA | `docs/ai/01-machine-learning/pca.md` |
| 23 | GAN | `docs/ai/02-deep-learning/gan.md` |
| 24 | DCGAN | `docs/ai/02-deep-learning/dcgan.md` |
| 25 | Q-러닝 | `docs/ai/01-machine-learning/q-learning.md` |
| 26 | 혼동 행렬 | `docs/ai/06-ml-evaluation/confusion-matrix.md` |
| 27 | 정밀도/재현율 | `docs/ai/06-ml-evaluation/precision-recall.md` |
| 28 | 파괴적 망각 | `docs/ai/02-deep-learning/catastrophic-forgetting.md` |
| 29 | 기계독해(MRC) | `docs/ai/04-nlp/mrc.md` |
| 30 | ELECTRA | `docs/ai/04-nlp/electra.md` |
| 31 | 연합학습 | `docs/ai/03-neural-network/federated-learning.md` |
| 32 | GNN | `docs/ai/03-neural-network/gnn.md` |
| 33 | 적대적공격 | `docs/ai/05-ai-ethics/adversarial-attack.md` |
| 34 | AI 학습용데이터 비용산정 | `docs/ai/11-ai-training-data/training-data-cost.md` |
| 35 | 메타학습 | `docs/ai/07-learning-techniques/meta-learning.md` |
| 36 | 퓨샷러닝 | `docs/ai/07-learning-techniques/few-shot-learning.md` |
| 37 | 트랜스포머 | `docs/ai/04-nlp/transformer.md` |
| 38 | ChatGPT | `docs/ai/04-nlp/chatgpt.md` |
| 39 | AI윤리 | `docs/ai/05-ai-ethics/ai-ethics.md` |
| 40 | 딥뷰 | `docs/ai/07-ai-service/deep-view.md` |
| 41 | 워드 임베딩 | `docs/ai/04-nlp/word-embedding.md` |
| 42 | ROC/PR Curve | `docs/ai/06-ml-evaluation/roc-curve.md` |
| 43 | 편향(biased) | `docs/ai/05-ai-ethics/bias.md` |
| 44 | 인공지능 보안 | `docs/ai/05-ai-ethics/ai-security.md` |
| 45 | 추천시스템 | `docs/ai/07-ai-service/recommendation-system.md` |


