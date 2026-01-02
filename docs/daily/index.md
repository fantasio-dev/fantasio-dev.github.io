---
layout: default
title: 🃏 Daily
nav_order: 100
has_toc: false
permalink: /docs/daily
---

<div class="daily-deck" id="dailyDeckRoot">

  <div class="daily-deck__toolbar">
    <div class="daily-deck__row">
      <label class="daily-deck__label">
        도메인
        <select id="dailyDomain" class="daily-deck__select">
          <option value="ai" selected>AI</option>
          <option value="sw">SW</option>
          <option value="ds">DS</option>
          <option value="sec">SEC</option>
          <option value="nw">NW</option>
          <option value="db">DB</option>
          <option value="caos">CAOS</option>
          <option value="biz">BIZ</option>
        </select>
      </label>
      <label class="daily-deck__label">
        덱
        <select id="dailyDeckMode" class="daily-deck__select daily-deck__select--wide">
          <option value="topics-all" selected>전체 토픽</option>
        </select>
      </label>
      <label class="daily-deck__label">
        검색
        <input id="dailyDeckSearch" class="daily-deck__input daily-deck__input--wide" type="text" placeholder="예: Transformer / 테스트 / 보안">
      </label>
    </div>

    <div class="daily-deck__row daily-deck__row--meta">
      <div class="daily-deck__meta">
        <span id="dailyDeckStatus">로딩 중…</span>
        <span class="daily-deck__kbd">⌨️ ↑/↓ 이동 · Enter 원문</span>
      </div>
      <div class="daily-deck__nav-links">
        <a class="daily-deck__nav-pill" href="{{ site.baseurl }}/docs/exam">📝 통합 기출문제</a>
      </div>
    </div>
  </div>

  <div class="daily-deck__layout">
    <aside class="daily-deck__list" aria-label="항목 목록">
      <div id="dailyDeckList" class="daily-deck__items"></div>
    </aside>

    <section class="daily-deck__detail" aria-label="선택 항목 상세">
      <div class="daily-deck__detail-head">
        <div class="daily-deck__tag" id="dailyDeckTag">-</div>
        <div class="daily-deck__title" id="dailyDeckTitle">항목을 선택하세요</div>
        <div class="daily-deck__detail-actions">
          <button type="button" class="daily-deck__btn" id="dailyDeckPrev">↑ 이전</button>
          <button type="button" class="daily-deck__btn daily-deck__btn--primary" id="dailyDeckNext">↓ 다음</button>
          <a class="daily-deck__btn daily-deck__btn--ghost" id="dailyDeckOpenLink" href="#" target="_blank" rel="noopener">원문 보기</a>
          <button type="button" class="daily-deck__btn daily-deck__btn--ghost" id="dailyDeckMarkHard">어려움(⭐)</button>
        </div>
      </div>

      <div class="daily-deck__panes">
        <div class="daily-deck__pane">
          <div class="daily-deck__pane-title">개념 정의(한 줄)</div>
          <div class="daily-deck__pane-body" id="dailyDeckDefinition">-</div>
        </div>
        <div class="daily-deck__pane">
          <div class="daily-deck__pane-title">구성요소(표)</div>
          <div class="daily-deck__pane-body" id="dailyDeckComponents">-</div>
        </div>
        <div class="daily-deck__pane daily-deck__pane--wide">
          <div class="daily-deck__pane-title">암기법/핵심 구문</div>
          <div class="daily-deck__pane-body" id="dailyDeckMnemonic">-</div>
        </div>
      </div>

      <div class="daily-deck__footer">
        <details>
          <summary><strong>팁</strong> (클릭)</summary>
          <ul>
            <li><strong>루틴</strong>: 목록을 위아래로 쭉 훑는 방식이 노트 넘기기와 가장 유사합니다.</li>
            <li><strong>도메인 전환</strong>: 왼쪽 상단에서 AI/SW/DS 등 다른 영역으로 바로 전환할 수 있습니다.</li>
          </ul>
        </details>
      </div>
    </section>
  </div>
</div>

