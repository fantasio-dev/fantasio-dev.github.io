---
layout: default
title: DB (데이터베이스)
nav_order: 7
has_children: true
has_toc: false
permalink: /docs/db
---

# DB (데이터베이스) <span class="page-title-with-cta__ctas"><a class="exam-top-cta" href="{{ site.baseurl }}/docs/db/daily">🃏 데일리 암기 덱</a><a class="exam-top-cta" href="{{ site.baseurl }}/docs/db/exam">📝 기출문제</a></span>
{: .fs-9 .page-title-with-cta }


---

{% assign db_root = page.title %}

{% assign big_all = site.pages | where: "parent", "1. 빅데이터" | where: "grand_parent", db_root | sort: "nav_order" %}
{% assign basics_all = site.pages | where: "parent", "2. 데이터베이스 기본" | where: "grand_parent", db_root | sort: "nav_order" %}
{% assign modeling_all = site.pages | where: "parent", "3. 데이터 모델링 & 설계" | where: "grand_parent", db_root | sort: "nav_order" %}
{% assign tx_all = site.pages | where: "parent", "4. 트랜잭션" | where: "grand_parent", db_root | sort: "nav_order" %}
{% assign cc_all = site.pages | where: "parent", "5. 동시성 제어" | where: "grand_parent", db_root | sort: "nav_order" %}
{% assign rec_all = site.pages | where: "parent", "6. 데이터 회복" | where: "grand_parent", db_root | sort: "nav_order" %}
{% assign dq_all = site.pages | where: "parent", "7. 데이터 품질" | where: "grand_parent", db_root | sort: "nav_order" %}
{% assign pub_all = site.pages | where: "parent", "8. 공공데이터" | where: "grand_parent", db_root | sort: "nav_order" %}
{% assign perf_all = site.pages | where: "parent", "9. DB 성능" | where: "grand_parent", db_root | sort: "nav_order" %}
{% assign policy_all = site.pages | where: "parent", "10. 정책·데이터 활용" | where: "grand_parent", db_root | sort: "nav_order" %}

{% assign big_concept = big_all | where_exp: "p", "p.url contains '/bigdata-3v-6v' or p.url contains '/bigdata-visualization' or p.url contains '/bigdata-analysis-tool' or p.url contains '/correlation-causation'" %}
{% assign big_platform = big_all | where_exp: "p", "p.url contains '/hadoop-' or p.url contains '/lambda-kappa' or p.url contains '/apache-kafka' or p.url contains '/data-warehouse' or p.url contains '/data-lake' or p.url contains '/data-fabric'" %}
{% assign big_mining = big_all | where_exp: "p", "p.url contains '/bagging-boosting' or p.url contains '/random-forest' or p.url contains '/ensemble-learning' or p.url contains '/analysis-model-evaluation'" %}
{% assign big_security = big_all | where_exp: "p", "p.url contains '/bigdata-security'" %}

{% assign basics_type = basics_all | where_exp: "p", "p.url contains '/nosql' or p.url contains '/cap-theorem' or p.url contains '/pacelc' or p.url contains '/newsql' or p.url contains '/distributed-db' or p.url contains '/other-databases'" %}
{% assign basics_structure = basics_all | where_exp: "p", "p.url contains '/three-level-architecture' or p.url contains '/data-modeling' or p.url contains '/dimensional-modeling'" %}

{% assign model_norm = modeling_all | where_exp: "p", "p.url contains '/functional-dependency' or p.url contains '/normalization' or p.url contains '/denormalization' or p.url contains '/anomaly'" %}
{% assign model_integrity = modeling_all | where_exp: "p", "p.url contains '/integrity-constraints' or p.url contains '/relation-integrity' or p.url contains '/integrity-maintenance'" %}
{% assign model_keys = modeling_all | where_exp: "p", "p.url contains '/keys'" %}

