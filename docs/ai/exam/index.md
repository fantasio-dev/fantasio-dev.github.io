---
layout: default
title: 📝 기출문제
parent: AI (인공지능)
has_children: true
has_toc: false
nav_order: 99
permalink: /docs/ai/exam
---

<!-- DataTables CSS -->
<link rel="stylesheet" href="https://cdn.datatables.net/1.13.7/css/jquery.dataTables.min.css">
<link rel="stylesheet" href="https://cdn.datatables.net/searchpanes/2.2.0/css/searchPanes.dataTables.min.css">
<link rel="stylesheet" href="https://cdn.datatables.net/select/1.7.0/css/select.dataTables.min.css">

<style>
/* 페이지 전체 너비 확장 */
.main-content {
  max-width: 100% !important;
}
.main-content-wrap {
  max-width: 100% !important;
  padding-left: 1rem;
  padding-right: 1rem;
}

/* 테이블 스타일 */
#examTable {
  width: 100% !important;
  font-size: 0.85rem;
}
#examTable th {
  background-color: #f8f9fa;
  white-space: nowrap;
  text-align: center;
}
#examTable td {
  vertical-align: middle;
}
/* 회차, 정/컴, 교시, 번호 컬럼 - 폭 최소화 */
#examTable td:nth-child(1),
#examTable td:nth-child(2),
#examTable td:nth-child(3),
#examTable td:nth-child(4),
#examTable th:nth-child(1),
#examTable th:nth-child(2),
#examTable th:nth-child(3),
#examTable th:nth-child(4) {
  width: 1%;
  white-space: nowrap;
  text-align: center;
  padding: 0.2rem 0.25rem;
  font-size: 0.8rem;
}
/* 문제 컬럼 */
#examTable td:nth-child(5) {
  white-space: normal;
  min-width: 300px;
}
/* 관련토픽 컬럼 */
#examTable td:nth-child(6) {
  white-space: nowrap;
  width: 1%;
}
/* 암기법 컬럼 - 폭 넓게 */
#examTable td:nth-child(7),
#examTable th:nth-child(7) {
  font-family: 'Consolas', 'Monaco', monospace;
  font-size: 0.8rem;
  color: #d63384;
  min-width: 180px;
  white-space: nowrap;
}

/* 학습완료 행 스타일 */
.completed {
  background-color: #d4edda !important;
}

/* 필터 버튼 스타일 */
.filter-buttons {
  margin-bottom: 1rem;
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}
.filter-btn {
  padding: 0.4rem 0.8rem;
  border: 1px solid #dee2e6;
  border-radius: 4px;
  background: #fff;
  cursor: pointer;
  font-size: 0.85rem;
  transition: all 0.2s;
}
.filter-btn:hover {
  background: #e9ecef;
}
.filter-btn.active {
  background: #0d6efd;
  color: white;
  border-color: #0d6efd;
}

/* DataTables 커스텀 */
.dataTables_wrapper .dataTables_filter input {
  padding: 0.5rem 1rem;
  border: 2px solid #dee2e6;
  border-radius: 20px;
  font-size: 0.9rem;
  width: 250px;
}
.dataTables_wrapper .dataTables_filter input:focus {
  border-color: #0d6efd;
  outline: none;
}
.dataTables_wrapper .dataTables_length select {
  padding: 0.3rem;
  border-radius: 4px;
}

/* 링크 스타일 */
#examTable a {
  color: #0d6efd;
  text-decoration: none;
}
#examTable a:hover {
  text-decoration: underline;
}
</style>

# AI 기출문제
{: .fs-9 }

AI(인공지능) 관련 기출문제 모음입니다. **검색, 정렬, 필터링**이 가능합니다.
{: .fs-6 .fw-300 }

---

## 🔍 빠른 필터

<div class="filter-buttons">
  <button class="filter-btn active" data-filter="all">전체</button>
  <button class="filter-btn" data-filter="1">1교시 (단답형)</button>
  <button class="filter-btn" data-filter="essay">서술형 (2~4교시)</button>
  <button class="filter-btn" data-filter="2">2교시</button>
  <button class="filter-btn" data-filter="3">3교시</button>
  <button class="filter-btn" data-filter="4">4교시</button>
  <button class="filter-btn" data-filter="has-page">📄 학습페이지 있음</button>
  <button class="filter-btn" data-filter="has-mnemonic">🧠 암기법 있음</button>
</div>

---

## 📋 기출문제 목록

