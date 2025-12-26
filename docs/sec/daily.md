---
layout: default
title: 🃏 데일리 암기 덱 (SEC)
parent: SEC (정보보안)
nav_order: 1
has_toc: false
permalink: /docs/sec/daily
---

# 🃏 데일리 암기 덱 (SEC)
{: .no_toc }

**보안 전체 토픽 + 기출문제(1교시/2교시)**를 "노트 넘기기"처럼 보는 모드입니다.  
왼쪽에서 항목을 고르면, 오른쪽에 **정의/구성요소/암기**가 바로 펼쳐져서 *뒤집기 없이* 매일 보기 좋게 설계했습니다.

<div class="sec-deck" id="secDeckRoot"
  data-exam-url="{{ site.baseurl }}/docs/sec/exam"
  data-topics-url="{{ site.baseurl }}/docs/sec/topics.json"
  data-index-url="{{ site.baseurl }}/docs/sec">

  <div class="sec-deck__toolbar">
    <div class="sec-deck__row">
      <label class="sec-deck__label">
        덱
        <select id="secDeckMode" class="sec-deck__select">
          <option value="topics-all" selected>SEC 토픽 · 전체</option>
          <option value="topics-1">① 공격기법/위협</option>
          <option value="topics-2">② 보안 취약점</option>
          <option value="topics-3">③ 암호 기술</option>
          <option value="topics-4">④ 인증/접근통제</option>
          <option value="topics-5">⑤ 네트워크 보안</option>
          <option value="topics-6">⑥ 클라우드/IoT 보안</option>
          <option value="topics-7">⑦ 보안 운영/대응</option>
          <option value="topics-8">⑧ 디지털 포렌식</option>
          <option value="topics-9">⑨ 개인정보 보호</option>
          <option value="topics-10">⑩ 보안 정책/표준</option>
          <option value="topics-11">⑪ 개발보안/운영보안</option>
          <option value="topics-12">⑫ 보안 트렌드</option>
          <option value="exam-1">기출 · 1교시</option>
          <option value="exam-2">기출 · 2교시</option>
        </select>
      </label>

      <label class="sec-deck__label">
        검색
        <input id="secDeckSearch" class="sec-deck__input sec-deck__input--wide" type="text" placeholder="예: 랜섬웨어 / ISMS / 암호화">
      </label>
    </div>

    <div class="sec-deck__row sec-deck__row--meta">
      <div class="sec-deck__meta">
        <span id="secDeckStatus">로딩 중…</span>
        <span class="sec-deck__kbd">⌨️ ↑/↓ 이동 · Enter 원문</span>
      </div>
      <div class="sec-deck__nav-links">
        <a class="sec-deck__nav-pill" href="{{ site.baseurl }}/docs/sec/exam">📝 기출 테이블</a>
        <a class="sec-deck__nav-pill" href="{{ site.baseurl }}/docs/sec">🏠 SEC 메인</a>
      </div>
    </div>
  </div>

  <div class="sec-deck__layout">
    <aside class="sec-deck__list" aria-label="항목 목록">
      <div id="secDeckList" class="sec-deck__items"></div>
    </aside>

    <section class="sec-deck__detail" aria-label="선택 항목 상세">
      <div class="sec-deck__detail-head">
        <div class="sec-deck__tag" id="secDeckTag">-</div>
        <div class="sec-deck__title" id="secDeckTitle">항목을 선택하세요</div>
        <div class="sec-deck__detail-actions">
          <button type="button" class="sec-deck__btn" id="secDeckPrev">↑ 이전</button>
          <button type="button" class="sec-deck__btn sec-deck__btn--primary" id="secDeckNext">↓ 다음</button>
          <a class="sec-deck__btn sec-deck__btn--ghost" id="secDeckOpenLink" href="#" target="_blank" rel="noopener">원문 보기</a>
          <button type="button" class="sec-deck__btn sec-deck__btn--ghost" id="secDeckMarkHard">어려움(⭐)</button>
        </div>
      </div>

      <div class="sec-deck__panes">
        <div class="sec-deck__pane">
          <div class="sec-deck__pane-title">개념 정의(한 줄)</div>
          <div class="sec-deck__pane-body" id="secDeckDefinition">-</div>
        </div>
        <div class="sec-deck__pane">
          <div class="sec-deck__pane-title">구성요소(표)</div>
          <div class="sec-deck__pane-body" id="secDeckComponents">-</div>
        </div>
        <div class="sec-deck__pane sec-deck__pane--wide">
          <div class="sec-deck__pane-title">암기법/핵심 구문</div>
          <div class="sec-deck__pane-body" id="secDeckMnemonic">-</div>
        </div>
      </div>

      <div class="sec-deck__footer">
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
.sec-deck { margin-top: 1rem; }
.sec-deck__toolbar { border: 1px solid rgba(15, 23, 42, 0.10); border-radius: 14px; padding: 12px; background: rgba(248, 250, 252, 0.72); }
.sec-deck__row { display: flex; gap: 10px; flex-wrap: wrap; align-items: center; justify-content: space-between; }
.sec-deck__row--meta { margin-top: 8px; }
.sec-deck__label { display: inline-flex; gap: 8px; align-items: center; font-size: 12px; font-weight: 900; color: rgba(15, 23, 42, 0.82); }
.sec-deck__select, .sec-deck__input { border: 1px solid rgba(15, 23, 42, 0.14); border-radius: 10px; padding: 6px 10px; background: #fff; font-size: 13px; }
.sec-deck__input { width: 150px; }
.sec-deck__input--wide { width: 260px; }
.sec-deck__btn { border: 1px solid rgba(15, 23, 42, 0.14); background: #fff; border-radius: 12px; padding: 8px 12px; font-size: 13px; font-weight: 900; letter-spacing: -0.2px; cursor: pointer; text-decoration: none !important; display: inline-flex; align-items: center; justify-content: center; }
.sec-deck__btn:hover { background: rgba(226, 232, 240, 0.70); }
.sec-deck__btn--primary { background: linear-gradient(135deg, #dc2626, #ef4444); color: #fff; border-color: rgba(15, 23, 42, 0.10); }
.sec-deck__btn--primary:hover { filter: brightness(0.98); }
.sec-deck__btn--ghost { background: rgba(255, 255, 255, 0.65); }
.sec-deck__nav-links { display: flex; gap: 8px; }
.sec-deck__nav-pill { display: inline-flex; align-items: center; gap: 4px; padding: 6px 14px; border-radius: 20px; background: linear-gradient(135deg, rgba(220, 38, 38, 0.08), rgba(239, 68, 68, 0.12)); border: 1px solid rgba(220, 38, 38, 0.22); font-size: 12px; font-weight: 800; color: #b91c1c; text-decoration: none !important; transition: all 0.15s ease; }
.sec-deck__nav-pill:hover { background: linear-gradient(135deg, rgba(220, 38, 38, 0.16), rgba(239, 68, 68, 0.22)); border-color: rgba(220, 38, 38, 0.36); color: #991b1b; transform: translateY(-1px); box-shadow: 0 2px 8px rgba(220, 38, 38, 0.18); }
.sec-deck__meta { display: flex; gap: 12px; align-items: center; font-size: 12px; font-weight: 900; color: rgba(15, 23, 42, 0.76); width: 100%; justify-content: space-between; }
.sec-deck__kbd { font-weight: 900; color: rgba(15, 23, 42, 0.62); }

.sec-deck__layout { margin-top: 12px; display: grid; gap: 12px; grid-template-columns: 360px 1fr; align-items: start; }
@media (max-width: 66.49rem) {
  .sec-deck__layout { grid-template-columns: 1fr; }
  .sec-deck__input--wide { width: 100%; }
}

.sec-deck__list { border: 1px solid rgba(15, 23, 42, 0.10); border-radius: 14px; background: #fff; overflow: hidden; }
.sec-deck__items { max-height: calc(100vh - 280px); overflow: auto; }
@media (max-width: 66.49rem) { .sec-deck__items { max-height: 44vh; } }

.sec-deck__item { display: grid; gap: 6px; padding: 10px 10px; border-bottom: 1px solid rgba(15, 23, 42, 0.08); cursor: pointer; }
.sec-deck__item:hover { background: rgba(248, 250, 252, 0.85); }
.sec-deck__item.is-active { background: rgba(254, 226, 226, 0.30); }
.sec-deck__item-title { font-size: 13px; font-weight: 900; letter-spacing: -0.2px; color: rgba(15, 23, 42, 0.90); }
.sec-deck__item-tagline { display: flex; gap: 8px; align-items: center; justify-content: space-between; }
.sec-deck__pill { display: inline-flex; align-items: center; padding: 3px 8px; border-radius: 999px; font-size: 12px; font-weight: 900; color: rgba(15, 23, 42, 0.82); background: rgba(226, 232, 240, 0.75); border: 1px solid rgba(15, 23, 42, 0.10); }
.sec-deck__pill--hard { background: rgba(254, 202, 202, 0.60); border-color: rgba(239, 68, 68, 0.22); color: rgba(127, 29, 29, 0.92); }

.sec-deck__detail { border: 1px solid rgba(15, 23, 42, 0.10); border-radius: 14px; background: #fff; padding: 12px; }
.sec-deck__detail-head { display: grid; gap: 10px; border-bottom: 1px solid rgba(15, 23, 42, 0.10); padding-bottom: 10px; margin-bottom: 10px; }
.sec-deck__tag { display: inline-flex; width: fit-content; align-items: center; padding: 4px 10px; border-radius: 999px; font-size: 12px; font-weight: 900; color: rgba(15, 23, 42, 0.86); background: rgba(226, 232, 240, 0.75); border: 1px solid rgba(15, 23, 42, 0.10); }
.sec-deck__title { font-size: 20px; font-weight: 900; letter-spacing: -0.4px; color: #0f172a; line-height: 1.3; }
.sec-deck__detail-actions { display: flex; gap: 10px; flex-wrap: wrap; }

.sec-deck__panes { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }
.sec-deck__pane { border: 1px solid rgba(15, 23, 42, 0.08); border-radius: 12px; background: rgba(248, 250, 252, 0.65); padding: 10px; }
.sec-deck__pane--wide { grid-column: 1 / -1; }
.sec-deck--exam .sec-deck__panes { grid-template-columns: 1fr; }
.sec-deck--exam .sec-deck__pane:not(.sec-deck__pane--wide) { display: none; }
.sec-deck--exam .sec-deck__pane--wide { grid-column: auto; }
.sec-deck__pane-title { font-size: 12px; font-weight: 900; color: rgba(15, 23, 42, 0.75); margin-bottom: 6px; }
.sec-deck__pane-body { font-size: 13px; line-height: 1.5; color: rgba(15, 23, 42, 0.92); }
.sec-deck__pane-body code { font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace; font-size: 12px; padding: 2px 6px; border-radius: 8px; background: rgba(254, 226, 226, 0.55); border: 1px solid rgba(239, 68, 68, 0.18); color: #b91c1c; margin-right: 6px; display: inline-block; margin-bottom: 6px; }
.sec-deck__pane-body table { width: 100% !important; font-size: 12px; }
.sec-deck__pane-body table td, .sec-deck__pane-body table th { padding: 6px 8px; white-space: normal; }
.sec-deck__pane-body table thead th { white-space: nowrap; }
.sec-deck__pane-body .highlight-purple { background: rgba(254, 226, 226, 0.45); border-radius: 10px; padding: 8px; }
.sec-deck__footer { margin-top: 10px; }
</style>

<script>
(function() {
  var root = document.getElementById('secDeckRoot');
  if (!root) return;

  var examUrl = root.getAttribute('data-exam-url');
  var topicsUrl = root.getAttribute('data-topics-url');

  var elStatus = document.getElementById('secDeckStatus');
  var elMode = document.getElementById('secDeckMode');
  var elSearch = document.getElementById('secDeckSearch');

  var elList = document.getElementById('secDeckList');
  var elTag = document.getElementById('secDeckTag');
  var elTitle = document.getElementById('secDeckTitle');
  var elDef = document.getElementById('secDeckDefinition');
  var elComponents = document.getElementById('secDeckComponents');
  var elMnemonic = document.getElementById('secDeckMnemonic');
  var elOpenLink = document.getElementById('secDeckOpenLink');

  // Pane refs (exam cards show only Quick Reference)
  var paneDef = elDef && elDef.closest ? elDef.closest('.sec-deck__pane') : null;
  var paneComponents = elComponents && elComponents.closest ? elComponents.closest('.sec-deck__pane') : null;
  var paneMnemonic = elMnemonic && elMnemonic.closest ? elMnemonic.closest('.sec-deck__pane') : null;
  var paneMnemonicTitle = paneMnemonic ? paneMnemonic.querySelector('.sec-deck__pane-title') : null;
  var mnemonicTitleDefault = paneMnemonicTitle ? paneMnemonicTitle.textContent : '암기법/핵심 구문';

  var btnPrev = document.getElementById('secDeckPrev');
  var btnNext = document.getElementById('secDeckNext');
  var btnHard = document.getElementById('secDeckMarkHard');

  var STORAGE_PREFIX = 'peSecDeck:v1:';

  var examRows = [];
  var topicRows = [];

  var cardsAll = [];
  var cards = [];
  var idx = 0;
  var hardSet = new Set();
  var pageCache = new Map();

  function safeGet(key, fallback) {
    try { var v = localStorage.getItem(key); if (!v) return fallback; return JSON.parse(v); } catch (e) { return fallback; }
  }
  function safeSet(key, val) {
    try { localStorage.setItem(key, JSON.stringify(val)); } catch (e) {}
  }
  function normalizeText(s) { return (s || '').replace(/\s+/g, ' ').trim(); }
  function shortParentLabel(s) { var t = normalizeText(s || ''); t = t.replace(/^\d+\.\s*/, ''); return t; }
  function cardKey(c) { return [c.kind, c.url || c.title].join('|'); }
  function renderDefinition(s) { var t = normalizeText(s || ''); if (!t) return '-'; return escapeHtml(t); }
  function escapeHtml(s) { return String(s || '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/\"/g, '&quot;').replace(/'/g, '&#39;'); }
  function setStatus() { elStatus.textContent = (cards.length ? (idx + 1) + ' / ' + cards.length : '0') + ' · 후보 ' + cardsAll.length; }

  function topicGroupForUrl(url) {
    if (!url) return 'etc';
    if (url.indexOf('/docs/sec/05-cyber-attack/') >= 0) return '1';
    if (url.indexOf('/docs/sec/06-vulnerability/') >= 0) return '2';
    if (url.indexOf('/docs/sec/01-cryptography/') >= 0) return '3';
    if (url.indexOf('/docs/sec/02-iam/') >= 0) return '4';
    if (url.indexOf('/docs/sec/03-network-security/') >= 0) return '5';
    if (url.indexOf('/docs/sec/04-cloud-iot-smart/') >= 0) return '6';
    if (url.indexOf('/docs/sec/07-security-operations/') >= 0) return '7';
    if (url.indexOf('/docs/sec/08-digital-forensics/') >= 0) return '8';
    if (url.indexOf('/docs/sec/09-privacy/') >= 0) return '9';
    if (url.indexOf('/docs/sec/10-policy-standard/') >= 0) return '10';
    if (url.indexOf('/docs/sec/11-devsecops/') >= 0) return '11';
    if (url.indexOf('/docs/sec/12-security-trends/') >= 0) return '12';
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

    for (var i = 1; i <= 12; i++) {
      if (mode === 'topics-' + i) base = base.filter(function(c) { return topicGroupForUrl(c.url) === String(i); });
    }

    if (q) {
      base = base.filter(function(c) {
        return (c.title || '').toLowerCase().includes(q) || (c.parent || '').toLowerCase().includes(q) || (c.mnemonic_text || '').toLowerCase().includes(q);
      });
    }

    function toInt(x, fallback) { var n = parseInt(String(x || ''), 10); return isFinite(n) ? n : (fallback || 0); }

    base.sort(function(a, b) {
      if (a.kind === 'topic' && b.kind === 'topic') {
        var ao = toInt(a.nav_order, 9999); var bo = toInt(b.nav_order, 9999);
        if (ao !== bo) return ao - bo;
        return String(a.title || '').localeCompare(String(b.title || ''), 'ko');
      }
      if (a.kind === 'exam' && b.kind === 'exam') {
        var ar = toInt(a.round, 0); var br = toInt(b.round, 0); if (ar !== br) return br - ar;
        var as = toInt(a.session, 0); var bs = toInt(b.session, 0); if (as !== bs) return as - bs;
        var an = toInt(a.no, 0); var bn = toInt(b.no, 0); return an - bn;
      }
      return String(a.kind).localeCompare(String(b.kind));
    });

    cards = base;
    idx = 0;
    renderList();
    selectIndex(0, { scrollIntoView: true });
  }

  function renderList() {
    if (!cards.length) { elList.innerHTML = '<div class="sec-deck__item"><div class="sec-deck__item-title">결과가 없습니다.</div></div>'; setStatus(); clearDetail(); return; }
    var html = '';
    cards.forEach(function(c, i) {
      var hard = hardSet.has(cardKey(c));
      html += '<div class="sec-deck__item' + (i === idx ? ' is-active' : '') + '" data-idx="' + i + '">';
      html += '<div class="sec-deck__item-title">' + escapeHtml(c.title) + '</div>';
      html += '<div class="sec-deck__item-tagline">';
      html += '<span class="sec-deck__pill">' + escapeHtml(c.badge) + '</span>';
      html += (hard ? '<span class="sec-deck__pill sec-deck__pill--hard">⭐</span>' : '<span class="sec-deck__pill" style="opacity:.55"> </span>');
      html += '</div></div>';
    });
    elList.innerHTML = html;
    setStatus();
    Array.prototype.forEach.call(elList.querySelectorAll('.sec-deck__item[data-idx]'), function(node) {
      node.addEventListener('click', function() { var i = parseInt(node.getAttribute('data-idx') || '0', 10); selectIndex(i, { scrollIntoView: false }); });
    });
  }

  function clearDetail() { elTag.textContent = '-'; elTitle.textContent = '항목을 선택하세요'; elDef.innerHTML = '-'; elComponents.innerHTML = '-'; elMnemonic.innerHTML = '-'; elOpenLink.setAttribute('href', '#'); }
  function updateActiveRow() { Array.prototype.forEach.call(elList.querySelectorAll('.sec-deck__item[data-idx]'), function(node) { var i = parseInt(node.getAttribute('data-idx') || '0', 10); if (i === idx) node.classList.add('is-active'); else node.classList.remove('is-active'); }); }

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
    if (root && root.classList) root.classList.toggle('sec-deck--exam', isExam);

    // exam: show only Quick Reference pane
    if (paneDef) paneDef.style.display = isExam ? 'none' : '';
    if (paneComponents) paneComponents.style.display = isExam ? 'none' : '';
    if (paneMnemonic) {
      if (isExam) paneMnemonic.classList.remove('sec-deck__pane--wide');
      else paneMnemonic.classList.add('sec-deck__pane--wide');
    }
    if (paneMnemonicTitle) paneMnemonicTitle.textContent = isExam ? '핵심 암기 (Quick Reference)' : mnemonicTitleDefault;

    // Fast-fill: topics use mnemonic, exams wait for page extract
    elMnemonic.innerHTML = isExam ? '불러오는 중…' : (c.mnemonic_html || (c.mnemonic_text ? escapeHtml(c.mnemonic_text) : '-'));
    elDef.innerHTML = '-';
    elComponents.innerHTML = '-';
    hydrateFromPage(c);
    if (opts && opts.scrollIntoView) { var active = elList.querySelector('.sec-deck__item.is-active'); if (active && active.scrollIntoView) active.scrollIntoView({ block: 'nearest' }); }
  }

  function markHard() { if (!cards.length) return; var c = cards[idx]; var k = cardKey(c); if (hardSet.has(k)) hardSet.delete(k); else hardSet.add(k); safeSet(STORAGE_PREFIX + 'hard', Array.from(hardSet)); renderList(); updateActiveRow(); selectIndex(idx, { scrollIntoView: false }); }

  function parseExamHtml(htmlText) {
    var parser = new DOMParser(); var doc = parser.parseFromString(htmlText, 'text/html'); var rows = doc.querySelectorAll('#examTable tbody tr'); var out = [];
    rows.forEach(function(tr) { var tds = tr.querySelectorAll('td'); if (!tds || tds.length < 7) return; var a = tds[4].querySelector('a'); if (!a) return; var mnemonicText = normalizeText(tds[6].textContent); if (!mnemonicText || mnemonicText === '-') return;
      out.push({ kind: 'exam', round: normalizeText(tds[0].textContent), dept: normalizeText(tds[1].textContent), session: normalizeText(tds[2].textContent), no: normalizeText(tds[3].textContent), title: normalizeText(a.textContent), url: a.getAttribute('href') || '', badge: normalizeText(tds[0].textContent) + '회 · ' + normalizeText(tds[2].textContent) + '교시 · ' + normalizeText(tds[3].textContent) + '번', mnemonic_text: mnemonicText, mnemonic_html: (tds[6].innerHTML || '').trim() });
    });
    return out;
  }

  function findHeading(doc, keyword) { var headings = Array.prototype.slice.call(doc.querySelectorAll('h1,h2,h3,h4')); return headings.find(function(h) { return normalizeText(h.textContent).includes(keyword); }) || null; }
  function extractDefinition(doc) { var h = findHeading(doc, '개념 정의') || findHeading(doc, '개념') || findHeading(doc, '정의'); if (!h) return ''; var el = h.nextElementSibling; while (el && el.tagName === 'HR') el = el.nextElementSibling; if (!el) return ''; if (el.tagName === 'TABLE') { var firstRow = el.querySelector('tbody tr'); if (!firstRow) return ''; var tds = firstRow.querySelectorAll('td'); if (tds && tds.length >= 2) return normalizeText(tds[1].textContent); return normalizeText(firstRow.textContent); } if (el.tagName === 'BLOCKQUOTE') return normalizeText(el.textContent); return normalizeText(el.textContent); }
  function extractComponentsTables(doc) { var h = findHeading(doc, '구성요소') || findHeading(doc, '기술요소'); if (!h) return ''; var el = h.nextElementSibling; var tables = []; var guard = 0; while (el && guard < 50) { if (/^H[1-6]$/.test(el.tagName)) break; if (el.tagName === 'TABLE') tables.push(el); var innerTables = el.querySelectorAll ? el.querySelectorAll('table') : []; if (innerTables && innerTables.length) innerTables.forEach(function(t) { if (tables.indexOf(t) === -1) tables.push(t); }); if (tables.length >= 2) break; el = el.nextElementSibling; guard += 1; } if (!tables.length) return ''; return tables.slice(0, 2).map(function(t) { return t.outerHTML; }).join('\n'); }
  function normalizeMnemonicFallback(doc) { var headings = Array.prototype.slice.call(doc.querySelectorAll('h1,h2,h3,h4')); var target = headings.find(function(h) { return normalizeText(h.textContent).includes('암기'); }); if (!target) return null; var el = target.nextElementSibling; var tries = 0; while (el && tries < 6) { var codes = el.querySelectorAll ? el.querySelectorAll('code') : []; if (codes && codes.length) return el.innerHTML.trim(); if (el.tagName === 'TABLE') return el.outerHTML; el = el.nextElementSibling; tries += 1; } return null; }

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
    if (pageCache.has(card.url)) { applyExtracted(pageCache.get(card.url)); return; }
    var isExam = card.kind === 'exam';
    if (!isExam) { elDef.innerHTML = '불러오는 중…'; elComponents.innerHTML = '불러오는 중…'; }
    fetch(card.url, { credentials: 'same-origin' }).then(function(res) { return res.text(); }).then(function(html) {
      var parser = new DOMParser(); var doc = parser.parseFromString(html, 'text/html');
      var quickrefHtml = extractQuickReferenceHtml(doc);
      var definition = isExam ? '' : extractDefinition(doc);
      var componentsHtml = isExam ? '' : extractComponentsTables(doc);
      var mnemonic = card.mnemonic_html || normalizeMnemonicFallback(doc) || '';
      var payload = { url: card.url, quickref_html: quickrefHtml, definition: definition, components_html: componentsHtml, mnemonic_html: mnemonic };
      pageCache.set(card.url, payload); applyExtracted(payload);
    }).catch(function() {
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
    if (!cur.mnemonic_html || cur.mnemonic_text === '-' || !cur.mnemonic_text) { if (payload.mnemonic_html) elMnemonic.innerHTML = payload.mnemonic_html; }
  }

  function loadSources() {
    elStatus.textContent = '데이터 로딩…';
    return Promise.all([
      fetch(examUrl, { credentials: 'same-origin' }).then(function(r) { return r.text(); }).then(function(t) { examRows = parseExamHtml(t); }),
      fetch(topicsUrl, { credentials: 'same-origin' }).then(function(r) { return r.json(); }).then(function(j) {
        topicRows = (Array.isArray(j) ? j : []).map(function(p) { return { kind: 'topic', title: normalizeText(p.title), url: p.url, parent: p.parent, grand_parent: p.grand_parent, badge: shortParentLabel(p.parent || 'SEC 토픽'), nav_order: p.nav_order, mnemonic_text: '' }; });
      })
    ]);
  }

  function init() {
    try { var params = new URLSearchParams(window.location.search || ''); var qsDeck = params.get('deck') || params.get('mode'); if (qsDeck && elMode.querySelector('option[value="' + qsDeck + '"]')) { elMode.value = qsDeck; safeSet(STORAGE_PREFIX + 'prefs', { mode: qsDeck, search: '' }); } } catch (e) {}
    var prefs = safeGet(STORAGE_PREFIX + 'prefs', {}); if (prefs && typeof prefs === 'object') { if (prefs.mode) elMode.value = prefs.mode; if (prefs.search) elSearch.value = String(prefs.search); }
    var hardSaved = safeGet(STORAGE_PREFIX + 'hard', []); hardSet = new Set(Array.isArray(hardSaved) ? hardSaved : []);
    loadSources().then(function() { cardsAll = examRows.concat(topicRows); elStatus.textContent = '준비 완료'; applyModeAndSearch(); }).catch(function(err) { elStatus.textContent = '로딩 실패: ' + (err && err.message ? err.message : 'unknown'); clearDetail(); });
    elMode.addEventListener('change', function() { safeSet(STORAGE_PREFIX + 'prefs', { mode: elMode.value, search: elSearch.value }); applyModeAndSearch(); });
    elSearch.addEventListener('input', function() { safeSet(STORAGE_PREFIX + 'prefs', { mode: elMode.value, search: elSearch.value }); if (window.__secDeckSearchTimer) clearTimeout(window.__secDeckSearchTimer); window.__secDeckSearchTimer = setTimeout(applyModeAndSearch, 180); });
    btnPrev.addEventListener('click', function() { selectIndex(idx - 1, { scrollIntoView: true }); });
    btnNext.addEventListener('click', function() { selectIndex(idx + 1, { scrollIntoView: true }); });
    btnHard.addEventListener('click', function(e) { e.preventDefault(); markHard(); });
    window.addEventListener('keydown', function(e) { if (e.defaultPrevented) return; var ae = document.activeElement; if (ae) { var tag = (ae.tagName || '').toLowerCase(); if (tag === 'input' || tag === 'textarea' || tag === 'select') return; if (ae.isContentEditable) return; } if (e.key === 'ArrowDown') { e.preventDefault(); selectIndex(idx + 1, { scrollIntoView: true }); } if (e.key === 'ArrowUp') { e.preventDefault(); selectIndex(idx - 1, { scrollIntoView: true }); } if (e.key === 'Enter') { var cur = cards[idx]; if (cur && cur.url) window.open(cur.url, '_blank', 'noopener'); } });
  }

  init();
})();
</script>

