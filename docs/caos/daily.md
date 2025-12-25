---
layout: default
title: 🃏 데일리 암기 덱 (CAOS)
parent: CAOS (컴퓨터구조/OS)
nav_order: 1
has_toc: false
permalink: /docs/caos/daily
---

# 🃏 데일리 암기 덱 (CAOS)
{: .no_toc }

**컴퓨터구조/OS 전체 토픽**을 "노트 넘기기"처럼 보는 모드입니다.  
왼쪽에서 항목을 고르면, 오른쪽에 **정의/구성요소/암기**가 바로 펼쳐집니다.

<div class="domain-deck" id="domainDeckRoot"
  data-topics-url="{{ site.baseurl }}/docs/caos/topics.json"
  data-index-url="{{ site.baseurl }}/docs/caos"
  data-domain="CAOS"
  data-accent="#7c3aed">

  <div class="domain-deck__toolbar">
    <div class="domain-deck__row">
      <label class="domain-deck__label">
        덱
        <select id="domainDeckMode" class="domain-deck__select">
          <option value="topics-all" selected>CAOS 토픽 · 전체</option>
          <option value="topics-0">⓪ Computer</option>
          <option value="topics-1">① CPU 스케줄링</option>
          <option value="topics-2">② 동기화</option>
          <option value="topics-3">③ 교착상태</option>
          <option value="topics-4">④ 가상메모리</option>
          <option value="topics-5">⑤ 캐시메모리</option>
          <option value="topics-6">⑥ RAID</option>
          <option value="topics-7">⑦ 프로세스</option>
          <option value="topics-8">⑧ 파이프라인</option>
          <option value="topics-9">⑨ 메모리</option>
          <option value="topics-10">⑩ 인터럽트</option>
          <option value="topics-11">⑪ 운영체제</option>
          <option value="topics-12">⑫ 반도체</option>
          <option value="topics-13">⑬ CPU/GPU</option>
          <option value="topics-14">⑭ CA 기타</option>
        </select>
      </label>
      <label class="domain-deck__label">
        검색
        <input id="domainDeckSearch" class="domain-deck__input domain-deck__input--wide" type="text" placeholder="예: 캐시 / 스케줄링 / 교착상태">
      </label>
    </div>
    <div class="domain-deck__row domain-deck__row--meta">
      <div class="domain-deck__meta">
        <span id="domainDeckStatus">로딩 중…</span>
        <span class="domain-deck__kbd">⌨️ ↑/↓ 이동 · Enter 원문</span>
      </div>
      <div class="domain-deck__nav-links">
        <a class="domain-deck__nav-pill" href="{{ site.baseurl }}/docs/caos">🏠 CAOS 메인</a>
      </div>
    </div>
  </div>

  <div class="domain-deck__layout">
    <aside class="domain-deck__list" aria-label="항목 목록">
      <div id="domainDeckList" class="domain-deck__items"></div>
    </aside>
    <section class="domain-deck__detail" aria-label="선택 항목 상세">
      <div class="domain-deck__detail-head">
        <div class="domain-deck__tag" id="domainDeckTag">-</div>
        <div class="domain-deck__title" id="domainDeckTitle">항목을 선택하세요</div>
        <div class="domain-deck__detail-actions">
          <button type="button" class="domain-deck__btn" id="domainDeckPrev">↑ 이전</button>
          <button type="button" class="domain-deck__btn domain-deck__btn--primary" id="domainDeckNext">↓ 다음</button>
          <a class="domain-deck__btn domain-deck__btn--ghost" id="domainDeckOpenLink" href="#" target="_blank" rel="noopener">원문 보기</a>
        </div>
      </div>
      <div class="domain-deck__panes">
        <div class="domain-deck__pane"><div class="domain-deck__pane-title">개념 정의(한 줄)</div><div class="domain-deck__pane-body" id="domainDeckDefinition">-</div></div>
        <div class="domain-deck__pane"><div class="domain-deck__pane-title">구성요소(표)</div><div class="domain-deck__pane-body" id="domainDeckComponents">-</div></div>
        <div class="domain-deck__pane domain-deck__pane--wide"><div class="domain-deck__pane-title">암기법/핵심 구문</div><div class="domain-deck__pane-body" id="domainDeckMnemonic">-</div></div>
      </div>
    </section>
  </div>
</div>

{% include daily-deck-common.html accent="#7c3aed" accent_light="rgba(124, 58, 237, 0.08)" accent_border="rgba(124, 58, 237, 0.22)" %}

