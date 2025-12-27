---
layout: default
title: AI 학습 가이드
nav_order: 4
has_children: true
has_toc: false
permalink: /docs/ai
---

# AI 학습 가이드 <span class="page-title-with-cta__ctas"><a class="exam-top-cta" href="{{ site.baseurl }}/docs/ai/daily">🃏 데일리 암기 덱</a><a class="exam-top-cta" href="{{ site.baseurl }}/docs/ai/map">🧭 레거시 MAP</a><a class="exam-top-cta" href="{{ site.baseurl }}/docs/ai/legacy">🗂️ 레거시 메인</a><a class="exam-top-cta" href="{{ site.baseurl }}/docs/ai/exam">📝 기출문제</a></span>
{: .fs-9 .page-title-with-cta }

`수저처-선학평-배모튜`를 중심축으로, **AI 백엔드/AI 거버넌스(위험관리·보안 분리)**까지 한 페이지로 조망합니다.
{: .fs-6 .fw-300 }

---

{% assign ai_root = "AI (인공지능)" %}

{% assign ml_all = site.pages | where: "parent", "1. 기계학습" | where: "grand_parent", ai_root | sort: "nav_order" %}
{% assign dl_all = site.pages | where: "parent", "2. 딥러닝" | where: "grand_parent", ai_root | sort: "nav_order" %}
{% assign nn_all = site.pages | where: "parent", "3. 신경망 알고리즘" | where: "grand_parent", ai_root | sort: "nav_order" %}
{% assign nlp_all = site.pages | where: "parent", "4. 자연어처리" | where: "grand_parent", ai_root | sort: "nav_order" %}
{% assign ethics_all = site.pages | where: "parent", "5. 인공지능 윤리" | where: "grand_parent", ai_root | sort: "nav_order" %}
{% assign eval_all = site.pages | where: "parent", "6. 머신러닝 검증·평가" | where: "grand_parent", ai_root | sort: "nav_order" %}
{% assign learntech_all = site.pages | where: "parent", "7. 학습 기법" | where: "grand_parent", ai_root | sort: "nav_order" %}
{% assign process_all = site.pages | where: "parent", "8. 머신러닝 프로세스" | where: "grand_parent", ai_root | sort: "nav_order" %}
{% assign perf_all = site.pages | where: "parent", "9. 모델 성능" | where: "grand_parent", ai_root | sort: "nav_order" %}
{% assign etc_all = site.pages | where: "parent", "10. AI 기타" | where: "grand_parent", ai_root | sort: "nav_order" %}
{% assign data_all = site.pages | where: "parent", "11. AI 학습용 데이터" | where: "grand_parent", ai_root | sort: "nav_order" %}

{% assign ml_overview = ml_all | where_exp: "p", "p.url contains '/ml-concept' or p.url contains '/modelops' or p.url contains '/dsml' or p.url contains '/mlops' or p.url contains '/aiops'" %}
{% assign ml_supervised = ml_all | where_exp: "p", "p.url contains '/supervised-learning' or p.url contains '/regression-analysis' or p.url contains '/linear-regression' or p.url contains '/logistic-regression' or p.url contains '/multiple-regression' or p.url contains '/multicollinearity' or p.url contains '/knn' or p.url contains '/svm'" %}
{% assign ml_nn_basics = ml_all | where_exp: "p", "p.url contains '/perceptron' or p.url contains '/parameters' or p.url contains '/activation-function' or p.url contains '/vanishing-gradient' or p.url contains '/overfitting-underfitting' or p.url contains '/dropout' or p.url contains '/mlp'" %}
{% assign ml_unsupervised = ml_all | where_exp: "p", "p.url contains '/unsupervised-learning' or p.url contains '/k-means' or p.url contains '/dbscan' or p.url contains '/som' or p.url contains '/pca'" %}
{% assign ml_generative = ml_all | where_exp: "p", "p.url contains '/gan' or p.url contains '/dcgan'" %}
{% assign ml_rl = ml_all | where_exp: "p", "p.url contains '/reinforcement-learning' or p.url contains '/q-learning' or p.url contains '/deep-reinforcement-learning' or p.url contains '/inverse-reinforcement-learning' or p.url contains '/mdp'" %}

