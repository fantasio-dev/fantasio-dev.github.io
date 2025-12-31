---
layout: default
title: 📝 통합 기출문제
nav_order: 97
has_toc: false
permalink: /docs/exam
---

<!-- DataTables CSS -->
<link rel="stylesheet" href="https://cdn.datatables.net/1.13.7/css/jquery.dataTables.min.css">
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

/* 필터 섹션 */
.filter-section {
  background: #f8f9fa;
  border-radius: 12px;
  padding: 1.5rem;
  margin-bottom: 1.5rem;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
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

/* 통계 */
.stats-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
  padding: 0.8rem 1rem;
  background: #fff;
  border-radius: 8px;
  box-shadow: 0 1px 4px rgba(0,0,0,0.08);
}
.stats-bar .count {
  font-size: 1rem;
}
.stats-bar .count strong {
  color: #4A90D9;
  font-size: 1.2rem;
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
/* 회차, 영역, 정/컴, 교시, 번호 컬럼 */
#examTable td:nth-child(1),
#examTable td:nth-child(2),
#examTable td:nth-child(3),
#examTable td:nth-child(4),
#examTable td:nth-child(5),
#examTable th:nth-child(1),
#examTable th:nth-child(2),
#examTable th:nth-child(3),
#examTable th:nth-child(4),
#examTable th:nth-child(5) {
  width: 1%;
  white-space: nowrap;
  text-align: center;
  padding: 0.2rem 0.4rem;
  font-size: 0.8rem;
}
/* 문제 컬럼 */
#examTable td:nth-child(6) {
  white-space: normal;
  min-width: 300px;
}
/* 관련토픽 컬럼 */
#examTable td:nth-child(7) {
  white-space: nowrap;
  width: 1%;
}
/* 암기법 컬럼 */
#examTable td:nth-child(8),
#examTable th:nth-child(8) {
  font-family: 'Consolas', 'Monaco', monospace;
  font-size: 0.8rem;
  color: #d63384;
  min-width: 180px;
  white-space: nowrap;
}

/* 페이지 있는 행 */
tr.has-page td:nth-child(6) a {
  color: #0d6efd;
  font-weight: 500;
}
tr.has-page {
  background-color: #f0f7ff !important;
}

