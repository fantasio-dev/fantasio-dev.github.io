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

/* 모달 스타일 */
.modal-overlay {
  display: none;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0,0,0,0.5);
  z-index: 9999;
  justify-content: center;
  align-items: center;
}
.modal-overlay.show {
  display: flex;
}
.modal-content {
  background: #fff;
  border-radius: 12px;
  max-width: 700px;
  width: 90%;
  max-height: 80vh;
  overflow-y: auto;
  box-shadow: 0 10px 40px rgba(0,0,0,0.3);
}
.modal-header {
  padding: 1rem 1.5rem;
  border-bottom: 1px solid #dee2e6;
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: #f8f9fa;
  border-radius: 12px 12px 0 0;
}
.modal-header h3 {
  margin: 0;
  font-size: 1rem;
  color: #495057;
}
.modal-close {
  background: none;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
  color: #6c757d;
  line-height: 1;
}
.modal-close:hover {
  color: #dc3545;
}
.modal-body {
  padding: 1.5rem;
}
.modal-body .question-full {
  font-size: 1rem;
  line-height: 1.8;
  color: #212529;
}
.modal-body .question-meta {
  margin-top: 1rem;
  padding-top: 1rem;
  border-top: 1px solid #dee2e6;
  font-size: 0.85rem;
  color: #6c757d;
}
.modal-body .btn-go {
  display: inline-block;
  margin-top: 1rem;
  padding: 0.5rem 1rem;
  background: #4A90D9;
  color: #fff;
  border-radius: 6px;
  text-decoration: none;
  font-size: 0.9rem;
}
.modal-body .btn-go:hover {
  background: #3A7BC8;
}

/* 문제 클릭 가능 스타일 */
.question-cell {
  cursor: pointer;
}
.question-cell:hover {
  text-decoration: underline;
  color: #4A90D9;
}
</style>

# 📝 통합 기출문제

<!-- 모달 -->
<div class="modal-overlay" id="questionModal">
  <div class="modal-content">
    <div class="modal-header">
      <h3 id="modalTitle">문제 상세</h3>
      <button class="modal-close" onclick="closeModal()">&times;</button>
    </div>
    <div class="modal-body">
      <div class="question-full" id="modalQuestion"></div>
      <div class="question-meta" id="modalMeta"></div>
      <a href="#" class="btn-go" id="modalLink" style="display:none;">📄 학습 페이지로 이동</a>
    </div>
  </div>