{% assign ethics_core = ethics_all | where_exp: "p", "p.url contains '/ai-ethics' or p.url contains '/bias' or p.url contains '/ai-privacy'" %}
{% assign security_core = ethics_all | where_exp: "p", "p.url contains '/ai-security'" %}
{% assign adversarial_extra = data_all | where_exp: "p", "p.url contains '/adversarial-attack'" %}

{% assign dl_models = dl_all | where_exp: "p", "p.url contains '/cnn' or p.url contains '/rnn' or p.url contains '/lstm' or p.url contains '/gru' or p.url contains '/mlp' or p.url contains '/optimizer'" %}
{% assign dl_issues = dl_all | where_exp: "p", "p.url contains '/vanishing-gradient' or p.url contains '/overfitting-underfitting' or p.url contains '/dropout' or p.url contains '/catastrophic-forgetting'" %}
{% assign dl_gen = dl_all | where_exp: "p", "p.url contains '/gan' or p.url contains '/dcgan' or p.url contains '/vae'" %}

{% assign nlp_core = nlp_all | where_exp: "p", "p.url contains '/nlp-basics' or p.url contains '/word-embedding' or p.url contains '/transformer' or p.url contains '/hmm'" %}
{% assign nlp_llm = nlp_all | where_exp: "p", "p.url contains '/electra' or p.url contains '/mrc' or p.url contains '/chatgpt'" %}

{% assign ops_core = process_all | concat: learntech_all | sort: "nav_order" %}

{% assign risk_core = ethics_all | where_exp: "p", "p.url contains '/bias' or p.url contains '/ai-privacy'" %}
{% assign backend_core = ml_all | where_exp: "p", "p.url contains '/mlops' or p.url contains '/modelops' or p.url contains '/aiops'" %}
{% assign backend_process = process_all | where_exp: "p", "p.url contains '/ml-pipeline' or p.url contains '/automl' or p.url contains '/hyperparameters'" %}

