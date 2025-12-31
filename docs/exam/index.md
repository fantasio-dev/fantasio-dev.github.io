---
layout: default
title: 📝 통합 기출문제
nav_order: 97
has_toc: false
permalink: /docs/exam
---

<!-- DataTables CSS -->
<link rel="stylesheet" href="https://cdn.datatables.net/1.13.7/css/jquery.dataTables.min.css">

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

/* 필터 섹션 */
.filter-section {
  background: #fff;
  border-radius: 12px;
  padding: 1.5rem;
  margin-bottom: 1.5rem;
  border: 1px solid #dee2e6;
}
.filter-row {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  align-items: flex-end;
}
.filter-group {
  flex: 1;
  min-width: 150px;
}
.filter-group label {
  display: block;
  font-size: 0.85rem;
  font-weight: 600;
  color: #495057;
  margin-bottom: 0.4rem;
}
.filter-group select,
.filter-group input {
  width: 100%;
  padding: 0.6rem 0.8rem;
  border: 1px solid #dee2e6;
  border-radius: 8px;
  font-size: 0.9rem;
  background: #fff;
}
.filter-group select:focus,
.filter-group input:focus {
  outline: none;
  border-color: #4A90D9;
  box-shadow: 0 0 0 3px rgba(74, 144, 217, 0.15);
}
.filter-buttons-row {
  display: flex;
  gap: 0.5rem;
  margin-top: 1rem;
  justify-content: flex-end;
}
.btn-filter {
  padding: 0.6rem 1.5rem;
  border: none;
  border-radius: 8px;
  font-size: 0.9rem;
  cursor: pointer;
  transition: all 0.2s;
}
.btn-reset {
  background: #fff;
  border: 1px solid #dee2e6;
  color: #495057;
}
.btn-reset:hover {
  background: #e9ecef;
}
.btn-search {
  background: #4A90D9;
  color: #fff;
}
.btn-search:hover {
  background: #3A7BC8;
}

