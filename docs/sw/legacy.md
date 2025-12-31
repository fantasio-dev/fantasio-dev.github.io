---
layout: default
title: 🗂️ SW 레거시
parent: SW (소프트웨어공학)
nav_order: 99
has_toc: false
permalink: /docs/sw/legacy
---

# SW (소프트웨어공학) <span class="page-title-with-cta__ctas"><a class="exam-top-cta" href="{{ site.baseurl }}/docs/sw/daily">🃏 데일리 암기 덱</a><a class="exam-top-cta" href="{{ site.baseurl }}/docs/sw/exam">📝 기출문제</a></span>
{: .fs-9 .page-title-with-cta }


---

{% assign sw_root = page.title %}

{% assign safety_all = site.pages | where: "parent", "1. 소프트웨어 안전" | where: "grand_parent", sw_root | sort: "nav_order" %}
{% assign quality_all = site.pages | where: "parent", "2. 소프트웨어 품질" | where: "grand_parent", sw_root | sort: "nav_order" %}
{% assign pm_all = site.pages | where: "parent", "3. 프로젝트 관리" | where: "grand_parent", sw_root | sort: "nav_order" %}
{% assign arch_all = site.pages | where: "parent", "4. 소프트웨어 아키텍처" | where: "grand_parent", sw_root | sort: "nav_order" %}
{% assign uml_all = site.pages | where: "parent", "5. UML" | where: "grand_parent", sw_root | sort: "nav_order" %}
{% assign method_all = site.pages | where: "parent", "6. 개발방법론" | where: "grand_parent", sw_root | sort: "nav_order" %}
{% assign oop_all = site.pages | where: "parent", "7. 객체지향(OOP)" | where: "grand_parent", sw_root | sort: "nav_order" %}
{% assign pattern_all = site.pages | where: "parent", "8. 디자인 패턴" | where: "grand_parent", sw_root | sort: "nav_order" %}
{% assign test_all = site.pages | where: "parent", "9. 소프트웨어 테스트" | where: "grand_parent", sw_root | sort: "nav_order" %}
{% assign maint_all = site.pages | where: "parent", "10. 유지보수" | where: "grand_parent", sw_root | sort: "nav_order" %}
{% assign procure_all = site.pages | where: "parent", "11. 발주 프로세스 & 공공SW" | where: "grand_parent", sw_root | sort: "nav_order" %}
{% assign req_all = site.pages | where: "parent", "12. 요구사항 공학" | where: "grand_parent", sw_root | sort: "nav_order" %}
{% assign audit_all = site.pages | where: "parent", "13. 감리" | where: "grand_parent", sw_root | sort: "nav_order" %}
{% assign fp_all = site.pages | where: "parent", "14. FP(Function Point)" | where: "grand_parent", sw_root | sort: "nav_order" %}
{% assign devops_all = site.pages | where: "parent", "15. DevOps / TDD / SRE" | where: "grand_parent", sw_root | sort: "nav_order" %}
{% assign oss_all = site.pages | where: "parent", "16. 오픈소스" | where: "grand_parent", sw_root | sort: "nav_order" %}
{% assign etc_all = site.pages | where: "parent", "17. 기타 SW 일반" | where: "grand_parent", sw_root | sort: "nav_order" %}

<div class="sw-matrix">
  <div class="sw-matrix__grid">
    <!-- ① 개발방법론 -->
    <section class="sw-card">
      <div class="sw-card__header">① SW 개발방법론</div>
      <div class="sw-card__body">
        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/sw/06-methodology">개발방법론</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in method_all %}
                <a class="nw-link nw-link--blue" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ② 요구사항 -->
    <section class="sw-card">
      <div class="sw-card__header">② SW 요구사항</div>
      <div class="sw-card__body">
        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/sw/12-requirements">요구사항 공학</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in req_all %}
                <a class="nw-link nw-link--strong" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ③ 분석/설계 -->
    <section class="sw-card">
      <div class="sw-card__header">③ SW 분석/설계</div>
      <div class="sw-card__body">
        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/sw/04-architecture">아키텍처</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in arch_all %}
                <a class="nw-link nw-link--blue" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
            </div>
          </div>
        </div>

        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/sw/05-uml">UML</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in uml_all %}
                <a class="nw-link" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
            </div>
          </div>
        </div>

        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/sw/07-oop">OOP</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in oop_all %}
                <a class="nw-link" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
            </div>
          </div>
        </div>

        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/sw/08-design-pattern">디자인 패턴</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in pattern_all %}
                <a class="nw-link nw-link--strong" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ④ 증명/검증 -->
    <section class="sw-card">
      <div class="sw-card__header">④ SW 증명/검증(테스트)</div>
      <div class="sw-card__body">
        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/sw/09-testing">테스트</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in test_all %}
                <a class="nw-link nw-link--blue" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ⑤ 배포/운영 -->
    <section class="sw-card">
      <div class="sw-card__header">⑤ SW 배포/운영</div>
      <div class="sw-card__body">
        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/sw/15-devops">DevOps / TDD / SRE</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in devops_all %}
                <a class="nw-link nw-link--red" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
              {% for item in etc_all %}
                <a class="nw-link" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
            </div>
          </div>
        </div>

        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/sw/16-opensource">오픈소스</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in oss_all %}
                <a class="nw-link nw-link--blue" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ⑥ 유지관리 -->
    <section class="sw-card">
      <div class="sw-card__header">⑥ SW 유지관리</div>
      <div class="sw-card__body">
        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/sw/10-maintenance">유지보수</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in maint_all %}
                <a class="nw-link" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ⑦ 품질/안전 -->
    <section class="sw-card">
      <div class="sw-card__header">⑦ SW 품질/안전</div>
      <div class="sw-card__body">
        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/sw/02-quality">품질</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in quality_all %}
                <a class="nw-link nw-link--blue" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
            </div>
          </div>
        </div>
        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/sw/01-safety">안전</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in safety_all %}
                <a class="nw-link nw-link--red" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ⑧ 제도/가이드 -->
    <section class="sw-card">
      <div class="sw-card__header">⑧ 제도/가이드</div>
      <div class="sw-card__body">
        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/sw/11-procurement">발주/공공SW</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in procure_all %}
                <a class="nw-link nw-link--strong" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
            </div>
          </div>
        </div>

        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/sw/13-audit">감리</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in audit_all %}
                <a class="nw-link" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
            </div>
          </div>
        </div>

        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/sw/14-function-point">FP</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in fp_all %}
                <a class="nw-link nw-link--blue" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ⑨ 프로젝트관리/애자일 -->
    <section class="sw-card">
      <div class="sw-card__header">⑨ 프로젝트관리/애자일</div>
      <div class="sw-card__body">
        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/sw/03-project-management">프로젝트 관리(PM)</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in pm_all %}
                <a class="nw-link nw-link--strong" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
              {% assign agile_like = method_all | where_exp: "p", "p.url contains '/agile' or p.url contains '/scrum' or p.url contains '/kanban'" %}
              {% for item in agile_like %}
                <a class="nw-link nw-link--red" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
              {% assign safe_like = etc_all | where_exp: "p", "p.url contains '/safe'" %}
              {% for item in safe_like %}
                <a class="nw-link nw-link--red" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
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
    <strong>개발방법론</strong> → <strong>요구사항</strong> → <strong>분석/설계</strong>(아키텍처/UML/OOP/패턴) → <strong>검증</strong>(테스트) → <strong>배포/운영</strong>(DevOps/OSS) → <strong>유지관리</strong> → <strong>품질/안전</strong> → <strong>제도/PM</strong>
  </div>
</div>

