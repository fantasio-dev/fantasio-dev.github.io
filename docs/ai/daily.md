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
왼쪽에서 항목을 고르면, 오른쪽에 **정의/구성요소/암기**가 바로 펼쳐져서 *뒤집기 없이* 매일 보기 좋게 설계했습니다.

<div class="ai-deck2" id="aiDeckRoot"
  data-exam-url="{{ site.baseurl }}/docs/ai/exam"
  data-topics-url="{{ site.baseurl }}/docs/ai/topics.json"
  data-ai-index-url="{{ site.baseurl }}/docs/ai">

  <div class="ai-deck2__toolbar">
    <div class="ai-deck2__row">
      <label class="ai-deck2__label">
        덱
        <select id="aiDeckMode" class="ai-deck2__select">
          <option value="topics-all" selected>AI 토픽 · 전체</option>
          <option value="topics-1">① AI 개요</option>
          <option value="topics-2">② 기계학습 · 전체</option>
          <option value="topics-2-supervised">  └ 지도학습(분류/회귀)</option>
          <option value="topics-2-nn">  └ 신경망 기본/학습 이슈</option>
          <option value="topics-2-unsupervised">  └ 비지도/차원축소</option>
          <option value="topics-2-generative">  └ 생성/강화</option>
          <option value="topics-2-ops">  └ 검증/평가/운영</option>
          <option value="topics-3">③ AI 기술 · 전체</option>
          <option value="topics-3-dl-models">  └ 딥러닝 모델</option>
          <option value="topics-3-dl-issues">  └ 딥러닝 이슈/생성</option>
          <option value="topics-3-nlp">  └ 자연어처리</option>
          <option value="topics-3-nn">  └ 특수 신경망</option>
          <option value="topics-4">④ AI 윤리/보안</option>
          <option value="topics-6">⑥ 운영/프로세스</option>
          <option value="topics-7">⑦ 서비스</option>
          <option value="exam-1">기출 · 1교시</option>
          <option value="exam-2">기출 · 2교시</option>
        </select>
      </label>

      <label class="ai-deck2__label">
        검색
        <input id="aiDeckSearch" class="ai-deck2__input ai-deck2__input--wide" type="text" placeholder="예: Transformer / ROC / Dropout">
      </label>
    </div>

    <div class="ai-deck2__row ai-deck2__row--meta">
      <div class="ai-deck2__meta">
        <span id="aiDeckStatus">로딩 중…</span>
        <span class="ai-deck2__kbd">⌨️ ↑/↓ 이동 · Enter 원문</span>
      </div>
      <div class="ai-deck2__nav-links">
        <a class="ai-deck2__nav-pill" href="{{ site.baseurl }}/docs/ai/exam">📝 기출 테이블</a>
        <a class="ai-deck2__nav-pill" href="{{ site.baseurl }}/docs/ai">🏠 AI 메인</a>
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
          <div class="ai-deck2__pane-title">개념 정의(한 줄)</div>
          <div class="ai-deck2__pane-body" id="aiDeckDefinition">-</div>
        </div>
        <div class="ai-deck2__pane">
          <div class="ai-deck2__pane-title">구성요소(표)</div>
          <div class="ai-deck2__pane-body" id="aiDeckComponents">-</div>
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
.ai-deck2 { margin-top: 1rem; }
.ai-deck2__toolbar { border: 1px solid rgba(15, 23, 42, 0.10); border-radius: 14px; padding: 12px; background: rgba(248, 250, 252, 0.72); }
.ai-deck2__row { display: flex; gap: 10px; flex-wrap: wrap; align-items: center; justify-content: space-between; }
.ai-deck2__row--meta { margin-top: 8px; }
.ai-deck2__label { display: inline-flex; gap: 8px; align-items: center; font-size: 12px; font-weight: 900; color: rgba(15, 23, 42, 0.82); }
.ai-deck2__select, .ai-deck2__input { border: 1px solid rgba(15, 23, 42, 0.14); border-radius: 10px; padding: 6px 10px; background: #fff; font-size: 13px; }
.ai-deck2__input { width: 150px; }
.ai-deck2__input--wide { width: 260px; }
.ai-deck2__btn { border: 1px solid rgba(15, 23, 42, 0.14); background: #fff; border-radius: 12px; padding: 8px 12px; font-size: 13px; font-weight: 900; letter-spacing: -0.2px; cursor: pointer; text-decoration: none !important; display: inline-flex; align-items: center; justify-content: center; }
.ai-deck2__btn:hover { background: rgba(226, 232, 240, 0.70); }
.ai-deck2__btn--primary { background: linear-gradient(135deg, #4f46e5, #7c3aed); color: #fff; border-color: rgba(15, 23, 42, 0.10); }
.ai-deck2__btn--primary:hover { filter: brightness(0.98); }
.ai-deck2__btn--ghost { background: rgba(255, 255, 255, 0.65); }
.ai-deck2__nav-links { display: flex; gap: 8px; }
.ai-deck2__nav-pill { display: inline-flex; align-items: center; gap: 4px; padding: 6px 14px; border-radius: 20px; background: linear-gradient(135deg, rgba(99, 102, 241, 0.08), rgba(139, 92, 246, 0.12)); border: 1px solid rgba(99, 102, 241, 0.22); font-size: 12px; font-weight: 800; color: #4338ca; text-decoration: none !important; transition: all 0.15s ease; }
.ai-deck2__nav-pill:hover { background: linear-gradient(135deg, rgba(99, 102, 241, 0.16), rgba(139, 92, 246, 0.22)); border-color: rgba(99, 102, 241, 0.36); color: #3730a3; transform: translateY(-1px); box-shadow: 0 2px 8px rgba(99, 102, 241, 0.18); }
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
.ai-deck2__item-sub { font-size: 12px; font-weight: 900; letter-spacing: -0.2px; color: rgba(15, 23, 42, 0.60); }
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
.ai-deck2__pane-body table { width: 100% !important; font-size: 12px; }
.ai-deck2__pane-body table td, .ai-deck2__pane-body table th { padding: 6px 8px; white-space: normal; }
.ai-deck2__pane-body table thead th { white-space: nowrap; }
.ai-deck2__pane-body .highlight-purple { background: rgba(245, 243, 255, 0.55); border-radius: 10px; padding: 8px; }
.ai-deck2__footer { margin-top: 10px; }
</style>

<script>
(function() {
  var root = document.getElementById('aiDeckRoot');
  if (!root) return;

  var examUrl = root.getAttribute('data-exam-url');
  var topicsUrl = root.getAttribute('data-topics-url');
  var aiIndexUrl = root.getAttribute('data-ai-index-url');

  var elStatus = document.getElementById('aiDeckStatus');
  var elMode = document.getElementById('aiDeckMode');
  var elSearch = document.getElementById('aiDeckSearch');

  var elList = document.getElementById('aiDeckList');
  var elTag = document.getElementById('aiDeckTag');
  var elTitle = document.getElementById('aiDeckTitle');
  var elDef = document.getElementById('aiDeckDefinition');
  var elComponents = document.getElementById('aiDeckComponents');
  var elMnemonic = document.getElementById('aiDeckMnemonic');
  var elOpenLink = document.getElementById('aiDeckOpenLink');

  var btnPrev = document.getElementById('aiDeckPrev');
  var btnNext = document.getElementById('aiDeckNext');
  var btnHard = document.getElementById('aiDeckMarkHard');

  var STORAGE_PREFIX = 'peAiDeck2:v2:';

  var examRows = [];
  var topicRows = [];

  var cardsAll = [];
  var cards = [];
  var idx = 0;
  var hardSet = new Set();
  var pageCache = new Map(); // url -> extracted payload
  var aiTaxonomy = new Map(); // url(path) -> { main, sub }

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
    t = t.replace(/^[①-⑦]\s*/, '');
    return t;
  }

  function normalizeHrefToPath(href) {
    try {
      var u = new URL(href, window.location.origin);
      return u.pathname;
    } catch (e) {
      return (href || '').split('#')[0];
    }
  }

  function normalizeAiHeaderToMainLabel(s) {
    var t = normalizeText(s || '');
    t = t.replace(/^[①-⑦]\s*/, '');
    t = t.split('(')[0].trim();
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

  function applyModeAndSearch() {
    var mode = elMode.value;
    var q = normalizeText(elSearch.value).toLowerCase();

    var base = cardsAll.slice().filter(function(c) {
      if (mode.indexOf('topics-') === 0 || mode === 'topics-all') return c.kind === 'topic';
      if (mode === 'exam-1') return c.kind === 'exam' && c.session === '1';
      if (mode === 'exam-2') return c.kind === 'exam' && c.session === '2';
      return true;
    });

    function topicGroupForUrl(url) {
      if (!url) return '2';
      if (url.indexOf('/docs/ai/10-ai-etc/') >= 0) return '7';
      if (url.indexOf('/docs/ai/02-deep-learning/') >= 0 || url.indexOf('/docs/ai/03-neural-network/') >= 0 || url.indexOf('/docs/ai/04-nlp/') >= 0) return '3';
      if (url.indexOf('/docs/ai/05-ai-ethics/') >= 0) return '4';
      if (url.indexOf('/docs/ai/11-ai-training-data/adversarial-attack') >= 0) return '4';
      if (url.indexOf('/docs/ai/06-ml-evaluation/') >= 0 || url.indexOf('/docs/ai/07-learning-techniques/') >= 0 || url.indexOf('/docs/ai/08-ml-process/') >= 0 || url.indexOf('/docs/ai/09-model-performance/') >= 0 || url.indexOf('/docs/ai/11-ai-training-data/') >= 0) return '6';
      if (url.indexOf('/docs/ai/01-machine-learning/') >= 0) {
        if (url.indexOf('/ml-concept') >= 0 || url.indexOf('/modelops') >= 0 || url.indexOf('/dsml') >= 0 || url.indexOf('/mlops') >= 0 || url.indexOf('/aiops') >= 0) return '1';
        return '2';
      }
      return '2';
    }

    if (mode === 'topics-1') base = base.filter(function(c) { return topicGroupForUrl(c.url) === '1'; });
    if (mode === 'topics-2') base = base.filter(function(c) { return topicGroupForUrl(c.url) === '2'; });
    if (mode === 'topics-3') base = base.filter(function(c) { return topicGroupForUrl(c.url) === '3'; });
    if (mode === 'topics-4') base = base.filter(function(c) { return topicGroupForUrl(c.url) === '4'; });
    if (mode === 'topics-6') base = base.filter(function(c) { return topicGroupForUrl(c.url) === '6'; });
    if (mode === 'topics-7') base = base.filter(function(c) { return topicGroupForUrl(c.url) === '7'; });

    // 소분류 필터 (② 기계학습 하위)
    if (mode === 'topics-2-supervised') base = base.filter(function(c) {
      return c.url && (/\/supervised-learning|\/regression-analysis|\/linear-regression|\/logistic-regression|\/multiple-regression|\/multicollinearity|\/knn|\/svm/).test(c.url);
    });
    if (mode === 'topics-2-nn') base = base.filter(function(c) {
      return c.url && (/\/perceptron|\/parameters|\/activation-function|\/vanishing-gradient|\/overfitting-underfitting|\/dropout|\/mlp/).test(c.url);
    });
    if (mode === 'topics-2-unsupervised') base = base.filter(function(c) {
      return c.url && (/\/unsupervised-learning|\/k-means|\/dbscan|\/som|\/pca/).test(c.url);
    });
    if (mode === 'topics-2-generative') base = base.filter(function(c) {
      return c.url && (/\/gan|\/dcgan|\/reinforcement-learning|\/q-learning|\/deep-reinforcement-learning|\/inverse-reinforcement-learning|\/mdp/).test(c.url);
    });
    if (mode === 'topics-2-ops') base = base.filter(function(c) {
      return c.url && (c.url.indexOf('/docs/ai/06-ml-evaluation/') >= 0 || c.url.indexOf('/docs/ai/07-learning-techniques/') >= 0 || c.url.indexOf('/docs/ai/08-ml-process/') >= 0 || c.url.indexOf('/docs/ai/09-model-performance/') >= 0);
    });

    // 소분류 필터 (③ AI 기술 하위)
    if (mode === 'topics-3-dl-models') base = base.filter(function(c) {
      return c.url && c.url.indexOf('/docs/ai/02-deep-learning/') >= 0 && (/\/cnn|\/rnn|\/lstm|\/gru|\/mlp|\/optimizer/).test(c.url);
    });
    if (mode === 'topics-3-dl-issues') base = base.filter(function(c) {
      return c.url && c.url.indexOf('/docs/ai/02-deep-learning/') >= 0 && (/\/vanishing-gradient|\/overfitting-underfitting|\/dropout|\/catastrophic-forgetting|\/gan|\/dcgan|\/vae/).test(c.url);
    });
    if (mode === 'topics-3-nlp') base = base.filter(function(c) {
      return c.url && c.url.indexOf('/docs/ai/04-nlp/') >= 0;
    });
    if (mode === 'topics-3-nn') base = base.filter(function(c) {
      return c.url && c.url.indexOf('/docs/ai/03-neural-network/') >= 0;
    });

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
      if (c.kind === 'topic' && c.sub_badge) {
        html += '<div class="ai-deck2__item-sub">' + escapeHtml(c.badge + ' > ' + c.sub_badge) + '</div>';
      }
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
    elDef.innerHTML = '-';
    elComponents.innerHTML = '-';
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
    elDef.innerHTML = '-';
    elComponents.innerHTML = '-';

    // load page details (definition/components)
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

  // shuffle/reset removed: this is “노트 넘기기” 모드라서 고정 순서를 기본으로 사용

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
      // “본문/암기법 없는 템플릿성 페이지”는 덱에서 제외 (mnemonic '-' 기준)
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

        var payload = {
          url: card.url,
          definition: definition,
          components_html: componentsHtml,
          mnemonic_html: mnemonic
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
    if (!cur || cur.url !== payload.url) return; // stale

    elDef.innerHTML = renderDefinition(payload.definition);
    elComponents.innerHTML = payload.components_html ? payload.components_html : '-';
    // don't wipe mnemonic if exam table already has it; but enrich when empty
    if (!cur.mnemonic_html || cur.mnemonic_text === '-' || !cur.mnemonic_text) {
      if (payload.mnemonic_html) elMnemonic.innerHTML = payload.mnemonic_html;
    }
  }

  function loadSources() {
    elStatus.textContent = '데이터 로딩…';
    return Promise.all([
      fetch(examUrl, { credentials: 'same-origin' }).then(function(r) { return r.text(); }).then(function(t) { examRows = parseExamHtml(t); }),
      fetch(aiIndexUrl, { credentials: 'same-origin' })
        .then(function(r) { return r.text(); })
        .then(function(html) {
          // Build (상위/하위) 분류 맵: /docs/ai/* 링크 -> { main, sub }
          var parser = new DOMParser();
          var doc = parser.parseFromString(html, 'text/html');
          var aiCards = doc.querySelectorAll('.ai-card');
          aiCards.forEach(function(card) {
            var headerEl = card.querySelector('.ai-card__header');
            if (!headerEl) return;
            var mainLabel = normalizeAiHeaderToMainLabel(headerEl.textContent);

            // chip groups (예: 지도학습/비지도/생성/검증…)
            var chipGroups = card.querySelectorAll('.nw-chip-group');
            if (chipGroups && chipGroups.length) {
              chipGroups.forEach(function(g) {
                var gt = g.querySelector('.nw-chip-group__title');
                var subLabel = gt ? normalizeText(gt.textContent) : '';
                var links = g.querySelectorAll('a[href]');
                links.forEach(function(a) {
                  var path = normalizeHrefToPath(a.getAttribute('href') || '');
                  if (path && path.indexOf('/docs/ai/') === 0) aiTaxonomy.set(path, { main: mainLabel, sub: subLabel });
                });
              });
            }

            // fallback: direct nw-sub blocks
            var subs = card.querySelectorAll('.nw-sub');
            subs.forEach(function(s) {
              var st = s.querySelector('.nw-sub__title');
              var subLabel2 = st ? normalizeText(st.textContent) : '';
              var links2 = s.querySelectorAll('a[href]');
              links2.forEach(function(a) {
                var path2 = normalizeHrefToPath(a.getAttribute('href') || '');
                if (path2 && path2.indexOf('/docs/ai/') === 0 && !aiTaxonomy.has(path2)) aiTaxonomy.set(path2, { main: mainLabel, sub: subLabel2 });
              });
            });
          });
        })
        .catch(function() { /* taxonomy optional */ }),
      fetch(topicsUrl, { credentials: 'same-origin' }).then(function(r) { return r.json(); }).then(function(j) {
        topicRows = (Array.isArray(j) ? j : []).map(function(p) {
          var urlPath = normalizeHrefToPath(p.url || '');
          var tax = aiTaxonomy.get(urlPath);
          var mainBadge = (tax && tax.main) ? tax.main : shortParentLabel(p.parent || 'AI 토픽');
          var subBadge = (tax && tax.sub) ? tax.sub : '';
          return {
            kind: 'topic',
            title: normalizeText(p.title),
            url: p.url,
            parent: p.parent,
            grand_parent: p.grand_parent,
            badge: normalizeText(mainBadge || 'AI 토픽'),
            sub_badge: normalizeText(subBadge),
            nav_order: p.nav_order,
            mnemonic_text: ''
          };
        });
      })
    ]);
  }

  function init() {
    // query param(deck 또는 mode) > prefs
    try {
      var params = new URLSearchParams(window.location.search || '');
      var qsDeck = params.get('deck') || params.get('mode');
      if (qsDeck && elMode.querySelector('option[value="' + qsDeck + '"]')) {
        elMode.value = qsDeck;
        safeSet(STORAGE_PREFIX + 'prefs', { mode: qsDeck, search: '' });
      }
    } catch (e) {}

    // restore prefs
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
      // debounce-ish
      if (window.__aiDeckSearchTimer) clearTimeout(window.__aiDeckSearchTimer);
      window.__aiDeckSearchTimer = setTimeout(applyModeAndSearch, 180);
    });

    btnPrev.addEventListener('click', function() { selectIndex(idx - 1, { scrollIntoView: true }); });
    btnNext.addEventListener('click', function() { selectIndex(idx + 1, { scrollIntoView: true }); });
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