<div class="db-matrix">
  <div class="db-matrix__grid">
    <!-- ① DB 기초/트랜잭션 -->
    <section class="db-card db-card--core">
      <div class="db-card__header">① DB 기초/트랜잭션</div>
      <div class="db-card__body">
        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/db/02-db-basics">데이터베이스 기본</a></div>
          <div class="nw-sub__content">
            <div class="nw-chip-groups">
              <div class="nw-chip-group">
                <div class="nw-chip-group__title">DB 유형/분산</div>
                <div class="nw-links">
                  {% for item in basics_type %}
                    <a class="nw-link nw-link--blue" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
                  {% endfor %}
                </div>
              </div>
              <div class="nw-chip-group">
                <div class="nw-chip-group__title">구조/모델</div>
                <div class="nw-links">
                  {% for item in basics_structure %}
                    <a class="nw-link" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
                  {% endfor %}
                </div>
              </div>
              <div class="nw-chip-group">
                <div class="nw-chip-group__title">성능(튜닝)</div>
                <div class="nw-links">
                  {% for item in perf_all %}
                    <a class="nw-link" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
                  {% endfor %}
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/db/04-transaction">트랜잭션</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in tx_all %}
                <a class="nw-link nw-link--red" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
            </div>
          </div>
        </div>

        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/db/05-concurrency">동시성 제어</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in cc_all %}
                <a class="nw-link nw-link--strong" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
            </div>
          </div>
        </div>

        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/db/06-recovery">데이터 회복</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in rec_all %}
                <a class="nw-link" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ② 데이터 모델링 -->
    <section class="db-card db-card--modeling">
      <div class="db-card__header">② 데이터 모델링 🔥</div>
      <div class="db-card__body">
        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/db/03-modeling-design">모델링 & 설계</a></div>
          <div class="nw-sub__content">
            <div class="nw-chip-groups">
              <div class="nw-chip-group">
                <div class="nw-chip-group__title">정규화</div>
                <div class="nw-links">
                  {% for item in model_norm %}
                    <a class="nw-link nw-link--blue" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
                  {% endfor %}
                </div>
              </div>
              <div class="nw-chip-group">
                <div class="nw-chip-group__title">무결성</div>
                <div class="nw-links">
                  {% for item in model_integrity %}
                    <a class="nw-link" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
                  {% endfor %}
                </div>
              </div>
              <div class="nw-chip-group">
                <div class="nw-chip-group__title">KEY</div>
                <div class="nw-links">
                  {% for item in model_keys %}
                    <a class="nw-link nw-link--strong" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
                  {% endfor %}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ③ 데이터마이닝/빅데이터 분석 -->
    <section class="db-card db-card--analytics">
      <div class="db-card__header">③ 데이터마이닝/빅데이터 분석</div>
      <div class="db-card__body">
        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/db/01-bigdata">빅데이터</a></div>
          <div class="nw-sub__content">
            <div class="nw-chip-groups">
              <div class="nw-chip-group">
                <div class="nw-chip-group__title">개요</div>
                <div class="nw-links">
                  {% for item in big_concept %}
                    <a class="nw-link nw-link--blue" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
                  {% endfor %}
                </div>
              </div>
              <div class="nw-chip-group">
                <div class="nw-chip-group__title">플랫폼</div>
                <div class="nw-links">
                  {% for item in big_platform %}
                    <a class="nw-link" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
                  {% endfor %}
                </div>
              </div>
              <div class="nw-chip-group">
                <div class="nw-chip-group__title">분석/마이닝</div>
                <div class="nw-links">
                  {% for item in big_mining %}
                    <a class="nw-link nw-link--strong" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
                  {% endfor %}
                </div>
              </div>
              <div class="nw-chip-group">
                <div class="nw-chip-group__title">보안</div>
                <div class="nw-links">
                  {% for item in big_security %}
                    <a class="nw-link nw-link--red" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
                  {% endfor %}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ④ 데이터 품질 -->
    <section class="db-card db-card--quality">
      <div class="db-card__header">④ 데이터 품질관리 🔥</div>
      <div class="db-card__body">
        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/db/07-data-quality">데이터 품질</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in dq_all %}
                <a class="nw-link nw-link--blue" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ⑤ 정책/공공 -->
    <section class="db-card db-card--policy">
      <div class="db-card__header">⑤ 데이터 정책/공공데이터</div>
      <div class="db-card__body">
        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/db/10-data-policy">정책·활용</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in policy_all %}
                <a class="nw-link nw-link--blue" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
            </div>
          </div>
        </div>
        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/db/08-public-data">공공데이터</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in pub_all %}
                <a class="nw-link" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</div>

<div class="story-flow">
  <div class="story-flow__title">스토리 흐름</div>
  <div class="story-flow__line">
    <strong>DB 기초/트랜잭션</strong> → <strong>모델링</strong> → <strong>분석</strong>(빅데이터/마이닝) → <strong>품질</strong> → <strong>정책/공공데이터</strong>
  </div>
</div>

