---
layout: default
title: AI 이해 가이드 (MAP)
parent: AI (인공지능)
nav_order: 0
has_toc: true
permalink: /docs/ai/map
---

# AI 이해 가이드 (MAP)
{: .no_toc }

<style>
.section-divider {
  height: 2px;
  background: linear-gradient(90deg, transparent, #e2e8f0 20%, #e2e8f0 80%, transparent);
  margin: 2.5rem 0;
  border: none;
}
.section-divider-dot {
  text-align: center;
  margin: 2rem 0;
  color: #cbd5e1;
  letter-spacing: 0.5rem;
}
</style>

<details open markdown="1">
<summary><strong>📋 목차 (2단계까지)</strong></summary>

- **Part 1. AI 개발 Lifecycle**
  - 1.1 전체 흐름 (Big Picture)
  - 1.2 데이터 파이프라인
  - 1.3 모델 선정 - AI 알고리즘
  - 1.4 모델 학습 - AI 학습 프로세스
  - 1.5 모델 평가
  - 1.6 모델 배포
  - 1.7 모델 튜닝
  - 1.8 도구
- **Part 2. 인공지능 전략 및 생태계**
  - 2.1 국가 Level
  - 2.2 기업 Level
- **Part 3. 활용**
- **부록: 원문 전체**

</details>

<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 1.5rem 2rem; border-radius: 12px; margin: 2rem 0; box-shadow: 0 8px 24px rgba(102, 126, 234, 0.3);">
  <h1 style="margin: 0; font-size: 1.8rem;">📦 Part 1. AI 개발 Lifecycle</h1>
  <p style="margin: 0.5rem 0 0 0; opacity: 0.9; font-size: 0.95rem;">데이터 → 모델 → 운영 | 수저처 - 선학평 - 배모튜</p>
</div>

<style>
.lifecycle-nav {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
  justify-content: center;
  margin: 2rem 0;
}
.lifecycle-nav a {
  text-decoration: none !important;
  transition: transform 0.2s, box-shadow 0.2s;
}
.lifecycle-nav a:hover {
  transform: translateY(-4px);
}
.lifecycle-card {
  border-radius: 16px;
  padding: 1.5rem;
  min-width: 200px;
  color: white;
  cursor: pointer;
}
.lifecycle-card:hover {
  box-shadow: 0 15px 40px rgba(0,0,0,0.3) !important;
}
.lifecycle-arrow {
  display: flex;
  align-items: center;
  font-size: 2rem;
}
</style>

<div class="lifecycle-nav">
  <a href="#12-데이터-파이프라인">
    <div class="lifecycle-card" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);">
      <div style="font-size: 2rem; margin-bottom: 0.5rem;">📦</div>
      <div style="font-weight: 700; font-size: 1.2rem; margin-bottom: 0.3rem;">데이터</div>
      <div style="font-size: 1rem; opacity: 0.95; font-weight: 700; background: rgba(255,255,255,0.2); padding: 0.3rem 0.6rem; border-radius: 6px; display: inline-block;">수저처</div>
      <hr style="border-color: rgba(255,255,255,0.3); margin: 1rem 0;">
      <div style="font-size: 0.85rem; line-height: 1.8;">
        <div>▸ 수집</div>
        <div>▸ 저장</div>
        <div>▸ 전처리</div>
      </div>
      <div style="margin-top: 1rem; font-size: 0.75rem; opacity: 0.8;">👆 클릭하여 이동</div>
    </div>
  </a>
  <div class="lifecycle-arrow" style="color: #667eea;">→</div>
  <a href="#13-모델-선정---ai-알고리즘">
    <div class="lifecycle-card" style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); box-shadow: 0 10px 30px rgba(245, 87, 108, 0.3);">
      <div style="font-size: 2rem; margin-bottom: 0.5rem;">🧠</div>
      <div style="font-weight: 700; font-size: 1.2rem; margin-bottom: 0.3rem;">모델</div>
      <div style="font-size: 1rem; opacity: 0.95; font-weight: 700; background: rgba(255,255,255,0.2); padding: 0.3rem 0.6rem; border-radius: 6px; display: inline-block;">선학평</div>
      <hr style="border-color: rgba(255,255,255,0.3); margin: 1rem 0;">
      <div style="font-size: 0.85rem; line-height: 1.8;">
        <div>▸ 선정</div>
        <div>▸ 학습</div>
        <div>▸ 평가</div>
      </div>
      <div style="margin-top: 1rem; font-size: 0.75rem; opacity: 0.8;">👆 클릭하여 이동</div>
    </div>
  </a>
  <div class="lifecycle-arrow" style="color: #f5576c;">→</div>
  <a href="#16-모델-배포">
    <div class="lifecycle-card" style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); box-shadow: 0 10px 30px rgba(79, 172, 254, 0.3);">
      <div style="font-size: 2rem; margin-bottom: 0.5rem;">⚙️</div>
      <div style="font-weight: 700; font-size: 1.2rem; margin-bottom: 0.3rem;">운영</div>
      <div style="font-size: 1rem; opacity: 0.95; font-weight: 700; background: rgba(255,255,255,0.2); padding: 0.3rem 0.6rem; border-radius: 6px; display: inline-block;">배모튜</div>
      <hr style="border-color: rgba(255,255,255,0.3); margin: 1rem 0;">
      <div style="font-size: 0.85rem; line-height: 1.8;">
        <div>▸ 배포</div>
        <div>▸ 모니터링</div>
        <div>▸ 튜닝</div>
      </div>
      <div style="margin-top: 1rem; font-size: 0.75rem; opacity: 0.8;">👆 클릭하여 이동</div>
    </div>
  </a>
</div>

<div class="section-divider-dot">• • •</div>

## 1.1 전체 흐름 (Big Picture)

### 관련 용어

- **모델 서빙(Serving)**: 모델을 API/서비스 형태로 제공
- **딜리버리(Delivery)**: 배포/릴리즈 관점의 전달
- **Data Drift**: 입력 데이터 분포 변화
- **GPUaaS**: GPU를 서비스로 제공

<div class="section-divider-dot">• • •</div>

## 1.2 [데이터 파이프라인]

### 데이터 파이프라인 흐름도

