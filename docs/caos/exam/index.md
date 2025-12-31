---
layout: default
title: 📝 기출문제
parent: CAOS (컴퓨터구조/OS)
has_children: true
has_toc: false
nav_order: 99
permalink: /docs/caos/exam
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

# CAOS 기출문제
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
<tr><td>137</td><td>관리</td><td>2</td><td>1</td><td>캐시 메모리(Cache Memory)에 대하여 설명하시오. 가. 캐시 쓰기 정책(Write Policy) 나. 캐시 일관성(Cache Coherence) 문제의 원인과 해결 방법</td><td>Cache Memory</td><td>-</td></tr>
<tr><td>137</td><td>관리</td><td>3</td><td>1</td><td>운영체제 스케줄링 기법에 대한 각 내용을 설명하시오. 가. CPU 스케줄링과 디스크 스케줄링의 개념 나. SJF(Shortest Job First)와 SRT(Shortest Remaining Time) 다. SSTF(Short Seek Time First)와 SLTF(Shortest Latency Time First)</td><td>CPU Scheduling</td><td>-</td></tr>
<tr><td>137</td><td>컴시응</td><td>1</td><td>2</td><td>클라우드 AI와 온디바이스 AI의 개념 비교</td><td>프로세서, AI</td><td>-</td></tr>
<tr><td>137</td><td>컴시응</td><td>1</td><td>5</td><td>보안 운영체제(Secure OS)</td><td>Secure OS</td><td>-</td></tr>
<tr><td>137</td><td>컴시응</td><td>1</td><td>7</td><td>HBM(High Bandwidth Memory)</td><td>I/O, Memory</td><td>-</td></tr>
<tr><td>137</td><td>컴시응</td><td>1</td><td>10</td><td>GPU(Graphics Processing Unit)의 역할, 구조, 주요장점 및 활용분야</td><td>프로세서, GPU</td><td>-</td></tr>
<tr><td>137</td><td>컴시응</td><td>1</td><td>13</td><td>RISC-V</td><td>CISC, RISC</td><td>-</td></tr>
<tr><td>137</td><td>컴시응</td><td>2</td><td>3</td><td>운영체제의 기아현상(Starvation)에 대하여 다음 사항을 설명하시오. 가. 기아현상의 정의 및 발생조건 나. 기아현상의 해결방안 3가지 다. 교착상태와 기아현상의 비교</td><td>Deadlock, Starvation</td><td>-</td></tr>
<tr><td>137</td><td>컴시응</td><td>2</td><td>6</td><td>I/O(Input/Output) 장치와 메모리 사이에서 데이터를 직접 주고받기 위해서 사용하는 DMA(Direct Memory Access)에 대하여 다음 사항을 설명하시오. 가. Programmed I/O 방식과 DMA 방식 비교 나. Cycle Stealing Mode와 Transparent Mode 다. SG-DMA(Scatter-Gather DMA)와 RDMA(Remote DMA)</td><td>DMA, 인터럽트</td><td>-</td></tr>
<tr><td>137</td><td>컴시응</td><td>3</td><td>2</td><td>가상메모리 주소 변환을 위해 사용하는 MMU(Memory Management Unit)에 대하여 다음을 설명하시오. 가. MMU 구성요소 나. TLB(Translation Lookaside Buffer) 다. MMU와 IOMMU</td><td>Virtual Memory, MMU</td><td>-</td></tr>
<tr><td>137</td><td>컴시응</td><td>3</td><td>4</td><td>실시간 시스템에서 발생할 수 있는 우선순위 역전(Priority Inversion) 현상에 대하여 다음을 설명하시오. 가. 우선순위 역전 현상의 개념 및 발생원인 나. 우선순위 상속 프로토콜(PIP, Priority Inheritance Protocol)과 우선순위 상한 프로토콜(PCP, Priority Ceiling Protocols) 비교</td><td>CPU Scheduling</td><td>-</td></tr>
<tr><td>137</td><td>컴시응</td><td>3</td><td>6</td><td>시스템 버스(System Bus)와 버스 중재(Bus Arbitration) 방식을 설명하시오.</td><td>시스템 버스</td><td>-</td></tr>
<!-- 136회 -->
<tr><td>136</td><td>관리</td><td>1</td><td>7</td><td>세그먼테이션 오류(Segmentation Fault)</td><td>Virtual Memory</td><td>-</td></tr>
<tr><td>136</td><td>관리</td><td>1</td><td>8</td><td>CXL(Compute Express Link)</td><td>I/O</td><td>-</td></tr>
<tr><td>136</td><td>관리</td><td>3</td><td>6</td><td>메모리 관리 기법 중 동적 메모리 할당과 관련하여 다음을 설명하시오. 가. 동적 메모리 할당의 필요성 나. 메모리 누수(Memory Leak)로 인한 문제 다. 프로그래밍 언어(Java, Python 등)에서 지원하는 메모리 누수 해결방안</td><td>Virtual Memory</td><td>-</td></tr>
<tr><td>136</td><td>관리</td><td>4</td><td>2</td><td>프로세스 간 통신을 위해 사용되는 IPC(Inter Process Communication)에 대하여 다음을 설명하시오. 가. IPC의 개념과 목적 나. IPC 주요 기법 3가지 다. 공유 자원의 충돌이나 일관성 문제를 해결하기 위한 동기화 기법</td><td>프로세스, IPC</td><td>-</td></tr>
<!-- 135회 -->
<tr><td>135</td><td>컴시응</td><td>1</td><td>3</td><td>MMU(Memory Management Unit)</td><td>Virtual Memory, MMU</td><td>-</td></tr>
<tr><td>135</td><td>컴시응</td><td>1</td><td>11</td><td>운영체제(Operating System)에서 태스크 우선순위 상속(Priority Inheritance)</td><td>CPU Scheduling</td><td>-</td></tr>
<tr><td>135</td><td>컴시응</td><td>2</td><td>4</td><td>캐쉬 메모리(Cache Memory)에 대하여 아래 사항을 설명하시오. 가. 캐쉬 메모리(Cache Memory) 교체 기법 나. Write Through와 Write Back 비교 다. 캐쉬 일관성 유지를 위한 MESI 프로토콜</td><td>Cache Memory, MESI</td><td>-</td></tr>
<tr><td>135</td><td>컴시응</td><td>3</td><td>4</td><td>운영체제의 스케줄링 알고리즘에 대하여 아래 사항을 설명하시오. 가. RM(Rate Monotonic) 스케줄링 나. MLQ(Multi-Level Queue) 스케줄링 다. SQMS(Single Queue Multiprocessor Scheduling) 라. MQMS(Multi Queue Multiprocessor Scheduling)</td><td>CPU Scheduling</td><td>-</td></tr>
<tr><td>135</td><td>컴시응</td><td>4</td><td>5</td><td>고장허용(Fault Tolerant) 시스템과 고가용성(High Availability) 시스템에 대하여 아래 사항을 설명하시오. 가. 고장허용(Fault Tolerant)과 고가용성(High Availability) 시스템의 개념 나. 하드웨어, 소프트웨어, 데이터 측면에서 고장허용(Fault Tolerant) 기법 다. 고가용성(High Availability) 시스템의 구성 방법 라. 고장허용(Fault Tolerant) 시스템과 고가용성(High Availability) 시스템의 비교</td><td>FTS, HA</td><td>-</td></tr>
<tr><td>135</td><td>컴시응</td><td>4</td><td>6</td><td>파이프라인 해저드(Pipeline Hazard)에 대하여 아래 사항을 설명하시오. 가. 유형별 발생 원인 나. 해결 방법</td><td>Pipeline</td><td>-</td></tr>
<!-- 134회 -->
<tr><td>134</td><td>관리</td><td>1</td><td>12</td><td>고대역 초고속 메모리(High Bandwidth Memory)</td><td>HBM, Memory</td><td>-</td></tr>
<tr><td>134</td><td>관리</td><td>4</td><td>2</td><td>딥러닝에서 대규모 신경망을 효율적으로 훈련하기 위한 멀티 GPU 기술에 대하여 설명하시오. 가. 멀티 GPU 기술의 개념과 장점 나. 멀티 GPU 환경 구축 시 고려사항</td><td>GPU, 프로세서</td><td>-</td></tr>
<tr><td>134</td><td>컴시응</td><td>1</td><td>3</td><td>온디바이스 AI</td><td>프로세서, AI</td><td>-</td></tr>
<tr><td>134</td><td>컴시응</td><td>1</td><td>8</td><td>신경망 처리장치(NPU: Neural Processing Unit)</td><td>NPU, 프로세서</td><td>-</td></tr>
<tr><td>134</td><td>컴시응</td><td>2</td><td>5</td><td>교착 상태(Deadlock)에 대하여 다음을 설명하시오. 가. 교착 상태의 개념 나. 교착 상태의 필요조건 다. 교착 상태의 해결 방법</td><td>Deadlock</td><td>-</td></tr>
<tr><td>134</td><td>컴시응</td><td>4</td><td>3</td><td>병렬 컴퓨팅에 대하여 다음을 설명하시오. 가. 병렬 컴퓨팅의 개념 나. 병렬 프로세서의 분류</td><td>병렬컴퓨터</td><td>-</td></tr>
<!-- 132회 -->
<tr><td>132</td><td>컴시응</td><td>1</td><td>1</td><td>TCAM(Ternary Content Addressable Memory)의 개념과 활용사례</td><td>Memory</td><td>-</td></tr>
<tr><td>132</td><td>컴시응</td><td>1</td><td>2</td><td>폴락의 법칙(Pollack's Rule)</td><td>프로세서 성능</td><td>-</td></tr>
<tr><td>132</td><td>컴시응</td><td>1</td><td>4</td><td>세마포어(Semaphore)의 개념과 주요 연산(P연산, V연산)</td><td>Semaphore</td><td>-</td></tr>
<tr><td>132</td><td>컴시응</td><td>2</td><td>1</td><td>컴퓨터 시스템은 내부/외부에서 발생하는 각종 event에 대처하기 위해, 다양한 방식으로 인터럽트(interrupt) 체계를 구현하고 있다. 이와 관련하여 아래 사항을 설명하시오. 가. Polling 방식 나. Daisy-Chain 방식 다. Vector Interrupt 방식</td><td>인터럽트</td><td>-</td></tr>
<tr><td>132</td><td>컴시응</td><td>3</td><td>4</td><td>중앙처리장치(CPU) 내에 구성된 제어장치(Control Unit)의 구현 방법과 관련하여 아래 사항을 설명하시오. 가. micro-programmed 구현방법 나. hard-wired 구현방법 다. 구현 방법 간 상호비교</td><td>CISC, RISC</td><td>-</td></tr>
<tr><td>132</td><td>컴시응</td><td>4</td><td>1</td><td>컴퓨터 시스템의 캐시(Cache) 메모리와 관련하여 아래 사항을 설명하시오. 가. 캐시메모리에서 주소 매핑(mapping)이 필요한 이유와 주소 매핑(mapping) 방식 나. 캐시 쓰기 정책(write policy) 다. 다중 프로세서 시스템에서 캐시 일관성(Cache Coherence)을 유지하기 위한 기법</td><td>Cache Memory</td><td>-</td></tr>
<tr><td>132</td><td>컴시응</td><td>4</td><td>4</td><td>운영체제에서 발생할 수 있는 deadlock 현상에 대하여 아래 사항을 설명하시오. 가. deadlock의 개념 나. deadlock과 starvation의 차이점 다. deadlock이 발생하기 위한 조건 4가지 라. deadlock 발생시 처리 방안</td><td>Deadlock</td><td>-</td></tr>
<!-- 131회 -->
<tr><td>131</td><td>관리</td><td>3</td><td>5</td><td>운영체제 메모리 관리 기법 중 페이징 기법과 세그멘테이션 기법의 개념을 설명하고, 두 기법에 대하여 비교 설명하시오.</td><td>Virtual Memory</td><td>-</td></tr>
<tr><td>131</td><td>컴시응</td><td>1</td><td>6</td><td>PNM(Processing Near Memory)</td><td>Memory</td><td>-</td></tr>
<tr><td>131</td><td>컴시응</td><td>2</td><td>2</td><td>프로세스 스레싱(Thrashing)의 정의, 발생 원인과 해결방법을 설명하시오.</td><td>Thrashing</td><td>-</td></tr>
<tr><td>131</td><td>컴시응</td><td>2</td><td>5</td><td>칩렛(Chiplet)에 대하여 다음을 설명하시오. 가. 칩렛의 개념 나. 칩렛 구조의 장점 다. 칩렛을 이어붙이는 방법</td><td>프로세서</td><td>-</td></tr>
<tr><td>131</td><td>컴시응</td><td>3</td><td>3</td><td>디스크 여러 개를 활용하여 속도를 높이고 안정성을 향상시키는 기술인 RAID(Redundant Array of Inexpensive Disk) 기술 중 RAID5와 RAID6에 대하여 설명하고, 최소 디스크 수량 및 고장 허용 측면에서 비교하여 설명하시오.</td><td>RAID</td><td>-</td></tr>
<tr><td>131</td><td>컴시응</td><td>4</td><td>3</td><td>캐쉬 메모리(Cache Memory)에 대하여 다음을 설명하시오. 가. 캐쉬 메모리의 개념과 구조 나. 지역성(Locality)의 개념과 유형 다. 캐쉬 일관성(Coherence) 문제의 원인과 해결 방법</td><td>Cache Memory, Locality</td><td>-</td></tr>
</tbody>
</table>

---

## 💡 사용 팁

- **검색**: 상단 검색창에 키워드 입력 (예: "캐시", "Deadlock", "1교시")
- **정렬**: 각 컬럼 헤더 클릭하여 오름차순/내림차순 정렬
- **필터**: 빠른 필터 버튼으로 교시별, 학습페이지 유무 등 필터링

---

## 📊 통계

| 회차 | 문제 수 |
|:----:|:-------:|
| 137회 | 12개 |
| 136회 | 4개 |
| 135회 | 6개 |
| 134회 | 6개 |
| 132회 | 7개 |
| 131회 | 6개 |
| **합계** | **41개** |

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