/* 영역 버튼 */
.domain-buttons {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-bottom: 1rem;
}
.domain-btn {
  padding: 0.5rem 1rem;
  border: 2px solid #dee2e6;
  border-radius: 20px;
  background: #fff;
  cursor: pointer;
  font-size: 0.85rem;
  font-weight: 500;
  transition: all 0.2s;
}
.domain-btn:hover {
  border-color: #4A90D9;
  color: #4A90D9;
}
.domain-btn.active {
  background: #4A90D9;
  border-color: #4A90D9;
  color: #fff;
}
.domain-btn[data-domain="all"] { border-color: #6c757d; }
.domain-btn[data-domain="all"].active { background: #6c757d; border-color: #6c757d; }
.domain-btn[data-domain="SW"] { border-color: #28a745; }
.domain-btn[data-domain="SW"].active { background: #28a745; border-color: #28a745; }
.domain-btn[data-domain="AI"] { border-color: #6f42c1; }
.domain-btn[data-domain="AI"].active { background: #6f42c1; border-color: #6f42c1; }
.domain-btn[data-domain="SEC"] { border-color: #dc3545; }
.domain-btn[data-domain="SEC"].active { background: #dc3545; border-color: #dc3545; }
.domain-btn[data-domain="DS"] { border-color: #17a2b8; }
.domain-btn[data-domain="DS"].active { background: #17a2b8; border-color: #17a2b8; }
.domain-btn[data-domain="NW"] { border-color: #fd7e14; }
.domain-btn[data-domain="NW"].active { background: #fd7e14; border-color: #fd7e14; }
.domain-btn[data-domain="DB"] { border-color: #20c997; }
.domain-btn[data-domain="DB"].active { background: #20c997; border-color: #20c997; }
.domain-btn[data-domain="CAOS"] { border-color: #e83e8c; }
.domain-btn[data-domain="CAOS"].active { background: #e83e8c; border-color: #e83e8c; }
.domain-btn[data-domain="BIZ"] { border-color: #ffc107; color: #856404; }
.domain-btn[data-domain="BIZ"].active { background: #ffc107; border-color: #ffc107; color: #856404; }

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
/* 회차, 정/컴, 교시, 번호 컬럼 - 최소폭 */
#examTable td:nth-child(1),
#examTable td:nth-child(2),
#examTable td:nth-child(3),
#examTable td:nth-child(4),
#examTable th:nth-child(1),
#examTable th:nth-child(2),
#examTable th:nth-child(3),
#examTable th:nth-child(4) {
  width: 40px;
  max-width: 50px;
  white-space: nowrap;
  text-align: center;
  padding: 0.3rem 0.4rem;
  font-size: 0.8rem;
}
/* 문제 컬럼 */
#examTable td:nth-child(5) {
  white-space: normal;
  min-width: 300px;
}
/* 암기법 컬럼 */
#examTable td:nth-child(6),
#examTable th:nth-child(6) {
  font-family: 'Consolas', 'Monaco', monospace;
  font-size: 0.8rem;
  color: #d63384;
  min-width: 150px;
  white-space: nowrap;
}

/* 페이지 있는 행 */
tr.has-page td:nth-child(5) a {
  color: #0d6efd;
  font-weight: 500;
}
tr.has-page {
  background-color: #f0f7ff !important;
}

/* 영역 뱃지 (회차 옆에 작게) */
.domain-badge {
  display: inline-block;
  padding: 0.1rem 0.3rem;
  border-radius: 3px;
  font-size: 0.65rem;
  font-weight: 600;
  color: #fff;
  margin-left: 4px;
}
.domain-badge.sw { background: #28a745; }
.domain-badge.ai { background: #6f42c1; }
.domain-badge.sec { background: #dc3545; }
.domain-badge.ds { background: #17a2b8; }
.domain-badge.nw { background: #fd7e14; }
.domain-badge.db { background: #20c997; }
.domain-badge.caos { background: #e83e8c; }
.domain-badge.biz { background: #ffc107; color: #856404; }

/* 문제 컬럼 - 전체 표시 */
.question-cell {
  line-height: 1.6;
}
</style>

# 📝 통합 기출문제

<div class="filter-section">
  <div class="domain-buttons">
    <button class="domain-btn active" data-domain="all">전체</button>
    <button class="domain-btn" data-domain="SW">SW</button>
    <button class="domain-btn" data-domain="AI">AI</button>
    <button class="domain-btn" data-domain="SEC">SEC</button>
    <button class="domain-btn" data-domain="DS">DS</button>
    <button class="domain-btn" data-domain="NW">NW</button>
    <button class="domain-btn" data-domain="DB">DB</button>
    <button class="domain-btn" data-domain="CAOS">CAOS</button>
    <button class="domain-btn" data-domain="BIZ">BIZ</button>
  </div>
  
  <div class="filter-row">
    <div class="filter-group">
      <label>교시</label>
      <select id="filterClass">
        <option value="">전체</option>
        <option value="1">1교시</option>
        <option value="2">2교시</option>
        <option value="3">3교시</option>
        <option value="4">4교시</option>
      </select>
    </div>
    <div class="filter-group">
      <label>회차</label>
      <select id="filterRound">
        <option value="">전체</option>
        <option value="137">137회</option>
        <option value="136">136회</option>
        <option value="135">135회</option>
        <option value="134">134회</option>
        <option value="133">133회</option>
        <option value="132">132회</option>
        <option value="131">131회</option>
        <option value="130">130회</option>
      </select>
    </div>
    <div class="filter-group" style="flex: 2;">
      <label>검색어</label>
      <input type="text" id="filterKeyword" placeholder="예: 클라우드, DevOps, 보안">
    </div>
  </div>
  
  <div class="filter-buttons-row">
    <button class="btn-filter btn-reset" onclick="resetFilters()">리셋</button>
    <button class="btn-filter btn-search" onclick="applyFilters()">검색</button>
  </div>
</div>

<table id="examTable" class="display compact" style="width:100%">
<thead>
<tr>
<th>회차</th>
<th>정/컴</th>
<th>교시</th>
<th>번호</th>
<th>문제</th>
<th>암기법</th>
</tr>
</thead>
<tbody>
<!-- SW 영역 기출문제 (68개) - 전체 문제 포함 -->
<!-- 138회 -->
<tr data-domain="SW" data-full="소프트웨어 사업 대가산정에 대하여 다음을 설명하시오. (단, '소프트웨어 사업 대가산정 가이드 2025년 개정판'을 기준으로 한다.) 가. 소프트웨어 대가산정 가이드 목적 나. 인공지능(AI) 서비스 도입 사업유형과 사업비 산정 절차"><td>138<span class="domain-badge sw">SW</span></td><td>관리</td><td>2</td><td>6</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/sw/exam/138-2-6-sw-cost-estimation">소프트웨어 사업 대가산정 (2025년 개정판)</a></td><td><code>(목적) 적기절일 산품제투</code> <code>(유형) 단커시</code></td></tr>
<!-- 137회 -->
<tr class="has-page" data-domain="SW" data-full="소프트웨어 역공학과 재공학을 설명하시오."><td>137<span class="domain-badge sw">SW</span></td><td>관리</td><td>1</td><td>11</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/sw/exam/137-1-11-reverse-reengineering">소프트웨어 역공학과 재공학</a></td><td><code>(역공학) 추분문</code> <code>(재공학) 역재구</code></td></tr>
<tr data-domain="SW" data-full="소프트웨어 테스트 중 동적 테스트에 대하여 설명하시오. 가. 동적 테스트의 명세 기반 테스트와 구조 기반 테스트 비교 나. 아래의 [프로그램 명세]로 명세 기반 테스트 기법의 동등 분할과 분류 트리 기법의 테스트 케이스 작성"><td>137<span class="domain-badge sw">SW</span></td><td>관리</td><td>2</td><td>5</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/sw/exam/137-2-5-dynamic-testing">동적 테스트 (명세기반/구조기반)</a></td><td><code>(명세) 동분경의상유페</code> <code>(구조) 구분조경</code></td></tr>
<tr class="has-page" data-domain="SW" data-full="정보시스템 감리의 시스템 운영 및 유지보수 감리에 대하여 다음을 설명하시오. 가. 시스템 운영, 유지보수 감리의 개념 나. 시스템 운영 감리의 점검분야 다. 유지보수 감리의 점검분야"><td>137<span class="domain-badge sw">SW</span></td><td>관리</td><td>3</td><td>2</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/sw/exam/137-3-2-is-om-audit">정보시스템 운영 및 유지보수 감리</a></td><td><code>(운영) 릴테장/신서서</code> <code>(유지보수) 개상인</code></td></tr>
<tr class="has-page" data-domain="SW" data-full="UML(Unified Modeling Language)에서 사용하는 행위 다이어그램(Behavior Diagram)인 활동 다이어그램(Activity Diagram), 상태 다이어그램(State Diagram), 그리고 유스케이스 다이어그램(Use-Case Diagram)에 대하여 각각 설명하시오."><td>137<span class="domain-badge sw">SW</span></td><td>관리</td><td>4</td><td>4</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/sw/exam/137-4-4-uml-behavior-diagram">UML 행위 다이어그램</a></td><td>(Activity) 시종활선전구 (State) 시종상전</td></tr>
<tr data-domain="SW" data-full="소프트웨어 사업 대가산정에 대하여 다음을 설명하시오 (단, '소프트웨어 사업 대가산정 가이드 2025년 개정판'을 기준으로 한다.) 가. 소프트웨어 대가산정 가이드 목적 나. 인공지능(AI) 서비스 도입 사업유형과 사업비 산정 절차"><td>137<span class="domain-badge sw">SW</span></td><td>관리</td><td>4</td><td>6</td><td class="question-cell">소프트웨어 사업 대가산정 (2025년 개정판)</td><td><code>(목적) 적기절일 산품제투</code> <code>(유형) 단커시</code></td></tr>
<tr data-domain="SW" data-full="SIL(Software-in-the-Loop)과 HIL(Hardware-in-the-Loop) 테스팅"><td>137<span class="domain-badge sw">SW</span></td><td>컴시응</td><td>1</td><td>6</td><td class="question-cell">SIL(Software-in-the-Loop)과 HIL(Hardware-in-the-Loop) 테스팅</td><td>-</td></tr>
<tr class="has-page" data-domain="SW" data-full="소프트웨어 프로세스(SP, Software Process), 품질인증 제도에 대하여 다음 사항을 설명하시오. 가. 소프트웨어 프로세스 품질인증의 개념 나. 소프트웨어 프로세스 품질인증의 인증 기준 및 인증 등급"><td>137<span class="domain-badge sw">SW</span></td><td>컴시응</td><td>2</td><td>2</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/sw/exam/136-2-2-sp-certification">소프트웨어 프로세스(SP) 품질인증 제도</a></td><td><code>(체계) 과NIPA기</code> <code>(영역) 프개지조프</code></td></tr>
<tr data-domain="SW" data-full="소프트웨어 영향평가에 대하여 다음 사항을 설명하시오. 가. 영향평가 대상 기관 나. 소프트웨어사업 영향평가 체계"><td>137<span class="domain-badge sw">SW</span></td><td>컴시응</td><td>2</td><td>5</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/sw/exam/132-3-6-sw-impact-assessment">소프트웨어 영향평가</a></td><td><code>(대상) 국지공정과정출지</code> <code>(체계) 목기방절</code></td></tr>
<tr class="has-page" data-domain="SW" data-full="디지털서비스 전문계약제도에 대하여 주요 특징, 디지털서비스 종류 및 기대효과를 설명하시오."><td>137<span class="domain-badge sw">SW</span></td><td>컴시응</td><td>4</td><td>6</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/ds/exam/136-2-6-digital-service-contract">디지털서비스 전문계약제도</a></td><td><code>(특징) 간약사공표</code> <code>(종류) 클지융-I-S-P</code></td></tr>
<!-- 136회 -->
<tr data-domain="SW" data-full="프록시 디자인 패턴"><td>136<span class="domain-badge sw">SW</span></td><td>관리</td><td>1</td><td>5</td><td class="question-cell">프록시 디자인 패턴</td><td>-</td></tr>
<tr data-domain="SW" data-full="DevOps 장점과 단점"><td>136<span class="domain-badge sw">SW</span></td><td>관리</td><td>1</td><td>6</td><td class="question-cell">DevOps 장점과 단점</td><td>-</td></tr>
<tr class="has-page" data-domain="SW" data-full="정보시스템 구축 사업의 성공적인 수행을 위해 정보시스템 감리와 PMO(전자정부사업관리 위탁)를 활용하여 사업관리를 수행하고 있다. 이와 관련하여 다음을 설명하시오. 가. 정보시스템 감리의 법적 근거 나. PMO의 정의와 역할 다. PMO 대상 사업의 범위 라. PMO와 상주감리의 비교"><td>136<span class="domain-badge sw">SW</span></td><td>관리</td><td>2</td><td>2</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/sw/exam/136-2-2-pmo-audit">정보시스템 감리와 PMO</a></td><td><code>(법근) 전전전정-감</code> <code>(역할) 요분설구</code></td></tr>
<tr class="has-page" data-domain="SW" data-full="소프트웨어 개발방법론 중 하나인 제품계열(Product Line) 방법론에 대하여 다음을 설명하시오. 가. 개념과 특징 나. 활용 기술과 고려사항"><td>136<span class="domain-badge sw">SW</span></td><td>관리</td><td>2</td><td>4</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/sw/exam/136-2-4-product-line">제품계열(Product Line) 방법론</a></td><td><code>(특징) 핵품생초</code> <code>(기술) 도응관</code></td></tr>
<tr class="has-page" data-domain="SW" data-full="IT 프로젝트 수행 시 PM은 프로젝트 내 외부의 다양한 갈등을 관리하고 해소하여야 한다. PM의 입장에서 다음을 설명하시오. 가. 갈등과 프로젝트 성과의 관계 나. 갈등의 요인과 해결 전략 다. 터크만(Tuckman)의 팀 발달 5단계 모델"><td>136<span class="domain-badge sw">SW</span></td><td>관리</td><td>3</td><td>1</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/sw/exam/136-3-1-conflict-tuckman">갈등관리와 터크만 팀 발달 모델</a></td><td><code>(관계) 부적극</code> <code>(요인) 구인업환</code></td></tr>
<tr class="has-page" data-domain="SW" data-full="소프트웨어 품질보증과 관련하여 다음을 설명하시오. 가. 소프트웨어 품질의 의미 나. 소프트웨어 품질보증의 목적과 기능 다. 인스펙션(Inspection)과 인스펙션 프로세스(Inspection Process)"><td>136<span class="domain-badge sw">SW</span></td><td>관리</td><td>3</td><td>3</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/sw/exam/136-3-3-software-quality-assurance">소프트웨어 품질보증과 인스펙션</a></td><td><code>(품질특성) 기신사성유보호안</code></td></tr>
<tr class="has-page" data-domain="SW" data-full="대규모 중요 소프트웨어 사업 평가의 전문성을 높이고 수요기관의 전문성을 보완해 공정한 경쟁을 유도하기 위하여 '조달청 협상에 의한 계약 제안서평가 세부기준'이 2024년 9월 개정 시행되었다. 이와 관련하여 다음을 설명하시오. 가. 계약 제안서평가 세부기준 개정 주요 내용 나. 대형소프트웨어 사업 전문평가제도"><td>136<span class="domain-badge sw">SW</span></td><td>관리</td><td>4</td><td>3</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/sw/exam/136-4-3-sw-expert-evaluation">대형SW사업 전문평가제도</a></td><td><code>(개정) 전공중기</code> <code>(영역) 정정데디</code></td></tr>
<!-- 135회 -->
<tr data-domain="SW" data-full="요구사항 추적표(Requirement Traceability Matrix)"><td>135<span class="domain-badge sw">SW</span></td><td>관리</td><td>1</td><td>3</td><td class="question-cell">요구사항 추적표(Requirement Traceability Matrix)</td><td>-</td></tr>
<tr data-domain="SW" data-full="소프트웨어 기술 부채의 유형과 관리 방법"><td>135<span class="domain-badge sw">SW</span></td><td>관리</td><td>1</td><td>9</td><td class="question-cell">소프트웨어 기술 부채의 유형과 관리 방법</td><td>-</td></tr>
<tr class="has-page" data-domain="SW" data-full="CI/CD(Continuous Integration/Continuous Delivery or Continuous Deployment) 파이프라인에서 DevSecOps 적용방안에 대하여 설명하시오."><td>135<span class="domain-badge sw">SW</span></td><td>관리</td><td>2</td><td>2</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/sw/exam/135-2-2-cicd-devsecops">CI/CD 파이프라인에서 DevSecOps 적용방안</a></td><td><code>(구성) 버CI빌테코배모</code> <code>(적용) 초자컨배피문</code></td></tr>
<tr class="has-page" data-domain="SW" data-full="프로젝트 관리에 대하여 다음을 설명하시오. 가. IT 프로젝트 관리의 개념 나. IT 프로젝트 관리 프로그램 다. IT 프로젝트 관리, 프로그램 관리, 포트폴리오 관리의 비교"><td>135<span class="domain-badge sw">SW</span></td><td>관리</td><td>3</td><td>1</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/sw/exam/135-3-1-project-management">프로젝트 관리</a></td><td><code>(프로세스) 착계실감종</code> <code>(지식영역) 통이범자시원리품조의</code></td></tr>
<tr data-domain="SW" data-full="모놀리식 아키텍처(Monolithic Architecture)와 마이크로서비스 아키텍처(MicroService Architecture)를 비교 설명하시오."><td>135<span class="domain-badge sw">SW</span></td><td>컴시응</td><td>1</td><td>5</td><td class="question-cell">모놀리식 아키텍처 vs 마이크로서비스 아키텍처</td><td>-</td></tr>
<tr data-domain="SW" data-full="정보시스템 하드웨어 규모산정 지침 (TTAK.KO-10.0292/R3)에 따른 하드웨어 규모산정 방법 3가지"><td>135<span class="domain-badge sw">SW</span></td><td>컴시응</td><td>1</td><td>8</td><td class="question-cell">정보시스템 하드웨어 규모산정 지침에 따른 규모산정 방법 3가지</td><td>-</td></tr>
<tr class="has-page" data-domain="SW" data-full="소프트웨어 무중단 배포(Zero Downtime Deployment) 방식에 대하여 설명하시오."><td>135<span class="domain-badge sw">SW</span></td><td>컴시응</td><td>4</td><td>4</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/sw/exam/135-4-4-zero-downtime-deployment">무중단 배포(Zero Downtime Deployment)</a></td><td><code>(문제점) 다유롤</code> <code>(종류) 롤블카</code></td></tr>
<!-- 134회 -->
<tr data-domain="SW" data-full="프로젝트관리 터크만 사다리 모델(Tuckman Ladder Model)의 팀 발달 단계별 특징"><td>134<span class="domain-badge sw">SW</span></td><td>관리</td><td>1</td><td>1</td><td class="question-cell">터크만 사다리 모델(Tuckman Ladder Model)의 팀 발달 단계별 특징</td><td>-</td></tr>
<tr data-domain="SW" data-full="형상관리의 개념과 형상관리 기준선(Baseline)"><td>134<span class="domain-badge sw">SW</span></td><td>관리</td><td>1</td><td>4</td><td class="question-cell">형상관리의 개념과 형상관리 기준선(Baseline)</td><td>-</td></tr>
<tr data-domain="SW" data-full="객체 간의 데이터 보호를 위한 정보은닉(Information Hiding)"><td>134<span class="domain-badge sw">SW</span></td><td>관리</td><td>1</td><td>5</td><td class="question-cell">객체 간의 데이터 보호를 위한 정보은닉(Information Hiding)</td><td>-</td></tr>
<tr data-domain="SW" data-full="실행 중인 애플리케이션에 대한 배포 전략 및 테스트 전략에 대하여 설명하시오."><td>134<span class="domain-badge sw">SW</span></td><td>관리</td><td>3</td><td>1</td><td class="question-cell">실행 중인 애플리케이션에 대한 배포 전략 및 테스트 전략</td><td>-</td></tr>
<tr data-domain="SW" data-full="소프트웨어 테스트에 대하여 설명하시오. 가. 소프트웨어 테스트 원리 나. 블랙박스 테스트와 화이트박스 테스트 다. 명세기반, 구조기반, 경험기반 테스트 기법"><td>134<span class="domain-badge sw">SW</span></td><td>관리</td><td>3</td><td>2</td><td class="question-cell">소프트웨어 테스트 원리/블랙박스/화이트박스/명세기반/구조기반/경험기반</td><td>-</td></tr>
<tr data-domain="SW" data-full="IT 프로젝트 관리에서 리스크 대응에 대하여 설명하시오. 가. 리스크 대응 계획 수립 절차 나. 위협에 대한 대응 전략 다. 기회에 대한 대응 전략"><td>134<span class="domain-badge sw">SW</span></td><td>관리</td><td>4</td><td>1</td><td class="question-cell">IT 프로젝트 관리에서 리스크 대응 계획 수립</td><td>-</td></tr>
<tr data-domain="SW" data-full="클라우드 전환 사업의 단계별 감리 방법과 검토 항목에 대하여 설명하시오."><td>134<span class="domain-badge sw">SW</span></td><td>관리</td><td>4</td><td>5</td><td class="question-cell">클라우드 전환 사업의 단계별 감리 방법과 검토 항목</td><td>-</td></tr>
<tr data-domain="SW" data-full="플랫폼 엔지니어링(Platform Engineering)"><td>134<span class="domain-badge sw">SW</span></td><td>컴시응</td><td>1</td><td>9</td><td class="question-cell">플랫폼 엔지니어링(Platform Engineering)</td><td>-</td></tr>
<tr data-domain="SW" data-full="애자일(Agile) 소프트웨어 개발의 장점 및 단점"><td>134<span class="domain-badge sw">SW</span></td><td>컴시응</td><td>1</td><td>11</td><td class="question-cell">애자일(Agile) 소프트웨어 개발의 장점 및 단점</td><td>-</td></tr>
<tr data-domain="SW" data-full="소프트웨어 품질성능 평가시험"><td>134<span class="domain-badge sw">SW</span></td><td>컴시응</td><td>1</td><td>13</td><td class="question-cell">소프트웨어 품질성능 평가시험</td><td>-</td></tr>
<tr data-domain="SW" data-full="빅데이터 관련 정보화 사업에 대한 감리 수행 점검항목을 제시하는 '지능정보기술 감리 실무 가이드'에 대해서 다음을 설명하시오. 가. 빅데이터 분석단계 점검항목 나. 클라우드 계획수립 점검항목"><td>134<span class="domain-badge sw">SW</span></td><td>컴시응</td><td>3</td><td>2</td><td class="question-cell">지능정보기술 감리 실무 가이드 (빅데이터/클라우드)</td><td>-</td></tr>
<tr data-domain="SW" data-full="소프트웨어 프로세스 품질인증 제도의 운영과 활성화를 위하여 '소프트웨어 프로세스(SP: Software Process) 품질인증 운영에 관한 지침'을 시행하고 있다. 다음에 대해서 설명하시오. 가. 소프트웨어 프로세스 품질인증 기준 나. 소프트웨어 프로세스 인증등급 기준"><td>134<span class="domain-badge sw">SW</span></td><td>컴시응</td><td>4</td><td>1</td><td class="question-cell">소프트웨어 프로세스(SP) 품질인증 운영 지침</td><td>-</td></tr>
<tr data-domain="SW" data-full="자동차에 대한 기능안전 규격인 ISO 26262에 대하여 다음을 설명하시오. 가. ISO 26262 구성요소 나. 자동차 안전 무결성 수준(ASIL: Automotive Safety Integrity Level)"><td>134<span class="domain-badge sw">SW</span></td><td>컴시응</td><td>4</td><td>2</td><td class="question-cell">ISO 26262와 ASIL(자동차 안전 무결성 수준)</td><td>-</td></tr>
<!-- 133회 -->
<tr data-domain="SW" data-full="소프트웨어 테스트 유형 중 뮤테이션 테스트(Mutation Test)에 대하여 설명하시오."><td>133<span class="domain-badge sw">SW</span></td><td>관리</td><td>1</td><td>2</td><td class="question-cell">뮤테이션 테스트(Mutation Test)</td><td>-</td></tr>
<tr data-domain="SW" data-full="소프트웨어 유지보수 향상 및 비용절감을 위한 3R을 설명하시오."><td>133<span class="domain-badge sw">SW</span></td><td>관리</td><td>1</td><td>11</td><td class="question-cell">소프트웨어 유지보수 향상 및 비용절감을 위한 3R</td><td>-</td></tr>
<tr data-domain="SW" data-full="정보시스템 하드웨어 규모산정 지침(TTAK.KO-10.0292/R3, 2023.12.06. 개정)에 대하여 다음을 설명하시오. 가. 규모산정의 개념 및 대상 나. 규모산정 절차 다. 규모산정 방식"><td>133<span class="domain-badge sw">SW</span></td><td>관리</td><td>2</td><td>1</td><td class="question-cell">정보시스템 하드웨어 규모산정 지침</td><td>-</td></tr>
<tr data-domain="SW" data-full="소프트웨어 요구공학(Requirement Engineering)에 대하여 설명하시오. 가. 요구공학 정의 및 필요성 나. 요구공학 절차 다. 요구사항 명세서"><td>133<span class="domain-badge sw">SW</span></td><td>관리</td><td>3</td><td>5</td><td class="question-cell">소프트웨어 요구공학(Requirement Engineering)</td><td>-</td></tr>
<tr data-domain="SW" data-full="정보시스템 개발과 운영 단계에서 수행되는 소프트웨어 테스트의 종류를 쓰고, 이 중 신뢰성 테스트와 이식성 테스트의 세부 활동에 대하여 각각 설명하시오."><td>133<span class="domain-badge sw">SW</span></td><td>관리</td><td>4</td><td>2</td><td class="question-cell">소프트웨어 테스트 종류 - 신뢰성/이식성 테스트</td><td>-</td></tr>
<!-- 132회 -->
<tr data-domain="SW" data-full="ISO 31000"><td>132<span class="domain-badge sw">SW</span></td><td>관리</td><td>1</td><td>1</td><td class="question-cell">ISO 31000</td><td>-</td></tr>
<tr data-domain="SW" data-full="좋은 소프트웨어가 갖추어야 할 4가지 특징"><td>132<span class="domain-badge sw">SW</span></td><td>관리</td><td>1</td><td>9</td><td class="question-cell">좋은 소프트웨어가 갖추어야 할 4가지 특징</td><td>-</td></tr>
<tr data-domain="SW" data-full="현재, 소프트웨어 기술자 구분은 과거 기술자 등급제에서 IT역량분류체계를 기반으로 한 직무제(이하 IT직무제)로 변경되어 운영되고 있으나 실무 현장에서는 여전히 폐지된 등급제가 다수 활용되고 있는 실정이다. 소프트웨어 기술자 구분에 대하여 다음을 설명하시오. 가. 소프트웨어 기술자 등급제와 IT직무제의 개념과 특징 나. 현행 IT직무제의 문제점과 개선방향"><td>132<span class="domain-badge sw">SW</span></td><td>관리</td><td>2</td><td>3</td><td class="question-cell">소프트웨어 기술자 등급제와 IT직무제</td><td>-</td></tr>
<tr data-domain="SW" data-full="소프트웨어(이하 SW) 운영단계 대가산정에 대하여 다음을 설명하시오. (단, '소프트웨어 사업 대가 산정 가이드 2023년 개정판' 기준) 가. 응용SW 요율제 유지관리비 산정방식과 SW운영 투입공수 산정방식 나. 고정비/변동비 산정방식"><td>132<span class="domain-badge sw">SW</span></td><td>관리</td><td>3</td><td>1</td><td class="question-cell">SW 운영단계 대가산정 (2023년 개정판)</td><td>-</td></tr>
<tr data-domain="SW" data-full="정보시스템의 성능 요구사항 작성 시 고려해야 하는 주요 성능지표 및 내용에 대해 설명하시오."><td>132<span class="domain-badge sw">SW</span></td><td>관리</td><td>3</td><td>6</td><td class="question-cell">정보시스템 성능 요구사항 주요 성능지표</td><td>-</td></tr>
<tr data-domain="SW" data-full="소프트웨어 진흥법(시행 2023.10.19.)은 소프트웨어 산업의 발전을 위해 시행되어야 할 다양한 활동의 법적 근거를 마련하고 있다. 이와 관련하여 다음을 설명하시오. 가. 제5조(기본계획의 수립 등)의 2항에 따른 기본계획 내 포함되어야 할 사항 나. 제30조(소프트웨어안전 확보)의 2항에 따른 소프트웨어안전 확보를 위한 지침 내 포함되어야 할 사항"><td>132<span class="domain-badge sw">SW</span></td><td>관리</td><td>4</td><td>4</td><td class="question-cell">소프트웨어 진흥법</td><td>-</td></tr>
<tr data-domain="SW" data-full="소프트웨어 개발에 필요한 규모 산정 방식 종류와 특징을 비교 설명하고, 공공 소프트웨어 사업 규모 산정 방식의 현실적 개선 방안에 대하여 설명하시오."><td>132<span class="domain-badge sw">SW</span></td><td>관리</td><td>4</td><td>5</td><td class="question-cell">소프트웨어 규모 산정 방식 종류와 개선 방안</td><td>-</td></tr>
<tr data-domain="SW" data-full="Canary Test"><td>132<span class="domain-badge sw">SW</span></td><td>컴시응</td><td>1</td><td>3</td><td class="question-cell">Canary Test</td><td>-</td></tr>
<tr data-domain="SW" data-full="'소프트웨어 기술성 평가기준 지침'(과학기술정보통신부고시, 제2021-98호)에 명시된 기술제안서 평가항목"><td>132<span class="domain-badge sw">SW</span></td><td>컴시응</td><td>1</td><td>6</td><td class="question-cell">소프트웨어 기술성 평가기준 지침 - 기술제안서 평가항목</td><td>-</td></tr>
<tr data-domain="SW" data-full="전자정부사업관리 위탁(PMO, Project Management Office)"><td>132<span class="domain-badge sw">SW</span></td><td>컴시응</td><td>1</td><td>7</td><td class="question-cell">전자정부사업관리 위탁(PMO)</td><td>-</td></tr>
<tr data-domain="SW" data-full="이동형 로봇의 대인 충돌 안전성 평가 방법(정보통신단체표준, TTAK.KO-10.1223)에 대하여 아래 사항을 설명하시오. 가. 충돌 시험에서의 충격 속도 추정방법 나. 충돌 시험용 인체모형(더미, dummy) 다. 인체모형 측정 데이터"><td>132<span class="domain-badge sw">SW</span></td><td>컴시응</td><td>2</td><td>4</td><td class="question-cell">이동형 로봇 대인 충돌 안전성 평가 방법</td><td>-</td></tr>
<tr data-domain="SW" data-full="정보시스템 마스터플랜(ISMP, Information System Master Plan)에 대하여 아래 설명하시오. 가. ISMP와 EA(Enterprise Architecture), ISP(Information System Planning)에 대해 각각 설명하고 상호 비교 나. 투입공수에 의한 사업대가 산정방식을 적용한 ISMP수립비 산정 절차, 주요내용, 산출물"><td>132<span class="domain-badge sw">SW</span></td><td>컴시응</td><td>2</td><td>5</td><td class="question-cell">ISMP, EA, ISP 비교</td><td>-</td></tr>
<tr data-domain="SW" data-full="객체 지향 프로그래밍 기법을 활용한 소프트웨어 설계 시 고려해야 할 원칙(일명 SOLID 원칙) 5가지를 제시하고 설명하시오."><td>132<span class="domain-badge sw">SW</span></td><td>컴시응</td><td>3</td><td>5</td><td class="question-cell">객체 지향 SOLID 원칙 5가지</td><td>-</td></tr>
<tr data-domain="SW" data-full="한국지능정보사회진흥원에서 제시한 클라우드 서비스 활용사업 감리 점검에 대하여 아래 사항을 설명하시오. 가. 공공부문의 클라우드 사업 유형 나. 클라우드 서비스 활용사업의 점검 단계, 활동, 검토항목"><td>132<span class="domain-badge sw">SW</span></td><td>컴시응</td><td>4</td><td>2</td><td class="question-cell">클라우드 서비스 활용사업 감리 점검</td><td>-</td></tr>
<!-- 131회 -->
<tr data-domain="SW" data-full="폭포수 개발 방법론과 애자일 개발 방법론의 특징 및 장단점 비교"><td>131<span class="domain-badge sw">SW</span></td><td>관리</td><td>1</td><td>3</td><td class="question-cell">폭포수 vs 애자일 개발 방법론 특징 및 장단점 비교</td><td>-</td></tr>
<tr data-domain="SW" data-full="정보시스템 감리와 PMO(Project Management Office) 비교"><td>131<span class="domain-badge sw">SW</span></td><td>관리</td><td>1</td><td>6</td><td class="question-cell">정보시스템 감리와 PMO 비교</td><td>-</td></tr>
<tr data-domain="SW" data-full="객체지향 방법론에서 캡슐화(Encapsulation)와 정보은닉(Information Hiding)"><td>131<span class="domain-badge sw">SW</span></td><td>관리</td><td>1</td><td>12</td><td class="question-cell">캡슐화(Encapsulation)와 정보은닉(Information Hiding)</td><td>-</td></tr>
<tr data-domain="SW" data-full="아키텍처 스타일과 디자인 패턴에 대하여 다음을 설명하시오."><td>131<span class="domain-badge sw">SW</span></td><td>관리</td><td>2</td><td>6</td><td class="question-cell">아키텍처 스타일과 디자인 패턴</td><td>-</td></tr>
<tr data-domain="SW" data-full="통합테스트(Integration Test)에 대하여 다음을 설명하시오. 가. 비점진적 통합 방식과 점진적 통합 방식 나. 하향식(Top Down) 통합 테스트와 상향식(Bottom Up) 통합 테스트 다. 테스트 드라이버(Test Driver)와 테스트 스텁(Test Stub)"><td>131<span class="domain-badge sw">SW</span></td><td>관리</td><td>3</td><td>3</td><td class="question-cell">통합테스트(Integration Test)</td><td>-</td></tr>
<tr data-domain="SW" data-full="소프트웨어 안전성 분석의 필요성과 다음의 분석 기법을 설명하시오. 가. FTA(Fault Tree Analysis) 나. FMEA(Failure Mode and Effects Analysis) 다. HAZOP(Hazard and Operability Analysis)"><td>131<span class="domain-badge sw">SW</span></td><td>관리</td><td>3</td><td>4</td><td class="question-cell">안전성 분석 FTA, FMEA, HAZOP</td><td>-</td></tr>
<tr data-domain="SW" data-full="소프트웨어 규모산정에 대하여 다음을 설명하시오. 가. 필요성과 산정방법 나. 규모산정 방식의 종류별 특징"><td>131<span class="domain-badge sw">SW</span></td><td>관리</td><td>4</td><td>5</td><td class="question-cell">소프트웨어 규모산정</td><td>-</td></tr>
<tr data-domain="SW" data-full="ATAM(Architecture Tradeoff Analysis Method)과 CBAM(Cost Benefit Analysis Method)"><td>131<span class="domain-badge sw">SW</span></td><td>컴시응</td><td>1</td><td>5</td><td class="question-cell">ATAM과 CBAM</td><td>-</td></tr>
<tr data-domain="SW" data-full="현행 데이터베이스 데이터량을 기준으로 TO-BE 데이터량을 예측하고자 한다. 이와 관련하여 다음을 설명하시오. 가. 데이터베이스 용량산정 방법 별 개념 및 장,단점 나. 데이터베이스 용량산정 기준"><td>131<span class="domain-badge sw">SW</span></td><td>컴시응</td><td>2</td><td>3</td><td class="question-cell">데이터베이스 용량산정</td><td>-</td></tr>
<tr data-domain="SW" data-full="데이터옵스(DataOps)의 주요 기술을 설명하고, 데브옵스(DevOps)와의 차이점을 설명하시오."><td>131<span class="domain-badge sw">SW</span></td><td>컴시응</td><td>3</td><td>6</td><td class="question-cell">DataOps와 DevOps 비교</td><td>-</td></tr>
</tbody>
</table>

<!-- DataTables JS -->
<script src="https://code.jquery.com/jquery-3.7.0.min.js"></script>
<script src="https://cdn.datatables.net/1.13.7/js/jquery.dataTables.min.js"></script>

<script>
var table;
var currentDomain = 'all';

$(document).ready(function() {
  table = $('#examTable').DataTable({
    order: [[0, 'desc'], [2, 'asc'], [3, 'asc']],
    pageLength: -1,
    lengthMenu: [[-1, 25, 50, 100], ["전체", 25, 50, 100]],
    language: {
      search: "검색:",
      lengthMenu: "_MENU_ 개씩 보기",
      info: "_START_ - _END_ / _TOTAL_개",
      infoEmpty: "0개",
      infoFiltered: "(전체 _MAX_개 중)",
      paginate: { first: "처음", last: "마지막", next: "다음", previous: "이전" },
      zeroRecords: "검색 결과가 없습니다"
    },
    columnDefs: [
      { targets: [0, 1, 2, 3], className: 'dt-center' }
    ]
  });
  
  // 영역 버튼 클릭
  $('.domain-btn').click(function() {
    $('.domain-btn').removeClass('active');
    $(this).addClass('active');
    currentDomain = $(this).data('domain');
    applyFilters();
  });
  
  // 엔터키로 검색
  $('#filterKeyword').keypress(function(e) {
    if (e.which == 13) applyFilters();
  });
  
  // 셀렉트 변경 시 자동 필터
  $('#filterClass, #filterRound').change(function() {
    applyFilters();
  });
});

function applyFilters() {
  var classVal = $('#filterClass').val();
  var roundVal = $('#filterRound').val();
  var keyword = $('#filterKeyword').val();
  
  // 커스텀 필터링 함수
  $.fn.dataTable.ext.search.pop(); // 기존 필터 제거
  $.fn.dataTable.ext.search.push(function(settings, data, dataIndex) {
    var row = table.row(dataIndex).node();
    var rowDomain = $(row).data('domain');
    
    // 영역 필터
    if (currentDomain !== 'all' && rowDomain !== currentDomain) {
      return false;
    }
    
    // 교시 필터
    if (classVal && data[2] !== classVal) {
      return false;
    }
    
    // 회차 필터
    if (roundVal && !data[0].includes(roundVal)) {
      return false;
    }
    
    // 키워드 검색
    if (keyword) {
      var searchText = data[4].toLowerCase();
      if (!searchText.includes(keyword.toLowerCase())) {
        return false;
      }
    }
    
    return true;
  });
  
  table.draw();
}

function resetFilters() {
  $('#filterClass').val('');
  $('#filterRound').val('');
  $('#filterKeyword').val('');
  $('.domain-btn').removeClass('active');
  $('.domain-btn[data-domain="all"]').addClass('active');
  currentDomain = 'all';
  
  $.fn.dataTable.ext.search.pop();
  table.draw();
}

// 테이블 로드 후 data-full 값을 문제 컬럼에 표시
$('#examTable tbody tr').each(function() {
  var fullQuestion = $(this).attr('data-full');
  if (fullQuestion) {
    var questionCell = $(this).find('.question-cell');
    var link = questionCell.find('a');
    if (link.length) {
      link.text(fullQuestion);
    } else {
      questionCell.text(fullQuestion);
    }
  }
});
</script>