<div style="display: flex; align-items: center; gap: 0.5rem; flex-wrap: wrap; justify-content: center; margin: 2rem 0; padding: 1.5rem; background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%); border-radius: 12px;">
  <div style="background: #667eea; padding: 0.8rem 1.2rem; border-radius: 8px; color: white; font-weight: 600; font-size: 0.9rem;">📥 수집</div>
  <span style="color: #667eea; font-size: 1.5rem;">→</span>
  <div style="background: #764ba2; padding: 0.8rem 1.2rem; border-radius: 8px; color: white; font-weight: 600; font-size: 0.9rem;">💾 저장</div>
  <span style="color: #764ba2; font-size: 1.5rem;">→</span>
  <div style="background: #f093fb; padding: 0.8rem 1.2rem; border-radius: 8px; color: white; font-weight: 600; font-size: 0.9rem;">🔧 처리</div>
  <span style="color: #f093fb; font-size: 1.5rem;">→</span>
  <div style="background: #f5576c; padding: 0.8rem 1.2rem; border-radius: 8px; color: white; font-weight: 600; font-size: 0.9rem;">📊 분석</div>
  <span style="color: #f5576c; font-size: 1.5rem;">→</span>
  <div style="background: #4facfe; padding: 0.8rem 1.2rem; border-radius: 8px; color: white; font-weight: 600; font-size: 0.9rem;">📈 시각화</div>
</div>

{: .important }
> **인공지능은 항상 "데이터 품질"과 연결됨**
>
> 참고: 생성형AI 품질관리 가이드 3.5

<div class="section-divider-dot">• • •</div>

## 1.3 [모델 선정] - AI 알고리즘

### 알고리즘 분류 체계