</div>

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
<!-- SW 영역 기출문제 (68개) -->
<!-- 138회 -->
<tr data-domain="SW"><td>138<span class="domain-badge sw">SW</span></td><td>관리</td><td>2</td><td>6</td><td><a href="{{ site.baseurl }}/docs/sw/exam/138-2-6-sw-cost-estimation">소프트웨어 사업 대가산정 (2025년 개정판)</a></td><td><code>(목적) 적기절일 산품제투</code> <code>(유형) 단커시</code> <code>(절차) 사서커구AI</code></td></tr>
<!-- 137회 -->
<tr class="has-page" data-domain="SW"><td>137<span class="domain-badge sw">SW</span></td><td>관리</td><td>1</td><td>11</td><td><a href="{{ site.baseurl }}/docs/sw/exam/137-1-11-reverse-reengineering">소프트웨어 역공학과 재공학</a></td><td><code>(역공학) 추분문</code> <code>(재공학) 역재구</code></td></tr>
<tr data-domain="SW"><td>137<span class="domain-badge sw">SW</span></td><td>관리</td><td>2</td><td>5</td><td><a href="{{ site.baseurl }}/docs/sw/exam/137-2-5-dynamic-testing">동적 테스트 (명세기반/구조기반)</a></td><td><code>(명세) 동분경의상유페</code> <code>(구조) 구분조경</code></td></tr>
<tr class="has-page" data-domain="SW"><td>137<span class="domain-badge sw">SW</span></td><td>관리</td><td>3</td><td>2</td><td><a href="{{ site.baseurl }}/docs/sw/exam/137-3-2-is-om-audit">정보시스템 운영 및 유지보수 감리</a></td><td><code>(운영) 릴테장/신서서</code> <code>(유지보수) 개상인</code></td></tr>
<tr class="has-page" data-domain="SW"><td>137<span class="domain-badge sw">SW</span></td><td>관리</td><td>4</td><td>4</td><td><a href="{{ site.baseurl }}/docs/sw/exam/137-4-4-uml-behavior-diagram">UML 행위 다이어그램</a></td><td>(Activity) 시종활선전구 (State) 시종상전 (Use-Case) 액유시-연확포일그</td></tr>
<tr data-domain="SW"><td>137<span class="domain-badge sw">SW</span></td><td>관리</td><td>4</td><td>6</td><td>소프트웨어 사업 대가산정 (2025년 개정판)</td><td><code>(목적) 적기절일 산품제투</code> <code>(유형) 단커시</code></td></tr>
<tr data-domain="SW"><td>137<span class="domain-badge sw">SW</span></td><td>컴시응</td><td>1</td><td>6</td><td>SIL과 HIL 테스팅</td><td>-</td></tr>
<tr class="has-page" data-domain="SW"><td>137<span class="domain-badge sw">SW</span></td><td>컴시응</td><td>2</td><td>2</td><td><a href="{{ site.baseurl }}/docs/sw/exam/136-2-2-sp-certification">소프트웨어 프로세스(SP) 품질인증 제도</a></td><td><code>(체계) 과NIPA기</code> <code>(영역) 프개지조프</code></td></tr>
<tr data-domain="SW"><td>137<span class="domain-badge sw">SW</span></td><td>컴시응</td><td>2</td><td>5</td><td><a href="{{ site.baseurl }}/docs/sw/exam/132-3-6-sw-impact-assessment">소프트웨어 영향평가</a></td><td><code>(대상) 국지공정과정출지</code> <code>(체계) 목기방절</code></td></tr>
<tr class="has-page" data-domain="SW"><td>137<span class="domain-badge sw">SW</span></td><td>컴시응</td><td>4</td><td>6</td><td><a href="{{ site.baseurl }}/docs/ds/exam/136-2-6-digital-service-contract">디지털서비스 전문계약제도</a></td><td><code>(특징) 간약사공표</code> <code>(종류) 클지융-I-S-P</code></td></tr>
<!-- 136회 -->
<tr data-domain="SW"><td>136<span class="domain-badge sw">SW</span></td><td>관리</td><td>1</td><td>5</td><td>프록시 디자인 패턴</td><td>-</td></tr>
<tr data-domain="SW"><td>136<span class="domain-badge sw">SW</span></td><td>관리</td><td>1</td><td>6</td><td>DevOps 장점과 단점</td><td>-</td></tr>
<tr class="has-page" data-domain="SW"><td>136<span class="domain-badge sw">SW</span></td><td>관리</td><td>2</td><td>2</td><td><a href="{{ site.baseurl }}/docs/sw/exam/136-2-2-pmo-audit">정보시스템 감리와 PMO</a></td><td><code>(법근) 전전전정-감</code> <code>(역할) 요분설구</code> <code>(비교) 개추법책관자투역제산</code></td></tr>
<tr class="has-page" data-domain="SW"><td>136<span class="domain-badge sw">SW</span></td><td>관리</td><td>2</td><td>4</td><td><a href="{{ site.baseurl }}/docs/sw/exam/136-2-4-product-line">제품계열(Product Line) 방법론</a></td><td><code>(특징) 핵품생초</code> <code>(기술) 도응관</code> <code>(고려) 비기조투</code></td></tr>
<tr class="has-page" data-domain="SW"><td>136<span class="domain-badge sw">SW</span></td><td>관리</td><td>3</td><td>1</td><td><a href="{{ site.baseurl }}/docs/sw/exam/136-3-1-conflict-tuckman">갈등관리와 터크만 팀 발달 모델</a></td><td><code>(관계) 부적극</code> <code>(요인) 구인업환</code> <code>(터크만) FSNPA</code></td></tr>
<tr class="has-page" data-domain="SW"><td>136<span class="domain-badge sw">SW</span></td><td>관리</td><td>3</td><td>3</td><td><a href="{{ site.baseurl }}/docs/sw/exam/136-3-3-software-quality-assurance">소프트웨어 품질보증과 인스펙션</a></td><td><code>(품질특성) 기신사성유보호안</code> <code>(인스펙션) 동사개검재후</code></td></tr>
<tr class="has-page" data-domain="SW"><td>136<span class="domain-badge sw">SW</span></td><td>관리</td><td>4</td><td>3</td><td><a href="{{ site.baseurl }}/docs/sw/exam/136-4-3-sw-expert-evaluation">대형SW사업 전문평가제도</a></td><td><code>(개정) 전공중기</code> <code>(영역) 정정데디</code> <code>(배점) 공60전40</code></td></tr>
<!-- 135회 -->
<tr data-domain="SW"><td>135<span class="domain-badge sw">SW</span></td><td>관리</td><td>1</td><td>3</td><td>요구사항 추적표(RTM)</td><td>-</td></tr>
<tr data-domain="SW"><td>135<span class="domain-badge sw">SW</span></td><td>관리</td><td>1</td><td>9</td><td>소프트웨어 기술 부채의 유형과 관리 방법</td><td>-</td></tr>
<tr class="has-page" data-domain="SW"><td>135<span class="domain-badge sw">SW</span></td><td>관리</td><td>2</td><td>2</td><td><a href="{{ site.baseurl }}/docs/sw/exam/135-2-2-cicd-devsecops">CI/CD 파이프라인에서 DevSecOps 적용방안</a></td><td><code>(구성) 버CI빌테코배모</code> <code>(적용) 초자컨배피문</code></td></tr>
<tr class="has-page" data-domain="SW"><td>135<span class="domain-badge sw">SW</span></td><td>관리</td><td>3</td><td>1</td><td><a href="{{ site.baseurl }}/docs/sw/exam/135-3-1-project-management">프로젝트 관리</a></td><td><code>(프로세스) 착계실감종</code> <code>(지식영역) 통이범자시원리품조의</code></td></tr>
<tr data-domain="SW"><td>135<span class="domain-badge sw">SW</span></td><td>컴시응</td><td>1</td><td>5</td><td>모놀리식 vs 마이크로서비스 아키텍처</td><td>-</td></tr>
<tr data-domain="SW"><td>135<span class="domain-badge sw">SW</span></td><td>컴시응</td><td>1</td><td>8</td><td>하드웨어 규모산정 방법 3가지</td><td>-</td></tr>
<tr class="has-page" data-domain="SW"><td>135<span class="domain-badge sw">SW</span></td><td>컴시응</td><td>4</td><td>4</td><td><a href="{{ site.baseurl }}/docs/sw/exam/135-4-4-zero-downtime-deployment">무중단 배포(Zero Downtime Deployment)</a></td><td><code>(문제점) 다유롤</code> <code>(종류) 롤블카</code></td></tr>
<!-- 134회 -->
<tr data-domain="SW"><td>134<span class="domain-badge sw">SW</span></td><td>관리</td><td>1</td><td>1</td><td>터크만 사다리 모델(Tuckman Ladder Model)</td><td>-</td></tr>
<tr data-domain="SW"><td>134<span class="domain-badge sw">SW</span></td><td>관리</td><td>1</td><td>4</td><td>형상관리 개념과 기준선(Baseline)</td><td>-</td></tr>
<tr data-domain="SW"><td>134<span class="domain-badge sw">SW</span></td><td>관리</td><td>1</td><td>5</td><td>정보은닉(Information Hiding)</td><td>-</td></tr>
<tr data-domain="SW"><td>134<span class="domain-badge sw">SW</span></td><td>관리</td><td>3</td><td>1</td><td>배포 전략 및 테스트 전략</td><td>-</td></tr>
<tr data-domain="SW"><td>134<span class="domain-badge sw">SW</span></td><td>관리</td><td>3</td><td>2</td><td>소프트웨어 테스트 원리/블랙박스/화이트박스</td><td>-</td></tr>
<tr data-domain="SW"><td>134<span class="domain-badge sw">SW</span></td><td>관리</td><td>4</td><td>1</td><td>리스크 대응 계획 수립</td><td>-</td></tr>
<tr data-domain="SW"><td>134<span class="domain-badge sw">SW</span></td><td>관리</td><td>4</td><td>5</td><td>클라우드 전환 사업 감리 방법</td><td>-</td></tr>
<tr data-domain="SW"><td>134<span class="domain-badge sw">SW</span></td><td>컴시응</td><td>1</td><td>9</td><td>플랫폼 엔지니어링(Platform Engineering)</td><td>-</td></tr>
<tr data-domain="SW"><td>134<span class="domain-badge sw">SW</span></td><td>컴시응</td><td>1</td><td>11</td><td>애자일(Agile) 장점 및 단점</td><td>-</td></tr>
<tr data-domain="SW"><td>134<span class="domain-badge sw">SW</span></td><td>컴시응</td><td>1</td><td>13</td><td>소프트웨어 품질성능 평가시험</td><td>-</td></tr>
<tr data-domain="SW"><td>134<span class="domain-badge sw">SW</span></td><td>컴시응</td><td>3</td><td>2</td><td>지능정보기술 감리 실무 가이드</td><td>-</td></tr>
<tr data-domain="SW"><td>134<span class="domain-badge sw">SW</span></td><td>컴시응</td><td>4</td><td>1</td><td>소프트웨어 프로세스(SP) 품질인증 운영 지침</td><td>-</td></tr>
<tr data-domain="SW"><td>134<span class="domain-badge sw">SW</span></td><td>컴시응</td><td>4</td><td>2</td><td>ISO 26262와 ASIL</td><td>-</td></tr>
<!-- 133회 -->
<tr data-domain="SW"><td>133<span class="domain-badge sw">SW</span></td><td>관리</td><td>1</td><td>2</td><td>뮤테이션 테스트(Mutation Test)</td><td>-</td></tr>
<tr data-domain="SW"><td>133<span class="domain-badge sw">SW</span></td><td>관리</td><td>1</td><td>11</td><td>유지보수 향상 및 비용절감을 위한 3R</td><td>-</td></tr>
<tr data-domain="SW"><td>133<span class="domain-badge sw">SW</span></td><td>관리</td><td>2</td><td>1</td><td>정보시스템 하드웨어 규모산정 지침</td><td>-</td></tr>
<tr data-domain="SW"><td>133<span class="domain-badge sw">SW</span></td><td>관리</td><td>3</td><td>5</td><td>요구공학(Requirement Engineering)</td><td>-</td></tr>
<tr data-domain="SW"><td>133<span class="domain-badge sw">SW</span></td><td>관리</td><td>4</td><td>2</td><td>신뢰성 테스트와 이식성 테스트</td><td>-</td></tr>
<!-- 132회 -->
<tr data-domain="SW"><td>132<span class="domain-badge sw">SW</span></td><td>관리</td><td>1</td><td>1</td><td>ISO 31000</td><td>-</td></tr>
<tr data-domain="SW"><td>132<span class="domain-badge sw">SW</span></td><td>관리</td><td>1</td><td>9</td><td>좋은 소프트웨어가 갖추어야 할 4가지 특징</td><td>-</td></tr>
<tr data-domain="SW"><td>132<span class="domain-badge sw">SW</span></td><td>관리</td><td>2</td><td>3</td><td>소프트웨어 기술자 등급제와 IT직무제</td><td>-</td></tr>
<tr data-domain="SW"><td>132<span class="domain-badge sw">SW</span></td><td>관리</td><td>3</td><td>1</td><td>SW 운영단계 대가산정</td><td>-</td></tr>
<tr data-domain="SW"><td>132<span class="domain-badge sw">SW</span></td><td>관리</td><td>3</td><td>6</td><td>정보시스템 성능 요구사항 주요 성능지표</td><td>-</td></tr>
<tr data-domain="SW"><td>132<span class="domain-badge sw">SW</span></td><td>관리</td><td>4</td><td>4</td><td>소프트웨어 진흥법</td><td>-</td></tr>
<tr data-domain="SW"><td>132<span class="domain-badge sw">SW</span></td><td>관리</td><td>4</td><td>5</td><td>소프트웨어 규모 산정 방식 종류와 개선 방안</td><td>-</td></tr>
<tr data-domain="SW"><td>132<span class="domain-badge sw">SW</span></td><td>컴시응</td><td>1</td><td>3</td><td>Canary Test</td><td>-</td></tr>
<tr data-domain="SW"><td>132<span class="domain-badge sw">SW</span></td><td>컴시응</td><td>1</td><td>6</td><td>소프트웨어 기술성 평가기준 지침</td><td>-</td></tr>
<tr data-domain="SW"><td>132<span class="domain-badge sw">SW</span></td><td>컴시응</td><td>1</td><td>7</td><td>전자정부사업관리 위탁(PMO)</td><td>-</td></tr>
<tr data-domain="SW"><td>132<span class="domain-badge sw">SW</span></td><td>컴시응</td><td>2</td><td>4</td><td>이동형 로봇 대인 충돌 안전성 평가</td><td>-</td></tr>
<tr data-domain="SW"><td>132<span class="domain-badge sw">SW</span></td><td>컴시응</td><td>2</td><td>5</td><td>ISMP, EA, ISP 비교</td><td>-</td></tr>
<tr data-domain="SW"><td>132<span class="domain-badge sw">SW</span></td><td>컴시응</td><td>3</td><td>5</td><td>객체 지향 SOLID 원칙</td><td>-</td></tr>
<tr data-domain="SW"><td>132<span class="domain-badge sw">SW</span></td><td>컴시응</td><td>3</td><td>6</td><td><a href="{{ site.baseurl }}/docs/sw/exam/132-3-6-sw-impact-assessment">소프트웨어 영향평가</a></td><td><code>(대상) 국지공정과정출지</code> <code>(체계) 목기방절</code></td></tr>
<tr data-domain="SW"><td>132<span class="domain-badge sw">SW</span></td><td>컴시응</td><td>4</td><td>2</td><td>클라우드 서비스 활용사업 감리 점검</td><td>-</td></tr>
<!-- 131회 -->
<tr data-domain="SW"><td>131<span class="domain-badge sw">SW</span></td><td>관리</td><td>1</td><td>3</td><td>폭포수 vs 애자일 개발 방법론</td><td>-</td></tr>
<tr data-domain="SW"><td>131<span class="domain-badge sw">SW</span></td><td>관리</td><td>1</td><td>6</td><td>정보시스템 감리와 PMO 비교</td><td>-</td></tr>
<tr data-domain="SW"><td>131<span class="domain-badge sw">SW</span></td><td>관리</td><td>1</td><td>12</td><td>캡슐화(Encapsulation)와 정보은닉</td><td>-</td></tr>
<tr data-domain="SW"><td>131<span class="domain-badge sw">SW</span></td><td>관리</td><td>2</td><td>6</td><td>아키텍처 스타일과 디자인 패턴</td><td>-</td></tr>
<tr data-domain="SW"><td>131<span class="domain-badge sw">SW</span></td><td>관리</td><td>3</td><td>3</td><td>통합테스트(Integration Test)</td><td>-</td></tr>
<tr data-domain="SW"><td>131<span class="domain-badge sw">SW</span></td><td>관리</td><td>3</td><td>4</td><td>안전성 분석 FTA, FMEA, HAZOP</td><td>-</td></tr>
<tr data-domain="SW"><td>131<span class="domain-badge sw">SW</span></td><td>관리</td><td>4</td><td>5</td><td>소프트웨어 규모산정</td><td>-</td></tr>
<tr data-domain="SW"><td>131<span class="domain-badge sw">SW</span></td><td>컴시응</td><td>1</td><td>5</td><td>ATAM과 CBAM</td><td>-</td></tr>
<tr data-domain="SW"><td>131<span class="domain-badge sw">SW</span></td><td>컴시응</td><td>2</td><td>3</td><td>데이터베이스 용량산정</td><td>-</td></tr>
<tr data-domain="SW"><td>131<span class="domain-badge sw">SW</span></td><td>컴시응</td><td>3</td><td>6</td><td>DataOps와 DevOps 비교</td><td>-</td></tr>
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

