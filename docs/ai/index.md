---
layout: default
title: AI (인공지능)
nav_order: 4
has_children: true
permalink: /docs/ai
---

# AI (인공지능)
{: .fs-9 }

인공지능 관련 학습 자료입니다. 총 **80개** 항목
{: .fs-6 .fw-300 }

---

{% assign ai_root = page.title %}

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

{% assign ethics_core = ethics_all | where_exp: "p", "p.url contains '/ai-ethics' or p.url contains '/bias' or p.url contains '/ai-privacy' or p.url contains '/ai-security'" %}
{% assign ai_security_extra = data_all | where_exp: "p", "p.url contains '/adversarial-attack'" %}

{% assign dl_models = dl_all | where_exp: "p", "p.url contains '/cnn' or p.url contains '/rnn' or p.url contains '/lstm' or p.url contains '/gru' or p.url contains '/mlp' or p.url contains '/optimizer'" %}
{% assign dl_issues = dl_all | where_exp: "p", "p.url contains '/vanishing-gradient' or p.url contains '/overfitting-underfitting' or p.url contains '/dropout' or p.url contains '/catastrophic-forgetting'" %}
{% assign dl_gen = dl_all | where_exp: "p", "p.url contains '/gan' or p.url contains '/dcgan' or p.url contains '/vae'" %}

{% assign nlp_core = nlp_all | where_exp: "p", "p.url contains '/nlp-basics' or p.url contains '/word-embedding' or p.url contains '/transformer' or p.url contains '/hmm'" %}
{% assign nlp_llm = nlp_all | where_exp: "p", "p.url contains '/electra' or p.url contains '/mrc' or p.url contains '/chatgpt'" %}

{% assign ops_core = process_all | concat: learntech_all | concat: eval_all | concat: perf_all | sort: "nav_order" %}

