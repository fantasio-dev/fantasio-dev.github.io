---
layout: default
title: 🃏 데일리 암기 덱 (AI)
parent: AI (인공지능)
nav_order: 1
has_toc: false
permalink: /docs/ai/daily
---

# 🃏 데일리 암기 덱 (AI)
{: .no_toc }

**AI 전체 토픽 + 기출문제(1교시/2교시)**를 “노트 넘기기”처럼 보는 모드입니다.  
왼쪽에서 항목을 고르면, 오른쪽에 **핵심(암기/키워드)**가 바로 펼쳐져서 *뒤집기 없이* 매일 보기 좋게 설계했습니다.

<div class="ai-deck2" id="aiDeckRoot"
  data-exam-url="{{ site.baseurl }}/docs/ai/exam"
  data-topics-url="{{ site.baseurl }}/docs/ai/topics.json">

  <div class="ai-deck2__toolbar">
    <div class="ai-deck2__row">
      <label class="ai-deck2__label">
        덱
        <select id="aiDeckMode" class="ai-deck2__select">
          <option value="topics" selected>AI 토픽 전체</option>
          <option value="exam-1">기출 1교시</option>
          <option value="exam-2">기출 2교시</option>
        </select>
      </label>

      <label class="ai-deck2__label">
        오늘 N개
        <input id="aiDeckLimit" class="ai-deck2__input" type="number" min="10" max="300" step="10" value="40">
      </label>

      <label class="ai-deck2__label">
        검색
        <input id="aiDeckSearch" class="ai-deck2__input ai-deck2__input--wide" type="text" placeholder="예: Transformer / ROC / Dropout">
      </label>

      <button type="button" class="ai-deck2__btn" id="aiDeckShuffle">셔플</button>
      <button type="button" class="ai-deck2__btn ai-deck2__btn--ghost" id="aiDeckReset">리셋</button>

      <a class="ai-deck2__link" href="{{ site.baseurl }}/docs/ai/exam">기출 테이블</a>
      <a class="ai-deck2__link" href="{{ site.baseurl }}/docs/ai">AI 메인</a>
    </div>

    <div class="ai-deck2__row ai-deck2__row--meta">
      <div class="ai-deck2__meta">
        <span id="aiDeckStatus">로딩 중…</span>
        <span class="ai-deck2__kbd">⌨️ ↑/↓ 이동 · Enter 열기</span>
      </div>
    </div>
  </div>

  <div class="ai-deck2__layout">
    <aside class="ai-deck2__list" aria-label="항목 목록">
      <div id="aiDeckList" class="ai-deck2__items"></div>
    </aside>

    <section class="ai-deck2__detail" aria-label="선택 항목 상세">
      <div class="ai-deck2__detail-head">
        <div class="ai-deck2__tag" id="aiDeckTag">-</div>
        <div class="ai-deck2__title" id="aiDeckTitle">항목을 선택하세요</div>
        <div class="ai-deck2__detail-actions">
          <button type="button" class="ai-deck2__btn" id="aiDeckPrev">↑ 이전</button>
          <button type="button" class="ai-deck2__btn ai-deck2__btn--primary" id="aiDeckNext">↓ 다음</button>
          <a class="ai-deck2__btn ai-deck2__btn--ghost" id="aiDeckOpenLink" href="#" target="_blank" rel="noopener">원문 보기</a>
          <button type="button" class="ai-deck2__btn ai-deck2__btn--ghost" id="aiDeckMarkHard">어려움(⭐)</button>
        </div>
      </div>

      <div class="ai-deck2__panes">
        <div class="ai-deck2__pane">
          <div class="ai-deck2__pane-title">핵심 암기(Quick Reference)</div>
          <div class="ai-deck2__pane-body" id="aiDeckQuickRef">-</div>
        </div>
        <div class="ai-deck2__pane">
          <div class="ai-deck2__pane-title">핵심 키워드</div>
          <div class="ai-deck2__pane-body" id="aiDeckKeywords">-</div>
        </div>
        <div class="ai-deck2__pane ai-deck2__pane--wide">
          <div class="ai-deck2__pane-title">암기법/핵심 구문</div>
          <div class="ai-deck2__pane-body" id="aiDeckMnemonic">-</div>
        </div>
      </div>

      <div class="ai-deck2__footer">
        <details>
          <summary><strong>팁</strong> (클릭)</summary>
          <ul>
            <li><strong>루틴</strong>: 오늘 N개를 정하고, 목록을 위아래로 쭉 훑는 방식이 노트 넘기기와 가장 유사합니다.</li>
            <li><strong>키워드/암기</strong>가 비어있으면 해당 페이지 템플릿을 통일하면(지금처럼) 자동 추출 정확도가 올라갑니다.</li>
          </ul>
        </details>
      </div>
    </section>
  </div>