// 모달 기능
$('#examTable tbody').on('click', 'td:nth-child(5)', function() {
  var row = $(this).closest('tr');
  var data = table.row(row).data();
  
  // 메타 정보 추출
  var round = data[0].replace(/<[^>]+>/g, '').trim();
  var type = data[1];
  var period = data[2];
  var num = data[3];
  var question = $(this).text();
  var mnemonic = data[5];
  
  // 링크가 있는지 확인
  var link = $(this).find('a').attr('href');
  
  // 모달 제목
  $('#modalTitle').text(round + '회 ' + type + ' ' + period + '교시 ' + num + '번');
  
  // 문제 내용
  $('#modalQuestion').text(question);
  
  // 메타 정보
  var metaHtml = '<strong>암기법:</strong> ' + (mnemonic !== '-' ? mnemonic : '없음');
  $('#modalMeta').html(metaHtml);
  
  // 학습 페이지 링크
  if (link) {
    $('#modalLink').attr('href', link).show();
  } else {
    $('#modalLink').hide();
  }
  
  // 모달 표시
  $('#questionModal').addClass('show');
});

function closeModal() {
  $('#questionModal').removeClass('show');
}

// 모달 외부 클릭 시 닫기
$('#questionModal').on('click', function(e) {
  if (e.target === this) {
    closeModal();
  }
});

// ESC 키로 모달 닫기
$(document).keyup(function(e) {
  if (e.key === 'Escape') {
    closeModal();
  }
});
</script>