<div class="ai-matrix">
  <div class="ai-matrix__grid">
    <!-- ① AI 개요 -->
    <section class="ai-card ai-card--overview">
      <div class="ai-card__header">① AI 개요</div>
      <div class="ai-card__body">
        <div class="nw-sub">
          <div class="nw-sub__title">핵심 키워드</div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in ml_overview %}
                <a class="nw-link nw-link--blue" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
              {% for item in etc_all %}
                <a class="nw-link" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ② 기계학습 (크게) -->
    <section class="ai-card ai-card--ml">
      <div class="ai-card__header">② 기계학습 (Machine Learning)</div>
      <div class="ai-card__body">
        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/ai/01-machine-learning">기계학습</a></div>
          <div class="nw-sub__content">
            <div class="nw-chip-groups">
              <div class="nw-chip-group">
                <div class="nw-chip-group__title">지도학습(분류/회귀)</div>
                <div class="nw-links">
                  {% for item in ml_supervised %}
                    <a class="nw-link nw-link--blue" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
                  {% endfor %}
                </div>
              </div>
              <div class="nw-chip-group">
                <div class="nw-chip-group__title">신경망 기본/학습 이슈</div>
                <div class="nw-links">
                  {% for item in ml_nn_basics %}
                    <a class="nw-link" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
                  {% endfor %}
                </div>
              </div>
              <div class="nw-chip-group">
                <div class="nw-chip-group__title">비지도/차원축소</div>
                <div class="nw-links">
                  {% for item in ml_unsupervised %}
                    <a class="nw-link" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
                  {% endfor %}
                </div>
              </div>
              <div class="nw-chip-group">
                <div class="nw-chip-group__title">생성/강화</div>
                <div class="nw-links">
                  {% for item in ml_generative %}
                    <a class="nw-link nw-link--red" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
                  {% endfor %}
                  {% for item in ml_rl %}
                    <a class="nw-link nw-link--strong" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
                  {% endfor %}
                </div>
              </div>
              <div class="nw-chip-group">
                <div class="nw-chip-group__title">검증/평가/운영</div>
                <div class="nw-links">
                  {% for item in ops_core %}
                    <a class="nw-link" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
                  {% endfor %}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ③ AI 기술 -->
    <section class="ai-card ai-card--tech">
      <div class="ai-card__header">③ AI 기술</div>
      <div class="ai-card__body">
        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/ai/02-deep-learning">딥러닝</a></div>
          <div class="nw-sub__content">
            <div class="nw-chip-groups">
              <div class="nw-chip-group">
                <div class="nw-chip-group__title">모델</div>
                <div class="nw-links">
                  {% for item in dl_models %}
                    <a class="nw-link nw-link--blue" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
                  {% endfor %}
                </div>
              </div>
              <div class="nw-chip-group">
                <div class="nw-chip-group__title">이슈/생성</div>
                <div class="nw-links">
                  {% for item in dl_issues %}
                    <a class="nw-link" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
                  {% endfor %}
                  {% for item in dl_gen %}
                    <a class="nw-link nw-link--red" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
                  {% endfor %}
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/ai/04-nlp">자연어처리</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in nlp_core %}
                <a class="nw-link nw-link--blue" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
              {% for item in nlp_llm %}
                <a class="nw-link nw-link--red nw-link--strong" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
            </div>
          </div>
        </div>

        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/ai/03-neural-network">특수 신경망</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in nn_all %}
                <a class="nw-link" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ④ AI 윤리/보안 -->
    <section class="ai-card ai-card--ethics">
      <div class="ai-card__header">④ AI 윤리/보안</div>
      <div class="ai-card__body">
        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/ai/05-ai-ethics">윤리/신뢰</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in ethics_core %}
                <a class="nw-link nw-link--blue" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
              {% for item in ai_security_extra %}
                <a class="nw-link nw-link--red" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ⑤ 하드웨어 -->
    <section class="ai-card ai-card--hardware">
      <div class="ai-card__header">⑤ 하드웨어</div>
      <div class="ai-card__body">
        <div class="nw-sub">
          <div class="nw-sub__title">가속기/메모리</div>
          <div class="nw-sub__content">
            <div class="nw-links">
              <a class="nw-link nw-link--blue" href="{{ site.baseurl }}/docs/caos/13-cpu-gpu/cpu-gpu-fpga-asic">CPU, GPU, FPGA, ASIC</a>
              <a class="nw-link" href="{{ site.baseurl }}/docs/caos/12-semiconductor/npu-dpu">NPU/DPU</a>
              <a class="nw-link" href="{{ site.baseurl }}/docs/caos/12-semiconductor/memory-semiconductor">메모리 반도체</a>
              <a class="nw-link" href="{{ site.baseurl }}/docs/caos/14-ca-etc/memory-interleaving">메모리 인터리빙</a>
              <a class="nw-link" href="{{ site.baseurl }}/docs/caos/14-ca-etc/dma">DMA</a>
              <a class="nw-link" href="{{ site.baseurl }}/docs/caos/09-memory/pnm">PNM</a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ⑥ 운영 -->
    <section class="ai-card ai-card--ops">
      <div class="ai-card__header">⑥ 운영/프로세스</div>
      <div class="ai-card__body">
        <div class="nw-sub">
          <div class="nw-sub__title">프로세스/학습기법</div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in process_all %}
                <a class="nw-link" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
              {% for item in learntech_all %}
                <a class="nw-link nw-link--blue" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
              {% for item in perf_all %}
                <a class="nw-link" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
              {% for item in eval_all %}
                <a class="nw-link nw-link--strong" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
              {% for item in data_all %}
                <a class="nw-link" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ⑦ 서비스 -->
    <section class="ai-card ai-card--service">
      <div class="ai-card__header">⑦ 서비스</div>
      <div class="ai-card__body">
        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/ai/10-ai-etc">활용/기타</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in etc_all %}
                <a class="nw-link" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</div>