<style>
.algo-table th:nth-child(1),
.algo-table th:nth-child(2),
.algo-table th:nth-child(3),
.algo-table th:nth-child(4) { background-color: #1e3a5f; color: white; }
.algo-table td:nth-child(2),
.algo-table td:nth-child(3),
.algo-table td:nth-child(4) { background-color: #e8f4fc; font-weight: 600; }
</style>

{: .algo-table}
| 구분 | 대분류 | 중분류 | 알고리즘 | 핵심 개념 | 특징 / 활용 |
|:-----|:-------|:-------|:---------|:----------|:------------|
| 레거시 | **지도학습** | **분류** | SVM | 초평면으로 클래스 분리 | 고차원 강함 · 얼굴 인식, 텍스트 분류 |
| | | | KNN | 주변 k개 다수결 분류 | 단순, 계산량 큼 · 이미지 분류, 추천 |
| | | | Decision Tree | 규칙 기반 트리 분류 | 해석 쉬움 · 고객 세분화, 품질 분류 |
| | | | Random Forest | 여러 트리의 앙상블 | 안정적 · 의료 진단, 신용 평가 |
| | | | Naive Bayes | 조건부 확률 기반 분류 | 속도 빠름 · 스팸 필터링, 문서 분류 |
| | | | ANN | 가중치 학습, 비선형 인식 | 복잡한 문제 해결 · 음성/이미지/자율주행 |
| | | | Logistic Regression | 시그모이드 확률 분류 | 이진 분류 최적 · 이탈 예측 |
| | | **회귀** | Linear Regression | 선형 관계 학습 | 단순, 해석 용이 · 매출/가격 예측 |
| | | | Regularized LR | L1/L2 과적합 방지 | 라쏘/릿지 · 주가/의료 분석 |
| | | | Regression Tree | 트리 연속값 예측 | 비선형 처리 · 에너지/생산량 추정 |
| | | | RF Regression | 회귀 트리 앙상블 | 안정적 · 부동산/보험료 예측 |
| | | | SVR | 마진 기반 회귀 | 고차원 강함 · 날씨/수요 예측 |
| | **비지도학습** | **군집화** | K-Means | 유사도 기반 군집 | 간단 · 고객 군집, 마켓 세분화 |
| | | | DBSCAN | 밀도 기반 클러스터링 | 이상치 강함 · 위치 기반 분석 |
| | | | EM Clustering | 확률 기반 군집화 | 소프트 · 혼합 모델 추정 |
| | | | SOM | 자기조직화 맵 | 고차원→2D · 이상 탐지 |
| | | | Hierarchical | 거리 기반 트리 구조 | 시각화 용이 · 유전/조직 분류 |
| | | **차원 축소** | PCA | 분산 최대 방향 축소 | 시각화 · 이미지 압축, 특징 추출 |
| | | | LDA | 클래스 간/내 분산 | 지도형 축소 · 얼굴 인식, 패턴 분류 |
| | | | Factor Analysis | 잠재 요인 관계 설명 | 노이즈 제거 · 설문/심리 분석 |
| | | | MDS | 유사도 저차원 임베딩 | 거리 보존 · 마케팅 분석 |
| | | **연관 규칙** | MBA | 동시 발생 규칙 탐색 | 지지도/신뢰도 · 상품 추천, 교차판매 |
| | | | Sequence Analysis | 순서 패턴 탐색 | 시계열 활용 · 고객 행동, 클릭 패턴 |
| | | | Collaborative Filtering | 유사 사용자/아이템 추천 | 피드백 활용 · 영화/음악 추천 |
| | **강화학습** | **가치 기반** | Q-Learning | 가치함수 기반 학습 | 테이블 기반 · 게임 AI, 로봇 경로 |
| | | | DQN | Q-Learning + 딥러닝 | 이미지 환경 · AlphaGo, 자율주행 |
| | | **정책 기반** | Policy Gradient | 정책 직접 최적화 | 확률적 정책 · 드론 제어 |
| | | | PPO | 정책 안정화 알고리즘 | 안정성 · ChatGPT 학습, 시뮬레이션 |
| | | | SARSA | 현재 정책 기반 학습 | 보수적 · 강화형 로봇 제어 |
| | | **Actor-Critic** | Actor–Critic | 정책 + 가치 결합형 | 효율적 · 자율주행, 로봇 강화학습 |
| **현대** | **딥러닝** | | DBN | 확률 그래프 신경망 | 초기 모델 · 패턴/음성 인식 |
| | | | CNN | 픽셀 관계 학습 | 시각 특화 · 이미지/얼굴 인식 |
| | | | RNN | 시간 의존성 학습 | 시계열/NLP · 음성/텍스트 분석 |
| | | | GNN | 노드 연결 관계 학습 | 그래프 처리 · SNS/추천 시스템 |
| | | | Transformer | Attention 기반 병렬 | 긴 문맥 · 번역, 챗봇, 요약 |
| | | | LSTM | 장기 의존성 해결 RNN | 시계열 강함 · 음성, 주가 예측 |
| | | | GRU | LSTM 단순화 | 빠른 학습 · 텍스트, 음성 |
| | | | BERT | 양방향 Transformer | 문맥 이해 · 검색, QA, 번역 |
| | | | Diffusion Model | 노이즈 제거 생성 | 고품질 · Sora, 영상 합성 |
| | **생성형 AI** | | GPT | 대규모 언어 모델 | 자연어 생성 · ChatGPT, 코딩 보조 |
| | | | DALL·E | 텍스트→이미지 변환 | 창의적 생성 · 디자인 보조 |
| | | | Stable Diffusion | 확산 기반 이미지 생성 | 고품질 · 예술, 광고 |
| | | | GAN | 생성자-판별자 경쟁 | 사실적 · 딥페이크, 이미지 합성 |
| | | | AutoEncoder | 인코더-디코더 재구성 | 노이즈 제거 · 이상탐지, 압축 |
| | | | VAE | 확률적 잠재공간 생성 | 안정적 · 데이터 생성, 이상 탐지 |
| | | | CLIP | 이미지-텍스트 연결 | 멀티모달 · 이미지 검색, 분류 |
| | | | NeRF | 3D 장면 신경망 렌더링 | 사실적 3D · VR/AR, 시각효과 |
| | | | Latent Variable Model | 잠재 변수 기반 생성 | 데이터 분포 학습 |
| | | | Autoregressive Model | 순차적 토큰 생성 | GPT 계열 기반 |
| | | | Flow Matching | 연속적 분포 변환 | 확산 모델 대안 |
| | | | 가우시안 노이즈 | 노이즈 추가/제거 기반 | Diffusion 핵심 |
| | **멀티모달 AI** | | CLIP | 이미지-텍스트 상호 이해 | 멀티모달 표현 학습 · 이미지 검색, 비주얼 QA |
| | | | Gemini | 텍스트·이미지·음성 통합 모델 | 통합 처리 · AI 비서, 검색, 분석 |
| | | | GPT-4o | 실시간 멀티모달 처리 | 음성·이미지·텍스트 동시 인식 · 대화형 AI |
| | | | Flamingo | 비전-언어 결합 대규모 모델 | 통합 이해 · 비주얼 QA, 멀티모달 챗봇 |
| | | | Kosmos | 텍스트-비전 통합 Transformer | 다양한 입력 포맷 · 이미지 캡셔닝 |
| | **설명가능한 AI (XAI)** | | LIME | 입력 변수의 영향도 분석 | 예측 근거 설명 · 모델 신뢰성 평가 |
| | | | SHAP | SHAP 값 기반 기여도 분석 | 글로벌·로컬 설명 · 금융·의료 의사결정 |
| | | | Counterfactual | 반사실적 시나리오 생성 | "만약 ~였다면" 분석 · 윤리적 AI |
| | | | Grad-CAM | CNN의 시각적 주목영역 시각화 | 이미지 모델 해석 · 의료 영상, 객체 탐지 |
| | | | Integrated Gradients | 입력 특징의 중요도 누적 측정 | 의사결정 해석 · 금융·의료 모델 해석 |
| | **자율형 AI** | | 자율주행 | 센서 데이터 기반 환경 인식 | 실시간 의사결정 · 자율차, 드론 |
| | | | 로봇 제어 | 강화학습 기반 행동 최적화 | 물리 환경 학습 · 산업/서비스 로봇 |
| | | | AutoGPT | 자체 목표 설정 및 실행 | 에이전트형 AI · 업무 자동화, 연구 보조 |
| | | | ReAct | 추론과 행동을 결합한 LLM 프레임워크 | 에이전트 핵심 구조 · 작업 자동화 |
| | | | Chain-of-Thought (CoT) | 단계적 사고를 통한 논리적 추론 | 복잡한 문제 해결 · 수학, 논리 추론 |

<div class="section-divider-dot">• • •</div>

## 1.4 [모델 학습] - AI 학습 프로세스

<div style="background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%); border-radius: 16px; padding: 1.5rem; margin: 1.5rem 0;">
  <div style="text-align: center; color: white; margin-bottom: 1rem;">
    <span style="font-size: 1.3rem; font-weight: 700;">🧠 핵심 암기: </span>
    <span style="background: rgba(255,255,255,0.2); padding: 0.3rem 0.8rem; border-radius: 6px; font-weight: 700; font-size: 1.1rem;">인추판제행학</span>
  </div>
  <div style="display: flex; align-items: center; gap: 0.3rem; flex-wrap: wrap; justify-content: center;">
    <div style="background: linear-gradient(135deg, #667eea, #764ba2); padding: 0.8rem 1.2rem; border-radius: 10px; color: white; text-align: center; min-width: 70px;">
      <div style="font-weight: 700; font-size: 1.2rem;">인</div>
      <div style="font-size: 0.75rem; opacity: 0.9;">👁️ 감지</div>
    </div>
    <span style="color: #667eea; font-size: 1.2rem;">→</span>
    <div style="background: linear-gradient(135deg, #764ba2, #f093fb); padding: 0.8rem 1.2rem; border-radius: 10px; color: white; text-align: center; min-width: 70px;">
      <div style="font-weight: 700; font-size: 1.2rem;">추</div>
      <div style="font-size: 0.75rem; opacity: 0.9;">🧩 분석</div>
    </div>
    <span style="color: #f093fb; font-size: 1.2rem;">→</span>
    <div style="background: linear-gradient(135deg, #f093fb, #f5576c); padding: 0.8rem 1.2rem; border-radius: 10px; color: white; text-align: center; min-width: 70px;">
      <div style="font-weight: 700; font-size: 1.2rem;">판</div>
      <div style="font-size: 0.75rem; opacity: 0.9;">⚖️ 결정</div>
    </div>
    <span style="color: #f5576c; font-size: 1.2rem;">→</span>
    <div style="background: linear-gradient(135deg, #f5576c, #ff9a44); padding: 0.8rem 1.2rem; border-radius: 10px; color: white; text-align: center; min-width: 70px;">
      <div style="font-weight: 700; font-size: 1.2rem;">제</div>
      <div style="font-size: 0.75rem; opacity: 0.9;">🎛️ 조절</div>
    </div>
    <span style="color: #ff9a44; font-size: 1.2rem;">→</span>
    <div style="background: linear-gradient(135deg, #ff9a44, #4facfe); padding: 0.8rem 1.2rem; border-radius: 10px; color: white; text-align: center; min-width: 70px;">
      <div style="font-weight: 700; font-size: 1.2rem;">행</div>
      <div style="font-size: 0.75rem; opacity: 0.9;">🏃 실행</div>
    </div>
    <span style="color: #4facfe; font-size: 1.2rem;">→</span>
    <div style="background: linear-gradient(135deg, #4facfe, #00f2fe); padding: 0.8rem 1.2rem; border-radius: 10px; color: white; text-align: center; min-width: 70px;">
      <div style="font-weight: 700; font-size: 1.2rem;">학</div>
      <div style="font-size: 0.75rem; opacity: 0.9;">📚 개선</div>
    </div>
  </div>
  <div style="text-align: center; margin-top: 1rem; color: #00f2fe; font-size: 0.85rem;">
    ↺ 피드백 루프 (Feedback Loop)
  </div>
</div>

<div class="section-divider-dot">• • •</div>

## 1.5 [모델 평가]

### AI 모델평가 체크리스트

| 구분 | 키워드 | 설명 | 암기 힌트 |
|:-----|:-------|:-----|:----------|
| 데이터 분리 | Training / Validation / Test set | 학습, 검증, 테스트 데이터로 분리해 일반화 성능 확인 | |
| 검증 방법 | Hold-out / K-Fold Cross Validation / LOOCV | 데이터를 나눠서 모델을 반복 평가 | `홀트폴리` |
| 평가 지표 | Accuracy, Precision, Recall, F1-score, RMSE 등 | 모델 성능을 수치로 표현 | |
| 과적합 확인 | Overfitting / Underfitting | 학습 데이터에만 맞춰진 모델을 방지 | |
| 베이스라인 모델 | Baseline model | 기준 성능을 세워 상대적으로 모델 개선 효과 판단 | |
| 하이퍼파라미터 튜닝 | Grid Search / Random Search / Bayesian Optimization | 모델 성능을 최적화하기 위한 파라미터 조정 | |
| 모델 비교 | Model Selection | 여러 모델 중 가장 성능이 좋은 모델 선택 | |
| 신뢰성 검증 | Robustness / Fairness / Bias 검증 | 공정성과 안정성 측면에서도 모델 평가 | |
| 시각화 | Confusion Matrix / ROC Curve / Learning Curve | 평가 결과를 시각적으로 분석 | |

### AI 성능평가지표

| 대분류 | 중분류 | 지표 | 암기법 |
|:-------|:-------|:-----|:-------|
| **지도학습** | 분류 | 혼동행렬 | `혼확밀현, PNPP` |
| | | 정확도 | |
| | | 정밀도 | |
| | | 재현율 | |
| | | F1-Score | |
| | | ROC-AUC | |
| | 회귀 | 평균 절대 오차 | `절제근결` |
| | | 평균 제곱 오차 | |
| | | 평균 제곱근 오차 | |
| | | 결정계수 | |
| **비지도학습** | 군집화 | 실루엣 계수 | `실다던R` |
| | | 다비스-볼딘 지수 | |
| | | 던 지수 | |
| | | Rand Index | |
| | 차원 축소 | 재구성 오차 | `재분정거` |
| | | 분산설명비율 | |
| | | 정답 보존율 | |
| | | 거리 보존 | |

<div class="section-divider-dot">• • •</div>

## 1.6 [모델 배포]

*(원문에 상세 내용 없음)*

<div class="section-divider-dot">• • •</div>

## 1.7 [모델 튜닝]

**핵심 키워드**: 파인튜닝, 하이퍼파라미터

<div class="section-divider-dot">• • •</div>

## 1.8 [도구]

| 단계 | 세부 단계 | 주요 도구 | 설명 |
|:-----|:----------|:----------|:-----|
| **데이터** | 데이터 수집 | **Airflow**, **Kafka**, Flume, AWS Glue, Fivetran, Scrapy, BeautifulSoup | 크롤링, 배치 파이프라인, 스트리밍 수집 |
| | 데이터 저장 | **S3**, HDFS, **BigQuery**, **Snowflake**, PostgreSQL, MongoDB, Delta Lake, Iceberg | 원천 및 정제 데이터 저장소 (Data Lake / Warehouse) |
| | 전처리 | **Spark**, **Pandas**, DBT, Databricks, Trino, Feature Store (Feast) | 데이터 정제, 피처 엔지니어링, 통합 처리 |
| **모델** | 모델 선정 | **Scikit-learn**, AutoML (H2O.ai, Google AutoML, DataRobot), **Optuna** | 알고리즘 탐색 및 하이퍼파라미터 튜닝 |
| | 모델 학습 | **TensorFlow**, **PyTorch**, Keras, XGBoost, LightGBM, **Hugging Face Transformers**, Kubeflow Pipelines | 딥러닝/머신러닝 학습 및 분산 트레이닝 |
| | 모델 평가 | **MLflow**, **Weights & Biases (W&B)**, TensorBoard, Neptune.ai, Comet.ml | 성능 지표 관리, 실험 비교, 모델 버전 관리 |
| **운영** | 모델 배포 | **Docker**, **Kubernetes**, Seldon Core, MLflow Models, TensorFlow Serving, **FastAPI**, BentoML, AWS SageMaker | 모델 서빙, 컨테이너 기반 배포 |
| | 모니터링 | **Prometheus**, **Grafana**, Evidently AI, WhyLabs, Arize AI, Neptune.ai | 모델 드리프트, 성능, 리소스 모니터링 |
| | 튜닝(피드백 루프) | **Optuna**, Ray Tune, **MLflow Tracking**, Hyperopt, Katib (Kubeflow) | 성능 개선 및 재학습 자동화 |

<div style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); color: white; padding: 1.5rem 2rem; border-radius: 12px; margin: 2rem 0; box-shadow: 0 8px 24px rgba(79, 172, 254, 0.3);">
  <h1 style="margin: 0; font-size: 1.8rem;">🌐 Part 2. 인공지능 전략 및 생태계</h1>
  <p style="margin: 0.5rem 0 0 0; opacity: 0.9; font-size: 0.95rem;">거시적 관점 | 국가 Level · 기업 Level</p>
</div>

## 2.1 인공지능 국가 Level

| 구분 | 항목 | 내용 |
|:-----|:-----|:-----|
| 버전 | AI 3대 강국 도약 | |
| 목표 | | 글로벌 AI 선도기업 육성, AI 전환 생산성 증대 |
| **실천과제** | 인프라 | AI 인프라, GPU 5만개 |
| | 산업 | 민간투자 100조 |
| | 인재 | |
| | 제도 | AI 기본법(추산윤고) |

### AI 기본법 상세 (추산윤고)

```text
추진체계
  6조. 인공지능 기본계획 수립
  7조. 국가인공지능위원회
  8조. 위원회의 기능

산업 활성화
  21조. 전문인력 확보
  22조. 국제협력, 해외시장 진출 지원
  23조. 인공지능 집적단지 지정

인공지능 윤리
  27조. 인공지능 윤리원칙
  28조. 민간자율인공지능윤리위원회 설치
  29조. 인공지능 신뢰기반 조성위한 시책마련
  30조. 인공지능 안전성 신회검증, 인증 지원
  31조. 인공지능 투명성 확보의무
  32조. 인공지능 안정성 확보의무

고영향 인공지능
  33조. 고영향 인공지능의 확인
  34조. 고영향 인공지능과 관련한 사업자의 책무
  35조. 고영향 인공지능 영향평가
  36조. 국내 대리인 지정
```

| 구분 | 항목 | 내용 | 암기법 |
|:-----|:-----|:-----|:-------|
| | ㄴ AI 윤리 | 존공함, 인프다침 공연대 책안투 | 한 페이지에 |
| | ㄴ AI 신뢰성 인증제도 | | `위거신추 상이편오 편방설사` |
| | 활용 | 모두의 AI - 국가대표 생성형 AI | |

### DX 대전환

| 구분 | 내용 |
|:-----|:-----|
| 구성요소 | `서 인 거` |
| 단계 | `전파팀 교커업` / `공파벡L` |
| 상세 절차 | 1) 공통기초 모델 → 2) 기관별 파인튜닝 → 3) 벡터DB로 환각방지 → 4) UI 프롬프트 검색 후 기관별 sLLM이 답변 |
| 주요기술 | `파스파벡R` - LLM Foundation Model, sLLM, 파인튜닝, 벡터DB, RAG |

