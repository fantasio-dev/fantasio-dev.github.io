---
layout: default
title: 📝 기출문제
parent: BIZ (경영)
has_children: true
has_toc: false
nav_order: 99
permalink: /docs/biz/exam
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

# BIZ 기출문제
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
<!-- 137회 -->
<tr><td>137</td><td>관리</td><td>2</td><td>2</td><td>(A)기업은 전자상거래 정보시스템 개발 프로젝트를 완료하고 운영으로 전환하고자 한다. 각 항목을 설명하시오. 가. SLA(Service Level Agreement) 구성요소와 절차 나. (A)기업의 특성을 고려하여 하드웨어, 소프트웨어, 네트워크 영역별 SLA 평가지표와 측정방법에 대한 사례</td><td>SLA</td><td>-</td></tr>
<tr><td>137</td><td>관리</td><td>3</td><td>3</td><td>다중지역 동시 가동방식 (Multi-Region Active-Active) 재해복구시스템에 대하여 다음을 설명하시오. 가. 개념 및 특징 나. 주요 기술 요소</td><td>DRS</td><td>-</td></tr>
<tr><td>137</td><td>컴시응</td><td>1</td><td>4</td><td>IEEE 표준과 IEC 국제표준의 비교</td><td>표준</td><td>-</td></tr>
<!-- 136회 -->
<tr><td>136</td><td>관리</td><td>1</td><td>1</td><td>화이트 레이블 마케팅(White Label Marketing)</td><td>Growth Hacking</td><td>-</td></tr>
<tr><td>136</td><td>관리</td><td>2</td><td>1</td><td>공급망관리(SCM, Supply Chain Management)에 대하여 다음을 설명하시오. 가. 공급망관리의 정의와 배경 나. 공급망관리에서 효과성과 효율성</td><td>SCM, ERP</td><td>-</td></tr>
<!-- 134회 -->
<tr><td>134</td><td>관리</td><td>1</td><td>2</td><td>시장 규모 추정 방법인 TAM-SAM-SOM (Total Addressable Market-Serviceable Addressable Market-Serviceable Obtainable Market) 프레임워크</td><td>경영분석</td><td>-</td></tr>
<tr><td>134</td><td>관리</td><td>2</td><td>3</td><td>IT 거버넌스에 대하여 설명하시오. 가. IT 거버넌스의 구성요소 나. IT 거버넌스 효과 측정 지표 다. IT 거버넌스 효과 측정 방법론</td><td>IT Governance</td><td>-</td></tr>
<tr><td>134</td><td>관리</td><td>2</td><td>5</td><td>ESG(Environment, Social, Governance) 경영에 대하여 설명하시오. 가. ESG 경영의 정의 및 목표 나. ESG 경영의 주요 지표 다. ESG 경영 목표 달성을 지원하기 위한 정보기술(IT)</td><td>ESG</td><td>-</td></tr>
<tr><td>134</td><td>관리</td><td>4</td><td>6</td><td>군집분석 기법인 SOM(Self Organizing Map)에 대하여 설명하시오. 가. SOM 정의 및 특징 나. SOM 구성요소 다. SOM과 신경망 분석기법의 차이점</td><td>Data Mining, SOM</td><td>-</td></tr>
<tr><td>134</td><td>컴시응</td><td>1</td><td>12</td><td>전자정부 정보시스템 성과 측정지표</td><td>정보시스템 성과평가</td><td>-</td></tr>
<tr><td>134</td><td>컴시응</td><td>3</td><td>1</td><td>정보기술 아키텍처의 도입과 운영에 필요한 사항을 정하기 위한 "정보기술 아키텍처(EA: Enterprise Architecture) 도입·운영 지침"과 관련하여 다음을 설명하시오. 가. 범정부 정보기술 아키텍처 메타모델 나. 범정부 정보기술 아키텍처 참조모형의 종류 다. 범정부 정보기술 아키텍처 성숙도 모델</td><td>EA</td><td>-</td></tr>
<!-- 133회 -->
<tr><td>133</td><td>관리</td><td>1</td><td>6</td><td>기술수용모델(Technology Acceptance Model: TAM)의 개념과 주요 구성요소에 대하여 설명하시오.</td><td>TAM</td><td>-</td></tr>
<tr><td>133</td><td>관리</td><td>1</td><td>9</td><td>BCP(Business Continuity Planning) 수립 시의 주요 지표와 DRS(Disaster Recovery System) 구축 시의 핵심 고려사항에 대하여 설명하시오.</td><td>BCP, DRS</td><td>-</td></tr>
<tr><td>133</td><td>관리</td><td>2</td><td>3</td><td>ISO/IEC 20000에서 제시하는 기준을 중심으로, 정보기술 서비스 관리체계(ITSM)의 개념을 설명하고, 이 시스템의 서비스 설계 및 구축, 전환을 위한 활동에 대하여 설명하시오.</td><td>ITSM</td><td>-</td></tr>
<tr><td>133</td><td>관리</td><td>3</td><td>4</td><td>경영환경을 분석하는 방법인 SWOT(Strengths, Weaknesses, Opportunities, Threats), 3C(Customer, Competitor, Company), PEST(Political, Economical, Social, Technological) 분석에 대하여 각 방법의 특성과 적용을 위한 조건, 그리고 분석 방법에 대하여 설명하시오.</td><td>SWOT, 3C, PEST</td><td>-</td></tr>
<!-- 132회 -->
<tr><td>132</td><td>관리</td><td>2</td><td>2</td><td>머신러닝의 분류 모델인 서포트 벡터 머신(Support Vector Machine) 중 선형 서포트 벡터 머신의 마진(Margin) 분류 방법 2가지를 설명하시오.</td><td>SVM</td><td>-</td></tr>
<tr><td>132</td><td>관리</td><td>2</td><td>5</td><td>ISO 14000 인증의 개념과 필요성, 인증규격, 구축 및 인증절차, 인증효과를 설명하시오.</td><td>ISO 14000</td><td>-</td></tr>
<tr><td>132</td><td>컴시응</td><td>4</td><td>5</td><td>서포트 벡터 머신(Support Vector Machine)은 기계학습 분야에서 많이 활용되는 학습 모델이다. 아래 사항을 설명하시오. 가. SVM의 개념 나. SVM의 동작방식 다. SVM의 장단점 및 활용사례</td><td>SVM</td><td>-</td></tr>
<!-- 131회 -->
<tr><td>131</td><td>관리</td><td>1</td><td>1</td><td>디지털 트랜스포메이션(Digital Transformation)</td><td>DX</td><td>-</td></tr>
<tr><td>131</td><td>관리</td><td>2</td><td>1</td><td>ISP(Information Strategy Planning)과 BPR(Business Process Reengineering)의 개념과 수행절차를 비교 설명하고, 기업에서 이 두가지가 상호 보완적으로 활용하기 위한 방안을 설명하시오.</td><td>ISP, BPR</td><td>-</td></tr>
<tr><td>131</td><td>관리</td><td>4</td><td>1</td><td>전략적 기업경영(Strategic Enterprise Management)에 대하여 다음을 설명하시오. 가. 전략적 기업경영의 정의 나. 전략적 기업경영의 구성요소 다. 전략적 기업경영의 구축 방안 및 구축 절차</td><td>SEM, BI</td><td>-</td></tr>
<tr><td>131</td><td>컴시응</td><td>1</td><td>10</td><td>지능정보화 기본법</td><td>법률</td><td>-</td></tr>
</tbody>
</table>

---

## 💡 사용 팁

- **검색**: 상단 검색창에 키워드 입력 (예: "ESG", "BCP", "1교시")
- **정렬**: 각 컬럼 헤더 클릭하여 오름차순/내림차순 정렬
- **필터**: 빠른 필터 버튼으로 교시별, 학습페이지 유무 등 필터링

---

## 📊 통계

| 회차 | 문제 수 |
|:----:|:-------:|
| 137회 | 3개 |
| 136회 | 2개 |
| 134회 | 6개 |
| 133회 | 4개 |
| 132회 | 3개 |
| 131회 | 4개 |
| **합계** | **22개** |

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

