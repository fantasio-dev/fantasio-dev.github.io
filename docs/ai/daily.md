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

**기출문제 목록의 “문제 + 암기법”을 카드처럼 넘겨보는 모드**입니다.  
기본은 **1교시 + 암기법 있음**만 모아서 “앞면(문제) → 뒷면(암기법)”으로 반복합니다.

<div class="ai-deck" id="aiDeckRoot" data-exam-url="{{ site.baseurl }}/docs/ai/exam">
  <div class="ai-deck__toolbar">
    <div class="ai-deck__row">
      <label class="ai-deck__label">
        덱
        <select id="aiDeckFilter" class="ai-deck__select">
          <option value="1-mnemonic" selected>1교시 + 암기법 있음</option>
          <option value="all-mnemonic">전체 + 암기법 있음</option>
          <option value="all-has-page">전체 + 학습페이지 있음</option>
        </select>
      </label>

      <label class="ai-deck__label">
        오늘 N장
        <input id="aiDeckLimit" class="ai-deck__input" type="number" min="5" max="200" step="5" value="30">
      </label>

      <button type="button" class="ai-deck__btn" id="aiDeckShuffle">셔플</button>
      <button type="button" class="ai-deck__btn ai-deck__btn--ghost" id="aiDeckReset">리셋</button>
      <a class="ai-deck__link" href="{{ site.baseurl }}/docs/ai/exam">원본 기출 테이블로</a>
    </div>

    <div class="ai-deck__row ai-deck__row--meta">
      <div class="ai-deck__meta">
        <span id="aiDeckStatus">로딩 중…</span>
        <span class="ai-deck__kbd">⌨️ ←/→ 이동 · Space 뒤집기</span>
      </div>
    </div>
  </div>

  <div class="ai-deck__stage">
    <div class="ai-deck__card" id="aiDeckCard" role="button" tabindex="0" aria-label="카드 뒤집기">
      <div class="ai-deck__card-inner">
        <div class="ai-deck__face ai-deck__face--front">
          <div class="ai-deck__tag" id="aiDeckTag">-</div>
          <div class="ai-deck__q" id="aiDeckQuestion">로딩 중…</div>
          <div class="ai-deck__hint">클릭(또는 Space)해서 암기법 보기</div>
        </div>
        <div class="ai-deck__face ai-deck__face--back">
          <div class="ai-deck__tag ai-deck__tag--back" id="aiDeckTagBack">-</div>
          <div class="ai-deck__a" id="aiDeckMnemonic">-</div>
          <div class="ai-deck__actions">
            <a class="ai-deck__btn ai-deck__btn--primary" id="aiDeckOpenLink" href="#" target="_blank" rel="noopener">원문 보기</a>
            <button type="button" class="ai-deck__btn ai-deck__btn--ghost" id="aiDeckMarkHard">어려움(⭐)</button>
          </div>
        </div>
      </div>
    </div>

    <div class="ai-deck__nav">
      <button type="button" class="ai-deck__btn" id="aiDeckPrev">← 이전</button>
      <button type="button" class="ai-deck__btn ai-deck__btn--primary" id="aiDeckFlip">뒤집기</button>
      <button type="button" class="ai-deck__btn" id="aiDeckNext">다음 →</button>
    </div>
  </div>

  <div class="ai-deck__footer">
    <details>
      <summary><strong>팁</strong> (클릭)</summary>
      <ul>
        <li><strong>매일 보기 최적화</strong>: “오늘 N장”을 20~40으로 두고, 셔플 후 첫 N장만 반복하세요.</li>
        <li><strong>현실적인 목표</strong>: “하루 10분”만 성공 기준으로 잡아도 누적이 큽니다.</li>
        <li><strong>암기법이 없는 문제</strong>는 우선 덱에서 제외하고, 페이지를 채운 뒤 덱에 자연스럽게 들어오게 하세요.</li>
      </ul>
    </details>
  </div>
</div>

