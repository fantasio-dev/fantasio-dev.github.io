---
layout: default
title: 📝 기출문제
parent: SW (소프트웨어공학)
has_children: true
has_toc: false
nav_order: 99
permalink: /docs/sw/exam
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

# SW 기출문제
{: .fs-9 }


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
<!-- 138회 -->
<tr><td>138</td><td>관리</td><td>2</td><td>6</td><td><a href="{{ site.baseurl }}/docs/sw/exam/138-2-6-sw-cost-estimation">소프트웨어 사업 대가산정에 대하여 다음을 설명하시오. (단, "소프트웨어 사업 대가산정 가이드 2025년 개정판"을 기준으로 한다.) 가. 소프트웨어 대가산정 가이드 목적 나. 인공지능(AI) 서비스 도입 사업유형과 사업비 산정 절차</a></td><td>대가산정, AI</td><td><code>(목적) 적기절일 산품제투</code> <code>(유형) 단커시</code> <code>(절차) 사서커구AI</code></td></tr>
<!-- 137회 -->
<tr><td>137</td><td>관리</td><td>1</td><td>11</td><td>소프트웨어 역공학과 재공학을 설명하시오.</td><td>역공학, 재공학</td><td>-</td></tr>
<tr><td>137</td><td>관리</td><td>2</td><td>5</td><td><a href="{{ site.baseurl }}/docs/sw/exam/137-2-5-dynamic-testing">소프트웨어 테스트 중 동적 테스트에 대하여 설명하시오. 가. 동적 테스트의 명세 기반 테스트와 구조 기반 테스트 비교 나. 아래의 [프로그램 명세]로 명세 기반 테스트 기법의 동등 분할과 분류 트리 기법의 테스트 케이스 작성</a></td><td>동적 테스트</td><td><code>(명세) 동분경의상유페</code> <code>(구조) 구분조경</code> <code>(절차) 선설생</code></td></tr>
<tr><td>137</td><td>관리</td><td>3</td><td>2</td><td><a href="{{ site.baseurl }}/docs/sw/exam/137-3-2-is-om-audit">정보시스템 감리의 시스템 운영 및 유지보수 감리에 대하여 다음을 설명하시오. 가. 시스템 운영, 유지보수 감리의 개념 나. 시스템 운영 감리의 점검분야 다. 유지보수 감리의 점검분야</a></td><td>감리, 유지보수</td><td><code>(운영감리) 릴테장/신서서</code> <code>(유지보수) 개상인</code></td></tr>
<tr class="has-page"><td>137</td><td>관리</td><td>4</td><td>4</td><td><a href="{{ site.baseurl }}/docs/sw/exam/137-4-4-uml-behavior-diagram">UML(Unified Modeling Language)에서 사용하는 행위 다이어그램(Behavior Diagram)인 활동 다이어그램(Activity Diagram), 상태 다이어그램(State Diagram), 그리고 유스케이스 다이어그램(Use-Case Diagram)에 대하여 각각 설명하시오.</a></td><td>UML, 행위 다이어그램</td><td>(Activity) 시종활선전구 (State) 시종상전 (Use-Case) 액유시-연확포일그</td></tr>
<tr><td>137</td><td>관리</td><td>4</td><td>6</td><td><a href="{{ site.baseurl }}/docs/sw/exam/138-2-6-sw-cost-estimation">소프트웨어 사업 대가산정에 대하여 다음을 설명하시오 (단, "소프트웨어 사업 대가산정 가이드 2025년 개정판"을 기준으로 한다.) 가. 소프트웨어 대가산정 가이드 목적 나. 인공지능(AI) 서비스 도입 사업유형과 사업비 산정 절차</a></td><td>대가산정</td><td><code>(목적) 적기절일 산품제투</code> <code>(유형) 단커시</code> <code>(절차) 사서커구AI</code></td></tr>
<tr><td>137</td><td>컴시응</td><td>1</td><td>6</td><td>SIL(Software-in-the-Loop)과 HIL(Hardware-in-the-Loop) 테스팅</td><td>SIL, HIL</td><td>-</td></tr>
<tr class="has-page"><td>137</td><td>컴시응</td><td>2</td><td>2</td><td><a href="{{ site.baseurl }}/docs/sw/exam/136-2-2-sp-certification">소프트웨어 프로세스(SP, Software Process), 품질인증 제도에 대하여 다음 사항을 설명하시오. 가. 소프트웨어 프로세스 품질인증의 개념 나. 소프트웨어 프로세스 품질인증의 인증 기준 및 인증 등급</a></td><td>SP 품질인증</td><td><code>(체계) 과NIPA기</code> <code>(영역) 프개지조프</code> <code>(등급) 1개2지프3조프</code></td></tr>
<tr><td>137</td><td>컴시응</td><td>2</td><td>5</td><td><a href="{{ site.baseurl }}/docs/sw/exam/132-3-6-sw-impact-assessment">소프트웨어 영향평가에 대하여 다음 사항을 설명하시오. 가. 영향평가 대상 기관 나. 소프트웨어사업 영향평가 체계</a></td><td>영향평가</td><td><code>(대상) 국지공정과정출지</code> <code>(체계) 목기방절</code> <code>(항목) 침필공</code></td></tr>
<tr><td>137</td><td>컴시응</td><td>4</td><td>6</td><td>디지털서비스 전문계약제도에 대하여 주요 특징, 디지털서비스 종류 및 기대효과를 설명하시오.</td><td>디지털서비스 전문계약</td><td>-</td></tr>
<!-- 136회 -->
<tr><td>136</td><td>관리</td><td>1</td><td>5</td><td>프록시 디자인 패턴</td><td>디자인 패턴, Proxy</td><td>-</td></tr>
<tr><td>136</td><td>관리</td><td>1</td><td>6</td><td>DevOps 장점과 단점</td><td>DevOps</td><td>-</td></tr>
<tr class="has-page"><td>136</td><td>관리</td><td>2</td><td>2</td><td><a href="{{ site.baseurl }}/docs/sw/exam/136-2-2-pmo-audit">정보시스템 구축 사업의 성공적인 수행을 위해 정보시스템 감리와 PMO(전자정부사업관리 위탁)를 활용하여 사업관리를 수행하고 있다. 이와 관련하여 다음을 설명하시오. 가. 정보시스템 감리의 법적 근거 나. PMO의 정의와 역할 다. PMO 대상 사업의 범위 라. PMO와 상주감리의 비교</a></td><td>감리, PMO</td><td><code>(법근) 전전전정-감</code> <code>(역할) 요분설구</code> <code>(대상) 대공통행</code> <code>(비교) 개추법책관자투역제산</code></td></tr>
<tr class="has-page"><td>136</td><td>관리</td><td>2</td><td>4</td><td><a href="{{ site.baseurl }}/docs/sw/exam/136-2-4-product-line">소프트웨어 개발방법론 중 하나인 제품계열(Product Line) 방법론에 대하여 다음을 설명하시오. 가. 개념과 특징 나. 활용 기술과 고려사항</a></td><td>제품계열</td><td><code>(특징) 핵품생초</code> <code>(활용기술) 도응관</code> <code>(고려사항) 비기조투</code></td></tr>
<tr><td>136</td><td>관리</td><td>3</td><td>1</td><td>IT 프로젝트 수행 시 PM은 프로젝트 내 외부의 다양한 갈등을 관리하고 해소하여야 한다. PM의 입장에서 다음을 설명하시오. 가. 갈등과 프로젝트 성과의 관계 나. 갈등의 요인과 해결 전략 다. 터크만(Tuckman)의 팀 발달 5단계 모델</td><td>갈등관리, 터크만</td><td>-</td></tr>
<tr><td>136</td><td>컴시응</td><td>2</td><td>2</td><td><a href="{{ site.baseurl }}/docs/sw/exam/136-2-2-sp-certification">소프트웨어 프로세스(SP, Software Process) 품질인증 제도에 대하여 다음 사항을 설명하시오. 가. 소프트웨어 프로세스 품질인증의 개념 나. 소프트웨어 프로세스 품질인증의 인증 기준 및 인증 등급</a></td><td>SP 품질인증</td><td><code>(체계) 과NIPA기</code> <code>(영역) 프개지조프</code> <code>(등급) 1개2지프3조프</code></td></tr>
<tr><td>136</td><td>관리</td><td>3</td><td>3</td><td>소프트웨어 품질보증과 관련하여 다음을 설명하시오. 가. 소프트웨어 품질의 의미 나. 소프트웨어 품질보증의 목적과 기능 다. 인스펙션(Inspection)과 인스펙션 프로세스(Inspection Process)</td><td>품질보증, 인스펙션</td><td>-</td></tr>
<tr><td>136</td><td>관리</td><td>4</td><td>3</td><td>대규모 중요 소프트웨어 사업 평가의 전문성을 높이고 수요기관의 전문성을 보완해 공정한 경쟁을 유도하기 위하여 '조달청 협상에 의한 계약 제안서평가 세부기준'이 2024년 9월 개정 시행되었다. 이와 관련하여 다음을 설명하시오. 가. 계약 제안서평가 세부기준 개정 주요 내용 나. 대형소프트웨어 사업 전문평가제도</td><td>제안서평가, 전문평가제도</td><td>-</td></tr>
<!-- 135회 -->
<tr><td>135</td><td>관리</td><td>1</td><td>3</td><td>요구사항 추적표(Requirement Traceability Matrix)</td><td>요구사항 추적표</td><td>-</td></tr>
<tr><td>135</td><td>관리</td><td>1</td><td>9</td><td>소프트웨어 기술 부채의 유형과 관리 방법</td><td>기술 부채</td><td>-</td></tr>
<tr><td>135</td><td>관리</td><td>2</td><td>2</td><td>CI/CD(Continuous Integration/Continuous Delivery or Continuous Deployment) 파이프라인에서 DevSecOps 적용방안에 대하여 설명하시오.</td><td>CI/CD, DevSecOps</td><td>-</td></tr>
<tr><td>135</td><td>관리</td><td>3</td><td>1</td><td>프로젝트 관리에 대하여 다음을 설명하시오. 가. IT 프로젝트 관리의 개념 나. IT 프로젝트 관리 프로그램 다. IT 프로젝트 관리, 프로그램 관리, 포트폴리오 관리의 비교</td><td>프로젝트 관리</td><td>-</td></tr>
<tr><td>135</td><td>컴시응</td><td>1</td><td>5</td><td>모놀리식 아키텍처(Monolithic Architecture)와 마이크로서비스 아키텍처(MicroService Architecture)를 비교 설명하시오.</td><td>MSA, 모놀리식</td><td>-</td></tr>
<tr><td>135</td><td>컴시응</td><td>1</td><td>8</td><td>정보시스템 하드웨어 규모산정 지침 (TTAK.KO-10.0292/R3)에 따른 하드웨어 규모산정 방법 3가지</td><td>규모산정</td><td>-</td></tr>
<tr><td>135</td><td>컴시응</td><td>4</td><td>4</td><td>소프트웨어 무중단 배포(Zero Downtime Deployment) 방식에 대하여 설명하시오.</td><td>무중단 배포</td><td>-</td></tr>
<!-- 134회 -->
<tr><td>134</td><td>관리</td><td>1</td><td>1</td><td>프로젝트관리 터크만 사다리 모델(Tuckman Ladder Model)의 팀 발달 단계별 특징</td><td>터크만, PM</td><td>-</td></tr>
<tr><td>134</td><td>관리</td><td>1</td><td>4</td><td>형상관리의 개념과 형상관리 기준선(Baseline)</td><td>형상관리</td><td>-</td></tr>
<tr><td>134</td><td>관리</td><td>1</td><td>5</td><td>객체 간의 데이터 보호를 위한 정보은닉(Information Hiding)</td><td>정보은닉, OOP</td><td>-</td></tr>
<tr><td>134</td><td>관리</td><td>3</td><td>1</td><td>실행 중인 애플리케이션에 대한 배포 전략 및 테스트 전략에 대하여 설명하시오.</td><td>배포 전략, 테스트</td><td>-</td></tr>
<tr><td>134</td><td>관리</td><td>3</td><td>2</td><td>소프트웨어 테스트에 대하여 설명하시오. 가. 소프트웨어 테스트 원리 나. 블랙박스 테스트와 화이트박스 테스트 다. 명세기반, 구조기반, 경험기반 테스트 기법</td><td>테스트</td><td>-</td></tr>
<tr><td>134</td><td>관리</td><td>4</td><td>1</td><td>IT 프로젝트 관리에서 리스크 대응에 대하여 설명하시오. 가. 리스크 대응 계획 수립 절차 나. 위협에 대한 대응 전략 다. 기회에 대한 대응 전략</td><td>리스크 관리</td><td>-</td></tr>
<tr><td>134</td><td>관리</td><td>4</td><td>5</td><td>클라우드 전환 사업의 단계별 감리 방법과 검토 항목에 대하여 설명하시오.</td><td>클라우드 감리</td><td>-</td></tr>
<tr><td>134</td><td>컴시응</td><td>1</td><td>9</td><td>플랫폼 엔지니어링(Platform Engineering)</td><td>플랫폼 엔지니어링</td><td>-</td></tr>
<tr><td>134</td><td>컴시응</td><td>1</td><td>11</td><td>애자일(Agile) 소프트웨어 개발의 장점 및 단점</td><td>애자일</td><td>-</td></tr>
<tr><td>134</td><td>컴시응</td><td>1</td><td>13</td><td>소프트웨어 품질성능 평가시험</td><td>품질성능 평가</td><td>-</td></tr>
<tr><td>134</td><td>컴시응</td><td>3</td><td>2</td><td>빅데이터 관련 정보화 사업에 대한 감리 수행 점검항목을 제시하는 "지능정보기술 감리 실무 가이드"에 대해서 다음을 설명하시오. 가. 빅데이터 분석단계 점검항목 나. 클라우드 계획수립 점검항목</td><td>지능정보기술 감리</td><td>-</td></tr>
<tr><td>134</td><td>컴시응</td><td>4</td><td>1</td><td>소프트웨어 프로세스 품질인증 제도의 운영과 활성화를 위하여 "소프트웨어 프로세스(SP: Software Process) 품질인증 운영에 관한 지침"을 시행하고 있다. 다음에 대해서 설명하시오. 가. 소프트웨어 프로세스 품질인증 기준 나. 소프트웨어 프로세스 인증등급 기준</td><td>SP 품질인증</td><td>-</td></tr>
<tr><td>134</td><td>컴시응</td><td>4</td><td>2</td><td>자동차에 대한 기능안전 규격인 ISO 26262에 대하여 다음을 설명하시오. 가. ISO 26262 구성요소 나. 자동차 안전 무결성 수준(ASIL: Automotive Safety Integrity Level)</td><td>ISO 26262, ASIL</td><td>-</td></tr>
<!-- 133회 -->
<tr><td>133</td><td>관리</td><td>1</td><td>2</td><td>소프트웨어 테스트 유형 중 뮤테이션 테스트(Mutation Test)에 대하여 설명하시오.</td><td>뮤테이션 테스트</td><td>-</td></tr>
<tr><td>133</td><td>관리</td><td>1</td><td>11</td><td>소프트웨어 유지보수 향상 및 비용절감을 위한 3R을 설명하시오.</td><td>3R, 유지보수</td><td>-</td></tr>
<tr><td>133</td><td>관리</td><td>2</td><td>1</td><td>정보시스템 하드웨어 규모산정 지침(TTAK.KO-10.0292/R3, 2023.12.06. 개정)에 대하여 다음을 설명하시오. 가. 규모산정의 개념 및 대상 나. 규모산정 절차 다. 규모산정 방식</td><td>규모산정</td><td>-</td></tr>
<tr><td>133</td><td>관리</td><td>3</td><td>5</td><td>소프트웨어 요구공학(Requirement Engineering)에 대하여 설명하시오. 가. 요구공학 정의 및 필요성 나. 요구공학 절차 다. 요구사항 명세서</td><td>요구공학</td><td>-</td></tr>
<tr><td>133</td><td>관리</td><td>4</td><td>2</td><td>정보시스템 개발과 운영 단계에서 수행되는 소프트웨어 테스트의 종류를 쓰고, 이 중 신뢰성 테스트와 이식성 테스트의 세부 활동에 대하여 각각 설명하시오.</td><td>테스트, 신뢰성, 이식성</td><td>-</td></tr>
<!-- 132회 -->
<tr><td>132</td><td>관리</td><td>1</td><td>1</td><td>ISO 31000</td><td>ISO 31000, 리스크</td><td>-</td></tr>
<tr><td>132</td><td>관리</td><td>1</td><td>9</td><td>좋은 소프트웨어가 갖추어야 할 4가지 특징</td><td>소프트웨어 품질</td><td>-</td></tr>
<tr><td>132</td><td>관리</td><td>2</td><td>3</td><td>현재, 소프트웨어 기술자 구분은 과거 기술자 등급제에서 IT역량분류체계를 기반으로 한 직무제(이하 IT직무제)로 변경되어 운영되고 있으나 실무 현장에서는 여전히 폐지된 등급제가 다수 활용되고 있는 실정이다. 소프트웨어 기술자 구분에 대하여 다음을 설명하시오. 가. 소프트웨어 기술자 등급제와 IT직무제의 개념과 특징 나. 현행 IT직무제의 문제점과 개선방향</td><td>IT직무제, 등급제</td><td>-</td></tr>
<tr><td>132</td><td>관리</td><td>3</td><td>1</td><td>소프트웨어(이하 SW) 운영단계 대가산정에 대하여 다음을 설명하시오. (단, "소프트웨어 사업 대가 산정 가이드 2023년 개정판" 기준) 가. 응용SW 요율제 유지관리비 산정방식과 SW운영 투입공수 산정방식 나. 고정비/변동비 산정방식</td><td>대가산정</td><td>-</td></tr>
<tr><td>132</td><td>관리</td><td>3</td><td>6</td><td>정보시스템의 성능 요구사항 작성 시 고려해야 하는 주요 성능지표 및 내용에 대해 설명하시오.</td><td>성능 요구사항</td><td>-</td></tr>
<tr><td>132</td><td>관리</td><td>4</td><td>4</td><td>소프트웨어 진흥법(시행 2023.10.19.)은 소프트웨어 산업의 발전을 위해 시행되어야 할 다양한 활동의 법적 근거를 마련하고 있다. 이와 관련하여 다음을 설명하시오. 가. 제5조(기본계획의 수립 등)의 2항에 따른 기본계획 내 포함되어야 할 사항 나. 제30조(소프트웨어안전 확보)의 2항에 따른 소프트웨어안전 확보를 위한 지침 내 포함되어야 할 사항</td><td>소프트웨어 진흥법</td><td>-</td></tr>
<tr><td>132</td><td>관리</td><td>4</td><td>5</td><td>소프트웨어 개발에 필요한 규모 산정 방식 종류와 특징을 비교 설명하고, 공공 소프트웨어 사업 규모 산정 방식의 현실적 개선 방안에 대하여 설명하시오.</td><td>규모산정</td><td>-</td></tr>
<tr><td>132</td><td>컴시응</td><td>1</td><td>3</td><td>Canary Test</td><td>Canary 배포</td><td>-</td></tr>
<tr><td>132</td><td>컴시응</td><td>1</td><td>6</td><td>"소프트웨어 기술성 평가기준 지침"(과학기술정보통신부고시, 제2021-98호)에 명시된 기술제안서 평가항목</td><td>기술성 평가</td><td>-</td></tr>
<tr><td>132</td><td>컴시응</td><td>1</td><td>7</td><td>전자정부사업관리 위탁(PMO, Project Management Office)</td><td>PMO</td><td>-</td></tr>
<tr><td>132</td><td>컴시응</td><td>2</td><td>4</td><td>이동형 로봇의 대인 충돌 안전성 평가 방법(정보통신단체표준, TTAK.KO-10.1223)에 대하여 아래 사항을 설명하시오. 가. 충돌 시험에서의 충격 속도 추정방법 나. 충돌 시험용 인체모형(더미, dummy) 다. 인체모형 측정 데이터</td><td>로봇 안전성</td><td>-</td></tr>
<tr><td>132</td><td>컴시응</td><td>2</td><td>5</td><td>정보시스템 마스터플랜(ISMP, Information System Master Plan)에 대하여 아래 설명하시오. 가. ISMP와 EA(Enterprise Architecture), ISP(Information System Planning)에 대해 각각 설명하고 상호 비교 나. 투입공수에 의한 사업대가 산정방식을 적용한 ISMP수립비 산정 절차, 주요내용, 산출물</td><td>ISMP, EA, ISP</td><td>-</td></tr>
<tr><td>132</td><td>컴시응</td><td>3</td><td>5</td><td>객체 지향 프로그래밍 기법을 활용한 소프트웨어 설계 시 고려해야 할 원칙(일명 SOLID 원칙) 5가지를 제시하고 설명하시오.</td><td>SOLID, OOP</td><td>-</td></tr>
<tr><td>132</td><td>컴시응</td><td>3</td><td>6</td><td><a href="{{ site.baseurl }}/docs/sw/exam/132-3-6-sw-impact-assessment">정보통신산업진흥원에서 제시한 소프트웨어사업 영향평가에 대하여 아래 사항을 설명하시오. 가. 영향평가 대상기관 나. 소프트웨어사업 영향평가 체계 다. 평가항목</a></td><td>영향평가</td><td><code>(대상) 국지공정과정출지</code> <code>(체계) 목기방절</code> <code>(항목) 침필공</code></td></tr>
<tr><td>132</td><td>컴시응</td><td>4</td><td>2</td><td>한국지능정보사회진흥원에서 제시한 클라우드 서비스 활용사업 감리 점검에 대하여 아래 사항을 설명하시오. 가. 공공부문의 클라우드 사업 유형 나. 클라우드 서비스 활용사업의 점검 단계, 활동, 검토항목</td><td>클라우드 감리</td><td>-</td></tr>
<!-- 131회 -->
<tr><td>131</td><td>관리</td><td>1</td><td>3</td><td>폭포수 개발 방법론과 애자일 개발 방법론의 특징 및 장단점 비교</td><td>폭포수, 애자일</td><td>-</td></tr>
<tr><td>131</td><td>관리</td><td>1</td><td>6</td><td>정보시스템 감리와 PMO(Project Management Office) 비교</td><td>감리, PMO</td><td>-</td></tr>
<tr><td>131</td><td>관리</td><td>1</td><td>12</td><td>객체지향 방법론에서 캡슐화(Encapsulation)와 정보은닉(Information Hiding)</td><td>캡슐화, 정보은닉</td><td>-</td></tr>
<tr><td>131</td><td>관리</td><td>2</td><td>6</td><td>아키텍처 스타일과 디자인 패턴에 대하여 다음을 설명하시오.</td><td>아키텍처, 디자인 패턴</td><td>-</td></tr>
<tr><td>131</td><td>관리</td><td>3</td><td>3</td><td>통합테스트(Integration Test)에 대하여 다음을 설명하시오. 가. 비점진적 통합 방식과 점진적 통합 방식 나. 하향식(Top Down) 통합 테스트와 상향식(Bottom Up) 통합 테스트 다. 테스트 드라이버(Test Driver)와 테스트 스텁(Test Stub)</td><td>통합테스트</td><td>-</td></tr>
<tr><td>131</td><td>관리</td><td>3</td><td>4</td><td>소프트웨어 안전성 분석의 필요성과 다음의 분석 기법을 설명하시오. 가. FTA(Fault Tree Analysis) 나. FMEA(Failure Mode and Effects Analysis) 다. HAZOP(Hazard and Operability Analysis)</td><td>FTA, FMEA, HAZOP</td><td>-</td></tr>
<tr><td>131</td><td>관리</td><td>4</td><td>5</td><td>소프트웨어 규모산정에 대하여 다음을 설명하시오. 가. 필요성과 산정방법 나. 규모산정 방식의 종류별 특징</td><td>규모산정</td><td>-</td></tr>
<tr><td>131</td><td>컴시응</td><td>1</td><td>5</td><td>ATAM(Architecture Tradeoff Analysis Method)과 CBAM(Cost Benefit Analysis Method)</td><td>ATAM, CBAM</td><td>-</td></tr>
<tr><td>131</td><td>컴시응</td><td>2</td><td>3</td><td>현행 데이터베이스 데이터량을 기준으로 TO-BE 데이터량을 예측하고자 한다. 이와 관련하여 다음을 설명하시오. 가. 데이터베이스 용량산정 방법 별 개념 및 장,단점 나. 데이터베이스 용량산정 기준</td><td>DB 용량산정</td><td>-</td></tr>
<tr><td>131</td><td>컴시응</td><td>3</td><td>6</td><td>데이터옵스(DataOps)의 주요 기술을 설명하고, 데브옵스(DevOps)와의 차이점을 설명하시오.</td><td>DataOps, DevOps</td><td>-</td></tr>
</tbody>
</table>

---

## 💡 사용 팁

- **검색**: 상단 검색창에 키워드 입력 (예: "테스트", "감리", "1교시")
- **정렬**: 각 컬럼 헤더 클릭하여 오름차순/내림차순 정렬
- **필터**: 빠른 필터 버튼으로 교시별, 학습페이지 유무 등 필터링

---

## 📊 통계

| 회차 | 문제 수 |
|:----:|:-------:|
| 138회 | 1개 |
| 137회 | 9개 |
| 136회 | 8개 |
| 135회 | 7개 |
| 134회 | 13개 |
| 133회 | 5개 |
| 132회 | 15개 |
| 131회 | 10개 |
| **합계** | **68개** |

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

