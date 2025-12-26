---
layout: default
title: 🃏 데일리 암기 덱 (DS)
parent: DS (Digital Service)
nav_order: 1
has_toc: false
permalink: /docs/ds/daily
---

# 🃏 데일리 암기 덱 (DS)
{: .no_toc }

**DS 전체 토픽 + 기출문제(1교시/2교시)**를 "노트 넘기기"처럼 보는 모드입니다.  
왼쪽에서 항목을 고르면, 오른쪽에 **정의/구성요소/암기**가 바로 펼쳐져서 *뒤집기 없이* 매일 보기 좋게 설계했습니다.

<div class="ds-deck" id="dsDeckRoot"
  data-exam-url="{{ site.baseurl }}/docs/ds/exam"
  data-topics-url="{{ site.baseurl }}/docs/ds/topics.json"
  data-index-url="{{ site.baseurl }}/docs/ds">

  <div class="ds-deck__toolbar">
    <div class="ds-deck__row">
      <label class="ds-deck__label">
        덱
        <select id="dsDeckMode" class="ds-deck__select">
          <option value="topics-all" selected>DS 토픽 · 전체</option>
          <option value="topics-1">① 웹/UX</option>
          <option value="topics-2">② 연동/API</option>
          <option value="topics-3">③ 클라우드</option>
          <option value="topics-4">④ 가상화/컨테이너</option>
          <option value="topics-5">⑤ 분산 컴퓨팅</option>
          <option value="topics-6">⑥ XR/메타버스</option>
          <option value="topics-7">⑦ 블록체인</option>
          <option value="topics-8">⑧ 스마트카/자율주행</option>
          <option value="topics-9">⑨ 스마트팩토리/그리드</option>
          <option value="topics-10">⑩ IoT/드론/헬스케어</option>
          <option value="topics-11">⑪ 로봇/추천/영상</option>
          <option value="topics-12">⑫ 전자정부/정책</option>
          <option value="topics-13">⑬ 기타</option>
          <option value="exam-1">기출 · 1교시</option>
          <option value="exam-2">기출 · 2교시</option>
        </select>
      </label>

      <label class="ds-deck__label">
        검색
        <input id="dsDeckSearch" class="ds-deck__input ds-deck__input--wide" type="text" placeholder="예: 클라우드 / 블록체인 / 컨테이너">
      </label>
    </div>

    <div class="ds-deck__row ds-deck__row--meta">
      <div class="ds-deck__meta">
        <span id="dsDeckStatus">로딩 중…</span>
        <span class="ds-deck__kbd">⌨️ ↑/↓ 이동 · Enter 원문</span>
      </div>
      <div class="ds-deck__nav-links">
        <a class="ds-deck__nav-pill" href="{{ site.baseurl }}/docs/ds/exam">📝 기출 테이블</a>
        <a class="ds-deck__nav-pill" href="{{ site.baseurl }}/docs/ds">🏠 DS 메인</a>
      </div>
    </div>
  </div>

  <div class="ds-deck__layout">
    <aside class="ds-deck__list" aria-label="항목 목록">
      <div id="dsDeckList" class="ds-deck__items"></div>
    </aside>

    <section class="ds-deck__detail" aria-label="선택 항목 상세">
      <div class="ds-deck__detail-head">
        <div class="ds-deck__tag" id="dsDeckTag">-</div>
        <div class="ds-deck__title" id="dsDeckTitle">항목을 선택하세요</div>
        <div class="ds-deck__detail-actions">
          <button type="button" class="ds-deck__btn" id="dsDeckPrev">↑ 이전</button>
          <button type="button" class="ds-deck__btn ds-deck__btn--primary" id="dsDeckNext">↓ 다음</button>
          <a class="ds-deck__btn ds-deck__btn--ghost" id="dsDeckOpenLink" href="#" target="_blank" rel="noopener">원문 보기</a>
          <button type="button" class="ds-deck__btn ds-deck__btn--ghost" id="dsDeckMarkHard">어려움(⭐)</button>
        </div>
      </div>

      <div class="ds-deck__panes">
        <div class="ds-deck__pane">
          <div class="ds-deck__pane-title">개념 정의(한 줄)</div>
          <div class="ds-deck__pane-body" id="dsDeckDefinition">-</div>
        </div>
        <div class="ds-deck__pane">
          <div class="ds-deck__pane-title">구성요소(표)</div>
          <div class="ds-deck__pane-body" id="dsDeckComponents">-</div>
        </div>
        <div class="ds-deck__pane ds-deck__pane--wide">
          <div class="ds-deck__pane-title">암기법/핵심 구문</div>
          <div class="ds-deck__pane-body" id="dsDeckMnemonic">-</div>
        </div>
      </div>

      <div class="ds-deck__footer">
        <details>
          <summary><strong>팁</strong> (클릭)</summary>
          <ul>
            <li><strong>루틴</strong>: 목록을 위아래로 쭉 훑는 방식이 노트 넘기기와 가장 유사합니다.</li>
            <li><strong>추출 품질</strong>: 페이지 템플릿(정의/구성요소 표)을 통일하면 자동 추출 정확도가 올라갑니다.</li>
          </ul>
        </details>
      </div>
    </section>
  </div>
