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

# SW공학 기출문제
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
<tr class="has-page has-mnemonic"><td>138</td><td>관리</td><td>2</td><td>6</td><td><a href="{{ site.baseurl }}/docs/sw/exam/138-2-6-sw-cost-estimation">SW 비용산정 및 대가산정 가이드</a></td><td>FP, 대가산정</td><td><code>(산정) 유범이의데이트</code></td></tr>
<!-- 137회 -->
<tr class="has-page has-mnemonic"><td>137</td><td>관리</td><td>1</td><td>6</td><td><a href="{{ site.baseurl }}/docs/sw/exam/137-1-6-sil-hil-testing">SIL/HIL 테스팅</a></td><td>임베디드 테스트</td><td><code>(테스트) 모소하</code></td></tr>
<tr class="has-page has-mnemonic"><td>137</td><td>관리</td><td>1</td><td>11</td><td><a href="{{ site.baseurl }}/docs/sw/exam/137-1-11-reverse-reengineering">역공학과 재공학</a></td><td>유지보수</td><td><code>(역공학) 추분문논</code> <code>(재공학) 역재구모</code></td></tr>
<tr class="has-page has-mnemonic"><td>137</td><td>관리</td><td>2</td><td>5</td><td><a href="{{ site.baseurl }}/docs/sw/exam/137-2-5-sw-impact-assessment">SW 영향평가</a></td><td>공공SW</td><td><code>(절차) 사검민필종</code></td></tr>
<tr class="has-page has-mnemonic"><td>137</td><td>컴시응</td><td>2</td><td>5</td><td><a href="{{ site.baseurl }}/docs/sw/exam/137-2-5-dynamic-testing">동적 테스팅</a></td><td>SW테스트</td><td><code>(명세) 블동경의상</code> <code>(구조) 화제루커</code></td></tr>
<tr class="has-page has-mnemonic"><td>137</td><td>관리</td><td>3</td><td>2</td><td><a href="{{ site.baseurl }}/docs/sw/exam/137-3-2-is-om-audit">정보시스템 운영관리 감리</a></td><td>감리</td><td><code>(점검) 기현관업</code></td></tr>
<tr class="has-page has-mnemonic"><td>137</td><td>관리</td><td>4</td><td>4</td><td><a href="{{ site.baseurl }}/docs/sw/exam/137-4-4-uml-behavior-diagram">UML 행위 다이어그램</a></td><td>UML</td><td><code>(행위) USA I SCIT</code></td></tr>
<!-- 136회 -->
<tr class="has-page has-mnemonic"><td>136</td><td>관리</td><td>1</td><td>5</td><td><a href="{{ site.baseurl }}/docs/sw/exam/136-1-5-proxy-design-pattern">프록시(Proxy) 디자인 패턴</a></td><td>디자인패턴</td><td><code>(패턴) 주실대요</code> <code>(유형) 가보원스</code></td></tr>
<tr class="has-page has-mnemonic"><td>136</td><td>관리</td><td>1</td><td>6</td><td><a href="{{ site.baseurl }}/docs/sw/exam/136-1-6-devops-pros-cons">DevOps 장점과 단점</a></td><td>DevOps</td><td><code>(장점) 품프도</code></td></tr>
<tr class="has-page has-mnemonic"><td>136</td><td>관리</td><td>2</td><td>2</td><td><a href="{{ site.baseurl }}/docs/sw/exam/136-2-2-pmo-audit">PMO 기반 감리</a></td><td>감리</td><td><code>(역할) 관통계품</code></td></tr>
<tr class="has-page has-mnemonic"><td>136</td><td>관리</td><td>2</td><td>4</td><td><a href="{{ site.baseurl }}/docs/sw/exam/136-2-4-product-line">소프트웨어 프로덕트 라인</a></td><td>재사용</td><td><code>(절차) 도에코 프리인</code></td></tr>
<tr class="has-page has-mnemonic"><td>136</td><td>관리</td><td>3</td><td>1</td><td><a href="{{ site.baseurl }}/docs/sw/exam/136-3-1-conflict-tuckman">프로젝트 갈등 관리와 터크만 모델</a></td><td>PM</td><td><code>(터크만) 포스노퍼어</code></td></tr>
<tr class="has-page has-mnemonic"><td>136</td><td>관리</td><td>3</td><td>3</td><td><a href="{{ site.baseurl }}/docs/sw/exam/136-3-3-software-quality-assurance">소프트웨어 품질보증(SQA)</a></td><td>품질</td><td><code>(활동) 검감기분</code></td></tr>
<tr class="has-page has-mnemonic"><td>136</td><td>관리</td><td>4</td><td>3</td><td><a href="{{ site.baseurl }}/docs/sw/exam/136-4-3-sw-expert-evaluation">SW 전문가 평가제도</a></td><td>공공SW</td><td><code>(평가) 기보데디</code></td></tr>
<!-- 135회 -->
<tr class="has-page has-mnemonic"><td>135</td><td>관리</td><td>1</td><td>3</td><td><a href="{{ site.baseurl }}/docs/sw/exam/135-1-3-requirement-traceability-matrix">요구사항 추적 매트릭스(RTM)</a></td><td>요구사항</td><td><code>(구성) 요설테프배</code></td></tr>
<tr class="has-page has-mnemonic"><td>135</td><td>관리</td><td>1</td><td>5</td><td><a href="{{ site.baseurl }}/docs/sw/exam/135-1-5-monolithic-vs-microservice">모놀리식 vs 마이크로서비스</a></td><td>아키텍처</td><td><code>(비교) 개목특기요</code></td></tr>
<tr class="has-page has-mnemonic"><td>135</td><td>관리</td><td>1</td><td>8</td><td><a href="{{ site.baseurl }}/docs/sw/exam/135-1-8-hw-sizing-methods">H/W 규모산정 방법</a></td><td>비용산정</td><td><code>(방법) 수참시</code></td></tr>
<tr class="has-page has-mnemonic"><td>135</td><td>관리</td><td>1</td><td>9</td><td><a href="{{ site.baseurl }}/docs/sw/exam/135-1-9-technical-debt">기술 부채(Technical Debt)</a></td><td>유지보수</td><td><code>(유형) 의우설코</code></td></tr>
<tr class="has-page has-mnemonic"><td>135</td><td>관리</td><td>2</td><td>2</td><td><a href="{{ site.baseurl }}/docs/sw/exam/135-2-2-cicd-devsecops">CI/CD와 DevSecOps</a></td><td>DevOps</td><td><code>(CI/CD) 빌통배</code> <code>(DevSecOps) 시위보감</code></td></tr>
<tr class="has-page has-mnemonic"><td>135</td><td>관리</td><td>3</td><td>1</td><td><a href="{{ site.baseurl }}/docs/sw/exam/135-3-1-project-management">프로젝트 관리</a></td><td>PM</td><td><code>(지식영역) 통범일원품인의리이</code></td></tr>
<tr class="has-page has-mnemonic"><td>135</td><td>관리</td><td>4</td><td>4</td><td><a href="{{ site.baseurl }}/docs/sw/exam/135-4-4-zero-downtime-deployment">무중단 배포</a></td><td>DevOps</td><td><code>(전략) 롤블카</code></td></tr>
<!-- 134회 -->
<tr class="has-page has-mnemonic"><td>134</td><td>관리</td><td>1</td><td>1</td><td><a href="{{ site.baseurl }}/docs/sw/exam/134-1-1-tuckman-ladder-model">터크만 사다리 모델</a></td><td>PM</td><td><code>(단계) 포스노퍼어</code></td></tr>
<tr class="has-page has-mnemonic"><td>134</td><td>관리</td><td>1</td><td>5</td><td><a href="{{ site.baseurl }}/docs/sw/exam/134-1-5-information-hiding">정보은닉</a></td><td>OOP</td><td><code>(기법) PPPD</code></td></tr>
<tr class="has-page has-mnemonic"><td>134</td><td>관리</td><td>1</td><td>9</td><td><a href="{{ site.baseurl }}/docs/sw/exam/134-1-9-platform-engineering">플랫폼 엔지니어링</a></td><td>DevOps</td><td><code>(구성) IDP-포셀골</code></td></tr>
<tr class="has-page has-mnemonic"><td>134</td><td>관리</td><td>1</td><td>11</td><td><a href="{{ site.baseurl }}/docs/sw/exam/134-1-11-agile-pros-cons">애자일 장단점</a></td><td>방법론</td><td><code>(장점) 빠유효협</code></td></tr>
<tr class="has-page has-mnemonic"><td>134</td><td>관리</td><td>1</td><td>13</td><td><a href="{{ site.baseurl }}/docs/sw/exam/134-1-13-sw-quality-performance-test">SW 품질 성능 테스트</a></td><td>테스트</td><td><code>(지표) 처시사</code></td></tr>
</tbody>
</table>

---

## 💡 사용 팁

- **검색**: 상단 검색창에 키워드 입력 (예: "DevOps", "UML", "1교시")
- **정렬**: 각 컬럼 헤더 클릭하여 오름차순/내림차순 정렬
- **필터**: 빠른 필터 버튼으로 교시별, 학습페이지 유무 등 필터링

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