<div class="section-divider-dot">• • •</div>

## 2.2 인공지능 기업 Level (생성형 AI 중심)

| 구분 | 항목 | 내용 | 암기법 |
|:-----|:-----|:-----|:-------|
| 구축 | | 목표 >> 인프라 구축 >> 데이터 수집 >> 모델학습 >> 전사적 전파 | `목인데학전` |
| 구성요소 | | 아래 상세 참조 | `데모 임프테 최모C` |
| 활동 | | 아래 상세 참조 | `초대기이생프` |

### 구성요소 상세 (`데모 임프테 최모C`)

| 구성요소 | 도구 예시 |
|:---------|:----------|
| 데이터 수집, 저장 | Spark, Kafka, S3, Blob Storage |
| 기반 모델 | Open AI GPT, LLAMA, Gemini, Hugging Face |
| 임베딩 처리 | Qdrant, Faiss Index, Milvus, Weaviate |
| 프롬프트 관리 | Gradient J, Honey Hive, Azure AI Studio |
| 테스트 | Fiddler AI, Humanloop |
| 버전관리 | AWS Code Commit, JenkinceX |
| 모니터링 | AnyScale, Arize |
| 최적화 | Autoblock, TruEra |

### 활동 상세 (`초대기이생프`)

| 활동 | 설명 | 예시 |
|:-----|:-----|:-----|
| 초개인화 | 추천 서비스 | Netflix, YouTube, Baemin 개인화 추천 |
| 대화형 인공지능 | 챗봇, 가상 비서 | ChatGPT, Siri, Alexa, 네이버클로바 |
| 기술 저변화 | 생명과학 AI | AlphaFold, BioNeMo |
| 이미지/음성/영상 생성 | 생성형 AI | Stable Diffusion, Midjourney |
| 이미지 생성 특화 | 이미지 생성 모델 | DALL·E |
| 개발 프로세스 혁신 | AI 개발 보조 도구 | Amazon CodeWhisperer, GitHub Copilot |