</div>

<style>
/* Page-scoped deck styles */
.ds-deck { margin-top: 1rem; }
.ds-deck__toolbar { border: 1px solid rgba(15, 23, 42, 0.10); border-radius: 14px; padding: 12px; background: rgba(248, 250, 252, 0.72); }
.ds-deck__row { display: flex; gap: 10px; flex-wrap: wrap; align-items: center; justify-content: space-between; }
.ds-deck__row--meta { margin-top: 8px; }
.ds-deck__label { display: inline-flex; gap: 8px; align-items: center; font-size: 12px; font-weight: 900; color: rgba(15, 23, 42, 0.82); }
.ds-deck__select, .ds-deck__input { border: 1px solid rgba(15, 23, 42, 0.14); border-radius: 10px; padding: 6px 10px; background: #fff; font-size: 13px; }
.ds-deck__input { width: 150px; }
.ds-deck__input--wide { width: 260px; }
.ds-deck__btn { border: 1px solid rgba(15, 23, 42, 0.14); background: #fff; border-radius: 12px; padding: 8px 12px; font-size: 13px; font-weight: 900; letter-spacing: -0.2px; cursor: pointer; text-decoration: none !important; display: inline-flex; align-items: center; justify-content: center; }
.ds-deck__btn:hover { background: rgba(226, 232, 240, 0.70); }
.ds-deck__btn--primary { background: linear-gradient(135deg, #0891b2, #06b6d4); color: #fff; border-color: rgba(15, 23, 42, 0.10); }
.ds-deck__btn--primary:hover { filter: brightness(0.98); }
.ds-deck__btn--ghost { background: rgba(255, 255, 255, 0.65); }
.ds-deck__nav-links { display: flex; gap: 8px; }
.ds-deck__nav-pill { display: inline-flex; align-items: center; gap: 4px; padding: 6px 14px; border-radius: 20px; background: linear-gradient(135deg, rgba(8, 145, 178, 0.08), rgba(6, 182, 212, 0.12)); border: 1px solid rgba(8, 145, 178, 0.22); font-size: 12px; font-weight: 800; color: #0e7490; text-decoration: none !important; transition: all 0.15s ease; }
.ds-deck__nav-pill:hover { background: linear-gradient(135deg, rgba(8, 145, 178, 0.16), rgba(6, 182, 212, 0.22)); border-color: rgba(8, 145, 178, 0.36); color: #155e75; transform: translateY(-1px); box-shadow: 0 2px 8px rgba(8, 145, 178, 0.18); }
.ds-deck__meta { display: flex; gap: 12px; align-items: center; font-size: 12px; font-weight: 900; color: rgba(15, 23, 42, 0.76); width: 100%; justify-content: space-between; }
.ds-deck__kbd { font-weight: 900; color: rgba(15, 23, 42, 0.62); }

.ds-deck__layout { margin-top: 12px; display: grid; gap: 12px; grid-template-columns: 360px 1fr; align-items: start; }
@media (max-width: 66.49rem) {
  .ds-deck__layout { grid-template-columns: 1fr; }
  .ds-deck__input--wide { width: 100%; }
}

.ds-deck__list { border: 1px solid rgba(15, 23, 42, 0.10); border-radius: 14px; background: #fff; overflow: hidden; }
.ds-deck__items { max-height: calc(100vh - 280px); overflow: auto; }
@media (max-width: 66.49rem) { .ds-deck__items { max-height: 44vh; } }

.ds-deck__item { display: grid; gap: 6px; padding: 10px 10px; border-bottom: 1px solid rgba(15, 23, 42, 0.08); cursor: pointer; }
.ds-deck__item:hover { background: rgba(248, 250, 252, 0.85); }
.ds-deck__item.is-active { background: rgba(207, 250, 254, 0.30); }
.ds-deck__item-title { font-size: 13px; font-weight: 900; letter-spacing: -0.2px; color: rgba(15, 23, 42, 0.90); }
.ds-deck__item-sub { font-size: 12px; font-weight: 900; letter-spacing: -0.2px; color: rgba(15, 23, 42, 0.60); }
.ds-deck__item-tagline { display: flex; gap: 8px; align-items: center; justify-content: space-between; }
.ds-deck__pill { display: inline-flex; align-items: center; padding: 3px 8px; border-radius: 999px; font-size: 12px; font-weight: 900; color: rgba(15, 23, 42, 0.82); background: rgba(226, 232, 240, 0.75); border: 1px solid rgba(15, 23, 42, 0.10); }
.ds-deck__pill--hard { background: rgba(254, 202, 202, 0.60); border-color: rgba(239, 68, 68, 0.22); color: rgba(127, 29, 29, 0.92); }

.ds-deck__detail { border: 1px solid rgba(15, 23, 42, 0.10); border-radius: 14px; background: #fff; padding: 12px; }
.ds-deck__detail-head { display: grid; gap: 10px; border-bottom: 1px solid rgba(15, 23, 42, 0.10); padding-bottom: 10px; margin-bottom: 10px; }
.ds-deck__tag { display: inline-flex; width: fit-content; align-items: center; padding: 4px 10px; border-radius: 999px; font-size: 12px; font-weight: 900; color: rgba(15, 23, 42, 0.86); background: rgba(226, 232, 240, 0.75); border: 1px solid rgba(15, 23, 42, 0.10); }
.ds-deck__title { font-size: 20px; font-weight: 900; letter-spacing: -0.4px; color: #0f172a; line-height: 1.3; }
.ds-deck__detail-actions { display: flex; gap: 10px; flex-wrap: wrap; }

.ds-deck__panes { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }
.ds-deck__pane { border: 1px solid rgba(15, 23, 42, 0.08); border-radius: 12px; background: rgba(248, 250, 252, 0.65); padding: 10px; }
.ds-deck__pane--wide { grid-column: 1 / -1; }
.ds-deck--exam .ds-deck__panes { grid-template-columns: 1fr; }
.ds-deck--exam .ds-deck__pane:not(.ds-deck__pane--wide) { display: none; }
.ds-deck--exam .ds-deck__pane--wide { grid-column: auto; }
.ds-deck__pane-title { font-size: 12px; font-weight: 900; color: rgba(15, 23, 42, 0.75); margin-bottom: 6px; }
.ds-deck__pane-body { font-size: 13px; line-height: 1.5; color: rgba(15, 23, 42, 0.92); }
.ds-deck__pane-body code { font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace; font-size: 12px; padding: 2px 6px; border-radius: 8px; background: rgba(207, 250, 254, 0.55); border: 1px solid rgba(6, 182, 212, 0.18); color: #0e7490; margin-right: 6px; display: inline-block; margin-bottom: 6px; }
.ds-deck__pane-body table { width: 100% !important; font-size: 12px; }
.ds-deck__pane-body table td, .ds-deck__pane-body table th { padding: 6px 8px; white-space: normal; }
.ds-deck__pane-body table thead th { white-space: nowrap; }
.ds-deck__pane-body .highlight-purple { background: rgba(207, 250, 254, 0.45); border-radius: 10px; padding: 8px; }
.ds-deck__footer { margin-top: 10px; }
</style>

<script>
(function() {
  var root = document.getElementById('dsDeckRoot');
  if (!root) return;

  var examUrl = root.getAttribute('data-exam-url');
  var topicsUrl = root.getAttribute('data-topics-url');
  var indexUrl = root.getAttribute('data-index-url');

  var elStatus = document.getElementById('dsDeckStatus');
  var elMode = document.getElementById('dsDeckMode');
  var elSearch = document.getElementById('dsDeckSearch');

  var elList = document.getElementById('dsDeckList');
  var elTag = document.getElementById('dsDeckTag');
  var elTitle = document.getElementById('dsDeckTitle');
  var elDef = document.getElementById('dsDeckDefinition');
  var elComponents = document.getElementById('dsDeckComponents');
  var elMnemonic = document.getElementById('dsDeckMnemonic');
  var elOpenLink = document.getElementById('dsDeckOpenLink');

  // Pane refs (exam cards show only Quick Reference)
  var paneDef = elDef && elDef.closest ? elDef.closest('.ds-deck__pane') : null;
  var paneComponents = elComponents && elComponents.closest ? elComponents.closest('.ds-deck__pane') : null;
  var paneMnemonic = elMnemonic && elMnemonic.closest ? elMnemonic.closest('.ds-deck__pane') : null;
  var paneMnemonicTitle = paneMnemonic ? paneMnemonic.querySelector('.ds-deck__pane-title') : null;
  var mnemonicTitleDefault = paneMnemonicTitle ? paneMnemonicTitle.textContent : '암기법/핵심 구문';

  var btnPrev = document.getElementById('dsDeckPrev');
  var btnNext = document.getElementById('dsDeckNext');
  var btnHard = document.getElementById('dsDeckMarkHard');

  var STORAGE_PREFIX = 'peDsDeck:v1:';

  var examRows = [];
  var topicRows = [];

  var cardsAll = [];
  var cards = [];
  var idx = 0;
  var hardSet = new Set();
  var pageCache = new Map();

  function safeGet(key, fallback) {
    try {
      var v = localStorage.getItem(key);
      if (!v) return fallback;
      return JSON.parse(v);
    } catch (e) { return fallback; }
  }

  function safeSet(key, val) {
    try { localStorage.setItem(key, JSON.stringify(val)); } catch (e) {}
  }

  function normalizeText(s) {
    return (s || '').replace(/\s+/g, ' ').trim();
  }

  function shortParentLabel(s) {
    var t = normalizeText(s || '');
    t = t.replace(/^\d+\.\s*/, '');
    return t;
  }

  function cardKey(c) {
    return [c.kind, c.url || c.title].join('|');
  }

  function renderDefinition(s) {
    var t = normalizeText(s || '');
    if (!t) return '-';
    return escapeHtml(t);
  }

  function escapeHtml(s) {
    return String(s || '')
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/\"/g, '&quot;')
      .replace(/'/g, '&#39;');
  }

  function setStatus() {
    elStatus.textContent = (cards.length ? (idx + 1) + ' / ' + cards.length : '0') + ' · 후보 ' + cardsAll.length;
  }

  // DS 분류 매핑
  function topicGroupForUrl(url) {
    if (!url) return 'etc';
    if (url.indexOf('/docs/ds/24-web/') >= 0 || url.indexOf('/docs/ds/12-ui-ux/') >= 0) return '1';
    if (url.indexOf('/docs/ds/13-api/') >= 0) return '2';
    if (url.indexOf('/docs/ds/01-cloud/') >= 0) return '3';
    if (url.indexOf('/docs/ds/07-virtualization/') >= 0) return '4';
    if (url.indexOf('/docs/ds/11-distributed/') >= 0) return '5';
    if (url.indexOf('/docs/ds/02-xr-metaverse/') >= 0) return '6';
    if (url.indexOf('/docs/ds/03-blockchain/') >= 0) return '7';
    if (url.indexOf('/docs/ds/04-autonomous/') >= 0) return '8';
    if (url.indexOf('/docs/ds/05-smart-factory/') >= 0 || url.indexOf('/docs/ds/06-smart-grid/') >= 0) return '9';
    if (url.indexOf('/docs/ds/08-iot/') >= 0 || url.indexOf('/docs/ds/09-drone-uam/') >= 0 || url.indexOf('/docs/ds/10-healthcare/') >= 0) return '10';
    if (url.indexOf('/docs/ds/19-robot/') >= 0 || url.indexOf('/docs/ds/20-recommendation/') >= 0 || url.indexOf('/docs/ds/21-vision/') >= 0) return '11';
    if (url.indexOf('/docs/ds/16-e-gov/') >= 0 || url.indexOf('/docs/ds/15-design-thinking/') >= 0 || url.indexOf('/docs/ds/17-gartner/') >= 0 || url.indexOf('/docs/ds/14-spatial/') >= 0) return '12';
    if (url.indexOf('/docs/ds/18-etc/') >= 0 || url.indexOf('/docs/ds/22-finops/') >= 0 || url.indexOf('/docs/ds/23-infra/') >= 0) return '13';
    return 'etc';
  }

  function applyModeAndSearch() {
    var mode = elMode.value;
    var q = normalizeText(elSearch.value).toLowerCase();

    var base = cardsAll.slice().filter(function(c) {
      if (mode.indexOf('topics-') === 0 || mode === 'topics-all') return c.kind === 'topic';
      if (mode === 'exam-1') return c.kind === 'exam' && c.session === '1';
      if (mode === 'exam-2') return c.kind === 'exam' && c.session === '2';
      return true;
    });

    // 분류 필터
    if (mode === 'topics-1') base = base.filter(function(c) { return topicGroupForUrl(c.url) === '1'; });
    if (mode === 'topics-2') base = base.filter(function(c) { return topicGroupForUrl(c.url) === '2'; });
    if (mode === 'topics-3') base = base.filter(function(c) { return topicGroupForUrl(c.url) === '3'; });
    if (mode === 'topics-4') base = base.filter(function(c) { return topicGroupForUrl(c.url) === '4'; });
    if (mode === 'topics-5') base = base.filter(function(c) { return topicGroupForUrl(c.url) === '5'; });
    if (mode === 'topics-6') base = base.filter(function(c) { return topicGroupForUrl(c.url) === '6'; });
    if (mode === 'topics-7') base = base.filter(function(c) { return topicGroupForUrl(c.url) === '7'; });
    if (mode === 'topics-8') base = base.filter(function(c) { return topicGroupForUrl(c.url) === '8'; });
    if (mode === 'topics-9') base = base.filter(function(c) { return topicGroupForUrl(c.url) === '9'; });
    if (mode === 'topics-10') base = base.filter(function(c) { return topicGroupForUrl(c.url) === '10'; });
    if (mode === 'topics-11') base = base.filter(function(c) { return topicGroupForUrl(c.url) === '11'; });
    if (mode === 'topics-12') base = base.filter(function(c) { return topicGroupForUrl(c.url) === '12'; });
    if (mode === 'topics-13') base = base.filter(function(c) { return topicGroupForUrl(c.url) === '13'; });

    if (q) {
      base = base.filter(function(c) {
        return (c.title || '').toLowerCase().includes(q) ||
               (c.parent || '').toLowerCase().includes(q) ||
               (c.mnemonic_text || '').toLowerCase().includes(q);
      });
    }

    function toInt(x, fallback) {
      var n = parseInt(String(x || ''), 10);
      return isFinite(n) ? n : (fallback || 0);
    }

    base.sort(function(a, b) {
      if (a.kind === 'topic' && b.kind === 'topic') {
        var ao = toInt(a.nav_order, 9999);
        var bo = toInt(b.nav_order, 9999);
        if (ao !== bo) return ao - bo;
        return String(a.title || '').localeCompare(String(b.title || ''), 'ko');
      }
      if (a.kind === 'exam' && b.kind === 'exam') {
        var ar = toInt(a.round, 0);
        var br = toInt(b.round, 0);
        if (ar !== br) return br - ar;
        var as = toInt(a.session, 0);
        var bs = toInt(b.session, 0);
        if (as !== bs) return as - bs;
        var an = toInt(a.no, 0);
        var bn = toInt(b.no, 0);
        return an - bn;
      }
      return String(a.kind).localeCompare(String(b.kind));
    });

    cards = base;
    idx = 0;
    renderList();
    selectIndex(0, { scrollIntoView: true });
  }

  function renderList() {
    if (!cards.length) {
      elList.innerHTML = '<div class="ds-deck__item"><div class="ds-deck__item-title">결과가 없습니다.</div></div>';
      setStatus();
      clearDetail();
      return;
    }

    var html = '';
    cards.forEach(function(c, i) {
      var hard = hardSet.has(cardKey(c));
      html += '<div class="ds-deck__item' + (i === idx ? ' is-active' : '') + '" data-idx="' + i + '">';
      html +=   '<div class="ds-deck__item-title">' + escapeHtml(c.title) + '</div>';
      html +=   '<div class="ds-deck__item-tagline">';
      html +=     '<span class="ds-deck__pill">' + escapeHtml(c.badge) + '</span>';
      html +=     (hard ? '<span class="ds-deck__pill ds-deck__pill--hard">⭐</span>' : '<span class="ds-deck__pill" style="opacity:.55"> </span>');
      html +=   '</div>';
      html += '</div>';
    });
    elList.innerHTML = html;
    setStatus();

    Array.prototype.forEach.call(elList.querySelectorAll('.ds-deck__item[data-idx]'), function(node) {
      node.addEventListener('click', function() {
        var i = parseInt(node.getAttribute('data-idx') || '0', 10);
        selectIndex(i, { scrollIntoView: false });
      });
    });
  }

  function clearDetail() {
    elTag.textContent = '-';
    elTitle.textContent = '항목을 선택하세요';
    elDef.innerHTML = '-';
    elComponents.innerHTML = '-';
    elMnemonic.innerHTML = '-';
    elOpenLink.setAttribute('href', '#');
  }

  function updateActiveRow() {
    Array.prototype.forEach.call(elList.querySelectorAll('.ds-deck__item[data-idx]'), function(node) {
      var i = parseInt(node.getAttribute('data-idx') || '0', 10);
      if (i === idx) node.classList.add('is-active');
      else node.classList.remove('is-active');
    });
  }

  function selectIndex(i, opts) {
    if (!cards.length) return;
    if (i < 0) i = 0;
    if (i >= cards.length) i = cards.length - 1;
    idx = i;
    updateActiveRow();
    setStatus();

    var c = cards[idx];
    elTag.textContent = c.badge;
    elTitle.textContent = c.title;
    elOpenLink.setAttribute('href', c.url || '#');

    var isExam = c.kind === 'exam';
    if (root && root.classList) root.classList.toggle('ds-deck--exam', isExam);

    // exam: show only Quick Reference pane
    if (paneDef) paneDef.style.display = isExam ? 'none' : '';
    if (paneComponents) paneComponents.style.display = isExam ? 'none' : '';
    if (paneMnemonic) {
      if (isExam) paneMnemonic.classList.remove('ds-deck__pane--wide');
      else paneMnemonic.classList.add('ds-deck__pane--wide');
    }
    if (paneMnemonicTitle) paneMnemonicTitle.textContent = isExam ? '핵심 암기 (Quick Reference)' : mnemonicTitleDefault;

    // Fast-fill: topics use mnemonic, exams wait for page extract
    elMnemonic.innerHTML = isExam ? '불러오는 중…' : (c.mnemonic_html || (c.mnemonic_text ? escapeHtml(c.mnemonic_text) : '-'));
    elDef.innerHTML = '-';
    elComponents.innerHTML = '-';

    hydrateFromPage(c);

    if (opts && opts.scrollIntoView) {
      var active = elList.querySelector('.ds-deck__item.is-active');
      if (active && active.scrollIntoView) active.scrollIntoView({ block: 'nearest' });
    }
  }

  function markHard() {
    if (!cards.length) return;
    var c = cards[idx];
    var k = cardKey(c);
    if (hardSet.has(k)) hardSet.delete(k);
    else hardSet.add(k);
    safeSet(STORAGE_PREFIX + 'hard', Array.from(hardSet));
    renderList();
    updateActiveRow();
    selectIndex(idx, { scrollIntoView: false });
  }

  function parseExamHtml(htmlText) {
    var parser = new DOMParser();
    var doc = parser.parseFromString(htmlText, 'text/html');
    var rows = doc.querySelectorAll('#examTable tbody tr');
    var out = [];
    rows.forEach(function(tr) {
      var tds = tr.querySelectorAll('td');
      if (!tds || tds.length < 7) return;
      var a = tds[4].querySelector('a');
      if (!a) return;
      var mnemonicText = normalizeText(tds[6].textContent);
      if (!mnemonicText || mnemonicText === '-') return;
      out.push({
        kind: 'exam',
        round: normalizeText(tds[0].textContent),
        dept: normalizeText(tds[1].textContent),
        session: normalizeText(tds[2].textContent),
        no: normalizeText(tds[3].textContent),
        title: normalizeText(a.textContent),
        url: a.getAttribute('href') || '',
        badge: normalizeText(tds[0].textContent) + '회 · ' + normalizeText(tds[2].textContent) + '교시 · ' + normalizeText(tds[3].textContent) + '번',
        mnemonic_text: mnemonicText,
        mnemonic_html: (tds[6].innerHTML || '').trim()
      });
    });
    return out;
  }

  function findHeading(doc, keyword) {
    var headings = Array.prototype.slice.call(doc.querySelectorAll('h1,h2,h3,h4'));
    return headings.find(function(h) { return normalizeText(h.textContent).includes(keyword); }) || null;
  }

  function extractDefinition(doc) {
    var h = findHeading(doc, '개념 정의') || findHeading(doc, '개념') || findHeading(doc, '정의');
    if (!h) return '';
    var el = h.nextElementSibling;
    while (el && (el.tagName === 'HR')) el = el.nextElementSibling;
    if (!el) return '';
    if (el.tagName === 'TABLE') {
      var firstRow = el.querySelector('tbody tr');
      if (!firstRow) return '';
      var tds = firstRow.querySelectorAll('td');
      if (tds && tds.length >= 2) return normalizeText(tds[1].textContent);
      return normalizeText(firstRow.textContent);
    }
    if (el.tagName === 'BLOCKQUOTE') return normalizeText(el.textContent);
    return normalizeText(el.textContent);
  }

  function extractComponentsTables(doc) {
    var h = findHeading(doc, '구성요소') || findHeading(doc, '기술요소');
    if (!h) return '';
    var el = h.nextElementSibling;
    var tables = [];
    var guard = 0;
    while (el && guard < 50) {
      if (/^H[1-6]$/.test(el.tagName)) break;
      if (el.tagName === 'TABLE') tables.push(el);
      var innerTables = el.querySelectorAll ? el.querySelectorAll('table') : [];
      if (innerTables && innerTables.length) innerTables.forEach(function(t) { if (tables.indexOf(t) === -1) tables.push(t); });
      if (tables.length >= 2) break;
      el = el.nextElementSibling;
      guard += 1;
    }
    if (!tables.length) return '';
    return tables.slice(0, 2).map(function(t) { return t.outerHTML; }).join('\n');
  }

  function normalizeMnemonicFallback(doc) {
    var headings = Array.prototype.slice.call(doc.querySelectorAll('h1,h2,h3,h4'));
    var target = headings.find(function(h) { return normalizeText(h.textContent).includes('암기'); });
    if (!target) return null;
    var el = target.nextElementSibling;
    var tries = 0;
    while (el && tries < 6) {
      var codes = el.querySelectorAll ? el.querySelectorAll('code') : [];
      if (codes && codes.length) return el.innerHTML.trim();
      if (el.tagName === 'TABLE') return el.outerHTML;
      el = el.nextElementSibling;
      tries += 1;
    }
    return null;
  }

  function extractQuickReferenceHtml(doc) {
    // 1순위: 핵심 암기 / Quick Reference
    var h = findHeading(doc, '핵심 암기') || findHeading(doc, 'Quick Reference') || findHeading(doc, 'Quick');
    // 2순위: 기술사 수준 설명 아래 첫 블록
    if (!h) h = findHeading(doc, '기술사 수준 설명');
    // 3순위: 개념 정의
    if (!h) h = findHeading(doc, '개념 정의') || findHeading(doc, '개념');
    if (!h) return '';
    var el = h.nextElementSibling;
    while (el && (el.tagName === 'HR')) el = el.nextElementSibling;
    if (!el) return '';
    var parts = [];
    var guard = 0;
    while (el && guard < 10) {
      if (/^H[1-6]$/.test(el.tagName)) break;
      if (el.tagName === 'HR') break;
      parts.push(el.outerHTML);
      if (el.tagName === 'BLOCKQUOTE') break;
      if (el.tagName === 'TABLE') break;
      if (parts.length >= 3) break;
      el = el.nextElementSibling;
      guard += 1;
    }
    return parts.join('\n');
  }

  function hydrateFromPage(card) {
    if (!card || !card.url) return;
    if (pageCache.has(card.url)) {
      applyExtracted(pageCache.get(card.url));
      return;
    }
    var isExam = card.kind === 'exam';
    if (!isExam) {
      elDef.innerHTML = '불러오는 중…';
      elComponents.innerHTML = '불러오는 중…';
    }

    fetch(card.url, { credentials: 'same-origin' })
      .then(function(res) { return res.text(); })
      .then(function(html) {
        var parser = new DOMParser();
        var doc = parser.parseFromString(html, 'text/html');

        var quickrefHtml = extractQuickReferenceHtml(doc);
        var definition = isExam ? '' : extractDefinition(doc);
        var componentsHtml = isExam ? '' : extractComponentsTables(doc);
        var mnemonic = card.mnemonic_html || normalizeMnemonicFallback(doc) || '';

        var payload = {
          url: card.url,
          quickref_html: quickrefHtml,
          definition: definition,
          components_html: componentsHtml,
          mnemonic_html: mnemonic
        };
        pageCache.set(card.url, payload);
        applyExtracted(payload);
      })
      .catch(function() {
        if (isExam) elMnemonic.innerHTML = '-';
        else { elDef.innerHTML = '-'; elComponents.innerHTML = '-'; }
      });
  }

  function applyExtracted(payload) {
    if (!payload || !cards.length) return;
    var cur = cards[idx];
    if (!cur || cur.url !== payload.url) return;

    if (cur.kind === 'exam') {
      // exam: show only Quick Reference (fallback to mnemonic if not found)
      if (payload.quickref_html) elMnemonic.innerHTML = payload.quickref_html;
      else elMnemonic.innerHTML = cur.mnemonic_html || (cur.mnemonic_text ? escapeHtml(cur.mnemonic_text) : '-');
      return;
    }

    elDef.innerHTML = renderDefinition(payload.definition);
    elComponents.innerHTML = payload.components_html ? payload.components_html : '-';
    if (!cur.mnemonic_html || cur.mnemonic_text === '-' || !cur.mnemonic_text) {
      if (payload.mnemonic_html) elMnemonic.innerHTML = payload.mnemonic_html;
    }
  }

  function loadSources() {
    elStatus.textContent = '데이터 로딩…';
    return Promise.all([
      fetch(examUrl, { credentials: 'same-origin' }).then(function(r) { return r.text(); }).then(function(t) { examRows = parseExamHtml(t); }),
      fetch(topicsUrl, { credentials: 'same-origin' }).then(function(r) { return r.json(); }).then(function(j) {
        topicRows = (Array.isArray(j) ? j : []).map(function(p) {
          return {
            kind: 'topic',
            title: normalizeText(p.title),
            url: p.url,
            parent: p.parent,
            grand_parent: p.grand_parent,
            badge: shortParentLabel(p.parent || 'DS 토픽'),
            nav_order: p.nav_order,
            mnemonic_text: ''
          };
        });
      })
    ]);
  }

  function init() {
    try {
      var params = new URLSearchParams(window.location.search || '');
      var qsDeck = params.get('deck') || params.get('mode');
      if (qsDeck && elMode.querySelector('option[value="' + qsDeck + '"]')) {
        elMode.value = qsDeck;
        safeSet(STORAGE_PREFIX + 'prefs', { mode: qsDeck, search: '' });
      }
    } catch (e) {}

    var prefs = safeGet(STORAGE_PREFIX + 'prefs', {});
    if (prefs && typeof prefs === 'object') {
      if (prefs.mode) elMode.value = prefs.mode;
      if (prefs.search) elSearch.value = String(prefs.search);
    }
    var hardSaved = safeGet(STORAGE_PREFIX + 'hard', []);
    hardSet = new Set(Array.isArray(hardSaved) ? hardSaved : []);

    loadSources()
      .then(function() {
        cardsAll = examRows.concat(topicRows);
        elStatus.textContent = '준비 완료';
        applyModeAndSearch();
      })
      .catch(function(err) {
        elStatus.textContent = '로딩 실패: ' + (err && err.message ? err.message : 'unknown');
        clearDetail();
      });

    elMode.addEventListener('change', function() {
      safeSet(STORAGE_PREFIX + 'prefs', { mode: elMode.value, search: elSearch.value });
      applyModeAndSearch();
    });
    elSearch.addEventListener('input', function() {
      safeSet(STORAGE_PREFIX + 'prefs', { mode: elMode.value, search: elSearch.value });
      if (window.__dsDeckSearchTimer) clearTimeout(window.__dsDeckSearchTimer);
      window.__dsDeckSearchTimer = setTimeout(applyModeAndSearch, 180);
    });

    btnPrev.addEventListener('click', function() { selectIndex(idx - 1, { scrollIntoView: true }); });
    btnNext.addEventListener('click', function() { selectIndex(idx + 1, { scrollIntoView: true }); });
    btnHard.addEventListener('click', function(e) { e.preventDefault(); markHard(); });

    window.addEventListener('keydown', function(e) {
      if (e.defaultPrevented) return;
      var ae = document.activeElement;
      if (ae) {
        var tag = (ae.tagName || '').toLowerCase();
        if (tag === 'input' || tag === 'textarea' || tag === 'select') return;
        if (ae.isContentEditable) return;
      }
      if (e.key === 'ArrowDown') { e.preventDefault(); selectIndex(idx + 1, { scrollIntoView: true }); }
      if (e.key === 'ArrowUp') { e.preventDefault(); selectIndex(idx - 1, { scrollIntoView: true }); }
      if (e.key === 'Enter') {
        var cur = cards[idx];
        if (cur && cur.url) window.open(cur.url, '_blank', 'noopener');
      }
    });
  }

  init();
})();
</script>