<style>
/* Page-scoped deck styles (minimal, no global collision) */
.ai-deck { margin-top: 1rem; }
.ai-deck__toolbar { border: 1px solid rgba(15, 23, 42, 0.10); border-radius: 14px; padding: 12px; background: rgba(248, 250, 252, 0.72); }
.ai-deck__row { display: flex; gap: 10px; flex-wrap: wrap; align-items: center; justify-content: space-between; }
.ai-deck__row--meta { margin-top: 8px; }
.ai-deck__label { display: inline-flex; gap: 8px; align-items: center; font-size: 12px; font-weight: 800; color: rgba(15, 23, 42, 0.82); }
.ai-deck__select, .ai-deck__input { border: 1px solid rgba(15, 23, 42, 0.14); border-radius: 10px; padding: 6px 10px; background: #fff; font-size: 13px; }
.ai-deck__input { width: 90px; }
.ai-deck__btn { border: 1px solid rgba(15, 23, 42, 0.14); background: #fff; border-radius: 12px; padding: 8px 12px; font-size: 13px; font-weight: 900; letter-spacing: -0.2px; cursor: pointer; }
.ai-deck__btn:hover { background: rgba(226, 232, 240, 0.70); }
.ai-deck__btn--primary { background: linear-gradient(135deg, #4f46e5, #7c3aed); color: #fff; border-color: rgba(15, 23, 42, 0.10); }
.ai-deck__btn--primary:hover { filter: brightness(0.98); }
.ai-deck__btn--ghost { background: rgba(255, 255, 255, 0.65); }
.ai-deck__link { font-size: 13px; font-weight: 800; text-decoration: none !important; color: #1d4ed8; }
.ai-deck__link:hover { text-decoration: underline !important; }
.ai-deck__meta { display: flex; gap: 12px; align-items: center; font-size: 12px; font-weight: 800; color: rgba(15, 23, 42, 0.76); width: 100%; justify-content: space-between; }
.ai-deck__kbd { font-weight: 800; color: rgba(15, 23, 42, 0.62); }

.ai-deck__stage { margin-top: 14px; display: grid; gap: 12px; }
.ai-deck__card { border-radius: 18px; border: 1px solid rgba(15, 23, 42, 0.12); background: #fff; box-shadow: 0 10px 26px rgba(15, 23, 42, 0.08); min-height: 260px; outline: none; }
.ai-deck__card:focus-visible { outline: 3px solid rgba(99, 102, 241, 0.35); outline-offset: 2px; }
.ai-deck__card-inner { position: relative; width: 100%; height: 100%; transform-style: preserve-3d; transition: transform 220ms ease; }
.ai-deck__card.is-flipped .ai-deck__card-inner { transform: rotateY(180deg); }
.ai-deck__face { position: absolute; inset: 0; padding: 16px 16px 14px; backface-visibility: hidden; display: flex; flex-direction: column; gap: 10px; }
.ai-deck__face--back { transform: rotateY(180deg); }
.ai-deck__tag { display: inline-flex; width: fit-content; gap: 8px; align-items: center; padding: 4px 10px; border-radius: 999px; font-size: 12px; font-weight: 900; color: rgba(15, 23, 42, 0.86); background: rgba(226, 232, 240, 0.75); border: 1px solid rgba(15, 23, 42, 0.10); }
.ai-deck__tag--back { background: rgba(233, 213, 255, 0.55); border-color: rgba(124, 58, 237, 0.18); }
.ai-deck__q { font-size: 18px; font-weight: 900; letter-spacing: -0.4px; color: #0f172a; line-height: 1.35; }
.ai-deck__a { font-size: 14px; line-height: 1.5; color: rgba(15, 23, 42, 0.90); }
.ai-deck__a code { font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace; font-size: 12px; padding: 2px 6px; border-radius: 8px; background: rgba(245, 243, 255, 0.85); border: 1px solid rgba(124, 58, 237, 0.18); color: #6d28d9; margin-right: 6px; display: inline-block; margin-bottom: 6px; }
.ai-deck__hint { margin-top: auto; font-size: 12px; font-weight: 800; color: rgba(15, 23, 42, 0.62); }
.ai-deck__actions { margin-top: auto; display: flex; gap: 10px; flex-wrap: wrap; }
.ai-deck__nav { display: flex; gap: 10px; justify-content: center; flex-wrap: wrap; }
.ai-deck__footer { margin-top: 8px; }
</style>

<script>
(function() {
  var root = document.getElementById('aiDeckRoot');
  if (!root) return;

  var examUrl = root.getAttribute('data-exam-url');
  var elStatus = document.getElementById('aiDeckStatus');
  var elFilter = document.getElementById('aiDeckFilter');
  var elLimit = document.getElementById('aiDeckLimit');

  var elCard = document.getElementById('aiDeckCard');
  var elQuestion = document.getElementById('aiDeckQuestion');
  var elMnemonic = document.getElementById('aiDeckMnemonic');
  var elTag = document.getElementById('aiDeckTag');
  var elTagBack = document.getElementById('aiDeckTagBack');
  var elOpenLink = document.getElementById('aiDeckOpenLink');

  var btnPrev = document.getElementById('aiDeckPrev');
  var btnNext = document.getElementById('aiDeckNext');
  var btnFlip = document.getElementById('aiDeckFlip');
  var btnShuffle = document.getElementById('aiDeckShuffle');
  var btnReset = document.getElementById('aiDeckReset');
  var btnHard = document.getElementById('aiDeckMarkHard');

  var STORAGE_PREFIX = 'peAiDeck:v1:';
  var cardsAll = [];
  var cards = [];
  var idx = 0;
  var hardSet = new Set();

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

  function shuffleInPlace(arr) {
    for (var i = arr.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var tmp = arr[i]; arr[i] = arr[j]; arr[j] = tmp;
    }
    return arr;
  }

  function normalizeText(s) {
    return (s || '').replace(/\s+/g, ' ').trim();
  }

  function cardKey(c) {
    return [c.round, c.session, c.no, c.url].join('|');
  }

  function setFlipped(next) {
    if (!elCard) return;
    if (next) elCard.classList.add('is-flipped');
    else elCard.classList.remove('is-flipped');
  }

  function toggleFlip() {
    if (!elCard) return;
    elCard.classList.toggle('is-flipped');
  }

  function render() {
    if (!cards.length) {
      elStatus.textContent = '덱에 카드가 없습니다. (조건을 바꿔보세요)';
      elQuestion.textContent = '덱에 카드가 없습니다.';
      elMnemonic.textContent = '-';
      elTag.textContent = '-';
      elTagBack.textContent = '-';
      elOpenLink.setAttribute('href', examUrl);
      setFlipped(false);
      return;
    }

    if (idx < 0) idx = 0;
    if (idx >= cards.length) idx = cards.length - 1;

    var c = cards[idx];
    var tag = c.round + '회 · ' + c.session + '교시 · ' + c.no + '번';
    elTag.textContent = tag;
    elTagBack.textContent = tag + (hardSet.has(cardKey(c)) ? ' · ⭐' : '');

    elQuestion.textContent = c.question;
    elMnemonic.innerHTML = c.mnemonic_html || (c.mnemonic || '-');
    elOpenLink.setAttribute('href', c.url || examUrl);

    elStatus.textContent = (idx + 1) + ' / ' + cards.length + ' (총 후보 ' + cardsAll.length + ')';
    setFlipped(false);
  }

  function next() { idx += 1; render(); }
  function prev() { idx -= 1; render(); }

  function markHard() {
    if (!cards.length) return;
    var c = cards[idx];
    var k = cardKey(c);
    if (hardSet.has(k)) hardSet.delete(k);
    else hardSet.add(k);
    safeSet(STORAGE_PREFIX + 'hard', Array.from(hardSet));
    render();
  }

  function reset() {
    var mode = elFilter.value;
    var day = todayKey();
    try {
      localStorage.removeItem(STORAGE_PREFIX + 'order:' + mode + ':' + day);
    } catch (e) {}
    applyFilter();
  }

  function manualShuffle() {
    var mode = elFilter.value;
    var day = todayKey();
    var orderKey = STORAGE_PREFIX + 'order:' + mode + ':' + day;
    var filtered = cardsAll.slice();
    if (mode === '1-mnemonic') filtered = filtered.filter(function(c) { return c.session === '1' && c.mnemonic && c.mnemonic !== '-'; });
    if (mode === 'all-mnemonic') filtered = filtered.filter(function(c) { return c.mnemonic && c.mnemonic !== '-'; });
    if (mode === 'all-has-page') filtered = filtered.filter(function(c) { return c.url; });
    filtered = shuffleInPlace(filtered);
    safeSet(orderKey, filtered.map(cardKey));
    applyFilter();
  }

  function applyFilter() {
    var mode = elFilter.value;
    var limit = parseInt(elLimit.value || '30', 10);
    if (!isFinite(limit) || limit < 5) limit = 30;
    elLimit.value = String(limit);

    var filtered = cardsAll.slice();
    if (mode === '1-mnemonic') {
      filtered = filtered.filter(function(c) { return c.session === '1' && c.mnemonic && c.mnemonic !== '-' ; });
    } else if (mode === 'all-mnemonic') {
      filtered = filtered.filter(function(c) { return c.mnemonic && c.mnemonic !== '-'; });
    } else if (mode === 'all-has-page') {
      filtered = filtered.filter(function(c) { return c.url; });
    }

    var day = todayKey();
    var orderKey = STORAGE_PREFIX + 'order:' + mode + ':' + day;
    var saved = safeGet(orderKey, null);
    if (saved && Array.isArray(saved) && saved.length) {
      var map = new Map(filtered.map(function(c) { return [cardKey(c), c]; }));
      var rebuilt = [];
      saved.forEach(function(k) { if (map.has(k)) rebuilt.push(map.get(k)); });
      filtered.forEach(function(c) { if (rebuilt.indexOf(c) === -1) rebuilt.push(c); });
      filtered = rebuilt;
    } else {
      filtered = shuffleInPlace(filtered);
      safeSet(orderKey, filtered.map(cardKey));
    }

    cards = filtered.slice(0, Math.min(limit, filtered.length));
    idx = 0;

    var hardSaved = safeGet(STORAGE_PREFIX + 'hard', []);
    hardSet = new Set(Array.isArray(hardSaved) ? hardSaved : []);

    render();
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
        round: normalizeText(tds[0].textContent),
        dept: normalizeText(tds[1].textContent),
        session: normalizeText(tds[2].textContent),
        no: normalizeText(tds[3].textContent),
        question: normalizeText(a.textContent),
        url: a.getAttribute('href') || '',
        mnemonic: normalizeText(tds[6].textContent),
        mnemonic_html: (tds[6].innerHTML || '').trim()
      });
    });
    return out;
  }

  function init() {
    var prefs = safeGet(STORAGE_PREFIX + 'prefs', {});
    if (prefs && typeof prefs === 'object') {
      if (prefs.filter) elFilter.value = prefs.filter;
      if (prefs.limit) elLimit.value = String(prefs.limit);
    }

    elStatus.textContent = '기출 테이블 불러오는 중…';
    fetch(examUrl, { credentials: 'same-origin' })
      .then(function(res) { return res.text(); })
      .then(function(text) {
        cardsAll = parseExamHtml(text);
        elStatus.textContent = '덱 준비 중…';
        applyFilter();
      })
      .catch(function(err) {
        elStatus.textContent = '불러오기 실패: ' + (err && err.message ? err.message : 'unknown');
        elQuestion.textContent = '기출 테이블을 불러오지 못했어요.';
      });

    elFilter.addEventListener('change', function() {
      safeSet(STORAGE_PREFIX + 'prefs', { filter: elFilter.value, limit: parseInt(elLimit.value || '30', 10) });
      applyFilter();
    });
    elLimit.addEventListener('change', function() {
      safeSet(STORAGE_PREFIX + 'prefs', { filter: elFilter.value, limit: parseInt(elLimit.value || '30', 10) });
      applyFilter();
    });

    btnPrev.addEventListener('click', prev);
    btnNext.addEventListener('click', next);
    btnFlip.addEventListener('click', toggleFlip);
    btnShuffle.addEventListener('click', manualShuffle);
    btnReset.addEventListener('click', reset);
    btnHard.addEventListener('click', function(e) { e.preventDefault(); markHard(); });

    elCard.addEventListener('click', function(e) {
      var t = e.target;
      if (t && (t.tagName === 'A' || t.tagName === 'BUTTON')) return;
      toggleFlip();
    });
    elCard.addEventListener('keydown', function(e) {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); toggleFlip(); }
    });

    window.addEventListener('keydown', function(e) {
      if (e.defaultPrevented) return;
      var ae = document.activeElement;
      if (ae) {
        var tag = (ae.tagName || '').toLowerCase();
        if (tag === 'input' || tag === 'textarea' || tag === 'select') return;
        if (ae.isContentEditable) return;
      }
      if (e.key === 'ArrowRight') { e.preventDefault(); next(); }
      if (e.key === 'ArrowLeft') { e.preventDefault(); prev(); }
      if (e.key === ' ') { e.preventDefault(); toggleFlip(); }
    });
  }

  init();
})();
</script>