### 한계 - 거시적 측면 (STEEP 분석)

| 관점 | 한계 |
|:-----|:-----|
| 사회 (Social) | 저작권, IP |
| 기술 (Technological) | 할루시에이션, 부정확성, 최신미반영 |
| 경제 (Economic) | 대규모 컴퓨팅 자원 |
| 환경 (Environmental) | 온실가스, 에너지 위기 |
| 법/제도 (Political) | 규제미비, 입법 진행 중 |
| 윤리 | 차별표현, 불평등 |
| 보안 | 개인정보 포함 |

### 보안 위협

- 암기법: `인민공 대출과 프벡정무` / `식분평대 ISO 23894`

### 기술적 한계

| 한계 | 설명 |
|:-----|:-----|
| LLM 규모 증폭 | 파라미터 수 증폭, 연산량, 메모리 전력량 증폭 |
| 효율성 한계 | GPU 제한적 |
| 전문화 필요 | |

### LLM 성능 향상 기술

| 분류 | 기술 |
|:-----|:-----|
| 프롬프트 | CoT, MoE, 프롬프트 체이닝, 컨텍스트 엔지니어링 |
| 외부 | MCP, A2A, MAS, RAG |
| 파인튜닝 | PEFT, LoRA, LangGraph |

<div class="section-divider-dot">• • •</div>

<div style="background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%); color: white; padding: 1.5rem 2rem; border-radius: 12px; margin: 2rem 0; box-shadow: 0 8px 24px rgba(17, 153, 142, 0.3);">
  <h1 style="margin: 0; font-size: 1.8rem;">🚀 Part 3. 활용</h1>
  <p style="margin: 0.5rem 0 0 0; opacity: 0.9; font-size: 0.95rem;">실무 적용 사례 | 추후 업데이트 예정</p>
</div>

*(원문에 상세 내용 없음)*

<div style="background: linear-gradient(135deg, #3a3a3a 0%, #1a1a1a 100%); color: white; padding: 1.5rem 2rem; border-radius: 12px; margin: 2rem 0; box-shadow: 0 8px 24px rgba(0,0,0,0.3);">
  <h1 style="margin: 0; font-size: 1.8rem;">📄 부록: 원문 전체</h1>
  <p style="margin: 0.5rem 0 0 0; opacity: 0.9; font-size: 0.95rem;">AI - MAP.csv 원본 데이터 (누락 확인용)</p>
</div>

아래는 `AI - MAP.csv` 원문을 **그대로** 보존한 것입니다. 위의 정리본에서 누락된 내용이 있는지 확인할 때 사용하세요.

<details markdown="1">
<summary><strong>📄 원문 전체 보기</strong> (클릭해서 펼치기)</summary>