<table id="examTable" class="display compact">
<thead>
<tr>
  <th>회차</th>
  <th>정/컴</th>
  <th>교시</th>
  <th>번호</th>
  <th>문제</th>
  <th>관련토픽</th>
  <th>암기법</th>
</tr>
</thead>
<tbody>
<!-- 137회 -->
<tr class="has-page has-mnemonic"><td>137</td><td>관리</td><td>1</td><td>5</td><td><a href="/docs/ai/exam/137-1-5-gnn">GNN(Graph Neural Network)을 설명하시오</a></td><td>GNN</td><td><code>(절차) 변취업생</code> <code>(구성요소) 인노엣라</code> <code>(모델) GCN-SAGE-GAT-GIN</code></td></tr>
<tr class="has-page has-mnemonic"><td>137</td><td>관리</td><td>1</td><td>7</td><td><a href="/docs/ai/exam/137-1-7-moe">트랜스포머(Transformer)와 MoE(Mixture of Experts)를 설명하시오.</a></td><td>Transformer, MoE</td><td><code>(Transformer) 셀멀포피</code> <code>(MoE) 게전스로</code> <code>(비교) 연주활병로장단대</code></td></tr>
<tr class="has-page has-mnemonic"><td>137</td><td>관리</td><td>1</td><td>8</td><td><a href="/docs/ai/exam/137-1-8-ai">AI 신뢰성 검인증 제도(CAT)를 설명하시오</a></td><td>CAT</td><td><code>(암기법) 위거신추</code> <code>(암기법) 상이편오</code> <code>(암기법) 편방설사</code></td></tr>
<tr class="has-page has-mnemonic"><td>137</td><td>컴시응</td><td>1</td><td>8</td><td><a href="/docs/ai/exam/137-1-8-rag-fine-tuning">RAG(Retrieval Augmented Generation)과 Fine Tuning의 기본 개념과 대표 프레임워크</a></td><td>RAG, Fine-Tuning</td><td><code>(RAG절차) 질유관추프텍</code> <code>(FT절차) 데모하파평</code> <code>(RAG FW) L-L-H-R</code> <code>(FT FW) P-U-I-O</code></td></tr>
<tr class="has-page has-mnemonic"><td>137</td><td>컴시응</td><td>1</td><td>9</td><td><a href="/docs/ai/exam/137-1-9-topic">멀티모달(Multimodal)의 기술요소</a></td><td>Multimodal</td><td><code>(처리기술) 지음이추</code> <code>(융합기술) 얼레크</code> <code>(리스크) 입융추출</code></td></tr>
<tr class="has-page has-mnemonic"><td>137</td><td>관리</td><td>1</td><td>12</td><td><a href="/docs/ai/exam/137-1-12-bst">이진 탐색 트리를 설명하시오.</a></td><td>BST, AVL, Red-Black</td><td><code>(구성) 루부자리왼오</code> <code>(조건) 유전왼오</code> <code>(비교) 균동검삽시공</code></td></tr>
<tr class="has-page"><td>137</td><td>관리</td><td>2</td><td>3</td><td><a href="/docs/ai/exam/137-2-3-mcp">MCP(Model Context Protocol)를 이용한 인공지능 서비스 구축시 보안 취약점을 설명하고 대응방안을 제시하시오</a></td><td>-</td><td>-</td></tr>
<tr class="has-page"><td>137</td><td>관리</td><td>2</td><td>4</td><td><a href="/docs/ai/exam/137-2-4-ai-2-0-ai-ai-ai">"공공부문 초거대 AI 도입, 활용 가이드라인 2.0"에 대하여 다음을 설명하시오 가. 초거대 AI 의 개념과 구성요소 나. 초거대 AI 의 기술요소 다. 초거대 AI 의 도입절차</a></td><td>-</td><td>-</td></tr>
<tr class="has-page"><td>137</td><td>컴시응</td><td>2</td><td>4</td><td><a href="/docs/ai/exam/137-2-4-sllm-sllm-sllm-llm-sllm">sLLM(Smaller Large Language Model)에 대하여 다음 사항을 설명하시오 가. sLLM의 정의 및 필요성 나. sLLM의 주요 기술 및 활용분야 다. LLM과 sLLM 비교</a></td><td>-</td><td>-</td></tr>
<tr class="has-page"><td>137</td><td>관리</td><td>2</td><td>6</td><td><a href="/docs/ai/exam/137-2-6-text2sql-text2sql-text2sql-2">TEXT2SQL 에 대하여 다음 각 항목을 설명하시오. 가. TEXT2SQL 의 개념 나. TEXT2SQL 활용 사례 2 가지</a></td><td>-</td><td>-</td></tr>
<tr class="has-page"><td>137</td><td>컴시응</td><td>4</td><td>3</td><td><a href="/docs/ai/exam/137-4-3-topic-137-4-3">양자 머신러닝(QML, Quantum Machine Learning)의 주요 기술 및 알고리즘을 설명하고, 기존 머신러닝과 비교하시오.</a></td><td>-</td><td>-</td></tr>
<tr class="has-page"><td>137</td><td>관리</td><td>4</td><td>5</td><td><a href="/docs/ai/exam/137-4-5-topic-137-4-5">유전 알고리즘(Genetic Algorithm)에 대하여 설명하시오. 가. 유전 알고리즘의 개념 및 절차 나. 유전 알고리즘의 최적화 방법</a></td><td>-</td><td>-</td></tr>
<!-- 136회 -->
<tr class="has-page has-mnemonic"><td>136</td><td>관리</td><td>1</td><td>2</td><td><a href="/docs/ai/exam/136-1-2-ai-136-1-2">범용 AI(General-Purpose AI) 위험관리 프레임워크</a></td><td>GPAI Risk</td><td><code>(절차) 식분평대</code> <code>(대응) 제완모수</code> <code>(평가) 점3등</code></td></tr>
<tr class="has-page has-mnemonic"><td>136</td><td>관리</td><td>1</td><td>3</td><td><a href="/docs/ai/exam/136-1-3-ai-136-1-3">에이전틱 AI(Agentic AI)</a></td><td>Agentic AI</td><td><code>(루프) 인추행학</code> <code>(구성) LLM-메도데</code> <code>(특징) 자목상반</code></td></tr>
<tr class="has-page has-mnemonic"><td>136</td><td>관리</td><td>1</td><td>13</td><td><a href="/docs/ai/exam/136-1-13-mcp">MCP(Model Context Protocol)</a></td><td>MCP, A2A</td><td><code>(Actor) 호클서</code> <code>(Context) 리툴프</code> <code>(특징) 컨개확</code></td></tr>
<tr class="has-page"><td>136</td><td>관리</td><td>2</td><td>3</td><td><a href="/docs/ai/exam/136-2-3-ai-llm-3">AI 기반 소프트웨어 개발에서 LLM(Large Language Model)을 도입할 때 고려해야 할보안 위험을 3 가지 이상 쓰고 각 대응 방안을 설명하시오.</a></td><td>-</td><td>-</td></tr>
<tr class="has-page"><td>136</td><td>관리</td><td>3</td><td>2</td><td><a href="/docs/ai/exam/136-3-2-ax-ax-ax-3">최근 인공지능(AI)을 활용한 기업의 디지털 전환(AX, Al Transformation)이 다양한 산업 분야에서 빠르게 진행되고 있다. 이와 관련하여 다음을 설명하시오. 가. 기업에서 AX가 중요한 이유 나. 기업에서 AX를 성공적으로 추진하기 위한 전략적 추진 절차와 고려사항 다. 기업이 AX 를 추진할 때 발생 가능한 장애 요인 3 가지 이상과 각 대응방안</a></td><td>-</td><td>-</td></tr>
<tr class="has-page"><td>136</td><td>관리</td><td>3</td><td>4</td><td><a href="/docs/ai/exam/136-3-4-3">데이터 분석 시 아웃라이어(Outlier)에 대하여 다음을 설명하시오. 가. 아웃라이어의 개념 나. 아웃라이어와 노이즈(Noise)의 차이점 다. 아웃라이어의 3 가지 유형인 전역, 맥락, 군집</a></td><td>-</td><td>-</td></tr>
<tr class="has-page"><td>136</td><td>관리</td><td>3</td><td>5</td><td><a href="/docs/ai/exam/136-3-5-true-positive-100-false-positive-5-false-negative-7-true-neg">혼동행렬(Confusion Matrix) 결과를 참고하여 다음을 계산하고 설명하시오. 결과 : True Positive(TP)=100, False Positive(FP)=5, False Negative(FN)=7, True. Negative(TN)=9 (단, 계산 결과는 %로 표시하고 소수점은 버린다.) 가. 혼동행렬을 사용한 모델의 성능 평가 원리 나. 정확도, 정밀도, 재현율 계산 결과와 해석 다. F1-score 계산 결과와 해석</a></td><td>-</td><td>-</td></tr>
<tr class="has-page"><td>136</td><td>관리</td><td>4</td><td>1</td><td><a href="/docs/ai/exam/136-4-1-ai-3-10-ai">국내 인공지능(AI) 윤리기준과 생성형 AI에 대하여 다음을 설명하시오. 가. 3대 기본 원칙과 10대 핵심요건(과기정통부 인공지능 윤리기준) 나. 인공지능 윤리 관점에서 생성형 AI의 역기능 요소</a></td><td>-</td><td>-</td></tr>
<!-- 135회 -->
<tr class="has-page has-mnemonic"><td>135</td><td>관리</td><td>1</td><td>1</td><td><a href="/docs/ai/exam/135-1-1-pr-roc">PR(Precision Recall) 곡선과 ROC(Receiver Operating Characteristic) 곡선 비교</a></td><td>PR, ROC, AUC</td><td><code>(PR) 정재F1</code> <code>(ROC) 참거특</code> <code>(비교) 축목불곡AUC장단사</code></td></tr>
<tr class="has-page has-mnemonic"><td>135</td><td>관리</td><td>1</td><td>2</td><td><a href="/docs/ai/exam/135-1-2-multimodal-llm">Multimodal LLM(Large Language Model)</a></td><td>Multimodal LLM</td><td><code>(전처리) 토해스영</code> <code>(인코더) 트비웨</code> <code>(융합) 얼미레</code></td></tr>
<tr class="has-page"><td>135</td><td>컴시응</td><td>1</td><td>4</td><td><a href="/docs/ai/exam/135-1-4-topic-135-1-4">몬테카를로 트리탐색(Monte Carlo Tree Search)</a></td><td>-</td><td>-</td></tr>
<tr class="has-page has-mnemonic"><td>135</td><td>관리</td><td>1</td><td>6</td><td><a href="/docs/ai/exam/135-1-6-topic-135-1-6">실루엣 계수(Silhouette Coefficient)</a></td><td>Clustering 평가</td><td><code>(정의) 응분</code> <code>(공식) 바아맥</code> <code>(활용) 최K비이</code></td></tr>
<tr class="has-page has-mnemonic"><td>135</td><td>관리</td><td>1</td><td>8</td><td><a href="/docs/ai/exam/135-1-8-unbiased-estimator">불편추정량(Unbiased Estimator)</a></td><td>추정통계</td><td><code>(준거) 불효일충</code> <code>(유형) 평분비</code> <code>(조건) 기편표</code></td></tr>
<tr class="has-page"><td>135</td><td>컴시응</td><td>1</td><td>9</td><td><a href="/docs/ai/exam/135-1-9-topic-135-1-9">인공지능 성능 관련 차원의 저주 (Curse of Dimensionality)</a></td><td>-</td><td>-</td></tr>
<tr class="has-page"><td>135</td><td>관리</td><td>1</td><td>12</td><td><a href="/docs/ai/exam/135-1-12-vae">VAE(Variational AutoEncoder)</a></td><td>-</td><td>-</td></tr>
<tr class="has-page"><td>135</td><td>컴시응</td><td>1</td><td>12</td><td><a href="/docs/ai/exam/135-1-12-rag">RAG(Retrieval-Augmented Generation)</a></td><td>-</td><td>-</td></tr>
<tr class="has-page"><td>135</td><td>관리</td><td>1</td><td>13</td><td><a href="/docs/ai/exam/135-1-13-agi-ani">AGI(Artificial General Intelligence) 측면에서 ANI(Artificial Narrow Intelligence)의 필요성</a></td><td>-</td><td>-</td></tr>
<tr class="has-page"><td>135</td><td>컴시응</td><td>2</td><td>1</td><td><a href="/docs/ai/exam/135-2-1-topic-135-2-1">「생성형 인공지능 학습을 위한 멀티모달 데이터의 품질검증 방법(정보통신단체표준, TTAK.KO-10.1558)」 에 대하여 아래 사항을 설명하시오. 가. 생성형 인공지능 학습용 멀티모달 데이터 품질특성 나. 생성 데이터 유형별 유효성 검증 방법</a></td><td>-</td><td>-</td></tr>
<tr class="has-page"><td>135</td><td>관리</td><td>2</td><td>3</td><td><a href="/docs/ai/exam/135-2-3-topic-135-2-3">회귀모형에서 오차의 등분산성(Homoscedasticity)과 다중공선성(Multicollinearity)에 대하여 설명하시오.</a></td><td>-</td><td>-</td></tr>
<tr class="has-page"><td>135</td><td>관리</td><td>2</td><td>5</td><td><a href="/docs/ai/exam/135-2-5-5-5">최근 많은 공공기관에서 거대 언어 모델(Large Language Model)의 적용을 준비하고 있다. 다음에 대하여 설명하시오. 가. 거대 언어 모델 적용을 위한 5가지 고려사항 나. 현재 구현 가능한 5가지 거대 언어 모델 아키텍처</a></td><td>-</td><td>-</td></tr>
<tr class="has-page"><td>135</td><td>관리</td><td>3</td><td>2</td><td><a href="/docs/ai/exam/135-3-2-topic-135-3-2">프롬프트 엔지니어링(Prompt Enginerng)의 기술 요소와 활용 방안에 대하여 설명하시오</a></td><td>-</td><td>-</td></tr>
<tr class="has-page"><td>135</td><td>컴시응</td><td>3</td><td>6</td><td><a href="/docs/ai/exam/135-3-6-topic-135-3-6">연결 리스트(Linked List)에 대하여 아래 사항을 설명하시오. 가. 연결 리스트의 개념 및 적용 분야 나. 연결 리스트 구현 방법 다. 배열 리스트(Array List)와 연결 리스트(Linked List)의 비교</a></td><td>-</td><td>-</td></tr>
<tr class="has-page"><td>135</td><td>관리</td><td>4</td><td>1</td><td><a href="/docs/ai/exam/135-4-1-topic-135-4-1">확장성 해싱 (Extendible Hashing)기법에 대하여 다음을 설명하시오. 가. 개념 및 구성요소 나. 충돌회피 기법</a></td><td>-</td><td>-</td></tr>
<tr class="has-page"><td>135</td><td>관리</td><td>4</td><td>3</td><td><a href="/docs/ai/exam/135-4-3-topic-135-4-3">이항 분포(Binomial Distribution)와 포아송 분포(Poisson Distribution)를 비교 설명하시오.</a></td><td>-</td><td>-</td></tr>
<tr class="has-page"><td>135</td><td>관리</td><td>4</td><td>5</td><td><a href="/docs/ai/exam/135-4-5-topic-135-4-5">인공지능 소프트웨어 품질 보증을 위한 테스트 기법에 대하여 설명하시오. 가. 메타모픽 테스트(Metamorphic Test) 나. 뉴런 커버리지 테스트(Neuron Coverage Test) 다. 안전 변경 최대화 테스트</a></td><td>-</td><td>-</td></tr>
<!-- 134회 -->
<tr class="has-page"><td>134</td><td>관리</td><td>1</td><td>3</td><td><a href="/docs/ai/exam/134-1-3-topic-134-1-3">머신러닝(Machine Learning) 성능지표</a></td><td>-</td><td>-</td></tr>
<tr class="has-page"><td>134</td><td>관리</td><td>1</td><td>6</td><td><a href="/docs/ai/exam/134-1-6-topic-134-1-6">이미지 데이터 어노테이션(Data Annotation) 유형과 기법</a></td><td>-</td><td>-</td></tr>
<tr class="has-page"><td>134</td><td>관리</td><td>1</td><td>13</td><td><a href="/docs/ai/exam/134-1-13-rag-134-1-13">RAG(Retrieval Augmented Generation)</a></td><td>-</td><td>-</td></tr>
<tr class="has-page"><td>134</td><td>컴시응</td><td>2</td><td>2</td><td><a href="/docs/ai/exam/134-2-2-ai-al-ai-al">최근 초거대 인공지능(Al: Artificial Intelligence) 도입 및 활용에 필요한 사항을 담은 "공공 부문 초거대 AI 도입•활용 가이드라인"이 발표되었다. 다음 항목에 관하여 설명하시오. 가. 초거대 Al 개념 나. 초거대 AI 도입 원칙 다. 초거대 Al 도입 시 사전 고려사항</a></td><td>-</td><td>-</td></tr>
<tr class="has-page"><td>134</td><td>관리</td><td>3</td><td>4</td><td><a href="/docs/ai/exam/134-3-4-o-notation">알고리즘의 복잡도를 설명하고 성능을 표기하기 위한 O-Notation의 개념과 유형 및 유형별 연산시간의 차이를 설명하시오.</a></td><td>-</td><td>-</td></tr>
<tr class="has-page"><td>134</td><td>관리</td><td>4</td><td>3</td><td><a href="/docs/ai/exam/134-4-3-ai-134-4-3">AI 시스템에 대한 법적 이슈, 윤리적 문제, 기술적 문제에 대하여 설명하고 해결 방안을 제시하시오.</a></td><td>-</td><td>-</td></tr>
<tr class="has-page"><td>134</td><td>컴시응</td><td>4</td><td>6</td><td><a href="/docs/ai/exam/134-4-6-topic-134-4-6">멀티모달 인공지능에 관한 다음 사항을 설명하시오. 가. 개념 나. 구성요소 다. 핵심기술</a></td><td>-</td><td>-</td></tr>
<!-- 133회 -->
<tr class="has-page"><td>133</td><td>관리</td><td>1</td><td>8</td><td><a href="/docs/ai/exam/133-1-8-topic-133-1-8">인공지능 신뢰성의 개념과 핵심 속성에 대하여 설명하시오.</a></td><td>-</td><td>-</td></tr>
<tr class="has-page"><td>133</td><td>관리</td><td>2</td><td>4</td><td><a href="/docs/ai/exam/133-2-4-plm-llm">자연어 언어모델에서의 PLM(Pre-trained Language Model)의 특성을 설명하고, 이 모델이 최종 LLM(Large Language Model)으로 만들어지는 과정에 대하여 훈련 특성을 중심으로 설명하시오.</a></td><td>-</td><td>-</td></tr>
<tr class="has-page"><td>133</td><td>관리</td><td>3</td><td>2</td><td><a href="/docs/ai/exam/133-3-2-ai-ai-ai-ai">국가사이버안보센터는 생성형AI의 보안위협과 안전한 활용을 위한 가이드라인(챗GPT 등 생성형 AI 활용 보안 가이드라인, 2023.6)을 발간하였다. 이와 관련하여 다음을 설명하시오. 가. 생성형AI의 개념 및 활용 서비스 사례 나. 생성형AI의 보안 위협 종류별 주요 원인과 발생 가능한 보안위협 다. 생성형AI 모델/서비스 개발 시 보안 고려사항과 보안위협 대응방안</a></td><td>-</td><td>-</td></tr>
<tr class="has-page"><td>133</td><td>관리</td><td>3</td><td>6</td><td><a href="/docs/ai/exam/133-3-6-topic-133-3-6">인공신경망에 대하여 다음을 설명하시오. 가. 인공신경망의 개념, 구성요소, 역할 나. 피드포워드 뉴럴 네트워크(Feedforward Neural Network) 개념 및 절차 다. 역전파(Backpropagation) 개념 및 절차 라. 활성화 함수의 종류 및 역할</a></td><td>-</td><td>-</td></tr>
<!-- 132회 -->
<tr class="has-page"><td>132</td><td>관리</td><td>1</td><td>3</td><td><a href="/docs/ai/exam/132-1-3-topic-132-1-3">베이지안 최적화(Bayesian Optimization)</a></td><td>-</td><td>-</td></tr>
<tr class="has-page"><td>132</td><td>관리</td><td>1</td><td>10</td><td><a href="/docs/ai/exam/132-1-10-topic-132-1-10">모집단의 특성을 추론하는 점추정과 구간추정 비교</a></td><td>-</td><td>-</td></tr>
<tr class="has-page"><td>132</td><td>관리</td><td>1</td><td>11</td><td><a href="/docs/ai/exam/132-1-11-topic-132-1-11">다중공선성</a></td><td>-</td><td>-</td></tr>
<tr class="has-page"><td>132</td><td>컴시응</td><td>1</td><td>11</td><td><a href="/docs/ai/exam/132-1-11-topic-132-1-11">파인튜닝(Fine-tuning)</a></td><td>-</td><td>-</td></tr>
<tr class="has-page"><td>132</td><td>관리</td><td>2</td><td>1</td><td><a href="/docs/ai/exam/132-2-1-t-z">중심극한정리, t-검정, z-검정을 설명하시오.</a></td><td>-</td><td>-</td></tr>
<tr class="has-page"><td>132</td><td>관리</td><td>2</td><td>6</td><td><a href="/docs/ai/exam/132-2-6-topic-132-2-6">선형 자료 구조인 스택, 큐, 리스트의 자료 입출력 원리를 설명하시오.</a></td><td>-</td><td>-</td></tr>
<tr class="has-page"><td>132</td><td>관리</td><td>3</td><td>3</td><td><a href="/docs/ai/exam/132-3-3-tf-idf">다음과 같이 형태소 분석을 통하여 문서 별로 단어의 점수가 식별되었다. 각 문서의 TF-IDF(Term Frequency-Inverse Document Frequency)를 식별하기 위한 계산과정과 그 결과를 설명하시오. ( 단, Inverse Document Frequency 계산 시 log을 취하여 구하되 Document Emergency 값을 임의로 가공하지 않아야 하며, 주어진 Log값많을 활용한다.)</a></td><td>-</td><td>-</td></tr>
<tr class="has-page"><td>132</td><td>관리</td><td>4</td><td>3</td><td><a href="/docs/ai/exam/132-4-3-langchain-langchain-llm-langchain">설비 예지정비(Predictive Maintenance) 시스템 구축 시 LangChain 프레임위크를 활용할 수 있는 방안에 대하여 다음을 설명하시오 가. 설비 예지정비의 개념 및 필요성 나. LangChain 프레임워크와 LLM(Large Language Model) 다. LangChain을 이용한 설비 예지정비</a></td><td>-</td><td>-</td></tr>
<!-- 131회 -->
<tr class="has-page"><td>131</td><td>컴시응</td><td>1</td><td>1</td><td><a href="/docs/ai/exam/131-1-1-topic-131-1-1">몬테 카를로 방법(Monte Carlo Method)</a></td><td>-</td><td>-</td></tr>
<tr class="has-page"><td>131</td><td>컴시응</td><td>1</td><td>3</td><td><a href="/docs/ai/exam/131-1-3-topic-131-1-3">오토인코더(Autoencoder)</a></td><td>-</td><td>-</td></tr>
<tr class="has-page"><td>131</td><td>컴시응</td><td>1</td><td>4</td><td><a href="/docs/ai/exam/131-1-4-topic-131-1-4">전이학습(Transfer Learning)</a></td><td>-</td><td>-</td></tr>
<tr class="has-page"><td>131</td><td>관리</td><td>1</td><td>5</td><td><a href="/docs/ai/exam/131-1-5-topic-131-1-5">데이터 차원 축소(Data Dimensionality Reduction)</a></td><td>-</td><td>-</td></tr>
<tr class="has-page"><td>131</td><td>관리</td><td>1</td><td>7</td><td><a href="/docs/ai/exam/131-1-7-topic-131-1-7">머신러닝(Machin Learning)과 딥러닝(Deep Learning) 차이</a></td><td>-</td><td>-</td></tr>
<tr class="has-page"><td>131</td><td>관리</td><td>1</td><td>9</td><td><a href="/docs/ai/exam/131-1-9-t-t">독립표본 t-검정(Independent t-test)과 대응표본 t-검정(Paired t-test)</a></td><td>-</td><td>-</td></tr>
<tr class="has-page"><td>131</td><td>컴시응</td><td>1</td><td>9</td><td><a href="/docs/ai/exam/131-1-9-topic-131-1-9">알고리즘의 시간복잡도(Time Complexity), 공간복잡도(Space Complexity)</a></td><td>-</td><td>-</td></tr>
<tr class="has-page"><td>131</td><td>컴시응</td><td>2</td><td>1</td><td><a href="/docs/ai/exam/131-2-1-topic-131-2-1">마르코프 특성(Markov Property)은 미래 상태의 조건부 확률분포가 과거 상태와는 독립적으로 현재 상태에 의해서만 결정된다는 것을 뜻한다. 이와 관련하여 다음을 설명하시오. 가. 마르코프 결정 프로세스(Markov Decision Process)와 전이확률(Transition Probability) 나. 상태가치함수(State Value Function)와 액션가치함수(State-Action Value Function) 다. 벨만기대방정식(Bellman Expectation Equation)과 벨만최적방정식(Bellman Optimality Equation)</a></td><td>-</td><td>-</td></tr>
<tr class="has-page"><td>131</td><td>관리</td><td>3</td><td>1</td><td><a href="/docs/ai/exam/131-3-1-topic-131-3-1">인공지능 학습용 데이터 허브 구축 과정에서 생성된 학습용 데이터 셋의 품질확보를 위한 주요활동과 데이터 생애 주기별 품질관리 수행절차에 대하여 설명하시오.</a></td><td>-</td><td>-</td></tr>
<tr class="has-page"><td>131</td><td>관리</td><td>3</td><td>2</td><td><a href="/docs/ai/exam/131-3-2-topic-131-3-2">데이터 구조(Data Structure)에 대하여 다음을 설명하시오. 가. 선형 구조(Linear Structure)의 개념 및 유형 나. 비선형 구조(Non-Linear Structure)의 개념 및 유형 다. 선형 구조(Linear Structure)와 비선형 구조(Non-Linear Structure) 비교</a></td><td>-</td><td>-</td></tr>
<tr class="has-page"><td>131</td><td>컴시응</td><td>4</td><td>1</td><td><a href="/docs/ai/exam/131-4-1-topic-131-4-1">강화학습(Reinforcement Learning)은 최적의 행동정책을 찾아가는 기계학습 방법이다. 이와 관련하여 다음을 설명하시오. 가. 가치기반 강화학습, 정책기반 강화학습, 엑터 크리틱(Actor-Critic) 강화학습 나. 정책경사(Policy Gradient) 방식 강화학습</a></td><td>-</td><td>-</td></tr>
<tr class="has-page"><td>131</td><td>관리</td><td>4</td><td>4</td><td><a href="/docs/ai/exam/131-4-4-topic-131-4-4">인공지능 분야에서 파운데이션 모델의 개념, 특징, 기반기술 및 구현시 법적, 사회적 측면의 고려사항에 대하여 설명하시오.</a></td><td>-</td><td>-</td></tr>
<tr class="has-page"><td>131</td><td>관리</td><td>4</td><td>6</td><td><a href="/docs/ai/exam/131-4-6-set">정렬 알고리즘은 데이터Set이 주어졌을 때, 이를 사용자가 지정한 기준에 맞게 순서대로 나열하여 재배치하는 기법이다. 정렬 알고리즘과 관련하여 다음에 대하여 설명하시오. 가. 버블 정렬 나. 삽입 정렬 다. 퀵 정렬</a></td><td>-</td><td>-</td></tr>
</tbody>
</table>