<style>
/* Daily Deck Styles */
.daily-deck { margin-top: 1rem; }
.daily-deck__toolbar { border: 1px solid rgba(15, 23, 42, 0.10); border-radius: 14px; padding: 12px; background: rgba(248, 250, 252, 0.72); }
.daily-deck__row { display: flex; gap: 10px; flex-wrap: wrap; align-items: center; justify-content: space-between; }
.daily-deck__row--meta { margin-top: 8px; }
.daily-deck__label { display: inline-flex; gap: 8px; align-items: center; font-size: 12px; font-weight: 900; color: rgba(15, 23, 42, 0.82); }
.daily-deck__select, .daily-deck__input { border: 1px solid rgba(15, 23, 42, 0.14); border-radius: 10px; padding: 6px 10px; background: #fff; font-size: 13px; }
.daily-deck__select--wide { min-width: 180px; }
.daily-deck__input { width: 150px; }
.daily-deck__input--wide { width: 220px; }
.daily-deck__btn { border: 1px solid rgba(15, 23, 42, 0.14); background: #fff; border-radius: 12px; padding: 8px 12px; font-size: 13px; font-weight: 900; letter-spacing: -0.2px; cursor: pointer; text-decoration: none !important; display: inline-flex; align-items: center; justify-content: center; }
.daily-deck__btn:hover { background: rgba(226, 232, 240, 0.70); }
.daily-deck__btn--primary { background: linear-gradient(135deg, #4f46e5, #7c3aed); color: #fff; border-color: rgba(15, 23, 42, 0.10); }
.daily-deck__btn--primary:hover { filter: brightness(0.98); }
.daily-deck__btn--ghost { background: rgba(255, 255, 255, 0.65); }
.daily-deck__nav-links { display: flex; gap: 8px; }
.daily-deck__nav-pill { display: inline-flex; align-items: center; gap: 4px; padding: 6px 14px; border-radius: 20px; background: linear-gradient(135deg, rgba(99, 102, 241, 0.08), rgba(139, 92, 246, 0.12)); border: 1px solid rgba(99, 102, 241, 0.22); font-size: 12px; font-weight: 800; color: #4338ca; text-decoration: none !important; transition: all 0.15s ease; }
.daily-deck__nav-pill:hover { background: linear-gradient(135deg, rgba(99, 102, 241, 0.16), rgba(139, 92, 246, 0.22)); border-color: rgba(99, 102, 241, 0.36); color: #3730a3; transform: translateY(-1px); box-shadow: 0 2px 8px rgba(99, 102, 241, 0.18); }
.daily-deck__meta { display: flex; gap: 12px; align-items: center; font-size: 12px; font-weight: 900; color: rgba(15, 23, 42, 0.76); width: 100%; justify-content: space-between; }
.daily-deck__kbd { font-weight: 900; color: rgba(15, 23, 42, 0.62); }

.daily-deck__layout { margin-top: 12px; display: grid; gap: 12px; grid-template-columns: 360px 1fr; align-items: start; }
@media (max-width: 66.49rem) {
  .daily-deck__layout { grid-template-columns: 1fr; }
  .daily-deck__input--wide { width: 100%; }
  .daily-deck__select--wide { min-width: 120px; }
}

.daily-deck__list { border: 1px solid rgba(15, 23, 42, 0.10); border-radius: 14px; background: #fff; overflow: hidden; }
.daily-deck__items { max-height: calc(100vh - 280px); overflow: auto; }
@media (max-width: 66.49rem) { .daily-deck__items { max-height: 44vh; } }

.daily-deck__item { display: grid; gap: 6px; padding: 10px 10px; border-bottom: 1px solid rgba(15, 23, 42, 0.08); cursor: pointer; }
.daily-deck__item:hover { background: rgba(248, 250, 252, 0.85); }
.daily-deck__item.is-active { background: rgba(233, 213, 255, 0.30); }
.daily-deck__item-title { font-size: 13px; font-weight: 900; letter-spacing: -0.2px; color: rgba(15, 23, 42, 0.90); }
.daily-deck__item-sub { font-size: 12px; font-weight: 900; letter-spacing: -0.2px; color: rgba(15, 23, 42, 0.60); }
.daily-deck__item-tagline { display: flex; gap: 8px; align-items: center; justify-content: space-between; }
.daily-deck__pill { display: inline-flex; align-items: center; padding: 3px 8px; border-radius: 999px; font-size: 12px; font-weight: 900; color: rgba(15, 23, 42, 0.82); background: rgba(226, 232, 240, 0.75); border: 1px solid rgba(15, 23, 42, 0.10); }
.daily-deck__pill--hard { background: rgba(254, 202, 202, 0.60); border-color: rgba(239, 68, 68, 0.22); color: rgba(127, 29, 29, 0.92); }

.daily-deck__detail { border: 1px solid rgba(15, 23, 42, 0.10); border-radius: 14px; background: #fff; padding: 12px; }
.daily-deck__detail-head { display: grid; gap: 10px; border-bottom: 1px solid rgba(15, 23, 42, 0.10); padding-bottom: 10px; margin-bottom: 10px; }
.daily-deck__tag { display: inline-flex; width: fit-content; align-items: center; padding: 4px 10px; border-radius: 999px; font-size: 12px; font-weight: 900; color: rgba(15, 23, 42, 0.86); background: rgba(226, 232, 240, 0.75); border: 1px solid rgba(15, 23, 42, 0.10); }
.daily-deck__title { font-size: 20px; font-weight: 900; letter-spacing: -0.4px; color: #0f172a; line-height: 1.3; }
.daily-deck__detail-actions { display: flex; gap: 10px; flex-wrap: wrap; }

.daily-deck__panes { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }
.daily-deck__pane { border: 1px solid rgba(15, 23, 42, 0.08); border-radius: 12px; background: rgba(248, 250, 252, 0.65); padding: 10px; }
.daily-deck__pane--wide { grid-column: 1 / -1; }
.daily-deck__pane-title { font-size: 12px; font-weight: 900; color: rgba(15, 23, 42, 0.75); margin-bottom: 6px; }
.daily-deck__pane-body { font-size: 13px; line-height: 1.5; color: rgba(15, 23, 42, 0.92); }
.daily-deck__pane-body code { font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace; font-size: 12px; padding: 2px 6px; border-radius: 8px; background: rgba(245, 243, 255, 0.85); border: 1px solid rgba(124, 58, 237, 0.18); color: #6d28d9; margin-right: 6px; display: inline-block; margin-bottom: 6px; }
.daily-deck__pane-body table { width: 100% !important; font-size: 12px; }
.daily-deck__pane-body table td, .daily-deck__pane-body table th { padding: 6px 8px; white-space: normal; }
.daily-deck__pane-body table thead th { white-space: nowrap; }
.daily-deck__pane-body .highlight-purple { background: rgba(245, 243, 255, 0.55); border-radius: 10px; padding: 8px; }
.daily-deck__footer { margin-top: 10px; }
</style>

<script>
(function() {
  var root = document.getElementById('dailyDeckRoot');
  if (!root) return;

  var baseUrl = '{{ site.baseurl }}';

  // Domain configurations
  var domainConfig = {
    ai: {
      topicsUrl: baseUrl + '/docs/ai/topics.json',
      examUrl: baseUrl + '/docs/ai/exam.json',
      indexUrl: baseUrl + '/docs/ai',
      label: 'AI',
      hasExam: true,
      categories: [
        { value: 'topics-all', label: 'AI 토픽 · 전체' },
        { value: 'topics-1', label: '① AI 개요' },
        { value: 'topics-2', label: '② 기계학습' },
        { value: 'topics-3', label: '③ AI 기술' },
        { value: 'topics-4', label: '④ AI 윤리/보안' },
        { value: 'topics-6', label: '⑥ 운영/프로세스' },
        { value: 'topics-7', label: '⑦ 서비스' },
        { value: 'exam-1', label: '📝 기출 1교시형' },
        { value: 'exam-2', label: '📝 기출 1교시형 외' }
      ]
    },
    sw: {
      topicsUrl: baseUrl + '/docs/sw/topics.json',
      examUrl: baseUrl + '/docs/sw/exam.json',
      indexUrl: baseUrl + '/docs/sw',
      label: 'SW',
      hasExam: true,
      categories: [
        { value: 'topics-all', label: 'SW 토픽 · 전체' },
        { value: 'topics-1', label: '① 안전성' },
        { value: 'topics-2', label: '② 품질' },
        { value: 'topics-3', label: '③ 프로젝트 관리' },
        { value: 'topics-4', label: '④ 아키텍처' },
        { value: 'topics-5', label: '⑤ UML' },
        { value: 'topics-6', label: '⑥ 방법론' },
        { value: 'topics-9', label: '⑨ 테스팅' },
        { value: 'topics-10', label: '⑩ 유지보수' },
        { value: 'topics-11', label: '⑪ 조달/계약' },
        { value: 'topics-15', label: '⑮ DevOps' },
        { value: 'exam-1', label: '📝 기출 1교시형' },
        { value: 'exam-2', label: '📝 기출 1교시형 외' }
      ]
    },
    ds: {
      topicsUrl: baseUrl + '/docs/ds/topics.json',
      examUrl: baseUrl + '/docs/ds/exam.json',
      indexUrl: baseUrl + '/docs/ds',
      label: 'DS',
      hasExam: true,
      categories: [
        { value: 'topics-all', label: 'DS 토픽 · 전체' },
        { value: 'topics-1', label: '① 클라우드' },
        { value: 'topics-3', label: '③ 블록체인' },
        { value: 'topics-4', label: '④ 스마트카/자율주행' },
        { value: 'topics-7', label: '⑦ 가상화/컨테이너' },
        { value: 'exam-1', label: '📝 기출 1교시형' },
        { value: 'exam-2', label: '📝 기출 1교시형 외' }
      ]
    },
    sec: {
      topicsUrl: baseUrl + '/docs/sec/topics.json',
      examUrl: baseUrl + '/docs/sec/exam.json',
      indexUrl: baseUrl + '/docs/sec',
      label: 'SEC',
      hasExam: true,
      categories: [
        { value: 'topics-all', label: 'SEC 토픽 · 전체' },
        { value: 'exam-1', label: '📝 기출 1교시형' },
        { value: 'exam-2', label: '📝 기출 1교시형 외' }
      ]
    },
    nw: {
      topicsUrl: baseUrl + '/docs/nw/topics.json',
      examUrl: baseUrl + '/docs/nw/exam.json',
      indexUrl: baseUrl + '/docs/nw',
      label: 'NW',
      hasExam: true,
      categories: [
        { value: 'topics-all', label: 'NW 토픽 · 전체' },
        { value: 'exam-1', label: '📝 기출 1교시형' },
        { value: 'exam-2', label: '📝 기출 1교시형 외' }
      ]
    },
    db: {
      topicsUrl: baseUrl + '/docs/db/topics.json',
      indexUrl: baseUrl + '/docs/db',
      label: 'DB',
      hasExam: false,
      categories: [
        { value: 'topics-all', label: 'DB 토픽 · 전체' }
      ]
    },
    caos: {
      topicsUrl: baseUrl + '/docs/caos/topics.json',
      indexUrl: baseUrl + '/docs/caos',
      label: 'CAOS',
      hasExam: false,
      categories: [
        { value: 'topics-all', label: 'CAOS 토픽 · 전체' }
      ]
    },
    biz: {
      topicsUrl: baseUrl + '/docs/biz/topics.json',
      indexUrl: baseUrl + '/docs/biz',
      label: 'BIZ',
      hasExam: false,
      categories: [
        { value: 'topics-all', label: 'BIZ 토픽 · 전체' }
      ]
    }
  };

  var elStatus = document.getElementById('dailyDeckStatus');
  var elDomain = document.getElementById('dailyDomain');
  var elMode = document.getElementById('dailyDeckMode');
  var elSearch = document.getElementById('dailyDeckSearch');

  var elList = document.getElementById('dailyDeckList');
  var elTag = document.getElementById('dailyDeckTag');
  var elTitle = document.getElementById('dailyDeckTitle');
  var elDef = document.getElementById('dailyDeckDefinition');
  var elComponents = document.getElementById('dailyDeckComponents');
  var elMnemonic = document.getElementById('dailyDeckMnemonic');
  var elOpenLink = document.getElementById('dailyDeckOpenLink');

  var btnPrev = document.getElementById('dailyDeckPrev');
  var btnNext = document.getElementById('dailyDeckNext');
  var btnHard = document.getElementById('dailyDeckMarkHard');

  var STORAGE_PREFIX = 'peDailyDeck:v1:';

  var topicRows = [];
  var examRows = [];
  var cardsAll = [];
  var cards = [];
  var idx = 0;
  var hardSet = new Set();
  var pageCache = new Map();
  var currentDomain = 'ai';
  var currentMode = 'topics-all';

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
    t = t.replace(/^[①-⑰]\s*/, '');
    return t;
  }

  function cardKey(c) {
    return [currentDomain, c.url || c.title].join('|');
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

  function updateModeOptions() {
    var config = domainConfig[currentDomain];
    if (!config) return;
    
    elMode.innerHTML = '';
    config.categories.forEach(function(cat) {
      var opt = document.createElement('option');
      opt.value = cat.value;
      opt.textContent = cat.label;
      elMode.appendChild(opt);
    });
  }

  function applyModeAndSearch() {
    var mode = elMode.value;
    currentMode = mode;
    var q = normalizeText(elSearch.value).toLowerCase();

    var base;

    // 기출문제 모드 처리
    if (mode && mode.indexOf('exam-') === 0) {
      var examType = mode.replace('exam-', '');
      base = examRows.slice();
      if (examType === '1') {
        base = base.filter(function(c) { return c.exam_type === '1'; });
      } else {
        base = base.filter(function(c) { return c.exam_type !== '1'; });
      }
    } else {
      base = topicRows.slice();
      
      // Category filter (topics-1, topics-2, etc.)
      if (mode && mode !== 'topics-all' && mode.indexOf('topics-') === 0) {
        var catNum = mode.replace('topics-', '');
        base = base.filter(function(c) {
          // Match by nav_order prefix or parent category
          var navStr = String(c.nav_order || '');
          if (navStr.indexOf(catNum) === 0) return true;
          var parentLower = (c.parent || '').toLowerCase();
          if (parentLower.indexOf(catNum + '.') >= 0) return true;
          if (parentLower.indexOf('① ') >= 0 && catNum === '1') return true;
          if (parentLower.indexOf('② ') >= 0 && catNum === '2') return true;
          if (parentLower.indexOf('③ ') >= 0 && catNum === '3') return true;
          if (parentLower.indexOf('④ ') >= 0 && catNum === '4') return true;
          if (parentLower.indexOf('⑤ ') >= 0 && catNum === '5') return true;
          if (parentLower.indexOf('⑥ ') >= 0 && catNum === '6') return true;
          if (parentLower.indexOf('⑦ ') >= 0 && catNum === '7') return true;
          if (parentLower.indexOf('⑧ ') >= 0 && catNum === '8') return true;
          if (parentLower.indexOf('⑨ ') >= 0 && catNum === '9') return true;
          if (parentLower.indexOf('⑩ ') >= 0 && catNum === '10') return true;
          if (parentLower.indexOf('⑪ ') >= 0 && catNum === '11') return true;
          if (parentLower.indexOf('⑫ ') >= 0 && catNum === '12') return true;
          if (parentLower.indexOf('⑬ ') >= 0 && catNum === '13') return true;
          if (parentLower.indexOf('⑭ ') >= 0 && catNum === '14') return true;
          if (parentLower.indexOf('⑮ ') >= 0 && catNum === '15') return true;
          if (parentLower.indexOf('⑯ ') >= 0 && catNum === '16') return true;
          if (parentLower.indexOf('⑰ ') >= 0 && catNum === '17') return true;
          return false;
        });
      }
    }

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
      var ao = toInt(a.nav_order, 9999);
      var bo = toInt(b.nav_order, 9999);
      if (ao !== bo) return ao - bo;
      return String(a.title || '').localeCompare(String(b.title || ''), 'ko');
    });

    cards = base;
    idx = 0;
    renderList();
    selectIndex(0, { scrollIntoView: true });
  }

  function renderList() {
    if (!cards.length) {
      elList.innerHTML = '<div class="daily-deck__item"><div class="daily-deck__item-title">결과가 없습니다.</div></div>';
      setStatus();
      clearDetail();
      return;
    }

    var html = '';
    cards.forEach(function(c, i) {
      var hard = hardSet.has(cardKey(c));
      html += '<div class="daily-deck__item' + (i === idx ? ' is-active' : '') + '" data-idx="' + i + '">';
      html +=   '<div class="daily-deck__item-title">' + escapeHtml(c.title) + '</div>';
      if (c.sub_badge) {
        html += '<div class="daily-deck__item-sub">' + escapeHtml(c.badge + ' > ' + c.sub_badge) + '</div>';
      }
      html +=   '<div class="daily-deck__item-tagline">';
      html +=     '<span class="daily-deck__pill">' + escapeHtml(c.badge) + '</span>';
      html +=     (hard ? '<span class="daily-deck__pill daily-deck__pill--hard">⭐</span>' : '<span class="daily-deck__pill" style="opacity:.55"> </span>');
      html +=   '</div>';
      html += '</div>';
    });
    elList.innerHTML = html;
    setStatus();

    Array.prototype.forEach.call(elList.querySelectorAll('.daily-deck__item[data-idx]'), function(node) {
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
    Array.prototype.forEach.call(elList.querySelectorAll('.daily-deck__item[data-idx]'), function(node) {
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

    elMnemonic.innerHTML = c.mnemonic_html || (c.mnemonic_text ? escapeHtml(c.mnemonic_text) : '-');
    elDef.innerHTML = '-';
    elComponents.innerHTML = '-';

    hydrateFromPage(c);

    if (opts && opts.scrollIntoView) {
      var active = elList.querySelector('.daily-deck__item.is-active');
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

  function hydrateFromPage(card) {
    if (!card || !card.url) return;
    if (pageCache.has(card.url)) {
      applyExtracted(pageCache.get(card.url));
      return;
    }
    elDef.innerHTML = '불러오는 중…';
    elComponents.innerHTML = '불러오는 중…';

    fetch(card.url, { credentials: 'same-origin' })
      .then(function(res) { return res.text(); })
      .then(function(html) {
        var parser = new DOMParser();
        var doc = parser.parseFromString(html, 'text/html');

        var definition = extractDefinition(doc);
        var componentsHtml = extractComponentsTables(doc);
        var mnemonic = card.mnemonic_html || normalizeMnemonicFallback(doc) || '';
        var quickRef = null;

        // 기출문제인 경우 Quick Reference 박스 추출
        if (card.kind === 'exam') {
          quickRef = extractQuickRef(doc);
        }

        var payload = {
          url: card.url,
          definition: definition,
          components_html: componentsHtml,
          mnemonic_html: mnemonic,
          quick_ref_html: quickRef
        };
        pageCache.set(card.url, payload);
        applyExtracted(payload);
      })
      .catch(function() {
        elDef.innerHTML = '-';
        elComponents.innerHTML = '-';
      });
  }

  function applyExtracted(payload) {
    if (!payload || !cards.length) return;
    var cur = cards[idx];
    if (!cur || cur.url !== payload.url) return;

    // 기출문제인 경우 Quick Reference 박스를 개념 정의 영역에 표시
    if (cur.kind === 'exam' && payload.quick_ref_html) {
      elDef.innerHTML = payload.quick_ref_html;
      elComponents.innerHTML = payload.components_html ? payload.components_html : '-';
    } else {
      elDef.innerHTML = renderDefinition(payload.definition);
      elComponents.innerHTML = payload.components_html ? payload.components_html : '-';
    }
    
    if (!cur.mnemonic_html || cur.mnemonic_text === '-' || !cur.mnemonic_text) {
      if (payload.mnemonic_html) elMnemonic.innerHTML = payload.mnemonic_html;
    }
  }

  function loadTopics() {
    var config = domainConfig[currentDomain];
    if (!config) return Promise.resolve();

    elStatus.textContent = config.label + ' 데이터 로딩…';

    return fetch(config.topicsUrl, { credentials: 'same-origin' })
      .then(function(r) { return r.json(); })
      .then(function(j) {
        topicRows = (Array.isArray(j) ? j : []).map(function(p) {
          var mainBadge = shortParentLabel(p.parent || config.label + ' 토픽');
          return {
            kind: 'topic',
            title: normalizeText(p.title),
            url: p.url,
            parent: p.parent,
            grand_parent: p.grand_parent,
            badge: normalizeText(mainBadge || config.label + ' 토픽'),
            sub_badge: '',
            nav_order: p.nav_order,
            mnemonic_text: ''
          };
        });
      });
  }

  function loadExam() {
    var config = domainConfig[currentDomain];
    if (!config || !config.hasExam || !config.examUrl) {
      examRows = [];
      return Promise.resolve();
    }

    return fetch(config.examUrl, { credentials: 'same-origin' })
      .then(function(r) { return r.json(); })
      .then(function(j) {
        examRows = (Array.isArray(j) ? j : []).map(function(p) {
          var roundStr = p.round ? p.round + '회' : '';
          var sessionStr = p.session ? p.session + '교시' : '';
          var numStr = p.number ? p.number + '번' : '';
          var badge = [roundStr, sessionStr, numStr].filter(Boolean).join(' ');
          return {
            kind: 'exam',
            title: p.topic || p.title,
            fullTitle: p.title,
            url: p.url,
            badge: badge || '기출문제',
            sub_badge: p.exam_type === '1' ? '1교시형' : '2교시형 외',
            nav_order: p.nav_order,
            exam_type: p.exam_type,
            round: p.round,
            session: p.session,
            number: p.number,
            mnemonic_text: ''
          };
        });
      })
      .catch(function() {
        examRows = [];
      });
  }

  function extractQuickRef(doc) {
    // .highlight 클래스를 가진 blockquote 찾기
    var highlight = doc.querySelector('.highlight');
    if (highlight) return highlight.outerHTML;
    
    // 핵심 암기 (Quick Reference) 헤딩 찾기
    var headings = Array.prototype.slice.call(doc.querySelectorAll('h1,h2,h3,h4'));
    var target = headings.find(function(h) { 
      var t = normalizeText(h.textContent);
      return t.includes('핵심 암기') || t.includes('Quick Reference');
    });
    if (!target) return null;
    
    var el = target.nextElementSibling;
    var tries = 0;
    while (el && tries < 5) {
      if (/^H[1-6]$/.test(el.tagName)) break;
      if (el.classList && el.classList.contains('highlight')) return el.outerHTML;
      if (el.tagName === 'BLOCKQUOTE') return el.outerHTML;
      el = el.nextElementSibling;
      tries++;
    }
    return null;
  }

  function switchDomain(domain) {
    currentDomain = domain;
    updateModeOptions();
    
    Promise.all([loadTopics(), loadExam()])
      .then(function() {
        elStatus.textContent = '준비 완료';
        applyModeAndSearch();
      })
      .catch(function(err) {
        elStatus.textContent = '로딩 실패: ' + (err && err.message ? err.message : 'unknown');
        clearDetail();
      });
  }

  function init() {
    // restore prefs
    var prefs = safeGet(STORAGE_PREFIX + 'prefs', {});
    if (prefs && typeof prefs === 'object') {
      if (prefs.domain && domainConfig[prefs.domain]) {
        currentDomain = prefs.domain;
        elDomain.value = currentDomain;
      }
      if (prefs.search) elSearch.value = String(prefs.search);
    }
    var hardSaved = safeGet(STORAGE_PREFIX + 'hard', []);
    hardSet = new Set(Array.isArray(hardSaved) ? hardSaved : []);

    updateModeOptions();
    if (prefs && prefs.mode) {
      var modeOpt = elMode.querySelector('option[value="' + prefs.mode + '"]');
      if (modeOpt) elMode.value = prefs.mode;
    }

    switchDomain(currentDomain);

    elDomain.addEventListener('change', function() {
      safeSet(STORAGE_PREFIX + 'prefs', { domain: elDomain.value, mode: 'topics-all', search: elSearch.value });
      switchDomain(elDomain.value);
    });

    elMode.addEventListener('change', function() {
      safeSet(STORAGE_PREFIX + 'prefs', { domain: currentDomain, mode: elMode.value, search: elSearch.value });
      applyModeAndSearch();
    });

    elSearch.addEventListener('input', function() {
      safeSet(STORAGE_PREFIX + 'prefs', { domain: currentDomain, mode: elMode.value, search: elSearch.value });
      if (window.__dailyDeckSearchTimer) clearTimeout(window.__dailyDeckSearchTimer);
      window.__dailyDeckSearchTimer = setTimeout(applyModeAndSearch, 180);
    });

    btnPrev.addEventListener('click', function() { selectIndex(idx - 1, { scrollIntoView: true }); });
    btnNext.addEventListener('click', function() { selectIndex(idx + 1, { scrollIntoView: true }); });
    btnHard.addEventListener('click', function(e) { e.preventDefault(); markHard(); });

    // keyboard nav
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