```text
,,,,,,
목표: 주간 모의고사에서 문제에 많은 키워드를 올바른 형식에 맞추어서 작성한다.,,,,,,
,,,,,,
<< AI 개발 Lifecycle / 머신러닝 파이프라인 >>,,,,,,
,,,,,,
수저처,선학평,배모튜,,,,
,,,,,,
"+---------------------------+      +---------------------------+      +---------------------------+
|           데이터          |      |            모델           |      |            운영           |
+---------------------------+      +---------------------------+      +---------------------------+
|  [데이터 수집]            | ---> |  [모델 선정]              | ---> |  [모델 배포]              |
|        ↓                  |      |        ↓                  |      |        ↓                  |
|  [데이터 저장]            |      |  [모델 학습]              |      |  [모니터링 / 로그]        |
|        ↓                  |      |        ↓                  |      |        ↓                  |
|  [전처리]                 |      |  [모델 평가]              |      |  [튜닝]                   |
+---------------------------+      +---------------------------+      +---------------------------+
",,,,,,
,,,,,,
"용어: 모델 서빙, 딜리버리, Data Drift, GPUaaS",,,,,,
,,,,,,
,,,,,,
[데이터 파이프라인],,,,,,
,,,,,,
"                Data Pipeline Lifecycle
┌──────────────────────────────────────────────────────────────────────────────┐
│                           데이터 파이프라인 단계                             │
└──────────────────────────────────────────────────────────────────────────────┘

[데이터 수집]
      ↓
[데이터 저장]
      ↓
[데이터 처리]
      ↓
[데이터 분석]
      ↓
[데이터 시각화]
",,,,,,
,,,,,,
인공지능은 항상 "데이터 품질"과 연결됨,,,,,,
생성형AI 품질관리 가이드 3.5,,,,,,
,,,,,,
,,,,,,
,,,,,,
[모델 선정],,,,,,
,,,,,,
AI 알고리즘,,,,,,
,,,,,,
구분,대분류,중분류,알고리즘,핵심 개념,특징,대표 활용 예시
"레거시
인공지능
알고리즘","지도학습
(Supervised Learning)

- 라벨 제공
- 미래데이터 예측
- Y = f(x)","분류
(Classification)

- 이미지 분류
- 사기 감지
- 문제 진단",SVM (Support Vector Machine),초평면으로 클래스 분리,고차원 데이터에 강함,"얼굴 인식, 텍스트 분류"
,,,KNN (K-Nearest Neighbors),주변 k개 데이터 다수결 분류,단순하지만 계산량 큼,"이미지 분류, 추천"
,,,Decision Tree,규칙 기반 트리 구조로 분류,"해석 쉬움, 과적합 위험","고객 세분화, 품질 분류"
,,,Random Forest,여러 트리의 앙상블,"과적합 감소, 안정적","의료 진단, 신용 평가"
,,,Naive Bayes,확률(조건부 확률) 기반 분류,"데이터 적어도 가능, 속도 빠름","스팸 필터링, 문서 분류"
,,,ANN,"노드 가중치 학습, 비선형 패턴 인식",복잡한 비선형 문제 해결,"음성 인식, 이미지 분류, 자율주행"
,,,Logistic Regression,확률적 분류 (시그모이드 함수),"이진 분류에 최적, 속도 빠름","스팸 메일 판별, 고객 이탈 예측"
,,"회귀
(Regression)

- 예측
- 공정최적화
- 인사이트 발견",Linear Regression,입력과 출력의 선형 관계 학습,"단순하고 해석 용이, 과적합 위험 낮음","매출 예측, 가격 예측"
,,,Regularized Linear Regression,가중치 제약(L1/L2)으로 과적합 방지,"라쏘(L1), 릿지(L2), 엘라스틱넷 혼합 사용","주가 예측, 의료 데이터 분석"
,,,Regression Tree,트리 구조로 연속값 예측,"비선형 관계 처리 가능, 과적합 주의","에너지 사용량 예측, 생산량 추정"
,,,Random Forest Regression,여러 회귀 트리의 앙상블 평균,"안정적, 과적합 감소","부동산 가격, 보험료 예측"
,,,Support Vector Regression (SVR),"마진 기반 회귀, 오차 허용 구간 내 학습","고차원 데이터 강함, 파라미터 민감","날씨 예측, 수요 예측"
,"비지도학습
(Unsupervised Learning)

- 라벨 미제공
- 데이터에 숨겨진
구조/특징 발견
- x~p(x), x=f(x)","군집화
(Clustering)

- 추천 시스템
- 타겟 마케팅
- 고객 분할",K-Means,유사도 기반 군집화,"간단, 초기값에 민감","고객 군집, 마켓 세분화"
,,,DBSCAN,밀도 기반 클러스터링,이상치 탐지에 강함,위치 기반 데이터 분석
,,,EM Clustering,확률기반 군집화(EM),,
,,,SOM,자기조직화 맵,,
,,,Hierarchical Clustering,유사도 거리 기반 트리 구조,시각화 용이,"생물 유전 분석, 조직 분류"
,,"차원 축소

- 빅데이터 가시화
- 데이터 압축
- 특징 추출",PCA (Principal Component Analysis),데이터 축소 (분산 최대 방향),차원 축소 및 시각화,"이미지 압축, 특징 추출"
,,,LDA (Linear Discriminant Analysis),"클래스 간 분산 최대, 클래스 내 분산 최소","지도형 차원 축소, 분류 성능 향상","얼굴 인식, 패턴 분류"
,,,Factor Analysis,잠재 요인으로 변수 간 관계 설명,"노이즈 제거, 변수 간 상관 해석","설문 분석, 심리 요인 분석"
,,,MDS (Multidimensional Scaling),유사도 기반 저차원 임베딩,"거리 보존, 시각화 용이","고객 세분화, 마케팅 분석"
,,연관성 규칙 발견,MBA (Market Basket Analysis),항목 간 동시 발생 규칙 탐색,"지지도·신뢰도 기반, 직관적 해석","상품 추천, 교차판매"
,,,Sequence Analysis,순서가 있는 패턴 탐색,시계열·구매 순서 분석에 활용,"고객 행동 예측, 웹 클릭 패턴"
,,,Collaborative Filtering,유사 사용자/아이템 기반 추천,명시적·암시적 피드백 활용,"영화·음악 추천, 개인화 서비스"
,"강화학습
(Reinforcement Learning)

- 실시간 의사결정
- 게임AI
- 작업 학습
- 로복 네비게이션","가치기반
(Value-based)",Q-Learning,가치함수 기반 행동 학습,"테이블 기반, 단순","게임 AI, 로봇 경로 탐색"
,,,DQN (Deep Q-Network),Q-Learning + 딥러닝,이미지 기반 환경 처리 가능,"AlphaGo, 자율주행"
,,"정책기반
(Policy-based)",Policy Gradient,정책함수 직접 최적화,확률적 정책 학습,"드론 제어, 강화형 게임"
,,,PPO (Proximal Policy Optimization),정책 기반 안정화 알고리즘,학습 안정성 높음,"ChatGPT 학습, 시뮬레이션 제어"
,,,SARSA,현재 정책 기반 학습,"안정적, 보수적",강화형 로봇 제어
,,"하이브리드
(Actor–Critic형)",Actor–Critic,정책 + 가치 결합형,"효율적 학습, 안정적 수렴","자율주행, 로봇 강화학습"
"현대
인공지능
알고리즘",딥러닝,,DBN (Deep Belief Network),확률 그래프 기반 신경망,딥러닝 전단계 구조 (초기 모델),"패턴 인식, 음성 인식"
,,,CNN (Convolutional Neural Network),이미지의 픽셀 관계를 학습,시각 정보 처리에 특화,"이미지 분류, 얼굴 인식"
,,,RNN (Recurrent Neural Network),순차 데이터의 시간 의존성 학습,"시계열, 자연어 처리에 강점","음성 인식, 텍스트 분석"
,,,GNN (Graph Neural Network),노드 간 연결 관계를 학습,비정형(그래프) 데이터 처리,"SNS 분석, 추천 시스템"
,,,Transformer,Attention 메커니즘 기반 병렬 학습,"긴 문맥 처리, 병렬화 우수","번역, 챗봇, 문서 요약"
,,,LSTM (Long Short-Term Memory),장기 의존성 문제 해결한 RNN 구조,시계열 예측에 강함,"음성 인식, 주가 예측"
,,,GRU (Gated Recurrent Unit),"LSTM 단순화 버전, 연산 효율 높음",빠른 학습 속도,"텍스트 분석, 음성 인식"
,,,BERT (Bidirectional Encoder Representations from Transformers),양방향 Transformer 인코더 구조,문맥 이해에 탁월,"검색, 질의응답, 번역"
,,,Diffusion Model,노이즈 제거 기반 데이터 생성,고품질 이미지·영상 생성,"이미지 생성, Sora, 영상 합성"
,생성형 AI (Generative AI),,GPT (Generative Pretrained Transformer),"대규모 언어 모델, 문맥 기반 생성",자연어 생성 및 이해,"ChatGPT, 코딩 보조"
,,,DALL·E,텍스트-이미지 변환 모델,창의적 이미지 생성,"이미지 생성, 디자인 보조"
,,,Stable Diffusion,확산(노이즈 제거) 기반 이미지 생성,고품질·세밀한 이미지 생성,"예술, 광고, 컨텐츠 생성"
,,,GAN (Generative Adversarial Network),생성자와 판별자의 경쟁 학습,사실적 이미지 생성에 강함,"딥페이크, 이미지 합성"
,,,AutoEncoder,인코더–디코더 구조로 데이터 재구성,"비선형 특성 학습, 노이즈 제거","이상탐지, 데이터 압축"
,,,VAE (Variational AutoEncoder),확률적 잠재공간 기반 생성,"안정적 학습, 잠재 변수 추출","데이터 생성, 이상 탐지"
,,,CLIP,,,
,,,NerF,,,
,,,Latent Variable Model,,,
,,,Autogressive Model,,,
,,,Flow Matching,,,
,,,가우시안 노이즈,,,
,멀티모달 AI (Multimodal AI),,CLIP,이미지-텍스트 상호 이해,멀티모달 표현 학습,"이미지 검색, 비주얼 QA"
,,,Gemini,텍스트·이미지·음성 통합 모델,다양한 입력을 통합 처리,"AI 비서, 검색, 분석"
,,,GPT-4o,실시간 멀티모달 처리,음성·이미지·텍스트 동시 인식,"대화형 AI, 고객 응대"
,,,Flamingo,비전-언어 결합 대규모 모델,이미지·텍스트 통합 이해,"비주얼 QA, 멀티모달 챗봇"
,,,Kosmos,텍스트-비전 통합 Transformer,다양한 입력 포맷 처리,"이미지 캡셔닝, 멀티모달 분석"
,설명가능한 AI (XAI),,LIME,입력 변수의 영향도 분석,모델 예측 근거 설명,모델 신뢰성 평가
,,,SHAP,SHAP 값 기반 기여도 분석,글로벌·로컬 설명 모두 가능,금융·의료 의사결정 지원
,,,Counterfactual,반사실적 시나리오 생성,"만약 ~였다면" 분석,"윤리적 AI, 정책 시뮬레이션"
,,,Grad-CAM (Gradient-weighted Class Activation Mapping),CNN의 시각적 주목영역 시각화,이미지 모델 해석 가능,"의료 영상, 객체 탐지"
,,,Integrated Gradients,입력 특징의 중요도 누적 측정,모델 의사결정 해석에 용이,금융·의료 모델 해석
,자율형 AI (Autonomous AI),,자율주행,센서 데이터 기반 환경 인식 및 판단,실시간 의사결정 및 제어,"자율차, 드론"
,,,로봇 제어,강화학습 기반 행동 최적화,물리적 환경에서 학습,"산업 로봇, 서비스 로봇"
,,,AutoGPT,자체 목표 설정 및 실행,"에이전트형 AI, 자율 문제 해결","업무 자동화, 연구 보조"
,,,ReAct (Reason + Act),추론과 행동을 결합한 LLM 프레임워크,에이전트형 AI 핵심 구조,"AutoGPT, 작업 자동화"
,,,Chain-of-Thought (CoT),단계적 사고를 통한 논리적 추론,복잡한 문제 해결 능력 향상,"수학 문제, 논리 추론 AI"
,,,,,,
,,,,,,
,,,,,,
[모델 학습],,,,,,
,,,,,,
AI 학습 프로세스,,,,,,
,,,,,,
인 추 판 제 행 학,,,,,,
,,,,,,
"                    학습 단계
┌──────────────────────────────────────────────────────────────────────┐
│                                                                      │
│  [인식] ──▶ [추론] ──▶ [판단] ──▶ [제어] ──▶ [행동] ──▶ [학습]        │
│    ▲                                                        │        │
│    └─────────────── 피드백 루프 (Feedback Loop) ───────────┘        │
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
",,,,,,
,,,,,,
[모델 평가],,,,,,
,,,,,,
AI 모델평가,,,,,,
,,,,,,
구분,키워드,,설명,,,
데이터 분리,Training / Validation / Test set,,"학습, 검증, 테스트 데이터로 분리해 일반화 성능 확인",,,
검증 방법,Hold-out / K-Fold Cross Validation / LOOCV,,데이터를 나눠서 모델을 반복 평가,홀트폴리,,
평가 지표,"Accuracy, Precision, Recall, F1-score, RMSE 등",,모델 성능을 수치로 표현,,,
과적합 확인,Overfitting / Underfitting,,학습 데이터에만 맞춰진 모델을 방지,,,
베이스라인 모델,Baseline model,,기준 성능을 세워 상대적으로 모델 개선 효과 판단,,,
하이퍼파라미터 튜닝,Grid Search / Random Search / Bayesian Optimization,,모델 성능을 최적화하기 위한 파라미터 조정,,,
모델 비교,Model Selection,,여러 모델 중 가장 성능이 좋은 모델 선택,,,
신뢰성 검증,Robustness / Fairness / Bias 검증,,공정성과 안정성 측면에서도 모델 평가,,,
시각화,Confusion Matrix / ROC Curve / Learning Curve,,평가 결과를 시각적으로 분석,,,
,,,,,,
,,,,,,
AI 성능평가지표,,,,,,
,,,,,,
대분류,중분류,알고리즘,,,,
지도학습,분류,혼동행렬,"혼확밀현, PNPP",,,
,,정확도,,,,
,,정밀도,,,,
,,재현율,,,,
,,F1-Score,,,,
,,ROC-AUC,,,,
,회귀,평균 절대 오차,절제근결,,,
,,평균 제곱 오차,,,,
,,평균 제곱근 오차,,,,
,,결정계수,,,,
비지도학습,군집화,실루엣 계수,실다던R,,,
,,다비스-볼딘 지수,,,,
,,던 지수,,,,
,,Rand Index,,,,
,차원 축소,재구성 오차,재분정거,,,
,,분산설명비율,,,,
,,정답 보존율,,,,
,,거리 보존,,,,
,,,,,,
,,,,,,
,,,,,,
[모델 배포],,,,,,
,,,,,,
,,,,,,
,,,,,,
,,,,,,
,,,,,,
,,,,,,
,,,,,,
,,,,,,
,,,,,,
,,,,,,
,,,,,,
,,,,,,
[모델 튜닝],,,,,,
,,,,,,
"파인튜닝, 하이퍼파라미터",,,,,,
,,,,,,
,,,,,,
,,,,,,
,,,,,,
[도구],,,,,,
,,,,,,
단계,세부 단계,주요 도구,,설명,,
데이터,데이터 수집,"Airflow, Kafka, Flume, AWS Glue, Fivetran, Scrapy, BeautifulSoup",,"크롤링, 배치 파이프라인, 스트리밍 수집",,
,데이터 저장,"S3, HDFS, BigQuery, Snowflake, PostgreSQL, MongoDB, Delta Lake, Iceberg",,원천 및 정제 데이터 저장소 (Data Lake / Warehouse),,
,전처리,"Spark, Pandas, DBT, Databricks, Trino, Feature Store (Feast)",,"데이터 정제, 피처 엔지니어링, 통합 처리",,
모델,모델 선정,"Scikit-learn, AutoML (H2O.ai, Google AutoML, DataRobot), Optuna",,알고리즘 탐색 및 하이퍼파라미터 튜닝,,
,모델 학습,"TensorFlow, PyTorch, Keras, XGBoost, LightGBM, Hugging Face Transformers, Kubeflow Pipelines",,딥러닝/머신러닝 학습 및 분산 트레이닝,,
,모델 평가,"MLflow, Weights & Biases (W&B), TensorBoard, Neptune.ai, Comet.ml",,"성능 지표 관리, 실험 비교, 모델 버전 관리",,
운영,모델 배포,"Docker, Kubernetes, Seldon Core, MLflow Models, TensorFlow Serving, FastAPI, BentoML, AWS SageMaker",,"모델 서빙, 컨테이너 기반 배포",,
,모니터링,"Prometheus, Grafana, Evidently AI, WhyLabs, Arize AI, Neptune.ai",,"모델 드리프트, 성능, 리소스 모니터링",,
,튜닝(피드백 루프),"Optuna, Ray Tune, MLflow Tracking, Hyperopt, Katib (Kubeflow)",,성능 개선 및 재학습 자동화,,
,,,,,,
,,,,,,
,,,,,,
,,,,,,
,,,,,,
,,,,,,
,,,,,,
,,,,,,
<< 인공지능 전략 및 생태계 (거시적 관점) >>,,,,,,
,,,,,,
인공지능 국가 Level,,,,,,
,,,,,,
구분,항목,,내용,,,
버전,AI 3대 강국 도약,,,,,
목표,"글로벌 AI 선도기업 육성, AI 전환 생산성 증대",,,,,
실천과제,인프라,,"AI 인프라, GPU 5만개",,,
,산업,,민간투자 100조,,,
,인재,,,,,
,제도,,"AI 기본법(추산윤고)

추진체계
6조. 인공지능 기본계획 수립
7조. 국가인공지능위원회
8조. 위원회의 기능

산업 활성화
21조. 전문인력 확보
22조. 국제협력, 해외시장 진출 지원
23조. 인공지능 집적단지 지정

인공지능 윤리
27조. 인공지능 윤리원칙
28조. 민간자율인공지능윤리위원회 설치
29조. 인공지능 신뢰기반 조성위한 시책마련
30조. 인공지능 안전성 신회검증, 인증 지원
31조. 인공지능 투명성 확보의무
32조. 인공지능 안정성 확보의무

고영향 인고지능
33조. 고영향 인공지능의 확인
34조. 고영향 인공지능과 관련한 사업자의 책무
35조. 고영향 인공지능 영향평가
36조. 국내 대리인 지정",,,
,ㄴ AI 윤리,,"존공함, 인프다침 공연대 책안투
 - 한 페이지에",,,
,ㄴ AI 신뢰성 인증제도,,위거신추 상이편오 편방설사,,,
,활용,,모두의 AI - 국가대표 생성형 AI,,,
,ㄴ DX 대전환,,"(구성요소) 서 인 거
(단계) 전파팀 교커업 / 공파벡L

1) 공통기초 모델
2) 기관별 파인튜닝
3) 벡터DB로 환각방지
4) UI 프롬프트 검색 후 기관별 sLLM이 답변 

(주요기술) 파스파벡R

LLM Foundation Model, sLLM, 파인튜닝, 벡터DB, RAG",,,
,,,,,,
,,,,,,
인공지능 기업 Level (생성형 AI 중심),,,,,,
,,,,,,
구분,항목,,내용,,,
구축,목인데학전,,목표 >> 인프라 구축 >> 데이터 수집 >> 모델학습 >> 전사적 전파,,,
구성요소,데모 임프테 최모C,,"데이터 수집, 저장 - Spark, Kafka, S3, Blob Storage
기반 모델 - Open AI GPT, LLAMA, Gemini, Hugging Face
임베딩 처리 - Qdrant, Faiss Index, Milvus, Weaviate
프롬프트 관리 - Gradient J, Honey Hive, Azure AI Studio
테스트 - Fiddler AI, Humanloop
버전관리 - AWS Code Commit, JenkinceX
모니터링 - AnyScale, Arize
최적화 - Autoblock, TruEra",,,
활동,초대기이생프,,"초개인화 - 추천 서비스 (예: Netflix, YouTube, Baemin 개인화 추천)
대화형 인공지능 - 챗봇, 가상 비서 (예: ChatGPT, Siri, Alexa, 네이버클로바)
기술 저변화 - 생명과학 AI (예: AlphaFold, BioNeMo)
이미지/음성/영상 생성 - 생성형 AI (예: Stable Diffusion, Midjourney)
이미지 생성 특화 - 이미지 생성 모델 (예: DALL·E)
개발 프로세스 혁신 - AI 개발 보조 도구 (예: Amazon CodeWhisperer, GitHub Copilot)",,,
한계,거시적 측면 한계 (STEEP 분석),,"STEEP

사회 - 저작권, IP
기술 - 할루시에이션, 부정확성, 최신미반영
경제 - 대규모 컴퓨팅 자원
환경 - 온실가스, 에너지 위기
법/제도 - 규제미비, 입법 진행 중
윤리 - 차별표현, 불평등
보안 - 개인정보 포함",,,
보안 위협,인민공 대출과 프벡정무 / 식분평대 ISO 23894,,,,,
기술적 한계,"LLM 규모 증폭, 효율성 한계, 전문화 필요",,"LLM 규모 증폭 - 파라미터 수 증폭, 연산량, 메모리 전력량 증폭
효율성 한계 - GPU 제한적
전문화 필요 ",,,
LLM 성능 향상 기술,,,,,,
ㄴ 프롬프트,"CoT, MoE, 프롬프트 체이닝, 컨텍스트 엔지니어링",,,,,
ㄴ 외부,"MCP, A2A, MAS, RAG",,,,,
ㄴ 파인튜닝,"PEFT, LoRA, LangGraph",,,,,
,,,,,,
,,,,,,
,,,,,,
,,,,,,
<< 활용 >>,,,,,,
```

</details>