---

## 💡 사용 팁

- **검색**: 상단 검색창에 키워드 입력 (예: "RAG", "LLM", "1교시")
- **정렬**: 각 컬럼 헤더 클릭하여 오름차순/내림차순 정렬
- **필터**: 빠른 필터 버튼으로 교시별, 학습페이지 유무 등 필터링

---

## 📊 통계

| 회차 | 문제 수 |
|:----:|:-------:|
| 137회 | 12개 |
| 136회 | 8개 |
| 135회 | 17개 |
| 134회 | 7개 |
| 133회 | 4개 |
| 132회 | 8개 |
| 131회 | 13개 |
| **합계** | **69개** |

---

<!-- jQuery & DataTables JS -->
<script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
<script src="https://cdn.datatables.net/1.13.7/js/jquery.dataTables.min.js"></script>

<script>
$(document).ready(function() {
    var table = $('#examTable').DataTable({
        pageLength: 50,
        lengthMenu: [[25, 50, 100, -1], [25, 50, 100, "전체"]],
        order: [[0, 'desc'], [2, 'asc'], [3, 'asc']],
        language: {
            search: "🔍 검색:",
            lengthMenu: "_MENU_ 개씩 보기",
            info: "총 _TOTAL_개 중 _START_ - _END_",
            infoEmpty: "데이터 없음",
            infoFiltered: "(전체 _MAX_개에서 필터됨)",
            paginate: { first: "처음", last: "마지막", next: "다음", previous: "이전" },
            zeroRecords: "일치하는 결과가 없습니다"
        },
        columnDefs: [
            { orderable: true, targets: [0,1,2,3,5,6] },
            { orderable: false, targets: [4] }
        ],
    });

    $('.filter-btn').click(function() {
        $('.filter-btn').removeClass('active');
        $(this).addClass('active');
        var filter = $(this).data('filter');
        table.search('').columns().search('').draw();

        if (filter === 'all') {
            table.draw();
        } else if (filter === 'has-page') {
            $.fn.dataTable.ext.search.push(function(settings, data, dataIndex) {
                return $(table.row(dataIndex).node()).hasClass('has-page');
            });
            table.draw();
            $.fn.dataTable.ext.search.pop();
        } else if (filter === 'has-mnemonic') {
            table.column(6).search('^(?!-$).*$', true, false).draw();
        } else if (filter === 'essay') {
            table.column(2).search('^[234]$', true, false).draw();
        } else {
            table.column(2).search('^' + filter + '$', true, false).draw();
        }
    });
});
</script>
