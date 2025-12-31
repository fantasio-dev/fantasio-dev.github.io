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
<tr class="has-page" data-domain="SW" data-full="소프트웨어 영향평가에 대하여 다음 사항을 설명하시오. 가. 영향평가 대상 기관 나. 소프트웨어사업 영향평가 체계"><td>137<span class="domain-badge sw">SW</span></td><td>컴시응</td><td>2</td><td>5</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/sw/exam/137-2-5-sw-impact-assessment">소프트웨어 영향평가</a></td><td><code>(대상) 국지공정과정출지</code> <code>(체계) 목기방절</code></td></tr>
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
<!-- AI 영역 기출문제 -->
<!-- 137회 -->
<tr class="has-page" data-domain="AI" data-full="GNN(Graph Neural Network)을 설명하시오"><td>137<span class="domain-badge ai">AI</span></td><td>관리</td><td>1</td><td>5</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/ai/exam/137-1-5-gnn">GNN(Graph Neural Network)</a></td><td><code>(절차) 변취업생</code> <code>(모델) GCN-SAGE-GAT-GIN</code></td></tr>
<tr class="has-page" data-domain="AI" data-full="트랜스포머(Transformer)와 MoE(Mixture of Experts)를 설명하시오."><td>137<span class="domain-badge ai">AI</span></td><td>관리</td><td>1</td><td>7</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/ai/exam/137-1-7-moe">Transformer와 MoE(Mixture of Experts)</a></td><td><code>(Transformer) 셀멀포피</code> <code>(MoE) 게전스로</code></td></tr>
<tr class="has-page" data-domain="AI" data-full="AI 신뢰성 검인증 제도(CAT)를 설명하시오"><td>137<span class="domain-badge ai">AI</span></td><td>관리</td><td>1</td><td>8</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/ai/exam/137-1-8-ai">AI 신뢰성 검인증 제도(CAT)</a></td><td><code>(암기법) 위거신추</code> <code>(암기법) 상이편오</code></td></tr>
<tr class="has-page" data-domain="AI" data-full="RAG(Retrieval Augmented Generation)과 Fine Tuning의 기본 개념과 대표 프레임워크"><td>137<span class="domain-badge ai">AI</span></td><td>컴시응</td><td>1</td><td>8</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/ai/exam/137-1-8-rag-fine-tuning">RAG와 Fine Tuning</a></td><td><code>(RAG절차) 질유관추프텍</code> <code>(FT절차) 데모하파평</code></td></tr>
<tr class="has-page" data-domain="AI" data-full="멀티모달(Multimodal)의 기술요소"><td>137<span class="domain-badge ai">AI</span></td><td>컴시응</td><td>1</td><td>9</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/ai/exam/137-1-9-topic">멀티모달(Multimodal)의 기술요소</a></td><td><code>(처리기술) 지음이추</code> <code>(융합기술) 얼레크</code></td></tr>
<tr class="has-page" data-domain="AI" data-full="이진 탐색 트리를 설명하시오."><td>137<span class="domain-badge ai">AI</span></td><td>관리</td><td>1</td><td>12</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/ai/exam/137-1-12-bst">이진 탐색 트리(BST, AVL, Red-Black)</a></td><td><code>(구성) 루부자리왼오</code> <code>(비교) 균동검삽시공</code></td></tr>
<tr class="has-page" data-domain="AI" data-full="MCP(Model Context Protocol)를 이용한 인공지능 서비스 구축시 보안 취약점을 설명하고 대응방안을 제시하시오"><td>137<span class="domain-badge ai">AI</span></td><td>관리</td><td>2</td><td>3</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/ai/exam/137-2-3-mcp">MCP 보안 취약점과 대응방안</a></td><td><code>(취약점) 컨위모감</code> <code>(대응) 인최사격</code></td></tr>
<tr class="has-page" data-domain="AI" data-full="공공부문 초거대 AI 도입·활용 가이드라인 2.0"><td>137<span class="domain-badge ai">AI</span></td><td>관리</td><td>2</td><td>4</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/ai/exam/137-2-4-hyperscale-ai-guideline">공공부문 초거대 AI 도입·활용 가이드라인 2.0</a></td><td><code>(구성요소) 데모컴학안</code> <code>(도입절차) 보클학서운성</code></td></tr>
<tr class="has-page" data-domain="AI" data-full="sLLM(Small Large Language Model)"><td>137<span class="domain-badge ai">AI</span></td><td>컴시응</td><td>2</td><td>4</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/ai/exam/137-2-4-sllm">sLLM(Small Large Language Model)</a></td><td><code>(필요성) 전T응</code> <code>(경량화) 양가지</code></td></tr>
<tr class="has-page" data-domain="AI" data-full="TEXT2SQL 에 대하여 다음 각 항목을 설명하시오. 가. TEXT2SQL 의 개념 나. TEXT2SQL 활용 사례 2 가지"><td>137<span class="domain-badge ai">AI</span></td><td>관리</td><td>2</td><td>6</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/ai/exam/137-2-6-text2sql-text2sql-text2sql-2">TEXT2SQL 개념과 활용 사례</a></td><td><code>(구성요소) 토구의스</code> <code>(사례) 비고</code></td></tr>
<tr class="has-page" data-domain="AI" data-full="양자 머신러닝(QML, Quantum Machine Learning)의 주요 기술 및 알고리즘을 설명하고, 기존 머신러닝과 비교하시오."><td>137<span class="domain-badge ai">AI</span></td><td>컴시응</td><td>4</td><td>3</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/ai/exam/137-4-3-qml">양자 머신러닝(QML)</a></td><td><code>(원리) 중얽간</code> <code>(알고리즘) HQV-SKP</code></td></tr>
<tr class="has-page" data-domain="AI" data-full="유전 알고리즘(Genetic Algorithm)"><td>137<span class="domain-badge ai">AI</span></td><td>관리</td><td>4</td><td>5</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/ai/exam/137-4-5-genetic-algorithm">유전 알고리즘(Genetic Algorithm)</a></td><td><code>(구성) 염유개인</code> <code>(절차) 초적선교변대반</code></td></tr>
<!-- 136회 -->
<tr class="has-page" data-domain="AI" data-full="범용 AI(General-Purpose AI) 위험관리 프레임워크"><td>136<span class="domain-badge ai">AI</span></td><td>관리</td><td>1</td><td>2</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/ai/exam/136-1-2-ai-136-1-2">범용 AI 위험관리 프레임워크</a></td><td><code>(절차) 식분평대</code> <code>(평가) 점3등</code></td></tr>
<tr class="has-page" data-domain="AI" data-full="에이전틱 AI(Agentic AI)"><td>136<span class="domain-badge ai">AI</span></td><td>관리</td><td>1</td><td>3</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/ai/exam/136-1-3-ai-136-1-3">에이전틱 AI(Agentic AI)</a></td><td><code>(루프) 인추행학</code> <code>(특징) 자목상반</code></td></tr>
<tr class="has-page" data-domain="AI" data-full="MCP(Model Context Protocol)"><td>136<span class="domain-badge ai">AI</span></td><td>관리</td><td>1</td><td>13</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/ai/exam/136-1-13-mcp">MCP(Model Context Protocol)</a></td><td><code>(Actor) 호클서</code> <code>(특징) 컨개확</code></td></tr>
<tr class="has-page" data-domain="AI" data-full="AI 기반 소프트웨어 개발에서 LLM(Large Language Model)을 도입할 때 고려해야 할 보안 위험을 3가지 이상 쓰고 각 대응 방안을 설명하시오."><td>136<span class="domain-badge ai">AI</span></td><td>관리</td><td>2</td><td>3</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/ai/exam/136-2-3-llm-security">LLM 도입 시 보안 위험과 대응방안</a></td><td><code>(SW내부) 인데권벡</code> <code>(전략) DevSec전AI</code></td></tr>
<tr class="has-page" data-domain="AI" data-full="최근 인공지능(AI)을 활용한 기업의 디지털 전환(AX, AI Transformation)이 다양한 산업 분야에서 빠르게 진행되고 있다. 이와 관련하여 다음을 설명하시오."><td>136<span class="domain-badge ai">AI</span></td><td>관리</td><td>3</td><td>2</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/ai/exam/136-3-2-ax-transformation">AX(AI Transformation)</a></td><td><code>(중요이유) 비운데보기</code> <code>(절차) 목인데모전</code></td></tr>
<tr data-domain="AI" data-full="데이터 분석 시 아웃라이어(Outlier)에 대하여 다음을 설명하시오. 가. 아웃라이어의 개념 나. 아웃라이어와 노이즈(Noise)의 차이점 다. 아웃라이어의 3 가지 유형인 전역, 맥락, 군집"><td>136<span class="domain-badge ai">AI</span></td><td>관리</td><td>3</td><td>4</td><td class="question-cell">아웃라이어(Outlier) 개념과 유형</td><td>-</td></tr>
<tr data-domain="AI" data-full="혼동행렬(Confusion Matrix) 결과를 참고하여 다음을 계산하고 설명하시오."><td>136<span class="domain-badge ai">AI</span></td><td>관리</td><td>3</td><td>5</td><td class="question-cell">혼동행렬(Confusion Matrix) 성능 평가</td><td>-</td></tr>
<tr data-domain="AI" data-full="국내 인공지능(AI) 윤리기준과 생성형 AI에 대하여 다음을 설명하시오. 가. 3대 기본 원칙과 10대 핵심요건 나. 인공지능 윤리 관점에서 생성형 AI의 역기능 요소"><td>136<span class="domain-badge ai">AI</span></td><td>관리</td><td>4</td><td>1</td><td class="question-cell">AI 윤리기준과 생성형 AI 역기능</td><td>-</td></tr>
<!-- 135회 -->
<tr class="has-page" data-domain="AI" data-full="PR(Precision Recall) 곡선과 ROC(Receiver Operating Characteristic) 곡선 비교"><td>135<span class="domain-badge ai">AI</span></td><td>관리</td><td>1</td><td>1</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/ai/exam/135-1-1-pr-roc">PR 곡선과 ROC 곡선 비교</a></td><td><code>(PR) 정재F1</code> <code>(ROC) 참거특</code></td></tr>
<tr class="has-page" data-domain="AI" data-full="Multimodal LLM(Large Language Model)"><td>135<span class="domain-badge ai">AI</span></td><td>관리</td><td>1</td><td>2</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/ai/exam/135-1-2-multimodal-llm">Multimodal LLM</a></td><td><code>(전처리) 토해스영</code> <code>(융합) 얼미레</code></td></tr>
<tr class="has-page" data-domain="AI" data-full="몬테카를로 트리탐색(Monte Carlo Tree Search)"><td>135<span class="domain-badge ai">AI</span></td><td>컴시응</td><td>1</td><td>4</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/ai/exam/135-1-4-mcts">몬테카를로 트리탐색(MCTS)</a></td><td><code>(절차) 선확시역</code> <code>(핵심) 탐활</code></td></tr>
<tr class="has-page" data-domain="AI" data-full="실루엣 계수(Silhouette Coefficient)"><td>135<span class="domain-badge ai">AI</span></td><td>관리</td><td>1</td><td>6</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/ai/exam/135-1-6-topic-135-1-6">실루엣 계수(Silhouette Coefficient)</a></td><td><code>(정의) 응분</code> <code>(활용) 최K비이</code></td></tr>
<tr class="has-page" data-domain="AI" data-full="불편추정량(Unbiased Estimator)"><td>135<span class="domain-badge ai">AI</span></td><td>관리</td><td>1</td><td>8</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/ai/exam/135-1-8-unbiased-estimator">불편추정량(Unbiased Estimator)</a></td><td><code>(준거) 불효일충</code> <code>(유형) 평분비</code></td></tr>
<tr class="has-page" data-domain="AI" data-full="인공지능 성능 관련 차원의 저주 (Curse of Dimensionality)"><td>135<span class="domain-badge ai">AI</span></td><td>컴시응</td><td>1</td><td>9</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/ai/exam/135-1-9-topic-135-1-9">차원의 저주(Curse of Dimensionality)</a></td><td><code>(원인) 희다과거</code> <code>(해결) 축선규증</code></td></tr>
<tr class="has-page" data-domain="AI" data-full="VAE(Variational AutoEncoder)"><td>135<span class="domain-badge ai">AI</span></td><td>관리</td><td>1</td><td>12</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/ai/exam/135-1-12-vae">VAE(Variational AutoEncoder)</a></td><td><code>(구조) 인잠디</code> <code>(핵심) 변재확인</code></td></tr>
<tr class="has-page" data-domain="AI" data-full="RAG(Retrieval-Augmented Generation)"><td>135<span class="domain-badge ai">AI</span></td><td>컴시응</td><td>1</td><td>12</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/ai/exam/135-1-12-rag">RAG(Retrieval-Augmented Generation)</a></td><td><code>(절차) 문입정답출</code> <code>(필요성) 지환범</code></td></tr>
<tr class="has-page" data-domain="AI" data-full="AGI(Artificial General Intelligence) 측면에서 ANI(Artificial Narrow Intelligence)의 필요성"><td>135<span class="domain-badge ai">AI</span></td><td>관리</td><td>1</td><td>13</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/ai/exam/135-1-13-agi-ani">AGI 측면에서 ANI의 필요성</a></td><td><code>(개발) 데전기시</code> <code>(비교) 특학적</code></td></tr>
<tr data-domain="AI" data-full="생성형 인공지능 학습을 위한 멀티모달 데이터의 품질검증 방법에 대하여 설명하시오."><td>135<span class="domain-badge ai">AI</span></td><td>컴시응</td><td>2</td><td>1</td><td class="question-cell">생성형 AI 멀티모달 데이터 품질검증</td><td>-</td></tr>
<tr data-domain="AI" data-full="회귀모형에서 오차의 등분산성(Homoscedasticity)과 다중공선성(Multicollinearity)에 대하여 설명하시오."><td>135<span class="domain-badge ai">AI</span></td><td>관리</td><td>2</td><td>3</td><td class="question-cell">등분산성과 다중공선성</td><td>-</td></tr>
<tr data-domain="AI" data-full="거대 언어 모델(Large Language Model) 적용을 위한 5가지 고려사항과 5가지 아키텍처"><td>135<span class="domain-badge ai">AI</span></td><td>관리</td><td>2</td><td>5</td><td class="question-cell">LLM 적용 고려사항과 아키텍처</td><td>-</td></tr>
<tr data-domain="AI" data-full="프롬프트 엔지니어링(Prompt Enginerng)의 기술 요소와 활용 방안에 대하여 설명하시오"><td>135<span class="domain-badge ai">AI</span></td><td>관리</td><td>3</td><td>2</td><td class="question-cell">프롬프트 엔지니어링</td><td>-</td></tr>
<tr data-domain="AI" data-full="연결 리스트(Linked List)에 대하여 설명하시오."><td>135<span class="domain-badge ai">AI</span></td><td>컴시응</td><td>3</td><td>6</td><td class="question-cell">연결 리스트(Linked List)</td><td>-</td></tr>
<tr data-domain="AI" data-full="확장성 해싱(Extendible Hashing)기법에 대하여 설명하시오."><td>135<span class="domain-badge ai">AI</span></td><td>관리</td><td>4</td><td>1</td><td class="question-cell">확장성 해싱(Extendible Hashing)</td><td>-</td></tr>
<tr data-domain="AI" data-full="이항 분포(Binomial Distribution)와 포아송 분포(Poisson Distribution)를 비교 설명하시오."><td>135<span class="domain-badge ai">AI</span></td><td>관리</td><td>4</td><td>3</td><td class="question-cell">이항 분포와 포아송 분포 비교</td><td>-</td></tr>
<tr data-domain="AI" data-full="인공지능 소프트웨어 품질 보증을 위한 테스트 기법에 대하여 설명하시오."><td>135<span class="domain-badge ai">AI</span></td><td>관리</td><td>4</td><td>5</td><td class="question-cell">AI SW 품질 보증 테스트 기법</td><td>-</td></tr>
<!-- 134회 -->
<tr data-domain="AI" data-full="머신러닝(Machine Learning) 성능지표"><td>134<span class="domain-badge ai">AI</span></td><td>관리</td><td>1</td><td>3</td><td class="question-cell">머신러닝 성능지표</td><td>-</td></tr>
<tr data-domain="AI" data-full="이미지 데이터 어노테이션(Data Annotation) 유형과 기법"><td>134<span class="domain-badge ai">AI</span></td><td>관리</td><td>1</td><td>6</td><td class="question-cell">이미지 데이터 어노테이션</td><td>-</td></tr>
<tr data-domain="AI" data-full="RAG(Retrieval Augmented Generation)"><td>134<span class="domain-badge ai">AI</span></td><td>관리</td><td>1</td><td>13</td><td class="question-cell">RAG(Retrieval Augmented Generation)</td><td>-</td></tr>
<tr data-domain="AI" data-full="공공 부문 초거대 AI 도입•활용 가이드라인에 대하여 설명하시오."><td>134<span class="domain-badge ai">AI</span></td><td>컴시응</td><td>2</td><td>2</td><td class="question-cell">공공부문 초거대 AI 도입 가이드라인</td><td>-</td></tr>
<tr data-domain="AI" data-full="알고리즘의 복잡도를 설명하고 O-Notation의 개념과 유형 및 유형별 연산시간의 차이를 설명하시오."><td>134<span class="domain-badge ai">AI</span></td><td>관리</td><td>3</td><td>4</td><td class="question-cell">알고리즘 복잡도와 O-Notation</td><td>-</td></tr>
<tr data-domain="AI" data-full="AI 시스템에 대한 법적 이슈, 윤리적 문제, 기술적 문제에 대하여 설명하고 해결 방안을 제시하시오."><td>134<span class="domain-badge ai">AI</span></td><td>관리</td><td>4</td><td>3</td><td class="question-cell">AI 시스템의 법적/윤리적/기술적 문제</td><td>-</td></tr>
<tr data-domain="AI" data-full="멀티모달 인공지능에 관한 다음 사항을 설명하시오."><td>134<span class="domain-badge ai">AI</span></td><td>컴시응</td><td>4</td><td>6</td><td class="question-cell">멀티모달 인공지능</td><td>-</td></tr>
<!-- 133회 -->
<tr data-domain="AI" data-full="인공지능 신뢰성의 개념과 핵심 속성에 대하여 설명하시오."><td>133<span class="domain-badge ai">AI</span></td><td>관리</td><td>1</td><td>8</td><td class="question-cell">인공지능 신뢰성</td><td>-</td></tr>
<tr data-domain="AI" data-full="자연어 언어모델에서의 PLM(Pre-trained Language Model)의 특성을 설명하고, LLM으로 만들어지는 과정에 대하여 설명하시오."><td>133<span class="domain-badge ai">AI</span></td><td>관리</td><td>2</td><td>4</td><td class="question-cell">PLM과 LLM 학습 과정</td><td>-</td></tr>
<tr data-domain="AI" data-full="생성형AI의 보안위협과 안전한 활용을 위한 가이드라인에 대하여 설명하시오."><td>133<span class="domain-badge ai">AI</span></td><td>관리</td><td>3</td><td>2</td><td class="question-cell">생성형AI 보안 가이드라인</td><td>-</td></tr>
<tr data-domain="AI" data-full="인공신경망에 대하여 설명하시오. 가. 개념, 구성요소, 역할 나. 피드포워드 뉴럴 네트워크 다. 역전파 라. 활성화 함수"><td>133<span class="domain-badge ai">AI</span></td><td>관리</td><td>3</td><td>6</td><td class="question-cell">인공신경망(피드포워드, 역전파, 활성화함수)</td><td>-</td></tr>
<!-- 132회 -->
<tr data-domain="AI" data-full="베이지안 최적화(Bayesian Optimization)"><td>132<span class="domain-badge ai">AI</span></td><td>관리</td><td>1</td><td>3</td><td class="question-cell">베이지안 최적화</td><td>-</td></tr>
<tr data-domain="AI" data-full="모집단의 특성을 추론하는 점추정과 구간추정 비교"><td>132<span class="domain-badge ai">AI</span></td><td>관리</td><td>1</td><td>10</td><td class="question-cell">점추정과 구간추정 비교</td><td>-</td></tr>
<tr data-domain="AI" data-full="다중공선성"><td>132<span class="domain-badge ai">AI</span></td><td>관리</td><td>1</td><td>11</td><td class="question-cell">다중공선성</td><td>-</td></tr>
<tr data-domain="AI" data-full="파인튜닝(Fine-tuning)"><td>132<span class="domain-badge ai">AI</span></td><td>컴시응</td><td>1</td><td>11</td><td class="question-cell">파인튜닝(Fine-tuning)</td><td>-</td></tr>
<tr data-domain="AI" data-full="중심극한정리, t-검정, z-검정을 설명하시오."><td>132<span class="domain-badge ai">AI</span></td><td>관리</td><td>2</td><td>1</td><td class="question-cell">중심극한정리, t-검정, z-검정</td><td>-</td></tr>
<tr data-domain="AI" data-full="선형 자료 구조인 스택, 큐, 리스트의 자료 입출력 원리를 설명하시오."><td>132<span class="domain-badge ai">AI</span></td><td>관리</td><td>2</td><td>6</td><td class="question-cell">스택, 큐, 리스트 입출력 원리</td><td>-</td></tr>
<tr data-domain="AI" data-full="TF-IDF(Term Frequency-Inverse Document Frequency)를 식별하기 위한 계산과정과 그 결과를 설명하시오."><td>132<span class="domain-badge ai">AI</span></td><td>관리</td><td>3</td><td>3</td><td class="question-cell">TF-IDF 계산</td><td>-</td></tr>
<tr data-domain="AI" data-full="설비 예지정비(Predictive Maintenance) 시스템 구축 시 LangChain 프레임워크를 활용할 수 있는 방안"><td>132<span class="domain-badge ai">AI</span></td><td>관리</td><td>4</td><td>3</td><td class="question-cell">LangChain을 이용한 설비 예지정비</td><td>-</td></tr>
<!-- 131회 -->
<tr data-domain="AI" data-full="몬테 카를로 방법(Monte Carlo Method)"><td>131<span class="domain-badge ai">AI</span></td><td>컴시응</td><td>1</td><td>1</td><td class="question-cell">몬테 카를로 방법</td><td>-</td></tr>
<tr data-domain="AI" data-full="오토인코더(Autoencoder)"><td>131<span class="domain-badge ai">AI</span></td><td>컴시응</td><td>1</td><td>3</td><td class="question-cell">오토인코더(Autoencoder)</td><td>-</td></tr>
<tr data-domain="AI" data-full="전이학습(Transfer Learning)"><td>131<span class="domain-badge ai">AI</span></td><td>컴시응</td><td>1</td><td>4</td><td class="question-cell">전이학습(Transfer Learning)</td><td>-</td></tr>
<tr data-domain="AI" data-full="데이터 차원 축소(Data Dimensionality Reduction)"><td>131<span class="domain-badge ai">AI</span></td><td>관리</td><td>1</td><td>5</td><td class="question-cell">데이터 차원 축소</td><td>-</td></tr>
<tr data-domain="AI" data-full="머신러닝(Machin Learning)과 딥러닝(Deep Learning) 차이"><td>131<span class="domain-badge ai">AI</span></td><td>관리</td><td>1</td><td>7</td><td class="question-cell">머신러닝과 딥러닝 차이</td><td>-</td></tr>
<tr data-domain="AI" data-full="독립표본 t-검정(Independent t-test)과 대응표본 t-검정(Paired t-test)"><td>131<span class="domain-badge ai">AI</span></td><td>관리</td><td>1</td><td>9</td><td class="question-cell">독립표본 t-검정과 대응표본 t-검정</td><td>-</td></tr>
<tr data-domain="AI" data-full="알고리즘의 시간복잡도(Time Complexity), 공간복잡도(Space Complexity)"><td>131<span class="domain-badge ai">AI</span></td><td>컴시응</td><td>1</td><td>9</td><td class="question-cell">시간복잡도와 공간복잡도</td><td>-</td></tr>
<tr data-domain="AI" data-full="마르코프 결정 프로세스(Markov Decision Process)와 벨만방정식에 대하여 설명하시오."><td>131<span class="domain-badge ai">AI</span></td><td>컴시응</td><td>2</td><td>1</td><td class="question-cell">마르코프 결정 프로세스와 벨만방정식</td><td>-</td></tr>
<tr data-domain="AI" data-full="인공지능 학습용 데이터 허브 구축 과정에서 생성된 학습용 데이터 셋의 품질확보를 위한 주요활동에 대하여 설명하시오."><td>131<span class="domain-badge ai">AI</span></td><td>관리</td><td>3</td><td>1</td><td class="question-cell">AI 학습용 데이터 품질관리</td><td>-</td></tr>
<tr data-domain="AI" data-full="데이터 구조(Data Structure)에 대하여 설명하시오. 가. 선형 구조 나. 비선형 구조 다. 비교"><td>131<span class="domain-badge ai">AI</span></td><td>관리</td><td>3</td><td>2</td><td class="question-cell">데이터 구조(선형/비선형)</td><td>-</td></tr>
<tr data-domain="AI" data-full="강화학습(Reinforcement Learning)에 대하여 설명하시오."><td>131<span class="domain-badge ai">AI</span></td><td>컴시응</td><td>4</td><td>1</td><td class="question-cell">강화학습(가치기반/정책기반/Actor-Critic)</td><td>-</td></tr>
<tr data-domain="AI" data-full="인공지능 분야에서 파운데이션 모델의 개념, 특징, 기반기술 및 고려사항에 대하여 설명하시오."><td>131<span class="domain-badge ai">AI</span></td><td>관리</td><td>4</td><td>4</td><td class="question-cell">파운데이션 모델</td><td>-</td></tr>
<tr data-domain="AI" data-full="정렬 알고리즘에 대하여 설명하시오. 가. 버블 정렬 나. 삽입 정렬 다. 퀵 정렬"><td>131<span class="domain-badge ai">AI</span></td><td>관리</td><td>4</td><td>6</td><td class="question-cell">정렬 알고리즘(버블/삽입/퀵)</td><td>-</td></tr>
<!-- SEC 영역 기출문제 -->
<!-- 137회 -->
<tr class="has-page" data-domain="SEC" data-full="디지털 포렌식에서 아트팩트(Artifact)를 설명하시오"><td>137<span class="domain-badge sec">SEC</span></td><td>관리</td><td>1</td><td>2</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/sec/exam/137-1-2-artifact">디지털 포렌식 아트팩트(Artifact)</a></td><td><code>(절차) 식우수무문</code> <code>(유형) 시응파메</code></td></tr>
<tr class="has-page" data-domain="SEC" data-full="암호문 공격(Ciphertext Attack)을 설명하시오"><td>137<span class="domain-badge sec">SEC</span></td><td>관리</td><td>1</td><td>4</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/sec/exam/137-1-4-ciphertext-attack">암호문 공격(Ciphertext Attack)</a></td><td><code>(특징) 제패고현</code> <code>(공격) 빈패통기</code></td></tr>
<tr class="has-page" data-domain="SEC" data-full="AI 거버넌스(Artificial Intelligence Governance)를 설명하시오"><td>137<span class="domain-badge sec">SEC</span></td><td>관리</td><td>1</td><td>6</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/sec/exam/137-1-6-ai-governance">AI 거버넌스</a></td><td><code>(필요성) 사편규</code> <code>(구성요소) 가조프검</code></td></tr>
<tr class="has-page" data-domain="SEC" data-full="국가 망 보안체계(N2SF)에 대하여 개념, 적용 절차, 고려사항을 설명하시오"><td>137<span class="domain-badge sec">SEC</span></td><td>관리</td><td>3</td><td>6</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/sec/exam/137-3-6-n2sf">국가 망 보안체계(N2SF)</a></td><td><code>CSO차자점</code> <code>준등위보적</code></td></tr>
<tr class="has-page" data-domain="SEC" data-full="BPFdoor 악성코드에 대하여 개념 및 기존 백도어와의 차이점, 위협 요소, 대응 방안을 설명하시오"><td>137<span class="domain-badge sec">SEC</span></td><td>관리</td><td>4</td><td>1</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/sec/exam/137-4-1-bpfdoor">BPFdoor 악성코드</a></td><td><code>스메보</code> <code>탐방은다APT</code></td></tr>
<tr class="has-page" data-domain="SEC" data-full="인공지능 시스템의 취약점"><td>137<span class="domain-badge sec">SEC</span></td><td>컴시응</td><td>1</td><td>11</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/sec/exam/137-1-11-ai-vulnerability">인공지능 시스템의 취약점</a></td><td><code>(개발단계) 요데모</code> <code>(적대적공격) PEIM</code></td></tr>
<tr class="has-page" data-domain="SEC" data-full="클라우드 네이티브 보안"><td>137<span class="domain-badge sec">SEC</span></td><td>컴시응</td><td>1</td><td>12</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/sec/exam/137-1-12-cloud-native-security">클라우드 네이티브 보안</a></td><td><code>(계층) 4C</code> <code>(특징) 동Dev제</code></td></tr>
<tr class="has-page" data-domain="SEC" data-full="공공 마이데이터 활용 방안에 대하여 설명하시오"><td>137<span class="domain-badge sec">SEC</span></td><td>컴시응</td><td>2</td><td>1</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/sec/exam/137-2-1-public-mydata">공공 마이데이터 활용 방안</a></td><td><code>정보본제</code> <code>맞행통취생</code></td></tr>
<tr class="has-page" data-domain="SEC" data-full="OPC UA에 대하여 등장배경, OPC와 비교, 활용분야를 설명하시오"><td>137<span class="domain-badge sec">SEC</span></td><td>컴시응</td><td>3</td><td>3</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/sec/exam/137-3-3-opc-ua">OPC UA</a></td><td><code>윈암구→플보상</code></td></tr>
<tr class="has-page" data-domain="SEC" data-full="샌드박스와 화이트박스의 목적, 적용 방법 및 예시를 설명하시오"><td>137<span class="domain-badge sec">SEC</span></td><td>컴시응</td><td>3</td><td>5</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/sec/exam/137-3-5-sandbox-whitebox">샌드박스와 화이트박스</a></td><td><code>보격</code> <code>품보</code></td></tr>
<tr class="has-page" data-domain="SEC" data-full="침입차단시스템(Firewall), IDS, IPS 및 VPN에 대하여 설명하시오"><td>137<span class="domain-badge sec">SEC</span></td><td>컴시응</td><td>4</td><td>5</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/sec/exam/137-4-5-firewall-ids-ips-vpn">Firewall, IDS, IPS, VPN</a></td><td><code>접사트트감프N</code></td></tr>
<!-- 136회 -->
<tr class="has-page" data-domain="SEC" data-full="개인정보 안심구역과 데이터안심구역 비교"><td>136<span class="domain-badge sec">SEC</span></td><td>관리</td><td>1</td><td>10</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/sec/exam/136-1-10-safe-zone-comparison">개인정보 안심구역과 데이터안심구역 비교</a></td><td><code>(상세비교) 법운목대이보</code></td></tr>
<tr class="has-page" data-domain="SEC" data-full="CC(Common Criteria)"><td>136<span class="domain-badge sec">SEC</span></td><td>관리</td><td>1</td><td>11</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/sec/exam/136-1-11-common-criteria">CC(Common Criteria)</a></td><td><code>(구성) 소기보</code> <code>(용어) TOE-PP-ST-EAL</code></td></tr>
<tr class="has-page" data-domain="SEC" data-full="타원곡선 암호(ECC)"><td>136<span class="domain-badge sec">SEC</span></td><td>관리</td><td>1</td><td>12</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/sec/exam/136-1-12-ecc">타원곡선 암호(ECC)</a></td><td><code>(방정식) y²=x³+ax+b</code></td></tr>
<tr class="has-page" data-domain="SEC" data-full="TLS에 대하여 프로토콜 구조와 핸드셰이크 과정, TLS 1.2 취약점과 TLS 1.3 개선 사항"><td>136<span class="domain-badge sec">SEC</span></td><td>관리</td><td>2</td><td>6</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/sec/exam/136-2-6-tls">TLS 프로토콜</a></td><td><code>RHCA</code> <code>CS인CF</code></td></tr>
<tr class="has-page" data-domain="SEC" data-full="공급망 보안을 설명하고, 제로트러스트 기반 공급망 보안 아키텍처"><td>136<span class="domain-badge sec">SEC</span></td><td>관리</td><td>4</td><td>4</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/sec/exam/136-4-4-supply-chain-security">공급망 보안과 제로트러스트</a></td><td><code>외탐위</code> <code>PE-PA-PEP</code></td></tr>
<tr class="has-page" data-domain="SEC" data-full="OWASP LLM Top 10에 대하여 배경과 주요 특징, 주요 보안 위협, 대응방안을 설명하시오"><td>136<span class="domain-badge sec">SEC</span></td><td>관리</td><td>4</td><td>5</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/sec/exam/136-4-5-owasp-llm-top10">OWASP LLM Top 10</a></td><td><code>인민공 대출과 프벡정무</code></td></tr>
<tr class="has-page" data-domain="SEC" data-full="소프트웨어 보안 품질에 대하여 정의와 중요성, 자동화 기술과 도구, 구현방안, 기대효과를 설명하시오"><td>136<span class="domain-badge sec">SEC</span></td><td>관리</td><td>4</td><td>6</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/sec/exam/136-4-6-sw-security-quality">소프트웨어 보안 품질</a></td><td><code>기무부책인</code> <code>요설개테배</code></td></tr>
<!-- 135회 -->
<tr class="has-page" data-domain="SEC" data-full="SIEM & SOAR 비교"><td>135<span class="domain-badge sec">SEC</span></td><td>관리</td><td>1</td><td>5</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/sec/exam/135-1-5-siem-soar-comparison">SIEM & SOAR 비교</a></td><td><code>(SIEM) 목로그이사보자</code> <code>(SOAR) 목자오사보자</code></td></tr>
<tr class="has-page" data-domain="SEC" data-full="개인정보 안심구역"><td>135<span class="domain-badge sec">SEC</span></td><td>관리</td><td>1</td><td>7</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/sec/exam/135-1-7-personal-info-safe-zone">개인정보 안심구역</a></td><td><code>안가P</code> <code>담공보</code></td></tr>
<tr data-domain="SEC" data-full="양자 암호 기술에 대하여 QKD, PQC, QKD와 PQC 비교를 설명하시오"><td>135<span class="domain-badge sec">SEC</span></td><td>관리</td><td>3</td><td>4</td><td class="question-cell">양자 암호 기술(QKD, PQC)</td><td>-</td></tr>
<tr data-domain="SEC" data-full="딥페이크에 대하여 개념 및 핵심 기술, 문제점, 대응방안을 설명하시오"><td>135<span class="domain-badge sec">SEC</span></td><td>관리</td><td>3</td><td>6</td><td class="question-cell">딥페이크 개념과 대응방안</td><td>-</td></tr>
<tr data-domain="SEC" data-full="경계 기반 보안과 제로 트러스트 성숙도모델 2.0 비교"><td>135<span class="domain-badge sec">SEC</span></td><td>관리</td><td>4</td><td>6</td><td class="question-cell">경계 기반 보안 vs 제로 트러스트</td><td>-</td></tr>
<tr data-domain="SEC" data-full="접근통제 정책(MAC, DAC, RBAC, ABAC)에 대하여 설명하시오"><td>135<span class="domain-badge sec">SEC</span></td><td>컴시응</td><td>2</td><td>3</td><td class="question-cell">접근통제 정책(MAC, DAC, RBAC, ABAC)</td><td>-</td></tr>
<tr data-domain="SEC" data-full="제로트러스트 가이드라인 2.0에 대하여 설명하시오"><td>135<span class="domain-badge sec">SEC</span></td><td>컴시응</td><td>3</td><td>3</td><td class="question-cell">제로트러스트 가이드라인 2.0</td><td>-</td></tr>
<!-- 134회 -->
<tr class="has-page" data-domain="SEC" data-full="개인정보 보호 강화기술(PET)"><td>134<span class="domain-badge sec">SEC</span></td><td>관리</td><td>1</td><td>11</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/sec/exam/134-1-11-pet">개인정보 보호 강화기술(PET)</a></td><td><code>난암연책</code> <code>차합영</code></td></tr>
<tr data-domain="SEC" data-full="다크패턴(Dark Pattern)의 세부 유형 및 대응 방안을 설명하시오"><td>134<span class="domain-badge sec">SEC</span></td><td>관리</td><td>2</td><td>2</td><td class="question-cell">다크패턴(Dark Pattern)</td><td>-</td></tr>
<tr data-domain="SEC" data-full="SBOM에 대하여 오픈소스 소프트웨어 취약점, SBOM 기반 관리 방안을 설명하시오"><td>134<span class="domain-badge sec">SEC</span></td><td>관리</td><td>3</td><td>3</td><td class="question-cell">SBOM과 오픈소스 취약점 관리</td><td>-</td></tr>
<tr class="has-page" data-domain="SEC" data-full="제로데이(Zero Day) 취약점"><td>134<span class="domain-badge sec">SEC</span></td><td>컴시응</td><td>1</td><td>2</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/sec/exam/134-1-2-zero-day">제로데이 취약점</a></td><td><code>발분개배업</code> <code>최방필교</code></td></tr>
<tr class="has-page" data-domain="SEC" data-full="제로 트러스트(Zero Trust)"><td>134<span class="domain-badge sec">SEC</span></td><td>컴시응</td><td>1</td><td>5</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/sec/exam/134-1-5-zero-trust">제로 트러스트</a></td><td><code>제데</code> <code>PE-PA-PEP</code></td></tr>
<tr class="has-page" data-domain="SEC" data-full="동적 WEP 키(Dynamic WEP Key)"><td>134<span class="domain-badge sec">SEC</span></td><td>컴시응</td><td>1</td><td>6</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/sec/exam/134-1-6-dynamic-wep-key">동적 WEP 키</a></td><td><code>인암</code> <code>공무키초</code></td></tr>
<tr class="has-page" data-domain="SEC" data-full="SBOM(Software Bill of Materials)"><td>134<span class="domain-badge sec">SEC</span></td><td>컴시응</td><td>1</td><td>7</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/sec/exam/134-1-7-sbom">SBOM</a></td><td><code>작시공구버해고관</code> <code>S-C-S</code></td></tr>
<tr data-domain="SEC" data-full="ISMS-P 간편인증에 대하여 목적, 대상, 기준을 설명하시오"><td>134<span class="domain-badge sec">SEC</span></td><td>컴시응</td><td>2</td><td>3</td><td class="question-cell">ISMS-P 간편인증</td><td>-</td></tr>
<tr data-domain="SEC" data-full="스푸핑 공격에 대하여 개념, ARP/IP/DNS 스푸핑 공격 방법과 보안 대책을 설명하시오"><td>134<span class="domain-badge sec">SEC</span></td><td>컴시응</td><td>2</td><td>4</td><td class="question-cell">스푸핑 공격(ARP/IP/DNS)</td><td>-</td></tr>
<tr data-domain="SEC" data-full="웹방화벽, IDS, IPS의 개념과 기능을 설명하시오"><td>134<span class="domain-badge sec">SEC</span></td><td>컴시응</td><td>3</td><td>6</td><td class="question-cell">웹방화벽, IDS, IPS</td><td>-</td></tr>
<tr data-domain="SEC" data-full="PET에 대하여 개념, 주요 유형, 적용 사례를 설명하시오"><td>134<span class="domain-badge sec">SEC</span></td><td>컴시응</td><td>4</td><td>4</td><td class="question-cell">PET 주요 유형과 적용 사례</td><td>-</td></tr>
<!-- 133회 -->
<tr class="has-page" data-domain="SEC" data-full="전자봉투 생성절차와 개봉절차를 설명하시오"><td>133<span class="domain-badge sec">SEC</span></td><td>관리</td><td>1</td><td>4</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/sec/exam/133-1-4-digital-envelope">전자봉투</a></td><td><code>메전비전전</code> <code>전암전무</code></td></tr>
<tr class="has-page" data-domain="SEC" data-full="동형암호의 동작원리와 유형을 설명하시오"><td>133<span class="domain-badge sec">SEC</span></td><td>관리</td><td>1</td><td>5</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/sec/exam/133-1-5-homomorphic-encryption">동형암호</a></td><td><code>부준완</code> <code>스부서다</code></td></tr>
<tr class="has-page" data-domain="SEC" data-full="딥페이크(Deepfake)에 대하여 설명하시오"><td>133<span class="domain-badge sec">SEC</span></td><td>관리</td><td>1</td><td>10</td><td class="question-cell"><a href="{{ site.baseurl }}/docs/sec/exam/133-1-10-deepfake">딥페이크</a></td><td><code>수학프합</code> <code>L-A</code></td></tr>
<tr data-domain="SEC" data-full="PbD(Privacy by Design)에 대하여 7대 원칙, 8대 전략을 설명하시오"><td>133<span class="domain-badge sec">SEC</span></td><td>관리</td><td>2</td><td>5</td><td class="question-cell">PbD(Privacy by Design)</td><td>-</td></tr>
<tr data-domain="SEC" data-full="안티포렌식에 대하여 배경 및 기술을 설명하시오"><td>133<span class="domain-badge sec">SEC</span></td><td>관리</td><td>3</td><td>1</td><td class="question-cell">안티포렌식</td><td>-</td></tr>
<tr data-domain="SEC" data-full="접근제어에 대하여 개념과 정책, 절차, 구현 매커니즘을 설명하시오"><td>133<span class="domain-badge sec">SEC</span></td><td>관리</td><td>4</td><td>3</td><td class="question-cell">접근제어</td><td>-</td></tr>
<tr data-domain="SEC" data-full="VPN에 대하여 개념 및 특징, IPSec VPN과 SSL VPN을 설명하시오"><td>133<span class="domain-badge sec">SEC</span></td><td>관리</td><td>4</td><td>6</td><td class="question-cell">VPN(IPSec/SSL)</td><td>-</td></tr>
<!-- 132회 -->
<tr data-domain="SEC" data-full="대칭 암호화와 비대칭 암호화"><td>132<span class="domain-badge sec">SEC</span></td><td>관리</td><td>1</td><td>4</td><td class="question-cell">대칭 암호화와 비대칭 암호화</td><td>-</td></tr>
<tr data-domain="SEC" data-full="ISA/IEC 62443"><td>132<span class="domain-badge sec">SEC</span></td><td>관리</td><td>1</td><td>5</td><td class="question-cell">ISA/IEC 62443</td><td>-</td></tr>
<tr data-domain="SEC" data-full="큐싱(Qshing)"><td>132<span class="domain-badge sec">SEC</span></td><td>관리</td><td>1</td><td>6</td><td class="question-cell">큐싱(Qshing)</td><td>-</td></tr>
<tr data-domain="SEC" data-full="TPM(Trusted Platform Module)"><td>132<span class="domain-badge sec">SEC</span></td><td>관리</td><td>1</td><td>8</td><td class="question-cell">TPM</td><td>-</td></tr>
<tr data-domain="SEC" data-full="마이데이터 전송 보안 안내서에 대하여 설명하시오"><td>132<span class="domain-badge sec">SEC</span></td><td>관리</td><td>2</td><td>4</td><td class="question-cell">마이데이터 전송 보안</td><td>-</td></tr>
<tr data-domain="SEC" data-full="APEC CBPR에 대하여 프라이버시 9원칙, 주요 인증기준을 설명하시오"><td>132<span class="domain-badge sec">SEC</span></td><td>관리</td><td>3</td><td>5</td><td class="question-cell">APEC CBPR</td><td>-</td></tr>
<tr data-domain="SEC" data-full="FIPS 140-2에 대하여 레벨 분류, 암호화 시스템 설계 시 고려사항을 설명하시오"><td>132<span class="domain-badge sec">SEC</span></td><td>관리</td><td>4</td><td>1</td><td class="question-cell">FIPS 140-2</td><td>-</td></tr>
<tr data-domain="SEC" data-full="정보보안 체계 수립에 대하여 정책의 개념, 시점별 보안 활동을 설명하시오"><td>132<span class="domain-badge sec">SEC</span></td><td>관리</td><td>4</td><td>6</td><td class="question-cell">정보보안 체계 수립</td><td>-</td></tr>
<tr data-domain="SEC" data-full="만리장성 모델(Chinese Wall Model, Brewer-Nash Model)"><td>132<span class="domain-badge sec">SEC</span></td><td>컴시응</td><td>1</td><td>10</td><td class="question-cell">만리장성 모델</td><td>-</td></tr>
<!-- 131회 -->
<tr data-domain="SEC" data-full="크리덴셜 스터핑(Credential stuffing)"><td>131<span class="domain-badge sec">SEC</span></td><td>관리</td><td>1</td><td>10</td><td class="question-cell">크리덴셜 스터핑</td><td>-</td></tr>
<tr data-domain="SEC" data-full="SBOM(Software Bill of Material)"><td>131<span class="domain-badge sec">SEC</span></td><td>관리</td><td>1</td><td>13</td><td class="question-cell">SBOM</td><td>-</td></tr>
<tr data-domain="SEC" data-full="인공지능 윤리와 거버넌스 모형에 대하여 설명하시오"><td>131<span class="domain-badge sec">SEC</span></td><td>관리</td><td>2</td><td>3</td><td class="question-cell">인공지능 윤리와 거버넌스</td><td>-</td></tr>
<tr data-domain="SEC" data-full="제로 트러스트 보안모델의 보안원리, 핵심원칙, 적용분야를 설명하시오"><td>131<span class="domain-badge sec">SEC</span></td><td>관리</td><td>2</td><td>4</td><td class="question-cell">제로 트러스트 보안모델</td><td>-</td></tr>
<tr data-domain="SEC" data-full="ISMS와 ISMS-P에 대하여 차이점, ISMS 의무 대상 기준을 설명하시오"><td>131<span class="domain-badge sec">SEC</span></td><td>관리</td><td>3</td><td>6</td><td class="question-cell">ISMS와 ISMS-P</td><td>-</td></tr>
<tr data-domain="SEC" data-full="개인정보의 안전성 확보조치 기준에 대하여 설명하시오"><td>131<span class="domain-badge sec">SEC</span></td><td>관리</td><td>4</td><td>2</td><td class="question-cell">개인정보 안전성 확보조치 기준</td><td>-</td></tr>
<tr data-domain="SEC" data-full="CBPR(Cross Border Privacy Rule)"><td>131<span class="domain-badge sec">SEC</span></td><td>컴시응</td><td>1</td><td>12</td><td class="question-cell">CBPR</td><td>-</td></tr>
<tr data-domain="SEC" data-full="CSRF(Cross-Site Request Forgery)"><td>131<span class="domain-badge sec">SEC</span></td><td>컴시응</td><td>1</td><td>13</td><td class="question-cell">CSRF</td><td>-</td></tr>
<tr data-domain="SEC" data-full="적대적 예제(Adversarial Example)에 대하여 설명하시오"><td>131<span class="domain-badge sec">SEC</span></td><td>컴시응</td><td>3</td><td>1</td><td class="question-cell">적대적 예제(Adversarial Example)</td><td>-</td></tr>
<tr data-domain="SEC" data-full="개인정보 비식별 처리에 대하여 유형, 위험 요인을 설명하시오"><td>131<span class="domain-badge sec">SEC</span></td><td>컴시응</td><td>3</td><td>2</td><td class="question-cell">개인정보 비식별 처리</td><td>-</td></tr>
<tr data-domain="SEC" data-full="공공기관 정보화 사업 추진 시 국가정보원 보안성 검토 절차를 설명하시오"><td>131<span class="domain-badge sec">SEC</span></td><td>컴시응</td><td>3</td><td>5</td><td class="question-cell">국정원 보안성 검토 절차</td><td>-</td></tr>
<!-- 130회 -->
<tr data-domain="SEC" data-full="블록 암호화 알고리즘"><td>130<span class="domain-badge sec">SEC</span></td><td>관리</td><td>1</td><td>6</td><td class="question-cell">블록 암호화 알고리즘</td><td>-</td></tr>
<tr data-domain="SEC" data-full="개인정보보호법 개정안에 대하여 주요 내용을 설명하시오"><td>130<span class="domain-badge sec">SEC</span></td><td>관리</td><td>2</td><td>4</td><td class="question-cell">개인정보보호법 개정안</td><td>-</td></tr>
<tr data-domain="SEC" data-full="메타버스 윤리원칙에 대하여 설명하시오"><td>130<span class="domain-badge sec">SEC</span></td><td>관리</td><td>2</td><td>5</td><td class="question-cell">메타버스 윤리원칙</td><td>-</td></tr>
<tr data-domain="SEC" data-full="디지털 역기능에 대하여 개념과 사례, 대응방안을 설명하시오"><td>130<span class="domain-badge sec">SEC</span></td><td>관리</td><td>2</td><td>6</td><td class="question-cell">디지털 역기능</td><td>-</td></tr>
<tr data-domain="SEC" data-full="인공지능 보안 위협에 대하여 설명하시오"><td>130<span class="domain-badge sec">SEC</span></td><td>관리</td><td>3</td><td>4</td><td class="question-cell">인공지능 보안 위협</td><td>-</td></tr>
<tr data-domain="SEC" data-full="디지털 포렌식에 대하여 개념, 유형과 절차를 설명하시오"><td>130<span class="domain-badge sec">SEC</span></td><td>관리</td><td>4</td><td>2</td><td class="question-cell">디지털 포렌식</td><td>-</td></tr>
<tr data-domain="SEC" data-full="클라우드 서비스 도입 시 고려해야 할 보안 요소를 설명하시오"><td>130<span class="domain-badge sec">SEC</span></td><td>관리</td><td>4</td><td>3</td><td class="question-cell">클라우드 보안 요소</td><td>-</td></tr>
<!-- 129회 -->
<tr data-domain="SEC" data-full="인공지능의 3대 기본원칙 및 10대 핵심요건"><td>129<span class="domain-badge sec">SEC</span></td><td>관리</td><td>1</td><td>2</td><td class="question-cell">AI 3대 기본원칙 및 10대 핵심요건</td><td>-</td></tr>
<tr data-domain="SEC" data-full="정보보호 제품 신속 확인 제도"><td>129<span class="domain-badge sec">SEC</span></td><td>관리</td><td>1</td><td>11</td><td class="question-cell">정보보호 제품 신속 확인 제도</td><td>-</td></tr>
<tr data-domain="SEC" data-full="접근 제어의 통제정책과 LDAP의 인증흐름에 대하여 설명하시오"><td>129<span class="domain-badge sec">SEC</span></td><td>관리</td><td>2</td><td>2</td><td class="question-cell">접근 제어와 LDAP 인증</td><td>-</td></tr>
<tr data-domain="SEC" data-full="인포스틸러(InfoStealer) 개념과 공격 절차, 대응방안을 설명하시오"><td>129<span class="domain-badge sec">SEC</span></td><td>관리</td><td>4</td><td>1</td><td class="question-cell">인포스틸러(InfoStealer)</td><td>-</td></tr>
<tr data-domain="SEC" data-full="CSAP (Cloud Security Assurance Program)"><td>129<span class="domain-badge sec">SEC</span></td><td>컴시응</td><td>1</td><td>2</td><td class="question-cell">CSAP</td><td>-</td></tr>
<tr data-domain="SEC" data-full="웹 애플리케이션 방화벽(WAF)"><td>129<span class="domain-badge sec">SEC</span></td><td>컴시응</td><td>1</td><td>3</td><td class="question-cell">WAF</td><td>-</td></tr>
<tr data-domain="SEC" data-full="양자 컴퓨터에 대하여 Qubit, 양자 우월성을 설명하시오"><td>129<span class="domain-badge sec">SEC</span></td><td>컴시응</td><td>3</td><td>4</td><td class="question-cell">양자 컴퓨터</td><td>-</td></tr>
<tr data-domain="SEC" data-full="디스크 이미징에 대하여 용도, 증거수집 방법을 설명하시오"><td>129<span class="domain-badge sec">SEC</span></td><td>컴시응</td><td>4</td><td>3</td><td class="question-cell">디스크 이미징</td><td>-</td></tr>
<!-- 128회 -->
<tr data-domain="SEC" data-full="개인정보의 가명 익명처리 기술에 대하여 설명하시오"><td>128<span class="domain-badge sec">SEC</span></td><td>관리</td><td>1</td><td>10</td><td class="question-cell">가명/익명처리 기술</td><td>-</td></tr>
<tr data-domain="SEC" data-full="랜섬웨어와 RaaS에 대하여 설명하시오"><td>128<span class="domain-badge sec">SEC</span></td><td>관리</td><td>1</td><td>12</td><td class="question-cell">랜섬웨어와 RaaS</td><td>-</td></tr>
<tr data-domain="SEC" data-full="큐비트(Qubit)에 대하여 설명하시오"><td>128<span class="domain-badge sec">SEC</span></td><td>관리</td><td>1</td><td>13</td><td class="question-cell">큐비트(Qubit)</td><td>-</td></tr>
<tr data-domain="SEC" data-full="데이터 3법과 마이데이터사업에 대하여 설명하시오"><td>128<span class="domain-badge sec">SEC</span></td><td>관리</td><td>2</td><td>4</td><td class="question-cell">데이터 3법과 마이데이터</td><td>-</td></tr>
<tr data-domain="SEC" data-full="양자암호통신에 대하여 암호키 분배방식, 취약점을 설명하시오"><td>128<span class="domain-badge sec">SEC</span></td><td>관리</td><td>4</td><td>4</td><td class="question-cell">양자암호통신</td><td>-</td></tr>
<tr data-domain="SEC" data-full="식별과 인증에 대하여 정의 및 차이점, 인증 방식 4가지 유형을 설명하시오"><td>128<span class="domain-badge sec">SEC</span></td><td>관리</td><td>4</td><td>6</td><td class="question-cell">식별과 인증</td><td>-</td></tr>
<tr data-domain="SEC" data-full="DRM, DLP 비교"><td>128<span class="domain-badge sec">SEC</span></td><td>컴시응</td><td>1</td><td>6</td><td class="question-cell">DRM, DLP 비교</td><td>-</td></tr>
<tr data-domain="SEC" data-full="디피-헬만 알고리즘(Diffie-Hellman Algorithm)"><td>128<span class="domain-badge sec">SEC</span></td><td>컴시응</td><td>1</td><td>12</td><td class="question-cell">디피-헬만 알고리즘</td><td>-</td></tr>
<tr data-domain="SEC" data-full="융합보안관제에 대하여 필요성, 구축 시 고려사항을 설명하시오"><td>128<span class="domain-badge sec">SEC</span></td><td>컴시응</td><td>2</td><td>4</td><td class="question-cell">융합보안관제</td><td>-</td></tr>
<tr data-domain="SEC" data-full="디지털 포렌식 증거 수집에 대하여 설명하시오"><td>128<span class="domain-badge sec">SEC</span></td><td>컴시응</td><td>3</td><td>3</td><td class="question-cell">디지털 포렌식 증거 수집</td><td>-</td></tr>
<!-- 127회 -->
<tr data-domain="SEC" data-full="메시지 인증 코드(Message Authentication Code)"><td>127<span class="domain-badge sec">SEC</span></td><td>관리</td><td>1</td><td>5</td><td class="question-cell">메시지 인증 코드(MAC)</td><td>-</td></tr>
<tr data-domain="SEC" data-full="변조(Modification)와 위조(Fabrication)"><td>127<span class="domain-badge sec">SEC</span></td><td>관리</td><td>1</td><td>9</td><td class="question-cell">변조와 위조</td><td>-</td></tr>
<tr data-domain="SEC" data-full="개인정보 안전성 확보조치 기준에 명시된 내부관리계획에 대해 설명하시오"><td>127<span class="domain-badge sec">SEC</span></td><td>관리</td><td>2</td><td>5</td><td class="question-cell">개인정보 내부관리계획</td><td>-</td></tr>
<tr data-domain="SEC" data-full="접근 통제 보안 모델에 대하여 벨 라파듈라, 비바, Clark and Wilson 모델을 설명하시오"><td>127<span class="domain-badge sec">SEC</span></td><td>관리</td><td>2</td><td>6</td><td class="question-cell">접근 통제 보안 모델</td><td>-</td></tr>
<tr data-domain="SEC" data-full="SOAR에 대하여 설명하시오"><td>127<span class="domain-badge sec">SEC</span></td><td>관리</td><td>3</td><td>6</td><td class="question-cell">SOAR</td><td>-</td></tr>
<tr data-domain="SEC" data-full="블록 암호 모드에 대하여 ECB, CBC, CFB, OFB 모드를 설명하시오"><td>127<span class="domain-badge sec">SEC</span></td><td>관리</td><td>4</td><td>6</td><td class="question-cell">블록 암호 모드</td><td>-</td></tr>
<!-- 126회 -->
<tr data-domain="SEC" data-full="파일슬랙(File Slack)"><td>126<span class="domain-badge sec">SEC</span></td><td>관리</td><td>1</td><td>13</td><td class="question-cell">파일슬랙</td><td>-</td></tr>
<tr data-domain="SEC" data-full="VPN과 Tor에 대하여 설명하시오"><td>126<span class="domain-badge sec">SEC</span></td><td>관리</td><td>4</td><td>4</td><td class="question-cell">VPN과 Tor</td><td>-</td></tr>
<tr data-domain="SEC" data-full="RSA 알고리즘과 DSA를 비교하여 설명하시오"><td>126<span class="domain-badge sec">SEC</span></td><td>관리</td><td>4</td><td>5</td><td class="question-cell">RSA와 DSA 비교</td><td>-</td></tr>
<tr data-domain="SEC" data-full="파일 카빙에 대하여 개념, 4종류 기법의 특징을 설명하시오"><td>126<span class="domain-badge sec">SEC</span></td><td>관리</td><td>4</td><td>6</td><td class="question-cell">파일 카빙</td><td>-</td></tr>
<tr data-domain="SEC" data-full="샌드박스의 주요 구성요소 및 활용분야"><td>126<span class="domain-badge sec">SEC</span></td><td>컴시응</td><td>1</td><td>3</td><td class="question-cell">샌드박스</td><td>-</td></tr>
<tr data-domain="SEC" data-full="ISMS-P"><td>126<span class="domain-badge sec">SEC</span></td><td>컴시응</td><td>1</td><td>6</td><td class="question-cell">ISMS-P</td><td>-</td></tr>
<tr data-domain="SEC" data-full="양자키분배(Quantum Key Distribution) 기술"><td>126<span class="domain-badge sec">SEC</span></td><td>컴시응</td><td>1</td><td>11</td><td class="question-cell">양자키분배(QKD)</td><td>-</td></tr>
<tr data-domain="SEC" data-full="스마트 팩토리의 보안위협과 보안 요구사항, 보안대책에 대하여 설명하시오"><td>126<span class="domain-badge sec">SEC</span></td><td>컴시응</td><td>2</td><td>4</td><td class="question-cell">스마트 팩토리 보안</td><td>-</td></tr>
<tr data-domain="SEC" data-full="소프트웨어 개발 보안 가이드에 대하여 설명하시오"><td>126<span class="domain-badge sec">SEC</span></td><td>컴시응</td><td>3</td><td>1</td><td class="question-cell">SW 개발 보안 가이드</td><td>-</td></tr>
<tr data-domain="SEC" data-full="ISO/IEC 29100 프라이버시 11원칙과 ISO/IEC 27701에 대하여 설명하시오"><td>126<span class="domain-badge sec">SEC</span></td><td>컴시응</td><td>3</td><td>2</td><td class="question-cell">ISO 29100 / ISO 27701</td><td>-</td></tr>
<tr data-domain="SEC" data-full="마이데이터 서비스에 대하여 절차, 인증 방식, 보안 문제점을 설명하시오"><td>126<span class="domain-badge sec">SEC</span></td><td>컴시응</td><td>3</td><td>5</td><td class="question-cell">마이데이터 서비스</td><td>-</td></tr>
<!-- 125회 -->
<tr data-domain="SEC" data-full="SECaaS(Security as a Service)"><td>125<span class="domain-badge sec">SEC</span></td><td>관리</td><td>1</td><td>1</td><td class="question-cell">SECaaS</td><td>-</td></tr>
<tr data-domain="SEC" data-full="동형암호(Homomorphic Encryption)"><td>125<span class="domain-badge sec">SEC</span></td><td>관리</td><td>1</td><td>2</td><td class="question-cell">동형암호</td><td>-</td></tr>
<tr data-domain="SEC" data-full="포스트 양자 암호(Post-Quantum Cryptography)"><td>125<span class="domain-badge sec">SEC</span></td><td>관리</td><td>1</td><td>9</td><td class="question-cell">포스트 양자 암호(PQC)</td><td>-</td></tr>
<tr data-domain="SEC" data-full="TOCTOU에 대하여 정의와 개념, 문제 상황과 보안대책을 설명하시오"><td>125<span class="domain-badge sec">SEC</span></td><td>관리</td><td>2</td><td>4</td><td class="question-cell">TOCTOU</td><td>-</td></tr>
<tr data-domain="SEC" data-full="EMP공격에 대하여 정의와 구분, HEMP의 원리를 설명하시오"><td>125<span class="domain-badge sec">SEC</span></td><td>관리</td><td>2</td><td>5</td><td class="question-cell">EMP공격</td><td>-</td></tr>
<tr data-domain="SEC" data-full="산업제어시스템의 퍼듀 모델에 대하여 개념, 계층별 특징을 설명하시오"><td>125<span class="domain-badge sec">SEC</span></td><td>관리</td><td>4</td><td>6</td><td class="question-cell">퍼듀 모델</td><td>-</td></tr>
<tr data-domain="SEC" data-full="디바이스 DNA"><td>125<span class="domain-badge sec">SEC</span></td><td>컴시응</td><td>1</td><td>13</td><td class="question-cell">디바이스 DNA</td><td>-</td></tr>
<tr data-domain="SEC" data-full="망분리시스템에 대하여 개념 및 원칙, 구축 유형 비교를 설명하시오"><td>125<span class="domain-badge sec">SEC</span></td><td>컴시응</td><td>2</td><td>1</td><td class="question-cell">망분리시스템</td><td>-</td></tr>
<tr data-domain="SEC" data-full="DDoS 공격에 대하여 공격기법, 보안 대책을 설명하시오"><td>125<span class="domain-badge sec">SEC</span></td><td>컴시응</td><td>2</td><td>6</td><td class="question-cell">DDoS 공격</td><td>-</td></tr>
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
