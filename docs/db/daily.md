---
layout: default
title: 🃏 데일리 암기 덱 (DB)
parent: DB (데이터베이스)
nav_order: 1
has_toc: false
permalink: /docs/db/daily
---

# 🃏 데일리 암기 덱 (DB)
{: .no_toc }

**DB 전체 토픽**을 "노트 넘기기"처럼 보는 모드입니다.  
왼쪽에서 항목을 고르면, 오른쪽에 **정의/구성요소/암기**가 바로 펼쳐집니다.

<div class="domain-deck" id="domainDeckRoot"
  data-topics-url="{{ site.baseurl }}/docs/db/topics.json"
  data-index-url="{{ site.baseurl }}/docs/db"
  data-domain="DB"
  data-accent="#16a34a">

  <div class="domain-deck__toolbar">
    <div class="domain-deck__row">
      <label class="domain-deck__label">
        덱
        <select id="domainDeckMode" class="domain-deck__select">
          <option value="topics-all" selected>DB 토픽 · 전체</option>
          <option value="topics-1">① 빅데이터</option>
          <option value="topics-2">② DB 기본</option>
          <option value="topics-3">③ 모델링/설계</option>
          <option value="topics-4">④ 트랜잭션</option>
          <option value="topics-5">⑤ 동시성 제어</option>
          <option value="topics-6">⑥ 데이터 회복</option>
          <option value="topics-7">⑦ 데이터 품질</option>
          <option value="topics-8">⑧ 공공데이터</option>
          <option value="topics-9">⑨ DB 성능</option>
          <option value="topics-10">⑩ 정책/활용</option>
        </select>
      </label>
      <label class="domain-deck__label">
        검색
        <input id="domainDeckSearch" class="domain-deck__input domain-deck__input--wide" type="text" placeholder="예: NoSQL / 정규화 / ACID">
      </label>
    </div>
    <div class="domain-deck__row domain-deck__row--meta">
      <div class="domain-deck__meta">
        <span id="domainDeckStatus">로딩 중…</span>
        <span class="domain-deck__kbd">⌨️ ↑/↓ 이동 · Enter 원문</span>
      </div>
      <div class="domain-deck__nav-links">
        <a class="domain-deck__nav-pill" href="{{ site.baseurl }}/docs/db">🏠 DB 메인</a>
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

{% include daily-deck-common.html accent="#16a34a" accent_light="rgba(22, 163, 74, 0.08)" accent_border="rgba(22, 163, 74, 0.22)" %}