/* 영역 뱃지 */
.domain-badge {
  display: inline-block;
  padding: 0.2rem 0.5rem;
  border-radius: 4px;
  font-size: 0.75rem;
  font-weight: 600;
  color: #fff;
}
.domain-badge.sw { background: #28a745; }
.domain-badge.ai { background: #6f42c1; }
.domain-badge.sec { background: #dc3545; }
.domain-badge.ds { background: #17a2b8; }
.domain-badge.nw { background: #fd7e14; }
.domain-badge.db { background: #20c997; }
.domain-badge.caos { background: #e83e8c; }
.domain-badge.biz { background: #ffc107; color: #856404; }
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

<div class="stats-bar">
  <div class="count">총 <strong id="totalCount">0</strong>개의 문제가 검색되었습니다</div>
  <div class="sort">정렬: 최신순</div>
</div>

---

<table id="examTable" class="display" style="width:100%">
<thead>
<tr>
<th>회차</th>
<th>영역</th>
<th>정/컴</th>
<th>교시</th>
<th>번호</th>
<th>문제</th>
<th>관련토픽</th>
<th>암기법</th>
</tr>
</thead>
<tbody>
<!-- SW 영역 기출문제 -->
<tr class="has-page"><td>137</td><td><span class="domain-badge sw">SW</span></td><td>관리</td><td>1</td><td>11</td><td><a href="{{ site.baseurl }}/docs/sw/exam/137-1-11-reverse-reengineering">소프트웨어 역공학과 재공학을 설명하시오.</a></td><td>역공학, 재공학</td><td><code>(역공학) 추분문논</code> <code>(재공학) 역재구모</code></td></tr>
<tr class="has-page"><td>137</td><td><span class="domain-badge sw">SW</span></td><td>관리</td><td>3</td><td>2</td><td><a href="{{ site.baseurl }}/docs/sw/exam/137-3-2-is-om-audit">정보시스템 감리의 시스템 운영 및 유지보수 감리에 대하여 다음을 설명하시오.</a></td><td>감리, 유지보수</td><td><code>(운영감리) 릴테장/신서서</code> <code>(유지보수) 개상인</code></td></tr>
<tr class="has-page"><td>136</td><td><span class="domain-badge sw">SW</span></td><td>관리</td><td>4</td><td>3</td><td><a href="{{ site.baseurl }}/docs/sw/exam/136-4-3-sw-expert-evaluation">대규모 중요 소프트웨어 사업 평가의 전문성을 높이고 수요기관의 전문성을 보완해 공정한 경쟁을 유도하기 위하여 '조달청 협상에 의한 계약 제안서평가 세부기준'이 2024년 9월 개정 시행되었다.</a></td><td>제안서평가, 전문평가제도</td><td><code>(개정내용) 전평확평</code> <code>(전문평가) 목대대평</code></td></tr>
<tr class="has-page"><td>135</td><td><span class="domain-badge sw">SW</span></td><td>관리</td><td>2</td><td>2</td><td><a href="{{ site.baseurl }}/docs/sw/exam/135-2-2-cicd-devsecops">CI/CD 파이프라인에서 DevSecOps 적용방안에 대하여 설명하시오.</a></td><td>CI/CD, DevSecOps</td><td><code>(구성) 버CI빌테코배모</code> <code>(적용) 초자컨배피문</code></td></tr>
<tr class="has-page"><td>135</td><td><span class="domain-badge sw">SW</span></td><td>관리</td><td>3</td><td>1</td><td><a href="{{ site.baseurl }}/docs/sw/exam/135-3-1-project-management">프로젝트 관리에 대하여 다음을 설명하시오.</a></td><td>프로젝트 관리</td><td><code>(프로세스) 착계실감종</code> <code>(지식영역) 통이범자시원리품조의</code></td></tr>

<!-- AI 영역 기출문제 (샘플) -->
<tr><td>137</td><td><span class="domain-badge ai">AI</span></td><td>관리</td><td>1</td><td>1</td><td>PR(Precision Recall) 곡선과 ROC 곡선 비교</td><td>PR곡선, ROC</td><td>-</td></tr>
<tr><td>137</td><td><span class="domain-badge ai">AI</span></td><td>관리</td><td>1</td><td>2</td><td>Multimodal LLM(Large Language Model)</td><td>LLM, Multimodal</td><td>-</td></tr>

<!-- SEC 영역 기출문제 (샘플) -->
<tr><td>137</td><td><span class="domain-badge sec">SEC</span></td><td>관리</td><td>1</td><td>5</td><td>SIEM(Security Information & Event Management) & SOAR 비교</td><td>SIEM, SOAR</td><td>-</td></tr>

<!-- DS 영역 기출문제 (샘플) -->
<tr><td>137</td><td><span class="domain-badge ds">DS</span></td><td>관리</td><td>1</td><td>4</td><td>IBN(Intent-Based Networking)</td><td>IBN, SDN</td><td>-</td></tr>

</tbody>
</table>

---

## 📊 영역별 기출문제 바로가기

| 영역 | 페이지 | 문제 수 |
|:-----|:------|:--------|
| **SW** | [SW 기출문제]({{ site.baseurl }}/docs/sw/exam) | - |
| **AI** | [AI 기출문제]({{ site.baseurl }}/docs/ai/exam) | - |
| **SEC** | [SEC 기출문제]({{ site.baseurl }}/docs/sec/exam) | - |
| **DS** | [DS 기출문제]({{ site.baseurl }}/docs/ds/exam) | - |
| **NW** | [NW 기출문제]({{ site.baseurl }}/docs/nw/exam) | - |
| **DB** | [DB 기출문제]({{ site.baseurl }}/docs/db/exam) | - |
| **CAOS** | [CAOS 기출문제]({{ site.baseurl }}/docs/caos/exam) | - |
| **BIZ** | [BIZ 기출문제]({{ site.baseurl }}/docs/biz/exam) | - |

<!-- DataTables JS -->
<script src="https://code.jquery.com/jquery-3.7.0.min.js"></script>
<script src="https://cdn.datatables.net/1.13.7/js/jquery.dataTables.min.js"></script>

<script>
var table;
var currentDomain = 'all';

$(document).ready(function() {
  table = $('#examTable').DataTable({
    order: [[0, 'desc'], [3, 'asc'], [4, 'asc']],
    pageLength: 25,
    lengthMenu: [[10, 25, 50, 100, -1], [10, 25, 50, 100, "전체"]],
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
      { targets: [0, 2, 3, 4], className: 'dt-center' }
    ],
    initComplete: function() {
      updateCount();
    }
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
  
  // 영역 필터
  if (currentDomain === 'all') {
    table.column(1).search('');
  } else {
    table.column(1).search(currentDomain);
  }
  
  // 교시 필터
  table.column(3).search(classVal);
  
  // 회차 필터
  table.column(0).search(roundVal);
  
  // 키워드 검색 (문제 컬럼)
  table.column(5).search(keyword);
  
  table.draw();
  updateCount();
}

function resetFilters() {
  $('#filterClass').val('');
  $('#filterRound').val('');
  $('#filterKeyword').val('');
  $('.domain-btn').removeClass('active');
  $('.domain-btn[data-domain="all"]').addClass('active');
  currentDomain = 'all';
  
  table.search('').columns().search('').draw();
  updateCount();
}

function updateCount() {
  var count = table.rows({ filter: 'applied' }).count();
  $('#totalCount').text(count.toLocaleString());
}
</script>