<style>
.section-divider-dot {
  text-align: center;
  margin: 2rem 0;
  color: #cbd5e1;
  letter-spacing: 0.5rem;
}
/* 진행률 바 */
.progress-bar {
  position: fixed;
  top: 0;
  left: 0;
  width: 0%;
  height: 4px;
  background: linear-gradient(90deg, #2d3436, #6c5ce7, #0984e3, #00b894);
  z-index: 9999;
  transition: width 0.1s;
}
/* Sticky 섹션 헤더 */
.sticky-header {
  position: sticky;
  top: 0;
  background: white;
  padding: 0.8rem 1rem;
  margin: 0 -1rem;
  z-index: 100;
  border-bottom: 2px solid #e2e8f0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}
.sticky-header-data {
  background: linear-gradient(135deg, #2d3436 0%, #636e72 100%);
  color: #f1f5f9;
  border-bottom: none;
  text-shadow: 0 1px 2px rgba(0,0,0,0.3);
}
.sticky-header-model {
  background: linear-gradient(135deg, #6c5ce7 0%, #a29bfe 100%);
  color: #fff;
  border-bottom: none;
}
.sticky-header-ops {
  background: linear-gradient(135deg, #0984e3 0%, #74b9ff 100%);
  color: #fff;
  border-bottom: none;
}
.sticky-header-backend {
  background: linear-gradient(135deg, #0f172a 0%, #334155 100%);
  color: #fff;
  border-bottom: none;
}
.sticky-header-governance {
  background: linear-gradient(135deg, #4b5563 0%, #111827 100%);
  color: #fff;
  border-bottom: none;
}
.sticky-header-strategy {
  background: linear-gradient(135deg, #00b894 0%, #55efc4 100%);
  color: #fff;
  border-bottom: none;
}

.lifecycle-nav {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
  justify-content: center;
  margin: 1.5rem 0 2rem;
}
.lifecycle-nav a { text-decoration: none !important; transition: transform 0.2s, box-shadow 0.2s; }
.lifecycle-nav a:hover { transform: translateY(-4px); }
.lifecycle-card {
  border-radius: 16px;
  padding: 1.25rem;
  min-width: 200px;
  color: #fff;
}
.lifecycle-card:hover { box-shadow: 0 15px 40px rgba(0,0,0,0.22) !important; }
.lifecycle-arrow { display: flex; align-items: center; font-size: 2rem; opacity: 0.65; }

.topic-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 0.9rem;
  margin: 1rem 0 0;
}
.topic-card {
  border: 1px solid #e5e7eb;
  border-radius: 14px;
  padding: 1rem;
  background: #fff;
  box-shadow: 0 6px 18px rgba(15, 23, 42, 0.06);
}
.topic-card__title { font-weight: 800; margin-bottom: 0.35rem; }
.topic-card__desc { color: #475569; font-size: 0.9rem; line-height: 1.55; margin: 0; }
.topic-card__meta { margin-top: 0.7rem; font-size: 0.8rem; color: #64748b; }

/* 토픽 목록 (Table) */
.topic-table {
  width: 100%;
  border-collapse: separate;
  border-spacing: 0;
  margin: 1rem 0 0;
  border: 1px solid #e5e7eb;
  border-radius: 14px;
  overflow: hidden;
  background: #fff;
  box-shadow: 0 6px 18px rgba(15, 23, 42, 0.06);
}
.topic-table thead th {
  text-align: left;
  font-size: 0.85rem;
  color: #0f172a;
  background: #f8fafc;
  padding: 0.85rem 1rem;
  border-bottom: 1px solid #e5e7eb;
}
.topic-table tbody td {
  vertical-align: top;
  padding: 0.85rem 1rem;
  border-bottom: 1px solid #eef2f7;
  color: #0f172a;
}
.topic-table tbody tr:last-child td { border-bottom: none; }
.topic-table__title a { font-weight: 800; text-decoration: none; }
.topic-table__desc { color: #475569; font-size: 0.9rem; line-height: 1.55; }
.topic-pill {
  display: inline-block;
  padding: 0.2rem 0.55rem;
  border-radius: 999px;
  font-size: 0.75rem;
  font-weight: 700;
  color: #0f172a;
  background: #e2e8f0;
  border: 1px solid #cbd5e1;
}
.topic-pill--data { background: #e2e8f0; }
.topic-pill--model { background: #ede9fe; border-color: #ddd6fe; }
.topic-pill--ops { background: #dbeafe; border-color: #bfdbfe; }
.topic-pill--backend { background: #e5e7eb; border-color: #d1d5db; }
.topic-pill--gov { background: #f1f5f9; border-color: #e2e8f0; }
</style>

<!-- 진행률 바 -->
<div class="progress-bar" id="progressBar"></div>
<script>
window.addEventListener('scroll', function() {
  var winScroll = document.body.scrollTop || document.documentElement.scrollTop;
  var height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
  var scrolled = (winScroll / height) * 100;
  document.getElementById('progressBar').style.width = scrolled + '%';
});
</script>

<details open markdown="1">
<summary><strong>📋 목차 (2단계까지)</strong></summary>

- **수저처 (데이터)**
  - [수집·저장·전처리](#s-data)
- **선학평 (모델)**
  - [선정(알고리즘)](#s-model-select)
  - [학습(딥러닝/NLP/학습기법)](#s-model-train)
  - [평가/성능](#s-model-eval)
- **배모튜 (운영)**
  - [배포·모니터링·튜닝](#s-ops)
- **AI 백엔드**
  - [플랫폼/인프라/프로세스](#s-backend)
- **AI 거버넌스**
  - [거버넌스 체계](#s-gov)
  - [AI 위험관리](#s-risk)
  - [AI 보안](#s-security)
- **전략/생태계**
  - [레거시 MAP (국가/기업)](#s-strategy)

</details>

<div class="lifecycle-nav">
  <a href="#s-data">
    <div class="lifecycle-card" style="background: linear-gradient(135deg, #2d3436 0%, #636e72 100%); box-shadow: 0 10px 26px rgba(45, 52, 54, 0.22);">
      <div style="font-size: 2rem; margin-bottom: 0.35rem;">📦</div>
      <div style="font-weight: 800; font-size: 1.1rem; margin-bottom: 0.35rem;">수저처</div>
      <div style="opacity: 0.92;">수집 · 저장 · 전처리</div>
    </div>
  </a>
  <div class="lifecycle-arrow">→</div>
  <a href="#s-model-select">
    <div class="lifecycle-card" style="background: linear-gradient(135deg, #6c5ce7 0%, #a29bfe 100%); box-shadow: 0 10px 26px rgba(108, 92, 231, 0.22);">
      <div style="font-size: 2rem; margin-bottom: 0.35rem;">🧠</div>
      <div style="font-weight: 800; font-size: 1.1rem; margin-bottom: 0.35rem;">선학평</div>
      <div style="opacity: 0.92;">선정 · 학습 · 평가</div>
    </div>
  </a>
  <div class="lifecycle-arrow">→</div>
  <a href="#s-ops">
    <div class="lifecycle-card" style="background: linear-gradient(135deg, #0984e3 0%, #74b9ff 100%); box-shadow: 0 10px 26px rgba(9, 132, 227, 0.22);">
      <div style="font-size: 2rem; margin-bottom: 0.35rem;">⚙️</div>
      <div style="font-weight: 800; font-size: 1.1rem; margin-bottom: 0.35rem;">배모튜</div>
      <div style="opacity: 0.92;">배포 · 모니터링 · 튜닝</div>
    </div>
  </a>
  <div class="lifecycle-arrow">•</div>
  <a href="#s-backend">
    <div class="lifecycle-card" style="background: linear-gradient(135deg, #0f172a 0%, #334155 100%); box-shadow: 0 10px 26px rgba(15, 23, 42, 0.18);">
      <div style="font-size: 2rem; margin-bottom: 0.35rem;">🧱</div>
      <div style="font-weight: 800; font-size: 1.1rem; margin-bottom: 0.35rem;">AI 백엔드</div>
      <div style="opacity: 0.92;">플랫폼 · 인프라 · 자동화</div>
    </div>
  </a>
  <a href="#s-gov">
    <div class="lifecycle-card" style="background: linear-gradient(135deg, #4b5563 0%, #111827 100%); box-shadow: 0 10px 26px rgba(17, 24, 39, 0.18);">
      <div style="font-size: 2rem; margin-bottom: 0.35rem;">🏛️</div>
      <div style="font-weight: 800; font-size: 1.1rem; margin-bottom: 0.35rem;">AI 거버넌스</div>
      <div style="opacity: 0.92;">체계 · 위험관리 · 보안</div>
    </div>
  </a>
</div>

<div class="section-divider-dot">• • •</div>

<div id="s-data" class="sticky-header sticky-header-data">📦 수저처 › 데이터</div>

<table class="topic-table">
  <thead>
    <tr>
      <th style="width: 28%;">토픽</th>
      <th>요약</th>
      <th style="width: 16%;">태그</th>
    </tr>
  </thead>
  <tbody>
    {% for item in data_all %}
    <tr>
      <td class="topic-table__title"><a href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a></td>
      <td class="topic-table__desc">{{ item.content | markdownify | strip_html | strip_newlines | replace: "  ", " " | truncate: 160 }}</td>
      <td><span class="topic-pill topic-pill--data">학습용 데이터</span></td>
    </tr>
    {% endfor %}
    {% for item in ml_all %}
      {% if item.url contains '/data-labeling' %}
      <tr>
        <td class="topic-table__title"><a href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a></td>
        <td class="topic-table__desc">{{ item.content | markdownify | strip_html | strip_newlines | replace: "  ", " " | truncate: 160 }}</td>
        <td><span class="topic-pill topic-pill--data">라벨링</span></td>
      </tr>
      {% endif %}
    {% endfor %}
  </tbody>
</table>

<div class="section-divider-dot">• • •</div>

<div id="s-model-select" class="sticky-header sticky-header-model">🧠 선학평 › 모델 선정(알고리즘)</div>

<table class="topic-table">
  <thead>
    <tr>
      <th style="width: 28%;">토픽</th>
      <th>요약</th>
      <th style="width: 16%;">태그</th>
    </tr>
  </thead>
  <tbody>
    {% for item in ml_supervised %}
    <tr>
      <td class="topic-table__title"><a href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a></td>
      <td class="topic-table__desc">{{ item.content | markdownify | strip_html | strip_newlines | replace: "  ", " " | truncate: 150 }}</td>
      <td><span class="topic-pill topic-pill--model">지도학습</span></td>
    </tr>
    {% endfor %}
    {% for item in ml_unsupervised %}
    <tr>
      <td class="topic-table__title"><a href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a></td>
      <td class="topic-table__desc">{{ item.content | markdownify | strip_html | strip_newlines | replace: "  ", " " | truncate: 150 }}</td>
      <td><span class="topic-pill topic-pill--model">비지도</span></td>
    </tr>
    {% endfor %}
    {% for item in ml_rl %}
    <tr>
      <td class="topic-table__title"><a href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a></td>
      <td class="topic-table__desc">{{ item.content | markdownify | strip_html | strip_newlines | replace: "  ", " " | truncate: 150 }}</td>
      <td><span class="topic-pill topic-pill--model">강화학습</span></td>
    </tr>
    {% endfor %}
  </tbody>
</table>

<div id="s-model-train" class="sticky-header sticky-header-model" style="margin-top: 1.2rem;">🧠 선학평 › 모델 학습(딥러닝/NLP/학습기법)</div>

<table class="topic-table">
  <thead>
    <tr>
      <th style="width: 28%;">토픽</th>
      <th>요약</th>
      <th style="width: 16%;">태그</th>
    </tr>
  </thead>
  <tbody>
    {% for item in dl_models %}
    <tr>
      <td class="topic-table__title"><a href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a></td>
      <td class="topic-table__desc">{{ item.content | markdownify | strip_html | strip_newlines | replace: "  ", " " | truncate: 150 }}</td>
      <td><span class="topic-pill topic-pill--model">딥러닝</span></td>
    </tr>
    {% endfor %}
    {% for item in nlp_core %}
    <tr>
      <td class="topic-table__title"><a href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a></td>
      <td class="topic-table__desc">{{ item.content | markdownify | strip_html | strip_newlines | replace: "  ", " " | truncate: 150 }}</td>
      <td><span class="topic-pill topic-pill--model">NLP</span></td>
    </tr>
    {% endfor %}
    {% for item in learntech_all %}
    <tr>
      <td class="topic-table__title"><a href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a></td>
      <td class="topic-table__desc">{{ item.content | markdownify | strip_html | strip_newlines | replace: "  ", " " | truncate: 150 }}</td>
      <td><span class="topic-pill topic-pill--model">학습기법</span></td>
    </tr>
    {% endfor %}
  </tbody>
</table>

<div id="s-model-eval" class="sticky-header sticky-header-model" style="margin-top: 1.2rem;">🧠 선학평 › 모델 평가/성능</div>

<table class="topic-table">
  <thead>
    <tr>
      <th style="width: 28%;">토픽</th>
      <th>요약</th>
      <th style="width: 16%;">태그</th>
    </tr>
  </thead>
  <tbody>
    {% for item in eval_all %}
    <tr>
      <td class="topic-table__title"><a href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a></td>
      <td class="topic-table__desc">{{ item.content | markdownify | strip_html | strip_newlines | replace: "  ", " " | truncate: 150 }}</td>
      <td><span class="topic-pill topic-pill--model">평가</span></td>
    </tr>
    {% endfor %}
    {% for item in perf_all %}
    <tr>
      <td class="topic-table__title"><a href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a></td>
      <td class="topic-table__desc">{{ item.content | markdownify | strip_html | strip_newlines | replace: "  ", " " | truncate: 150 }}</td>
      <td><span class="topic-pill topic-pill--model">성능</span></td>
    </tr>
    {% endfor %}
  </tbody>
</table>

<div class="section-divider-dot">• • •</div>

<div id="s-ops" class="sticky-header sticky-header-ops">⚙️ 배모튜 › 운영(배포·모니터링·튜닝)</div>

<table class="topic-table">
  <thead>
    <tr>
      <th style="width: 28%;">토픽</th>
      <th>요약</th>
      <th style="width: 16%;">태그</th>
    </tr>
  </thead>
  <tbody>
    {% for item in process_all %}
    <tr>
      <td class="topic-table__title"><a href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a></td>
      <td class="topic-table__desc">{{ item.content | markdownify | strip_html | strip_newlines | replace: "  ", " " | truncate: 160 }}</td>
      <td><span class="topic-pill topic-pill--ops">프로세스</span></td>
    </tr>
    {% endfor %}
    {% for item in ml_overview %}
      {% if item.url contains '/mlops' or item.url contains '/modelops' or item.url contains '/aiops' %}
      <tr>
        <td class="topic-table__title"><a href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a></td>
        <td class="topic-table__desc">{{ item.content | markdownify | strip_html | strip_newlines | replace: "  ", " " | truncate: 160 }}</td>
        <td><span class="topic-pill topic-pill--ops">운영</span></td>
      </tr>
      {% endif %}
    {% endfor %}
  </tbody>
</table>

<div class="section-divider-dot">• • •</div>

<div id="s-backend" class="sticky-header sticky-header-backend">🧱 AI 백엔드 › 플랫폼/인프라/자동화</div>

<table class="topic-table">
  <thead>
    <tr>
      <th style="width: 28%;">토픽</th>
      <th>요약</th>
      <th style="width: 16%;">태그</th>
    </tr>
  </thead>
  <tbody>
    {% for item in backend_core %}
    <tr>
      <td class="topic-table__title"><a href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a></td>
      <td class="topic-table__desc">{{ item.content | markdownify | strip_html | strip_newlines | replace: "  ", " " | truncate: 170 }}</td>
      <td><span class="topic-pill topic-pill--backend">플랫폼</span></td>
    </tr>
    {% endfor %}
    {% for item in backend_process %}
    <tr>
      <td class="topic-table__title"><a href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a></td>
      <td class="topic-table__desc">{{ item.content | markdownify | strip_html | strip_newlines | replace: "  ", " " | truncate: 170 }}</td>
      <td><span class="topic-pill topic-pill--backend">자동화</span></td>
    </tr>
    {% endfor %}
    <tr>
      <td class="topic-table__title">HW/인프라</td>
      <td class="topic-table__desc">가속기/메모리/인프라 기반 지식은 CAOS 섹션을 함께 보세요.</td>
      <td><span class="topic-pill topic-pill--backend">인프라</span></td>
    </tr>
  </tbody>
</table>
<div style="margin-top: 0.6rem; color: #64748b; font-size: 0.85rem;">
  <a href="{{ site.baseurl }}/docs/caos/13-cpu-gpu/cpu-gpu-fpga-asic">CPU/GPU/ASIC</a> ·
  <a href="{{ site.baseurl }}/docs/caos/12-semiconductor/npu-dpu">NPU/DPU</a> ·
  <a href="{{ site.baseurl }}/docs/caos/12-semiconductor/memory-semiconductor">메모리</a>
</div>

<div class="section-divider-dot">• • •</div>

<div id="s-gov" class="sticky-header sticky-header-governance">🏛️ AI 거버넌스 › 체계</div>

<table class="topic-table">
  <thead>
    <tr>
      <th style="width: 28%;">토픽</th>
      <th>요약</th>
      <th style="width: 16%;">태그</th>
    </tr>
  </thead>
  <tbody>
    {% for item in ethics_core %}
    <tr>
      <td class="topic-table__title"><a href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a></td>
      <td class="topic-table__desc">{{ item.content | markdownify | strip_html | strip_newlines | replace: "  ", " " | truncate: 170 }}</td>
      <td><span class="topic-pill topic-pill--gov">원칙/정책</span></td>
    </tr>
    {% endfor %}
  </tbody>
</table>

<div id="s-risk" class="sticky-header sticky-header-governance" style="margin-top: 1.2rem;">🏛️ AI 거버넌스 › 위험관리</div>

<table class="topic-table">
  <thead>
    <tr>
      <th style="width: 28%;">토픽</th>
      <th>요약</th>
      <th style="width: 16%;">태그</th>
    </tr>
  </thead>
  <tbody>
    {% for item in risk_core %}
    <tr>
      <td class="topic-table__title"><a href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a></td>
      <td class="topic-table__desc">{{ item.content | markdownify | strip_html | strip_newlines | replace: "  ", " " | truncate: 170 }}</td>
      <td><span class="topic-pill topic-pill--gov">리스크</span></td>
    </tr>
    {% endfor %}
    {% for item in perf_all %}
      {% if item.url contains '/drift' %}
      <tr>
        <td class="topic-table__title"><a href="{{ site.baseurl }}{{ item.url }}">Drift (운영 리스크)</a></td>
        <td class="topic-table__desc">{{ item.content | markdownify | strip_html | strip_newlines | replace: "  ", " " | truncate: 170 }}</td>
        <td><span class="topic-pill topic-pill--gov">운영 리스크</span></td>
      </tr>
      {% endif %}
    {% endfor %}
  </tbody>
</table>

<div id="s-security" class="sticky-header sticky-header-governance" style="margin-top: 1.2rem;">🏛️ AI 거버넌스 › AI 보안</div>

<table class="topic-table">
  <thead>
    <tr>
      <th style="width: 28%;">토픽</th>
      <th>요약</th>
      <th style="width: 16%;">태그</th>
    </tr>
  </thead>
  <tbody>
    {% for item in security_core %}
    <tr>
      <td class="topic-table__title"><a href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a></td>
      <td class="topic-table__desc">{{ item.content | markdownify | strip_html | strip_newlines | replace: "  ", " " | truncate: 170 }}</td>
      <td><span class="topic-pill topic-pill--gov">보안</span></td>
    </tr>
    {% endfor %}
    {% for item in adversarial_extra %}
    <tr>
      <td class="topic-table__title"><a href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a></td>
      <td class="topic-table__desc">{{ item.content | markdownify | strip_html | strip_newlines | replace: "  ", " " | truncate: 170 }}</td>
      <td><span class="topic-pill topic-pill--gov">적대적</span></td>
    </tr>
    {% endfor %}
  </tbody>
</table>

<div class="section-divider-dot">• • •</div>

<div id="s-strategy" class="sticky-header sticky-header-strategy">🌐 전략/생태계</div>

레거시 MAP에 정리된 “국가/기업 Level” 상세는 그대로 유지합니다.
{: .note }

- **레거시 MAP 바로가기**: [AI 학습 가이드 (MAP)]({{ site.baseurl }}/docs/ai/map#21-인공지능-국가-level)

<div class="topic-grid">
  <div class="topic-card">
    <div class="topic-card__title">국가 Level</div>
    <p class="topic-card__desc">국가 AI 전략/정책·법·윤리·신뢰성 인증 등 거시적 관점의 프레임을 정리합니다.</p>
    <div class="topic-card__meta">
      <a href="{{ site.baseurl }}/docs/ai/map#21-인공지능-국가-level">국가 Level 바로가기</a>
    </div>
  </div>
  <div class="topic-card">
    <div class="topic-card__title">기업 Level</div>
    <p class="topic-card__desc">기업의 생성형 AI 구축/운영 관점(데이터·모델·플랫폼·조직)과 한계·위협 요소를 정리합니다.</p>
    <div class="topic-card__meta">
      <a href="{{ site.baseurl }}/docs/ai/map#22-인공지능-기업-level">기업 Level 바로가기</a>
    </div>
  </div>
</div>

