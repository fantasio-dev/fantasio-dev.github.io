---
layout: default
title: 📝 기출문제
parent: DB (데이터베이스)
has_children: true
has_toc: false
nav_order: 99
permalink: /docs/db/exam
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

# DB 기출문제
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
<tr><td>137</td><td>관리</td><td>1</td><td>10</td><td>데이터 늪(Data Swamp)을 설명하시오.</td><td>빅데이터, Data Lake</td><td>-</td></tr>
<tr><td>137</td><td>관리</td><td>1</td><td>13</td><td>데이터마이닝의 연관 규칙 분석(Association Rule Analysis) 지표를 설명하시오.</td><td>Data Mining</td><td>-</td></tr>
<tr><td>137</td><td>관리</td><td>3</td><td>4</td><td>데이터베이스 트랜잭션 격리 수준(Transactional Isolation Level)과 관련하여 아래 사항을 설명하시오. 가. 데이터베이스 트랜잭션 격리수준 4가지 나. 데이터베이스 트랜잭션 격리 수준에 따라 발생할 수 있는 이상 현상</td><td>트랜잭션, 격리수준</td><td>-</td></tr>
<tr><td>137</td><td>관리</td><td>4</td><td>2</td><td>벡터 데이터베이스(Vector Database)의 효율적 검색을 위한 HNSW(Hierarchical Navigable Small World)와 IVF(Inverted File Index)의 동작원리를 설명하시오.</td><td>벡터DB, HNSW, IVF</td><td>-</td></tr>
<!-- 136회 -->
<tr><td>136</td><td>관리</td><td>1</td><td>4</td><td>제 4 정규형</td><td>정규화</td><td>-</td></tr>
<tr><td>136</td><td>관리</td><td>2</td><td>5</td><td>데이터베이스 인덱스(Index)를 설명하고, 클러스터드 인덱스(Clustered Index)와 논클러스터드 인덱스(Non-Clustered Index)를 비교하여 설명하시오.</td><td>인덱스</td><td>-</td></tr>
<!-- 135회 -->
<tr><td>135</td><td>관리</td><td>1</td><td>11</td><td>팬텀 충돌(Phantom Conflict)</td><td>동시성, 무결성</td><td>-</td></tr>
<tr><td>135</td><td>관리</td><td>2</td><td>1</td><td>물리 데이터 모델링 중 반정규화에 대하여 다음을 설명하시오. 가. 반정규화 절차 나. 반정규화 유형 다. 반정규화 시 고려사항</td><td>정규화, 반정규화</td><td>-</td></tr>
<tr><td>135</td><td>관리</td><td>3</td><td>5</td><td>데이터 거래를 위한 데이터 가치평가에 대하여 다음을 설명하시오. 가. 데이터 재화와 데이터 가치의 특징 나. 데이터 가치평가의 모델 및 절차 다. 데이터 가치평가의 활용방안</td><td>데이터 가치평가</td><td>-</td></tr>
<tr><td>135</td><td>관리</td><td>4</td><td>2</td><td>릴레이션 무결성 제약의 유형과 사례를 제시하고, 구현 방법에 대하여 설명하시오.</td><td>무결성</td><td>-</td></tr>
<tr><td>135</td><td>관리</td><td>4</td><td>4</td><td>빅데이터 시각화(Visualization)에 대하여 다음을 설명하시오. 가. 개념 및 절차 나. 방법 및 도구</td><td>빅데이터, 시각화</td><td>-</td></tr>
<tr><td>135</td><td>컴시응</td><td>1</td><td>10</td><td>공공데이터 품질인증</td><td>데이터 품질</td><td>-</td></tr>
<tr><td>135</td><td>컴시응</td><td>2</td><td>6</td><td>데이터베이스 트랜잭션 회복(Recovery) 기법에 대하여 아래 사항을 설명하시오. 가. REDO와 UNDO를 이용한 방법 나. 체크포인트(Checkpoint)를 이용한 방법 다. 그림자 페이징(Shadow Paging)을 이용한 방법</td><td>회복, REDO, UNDO</td><td>-</td></tr>
<!-- 134회 -->
<tr><td>134</td><td>관리</td><td>1</td><td>7</td><td>정적 SQL(Static SQL)과 동적 SQL(Dynamic SQL) 비교</td><td>SQL</td><td>-</td></tr>
<tr><td>134</td><td>관리</td><td>2</td><td>6</td><td>트랜잭션 격리 수준(Transaction Isolation Level) 4가지를 사례 중심으로 설명하시오.</td><td>트랜잭션, 격리수준</td><td>-</td></tr>
<tr><td>134</td><td>관리</td><td>3</td><td>5</td><td>다차원 색인구조(Multidimensional Index Structure)의 개념, 유형, 활용 사례에 대하여 설명하시오.</td><td>인덱스, R-Tree</td><td>-</td></tr>
<tr><td>134</td><td>컴시응</td><td>3</td><td>4</td><td>데이터베이스 무결성 제약 조건에 대하여 다음을 설명하시오. 가. 데이터베이스 무결성 제약 조건의 개념 나. 데이터베이스 무결성 제약 조건의 종류 다. 데이터베이스 무결성 제약 조건 생성 시 고려사항</td><td>무결성</td><td>-</td></tr>
<!-- 133회 -->
<tr><td>133</td><td>관리</td><td>1</td><td>3</td><td>NoSQL 유형과 모델링 절차를 설명하시오.</td><td>NoSQL</td><td>-</td></tr>
<tr><td>133</td><td>관리</td><td>1</td><td>7</td><td>데이터모델링에서 CRUD 매트릭스(Matrix)를 사용하는 목적과 이를 표현하는 방법에 대하여 설명하시오.</td><td>CRUD 매트릭스</td><td>-</td></tr>
<tr><td>133</td><td>관리</td><td>2</td><td>6</td><td>데이터 안심구역의 정의, 기능, 지정요건에 대하여 설명하시오.</td><td>데이터 안심구역</td><td>-</td></tr>
<tr><td>133</td><td>관리</td><td>4</td><td>4</td><td>DBMS를 적용하기 위한 데이터 모델링에 대하여 다음을 설명하시오. 가. 데이터 모델링의 개념 및 모델링 단계별 수행내용 나. 데이터 관계 모델링 시 식별(Identification)과 비식별(Non-Identification)에 대하여 비교 다. 데이터 모델링 시 고려사항</td><td>데이터 모델링</td><td>-</td></tr>
<!-- 132회 -->
<tr><td>132</td><td>관리</td><td>1</td><td>2</td><td>데이터 거래소</td><td>빅데이터</td><td>-</td></tr>
<tr><td>132</td><td>관리</td><td>1</td><td>7</td><td>ELK(Elasticsearch/Logstash/Kibana) 스택</td><td>빅데이터, ELK</td><td>-</td></tr>
<tr><td>132</td><td>관리</td><td>1</td><td>13</td><td>분산 데이터베이스 5가지 투명성</td><td>분산 DB</td><td>-</td></tr>
<tr><td>132</td><td>관리</td><td>4</td><td>2</td><td>행정안전부에서는 고품질의 공공데이터 제공 및 활용의 선제적 대응을 위해 '공공데이터베이스 표준화 관리 매뉴얼(2023.04.)'을 마련하여 예방적 품질관리 기준을 제시하고 있다. 이와 관련하여 다음을 설명하시오. 가. 시스템 구축 추진 단계별 예방적 품질관리 활동 나. 공공데이터 예방적 품질관리 4개 진단영역과 9개 진단항목</td><td>데이터 품질</td><td>-</td></tr>
<!-- 131회 -->
<tr><td>131</td><td>관리</td><td>1</td><td>11</td><td>데이터 표준화의 필요성과 기대효과</td><td>데이터 품질</td><td>-</td></tr>
<tr><td>131</td><td>관리</td><td>2</td><td>2</td><td>데이터 시각화(Data Visualization)와 관련하여 다음을 설명하시오. 가. 데이터 시각화의 개요 나. 데이터 시각화의 원리 및 절차 다. 데이터 시각화 유형 라. 효과적인 데이터 시각화를 위한 효율화 방안</td><td>시각화</td><td>-</td></tr>
<tr><td>131</td><td>관리</td><td>4</td><td>3</td><td>데이터 품질관리에 대하여 다음을 설명하시오. 가. 데이터 품질관리 아키텍처 나. 데이터 품질관리 성숙도 다. 정형 데이터 및 비정형 데이터 품질기준 라. 데이터 품질관리 전략</td><td>데이터 품질</td><td>-</td></tr>
<tr><td>131</td><td>컴시응</td><td>1</td><td>7</td><td>NoSQL의 CAP(Consistency, Availability, Partition Tolerance)</td><td>NoSQL, CAP</td><td>-</td></tr>
<tr><td>131</td><td>컴시응</td><td>3</td><td>4</td><td>데이터베이스에 사용되는 트랜잭션의 개념과 이를 정의하는 4가지 중요한 속성을 가리키는 ACID의 각 요소에 대하여 설명하시오.</td><td>트랜잭션, ACID</td><td>-</td></tr>
<tr><td>131</td><td>컴시응</td><td>4</td><td>2</td><td>추천시스템은 사용자의 과거 행동데이터 등을 바탕으로 사용자가 좋아할 만한 정보나 제품을 제시해 주는 시스템이다. 이와 관련하여 다음을 설명하시오. 가. 컨텐츠 기반 필터링(Content-based Filtering)과 협업적 필터링(Collaborative Filtering) 기법 나. 행렬분해(Matrix Factorization) 기반 협업적 필터링</td><td>추천시스템, 협업 필터링</td><td>-</td></tr>
</tbody>
</table>

---

## 💡 사용 팁

- **검색**: 상단 검색창에 키워드 입력 (예: "트랜잭션", "정규화", "1교시")
- **정렬**: 각 컬럼 헤더 클릭하여 오름차순/내림차순 정렬
- **필터**: 빠른 필터 버튼으로 교시별, 학습페이지 유무 등 필터링

---

## 📊 통계

| 회차 | 문제 수 |
|:----:|:-------:|
| 137회 | 4개 |
| 136회 | 2개 |
| 135회 | 7개 |
| 134회 | 4개 |
| 133회 | 5개 |
| 132회 | 4개 |
| 131회 | 6개 |
| **합계** | **32개** |

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