</div>

<style>
/* Page-scoped deck styles */
.ai-deck2 { margin-top: 1rem; }
.ai-deck2__toolbar { border: 1px solid rgba(15, 23, 42, 0.10); border-radius: 14px; padding: 12px; background: rgba(248, 250, 252, 0.72); }
.ai-deck2__row { display: flex; gap: 10px; flex-wrap: wrap; align-items: center; justify-content: space-between; }
.ai-deck2__row--meta { margin-top: 8px; }
.ai-deck2__label { display: inline-flex; gap: 8px; align-items: center; font-size: 12px; font-weight: 900; color: rgba(15, 23, 42, 0.82); }
.ai-deck2__select, .ai-deck2__input { border: 1px solid rgba(15, 23, 42, 0.14); border-radius: 10px; padding: 6px 10px; background: #fff; font-size: 13px; }
.ai-deck2__input { width: 110px; }
.ai-deck2__input--wide { width: 260px; }
.ai-deck2__btn { border: 1px solid rgba(15, 23, 42, 0.14); background: #fff; border-radius: 12px; padding: 8px 12px; font-size: 13px; font-weight: 900; letter-spacing: -0.2px; cursor: pointer; text-decoration: none !important; display: inline-flex; align-items: center; justify-content: center; }
.ai-deck2__btn:hover { background: rgba(226, 232, 240, 0.70); }
.ai-deck2__btn--primary { background: linear-gradient(135deg, #4f46e5, #7c3aed); color: #fff; border-color: rgba(15, 23, 42, 0.10); }
.ai-deck2__btn--primary:hover { filter: brightness(0.98); }
.ai-deck2__btn--ghost { background: rgba(255, 255, 255, 0.65); }
.ai-deck2__link { font-size: 13px; font-weight: 900; text-decoration: none !important; color: #1d4ed8; }
.ai-deck2__link:hover { text-decoration: underline !important; }
.ai-deck2__meta { display: flex; gap: 12px; align-items: center; font-size: 12px; font-weight: 900; color: rgba(15, 23, 42, 0.76); width: 100%; justify-content: space-between; }
.ai-deck2__kbd { font-weight: 900; color: rgba(15, 23, 42, 0.62); }

.ai-deck2__layout { margin-top: 12px; display: grid; gap: 12px; grid-template-columns: 360px 1fr; align-items: start; }
@media (max-width: 66.49rem) {
  .ai-deck2__layout { grid-template-columns: 1fr; }
  .ai-deck2__input--wide { width: 100%; }
}

.ai-deck2__list { border: 1px solid rgba(15, 23, 42, 0.10); border-radius: 14px; background: #fff; overflow: hidden; }
.ai-deck2__items { max-height: calc(100vh - 280px); overflow: auto; }
@media (max-width: 66.49rem) { .ai-deck2__items { max-height: 44vh; } }

.ai-deck2__item { display: grid; gap: 6px; padding: 10px 10px; border-bottom: 1px solid rgba(15, 23, 42, 0.08); cursor: pointer; }
.ai-deck2__item:hover { background: rgba(248, 250, 252, 0.85); }
.ai-deck2__item.is-active { background: rgba(233, 213, 255, 0.30); }
.ai-deck2__item-title { font-size: 13px; font-weight: 900; letter-spacing: -0.2px; color: rgba(15, 23, 42, 0.90); }
.ai-deck2__item-tagline { display: flex; gap: 8px; align-items: center; justify-content: space-between; }
.ai-deck2__pill { display: inline-flex; align-items: center; padding: 3px 8px; border-radius: 999px; font-size: 12px; font-weight: 900; color: rgba(15, 23, 42, 0.82); background: rgba(226, 232, 240, 0.75); border: 1px solid rgba(15, 23, 42, 0.10); }
.ai-deck2__pill--hard { background: rgba(254, 202, 202, 0.60); border-color: rgba(239, 68, 68, 0.22); color: rgba(127, 29, 29, 0.92); }

.ai-deck2__detail { border: 1px solid rgba(15, 23, 42, 0.10); border-radius: 14px; background: #fff; padding: 12px; }
.ai-deck2__detail-head { display: grid; gap: 10px; border-bottom: 1px solid rgba(15, 23, 42, 0.10); padding-bottom: 10px; margin-bottom: 10px; }
.ai-deck2__tag { display: inline-flex; width: fit-content; align-items: center; padding: 4px 10px; border-radius: 999px; font-size: 12px; font-weight: 900; color: rgba(15, 23, 42, 0.86); background: rgba(226, 232, 240, 0.75); border: 1px solid rgba(15, 23, 42, 0.10); }
.ai-deck2__title { font-size: 20px; font-weight: 900; letter-spacing: -0.4px; color: #0f172a; line-height: 1.3; }
.ai-deck2__detail-actions { display: flex; gap: 10px; flex-wrap: wrap; }

.ai-deck2__panes { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }
.ai-deck2__pane { border: 1px solid rgba(15, 23, 42, 0.08); border-radius: 12px; background: rgba(248, 250, 252, 0.65); padding: 10px; }
.ai-deck2__pane--wide { grid-column: 1 / -1; }
.ai-deck2__pane-title { font-size: 12px; font-weight: 900; color: rgba(15, 23, 42, 0.75); margin-bottom: 6px; }
.ai-deck2__pane-body { font-size: 13px; line-height: 1.5; color: rgba(15, 23, 42, 0.92); }
.ai-deck2__pane-body code { font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace; font-size: 12px; padding: 2px 6px; border-radius: 8px; background: rgba(245, 243, 255, 0.85); border: 1px solid rgba(124, 58, 237, 0.18); color: #6d28d9; margin-right: 6px; display: inline-block; margin-bottom: 6px; }
.ai-deck2__kw { display: flex; flex-wrap: wrap; gap: 6px; }
.ai-deck2__kw span { display: inline-flex; padding: 4px 8px; border-radius: 999px; font-size: 12px; font-weight: 900; background: #fff; border: 1px solid rgba(15, 23, 42, 0.10); color: rgba(15, 23, 42, 0.86); }
.ai-deck2__footer { margin-top: 10px; }
</style>

<script>
(function() {
  var root = document.getElementById('aiDeckRoot');
  if (!root) return;

  var examUrl = root.getAttribute('data-exam-url');
  var topicsUrl = root.getAttribute('data-topics-url');

  var elStatus = document.getElementById('aiDeckStatus');
  var elMode = document.getElementById('aiDeckMode');
  var elLimit = document.getElementById('aiDeckLimit');
  var elSearch = document.getElementById('aiDeckSearch');

  var elList = document.getElementById('aiDeckList');
  var elTag = document.getElementById('aiDeckTag');
  var elTitle = document.getElementById('aiDeckTitle');
  var elQuick = document.getElementById('aiDeckQuickRef');
  var elKeywords = document.getElementById('aiDeckKeywords');
  var elMnemonic = document.getElementById('aiDeckMnemonic');
  var elOpenLink = document.getElementById('aiDeckOpenLink');

  var btnPrev = document.getElementById('aiDeckPrev');
  var btnNext = document.getElementById('aiDeckNext');
  var btnShuffle = document.getElementById('aiDeckShuffle');
  var btnReset = document.getElementById('aiDeckReset');
  var btnHard = document.getElementById('aiDeckMarkHard');

  var STORAGE_PREFIX = 'peAiDeck2:v1:';

  var examRows = [];
  var topicRows = [];

  var cardsAll = [];
  var cards = [];
  var idx = 0;
  var hardSet = new Set();
  var pageCache = new Map(); // url -> extracted payload

  function todayKey() {
    var d = new Date();
    var yyyy = String(d.getFullYear());
    var mm = String(d.getMonth() + 1).padStart(2, '0');
    var dd = String(d.getDate()).padStart(2, '0');
    return yyyy + mm + dd;
  }

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

  function shuffleInPlace(arr) {
    for (var i = arr.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var tmp = arr[i]; arr[i] = arr[j]; arr[j] = tmp;
    }
    return arr;
  }

  function cardKey(c) {
    return [c.kind, c.url || c.title].join('|');
  }

  function renderKeywords(list) {
    if (!list || !list.length) return '-';
    var html = '<div class="ai-deck2__kw">';
    list.slice(0, 12).forEach(function(k) {
      html += '<span>' + escapeHtml(k) + '</span>';
    });
    html += '</div>';
    return html;
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

  function applyModeAndSearch() {
    var mode = elMode.value;
    var limit = parseInt(elLimit.value || '40', 10);
    if (!isFinite(limit) || limit < 10) limit = 40;
    elLimit.value = String(limit);

    var q = normalizeText(elSearch.value).toLowerCase();

    var base = cardsAll.slice().filter(function(c) {
      if (mode === 'topics') return c.kind === 'topic';
      if (mode === 'exam-1') return c.kind === 'exam' && c.session === '1';
      if (mode === 'exam-2') return c.kind === 'exam' && c.session === '2';
      return true;
    });

    if (q) {
      base = base.filter(function(c) {
        return (c.title || '').toLowerCase().includes(q) ||
               (c.parent || '').toLowerCase().includes(q) ||
               (c.mnemonic_text || '').toLowerCase().includes(q);
      });
    }

    var day = todayKey();
    var orderKey = STORAGE_PREFIX + 'order:' + mode + ':' + day + ':' + q;
    var saved = safeGet(orderKey, null);
    if (saved && Array.isArray(saved) && saved.length) {
      var map = new Map(base.map(function(c) { return [cardKey(c), c]; }));
      var rebuilt = [];
      saved.forEach(function(k) { if (map.has(k)) rebuilt.push(map.get(k)); });
      base.forEach(function(c) { if (rebuilt.indexOf(c) === -1) rebuilt.push(c); });
      base = rebuilt;
    } else {
      base = shuffleInPlace(base);
      safeSet(orderKey, base.map(cardKey));
    }

    cards = base.slice(0, Math.min(limit, base.length));
    idx = 0;
    renderList();
    selectIndex(0, { scrollIntoView: true });
  }

  function renderList() {
    if (!cards.length) {
      elList.innerHTML = '<div class="ai-deck2__item"><div class="ai-deck2__item-title">결과가 없습니다.</div></div>';
      setStatus();
      clearDetail();
      return;
    }

    var html = '';
    cards.forEach(function(c, i) {
      var hard = hardSet.has(cardKey(c));
      html += '<div class="ai-deck2__item' + (i === idx ? ' is-active' : '') + '" data-idx="' + i + '">';
      html +=   '<div class="ai-deck2__item-title">' + escapeHtml(c.title) + '</div>';
      html +=   '<div class="ai-deck2__item-tagline">';
      html +=     '<span class="ai-deck2__pill">' + escapeHtml(c.badge) + '</span>';
      html +=     (hard ? '<span class="ai-deck2__pill ai-deck2__pill--hard">⭐</span>' : '<span class="ai-deck2__pill" style="opacity:.55"> </span>');
      html +=   '</div>';
      html += '</div>';
    });
    elList.innerHTML = html;
    setStatus();

    Array.prototype.forEach.call(elList.querySelectorAll('.ai-deck2__item[data-idx]'), function(node) {
      node.addEventListener('click', function() {
        var i = parseInt(node.getAttribute('data-idx') || '0', 10);
        selectIndex(i, { scrollIntoView: false });
      });
    });
  }

  function clearDetail() {
    elTag.textContent = '-';
    elTitle.textContent = '항목을 선택하세요';
    elQuick.innerHTML = '-';
    elKeywords.innerHTML = '-';
    elMnemonic.innerHTML = '-';
    elOpenLink.setAttribute('href', '#');
  }

  function updateActiveRow() {
    Array.prototype.forEach.call(elList.querySelectorAll('.ai-deck2__item[data-idx]'), function(node) {
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

    // Fast-fill mnemonic from index when available
    elMnemonic.innerHTML = c.mnemonic_html || (c.mnemonic_text ? escapeHtml(c.mnemonic_text) : '-');
    elQuick.innerHTML = '-';
    elKeywords.innerHTML = '-';

    // load page details (keywords/quickref)
    hydrateFromPage(c);

    if (opts && opts.scrollIntoView) {
      var active = elList.querySelector('.ai-deck2__item.is-active');
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
    // re-render tag badge to include star in header
    selectIndex(idx, { scrollIntoView: false });
  }

  function resetOrder() {
    var mode = elMode.value;
    var q = normalizeText(elSearch.value).toLowerCase();
    var day = todayKey();
    try { localStorage.removeItem(STORAGE_PREFIX + 'order:' + mode + ':' + day + ':' + q); } catch (e) {}
    applyModeAndSearch();
  }

  function manualShuffle() {
    var mode = elMode.value;
    var q = normalizeText(elSearch.value).toLowerCase();
    var day = todayKey();
    var orderKey = STORAGE_PREFIX + 'order:' + mode + ':' + day + ':' + q;

    var base = cardsAll.slice().filter(function(c) {
      if (mode === 'topics') return c.kind === 'topic';
      if (mode === 'exam-1') return c.kind === 'exam' && c.session === '1';
      if (mode === 'exam-2') return c.kind === 'exam' && c.session === '2';
      return true;
    });
    if (q) base = base.filter(function(c) { return (c.title || '').toLowerCase().includes(q); });
    base = shuffleInPlace(base);
    safeSet(orderKey, base.map(cardKey));
    applyModeAndSearch();
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
      out.push({
        kind: 'exam',
        round: normalizeText(tds[0].textContent),
        dept: normalizeText(tds[1].textContent),
        session: normalizeText(tds[2].textContent),
        no: normalizeText(tds[3].textContent),
        title: normalizeText(a.textContent),
        url: a.getAttribute('href') || '',
        badge: normalizeText(tds[0].textContent) + '회 · ' + normalizeText(tds[2].textContent) + '교시 · ' + normalizeText(tds[3].textContent) + '번',
        mnemonic_text: normalizeText(tds[6].textContent),
        mnemonic_html: (tds[6].innerHTML || '').trim()
      });
    });
    return out;
  }

  function normalizeKeywordsFromHeading(doc) {
    var headings = Array.prototype.slice.call(doc.querySelectorAll('h1,h2,h3,h4'));
    var target = headings.find(function(h) { return normalizeText(h.textContent).includes('핵심 키워드'); });
    if (!target) return [];

    // find next element that is table or list/paragraph
    var el = target.nextElementSibling;
    while (el && (el.tagName === 'HR' || el.tagName === 'P' && !normalizeText(el.textContent) || el.tagName === 'DIV' && !normalizeText(el.textContent))) {
      el = el.nextElementSibling;
    }

    if (!el) return [];

    if (el.tagName === 'TABLE') {
      var kws = [];
      var rows = el.querySelectorAll('tbody tr');
      rows.forEach(function(r) {
        var first = r.querySelector('td');
        if (first) {
          var t = normalizeText(first.textContent).replace(/^\*+|\*+$/g, '');
          if (t) kws.push(t);
        }
      });
      return kws;
    }

    // sometimes keywords are inline code ticks
    var codes = el.querySelectorAll('code');
    if (codes && codes.length) {
      var kw2 = [];
      codes.forEach(function(c) {
        var t2 = normalizeText(c.textContent);
        if (t2) kw2.push(t2);
      });
      return kw2;
    }

    // fallback: split by commas
    var txt = normalizeText(el.textContent);
    if (!txt) return [];
    return txt.split(',').map(function(s) { return normalizeText(s); }).filter(Boolean).slice(0, 8);
  }

  function normalizeQuickRefFromHeading(doc) {
    var headings = Array.prototype.slice.call(doc.querySelectorAll('h1,h2,h3,h4'));
    var target = headings.find(function(h) { return normalizeText(h.textContent).includes('핵심 암기'); });
    if (!target) return null;
    var el = target.nextElementSibling;
    while (el && (el.tagName === 'HR')) el = el.nextElementSibling;
    if (!el) return null;
    // common: blockquote or div.highlight/important/note wrapper around blockquote
    if (el.tagName === 'BLOCKQUOTE') return el.innerHTML.trim();
    var bq = el.querySelector && el.querySelector('blockquote');
    if (bq) return bq.innerHTML.trim();
    return null;
  }

  function normalizeMnemonicFallback(doc) {
    // if there is a "암기법" heading, try to grab inline code nearby
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

  function hydrateFromPage(card) {
    if (!card || !card.url) return;
    if (pageCache.has(card.url)) {
      applyExtracted(pageCache.get(card.url));
      return;
    }
    // show loading markers
    elQuick.innerHTML = '불러오는 중…';
    elKeywords.innerHTML = '불러오는 중…';

    fetch(card.url, { credentials: 'same-origin' })
      .then(function(res) { return res.text(); })
      .then(function(html) {
        var parser = new DOMParser();
        var doc = parser.parseFromString(html, 'text/html');

        var keywords = normalizeKeywordsFromHeading(doc);
        var quick = normalizeQuickRefFromHeading(doc);
        var mnemonic = card.mnemonic_html || normalizeMnemonicFallback(doc) || '';

        var payload = {
          url: card.url,
          keywords: keywords,
          quick_html: quick,
          mnemonic_html: mnemonic
        };
        pageCache.set(card.url, payload);
        applyExtracted(payload);
      })
      .catch(function() {
        elQuick.innerHTML = '-';
        elKeywords.innerHTML = '-';
      });
  }

  function applyExtracted(payload) {
    if (!payload || !cards.length) return;
    var cur = cards[idx];
    if (!cur || cur.url !== payload.url) return; // stale

    elKeywords.innerHTML = renderKeywords(payload.keywords);
    elQuick.innerHTML = payload.quick_html ? payload.quick_html : '-';
    // don't wipe mnemonic if exam table already has it; but enrich when empty
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
            badge: normalizeText(p.parent || 'AI 토픽'),
            mnemonic_text: ''
          };
        });
      })
    ]);
  }

  function init() {
    // restore prefs
    var prefs = safeGet(STORAGE_PREFIX + 'prefs', {});
    if (prefs && typeof prefs === 'object') {
      if (prefs.mode) elMode.value = prefs.mode;
      if (prefs.limit) elLimit.value = String(prefs.limit);
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
      safeSet(STORAGE_PREFIX + 'prefs', { mode: elMode.value, limit: parseInt(elLimit.value || '40', 10), search: elSearch.value });
      applyModeAndSearch();
    });
    elLimit.addEventListener('change', function() {
      safeSet(STORAGE_PREFIX + 'prefs', { mode: elMode.value, limit: parseInt(elLimit.value || '40', 10), search: elSearch.value });
      applyModeAndSearch();
    });
    elSearch.addEventListener('input', function() {
      safeSet(STORAGE_PREFIX + 'prefs', { mode: elMode.value, limit: parseInt(elLimit.value || '40', 10), search: elSearch.value });
      // debounce-ish
      if (window.__aiDeckSearchTimer) clearTimeout(window.__aiDeckSearchTimer);
      window.__aiDeckSearchTimer = setTimeout(applyModeAndSearch, 180);
    });

    btnPrev.addEventListener('click', function() { selectIndex(idx - 1, { scrollIntoView: true }); });
    btnNext.addEventListener('click', function() { selectIndex(idx + 1, { scrollIntoView: true }); });
    btnShuffle.addEventListener('click', manualShuffle);
    btnReset.addEventListener('click', resetOrder);
    btnHard.addEventListener('click', function(e) { e.preventDefault(); markHard(); });

    // keyboard nav: ↑/↓ select, Enter open
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


