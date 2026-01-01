---
layout: default
title: BIZ (경영)
nav_order: 8
has_children: true
has_toc: false
permalink: /docs/biz
---

# BIZ (경영)
{: .fs-9 }


---

{% assign biz_root = page.title %}

{% assign vc_all = site.pages | where: "parent", "1. 가치사슬 (Value Chain)" | where: "grand_parent", biz_root | sort: "nav_order" %}
{% assign strategy_all = site.pages | where: "parent", "2. 경영전략" | where: "grand_parent", biz_root | sort: "nav_order" %}
{% assign bcp_all = site.pages | where_exp: "p", "p.parent contains '3.' and p.grand_parent == biz_root" | sort: "nav_order" %}
{% assign itsm_all = site.pages | where: "parent", "4. ITSM" | where: "grand_parent", biz_root | sort: "nav_order" %}
{% assign mining_all = site.pages | where: "parent", "5. 데이터 마이닝" | where: "grand_parent", biz_root | sort: "nav_order" %}
{% assign gov_all = site.pages | where: "parent", "6. IT 거버넌스" | where: "grand_parent", biz_root | sort: "nav_order" %}
{% assign society_all = site.pages | where: "parent", "7. 경영·경제·사회·정책" | where: "grand_parent", biz_root | sort: "nav_order" %}
{% assign out_all = site.pages | where: "parent", "8. IT 아웃소싱 & 컴플라이언스" | where: "grand_parent", biz_root | sort: "nav_order" %}

{% assign strat_tools = strategy_all | where_exp: "p", "p.url contains '/mece' or p.url contains '/liss' or p.url contains '/swot' or p.url contains '/4c-3c' or p.url contains '/pest' or p.url contains '/4p' or p.url contains '/5-forces' or p.url contains '/7s-model' or p.url contains '/decision-tree'" %}
{% assign strat_plan = strategy_all | where_exp: "p", "p.url contains '/isp' or p.url contains '/ismp' or p.url contains '/bcg-matrix'" %}
{% assign strat_kpi = strategy_all | where_exp: "p", "p.url contains '/bsc' or p.url contains '/it-bsc' or p.url contains '/kpi' or p.url contains '/okr' or p.url contains '/mbo' or p.url contains '/performance-evaluation'" %}
{% assign strat_inno = strategy_all | where_exp: "p", "p.url contains '/growth-hacking' or p.url contains '/design-thinking' or p.url contains '/empathy-map' or p.url contains '/customer-journey-map'" %}
{% assign strat_itinv = strategy_all | where_exp: "p", "p.url contains '/it-investment' or p.url contains '/it-roi' or p.url contains '/economic-evaluation'" %}
{% assign strat_adopt = strategy_all | where_exp: "p", "p.url contains '/chasm' or p.url contains '/death-valley'" %}

{% assign soc_esg = society_all | where_exp: "p", "p.url contains '/esg' or p.url contains '/k-esg' or p.url contains '/re100'" %}
{% assign soc_trend = society_all | where_exp: "p", "p.url contains '/sharing-economy' or p.url contains '/subscription-economy' or p.url contains '/intention-economy'" %}
{% assign soc_platform = society_all | where_exp: "p", "p.url contains '/data-commerce' or p.url contains '/digital-platform' or p.url contains '/digital-platform-gov'" %}
{% assign soc_society = society_all | where_exp: "p", "p.url contains '/living-lab' or p.url contains '/sos-lab' or p.url contains '/civic-hacking' or p.url contains '/digital-cartel' or p.url contains '/regulatory-sandbox'" %}

{% assign bcp_core = bcp_all | where_exp: "p", "p.url contains '/bcm-bcp' or p.url contains '/iso-22301'" %}
{% assign bcp_dr = bcp_all | where_exp: "p", "p.url contains '/drs' or p.url contains '/drp' or p.url contains '/draas'" %}
{% assign bcp_ops = bcp_all | where_exp: "p", "p.url contains '/rto-rpo' or p.url contains '/bia' or p.url contains '/ra'" %}

<div class="biz-matrix">
  <div class="biz-matrix__grid">
    <!-- ① 기업 외부 영향 -->
    <section class="biz-card">
      <div class="biz-card__header">① 기업 외부 영향</div>
      <div class="biz-card__body">
        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/biz/07-esg-society">경영·경제·사회·정책</a></div>
          <div class="nw-sub__content">
            <div class="nw-chip-groups">
              <div class="nw-chip-group">
                <div class="nw-chip-group__title">ESG/정책</div>
                <div class="nw-links">
                  {% for item in soc_esg %}
                    <a class="nw-link nw-link--red" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
                  {% endfor %}
                  {% for item in soc_platform %}
                    <a class="nw-link nw-link--blue" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
                  {% endfor %}
                </div>
              </div>
              <div class="nw-chip-group">
                <div class="nw-chip-group__title">사회/트렌드</div>
                <div class="nw-links">
                  {% for item in soc_trend %}
                    <a class="nw-link" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
                  {% endfor %}
                  {% for item in soc_society %}
                    <a class="nw-link" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
                  {% endfor %}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ② 기업 전략 -->
    <section class="biz-card">
      <div class="biz-card__header">② 기업 전략</div>
      <div class="biz-card__body">
        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/biz/02-strategy">경영전략</a></div>
          <div class="nw-sub__content">
            <div class="nw-chip-groups">
              <div class="nw-chip-group">
                <div class="nw-chip-group__title">도구/계획</div>
                <div class="nw-links">
                  {% for item in strat_tools %}
                    <a class="nw-link" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
                  {% endfor %}
                  {% for item in strat_plan %}
                    <a class="nw-link nw-link--blue" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
                  {% endfor %}
                </div>
              </div>
              <div class="nw-chip-group">
                <div class="nw-chip-group__title">성과/혁신</div>
                <div class="nw-links">
                  {% for item in strat_kpi %}
                    <a class="nw-link nw-link--strong" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
                  {% endfor %}
                  {% for item in strat_inno %}
                    <a class="nw-link" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
                  {% endfor %}
                </div>
              </div>
              <div class="nw-chip-group">
                <div class="nw-chip-group__title">IT 투자/수용</div>
                <div class="nw-links">
                  {% for item in strat_itinv %}
                    <a class="nw-link nw-link--red" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
                  {% endfor %}
                  {% for item in strat_adopt %}
                    <a class="nw-link" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
                  {% endfor %}
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/biz/06-it-governance">IT 거버넌스</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in gov_all %}
                <a class="nw-link nw-link--blue" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ③ 위험관리(BCP) -->
    <section class="biz-card">
      <div class="biz-card__header">③ 위험관리(BCP/BCM)</div>
      <div class="biz-card__body">
        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/biz/03-bcp-bcm">BCP/BCM</a></div>
          <div class="nw-sub__content">
            <div class="nw-chip-groups">
              <div class="nw-chip-group">
                <div class="nw-chip-group__title">기본/표준</div>
                <div class="nw-links">
                  {% for item in bcp_core %}
                    <a class="nw-link nw-link--blue" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
                  {% endfor %}
                </div>
              </div>
              <div class="nw-chip-group">
                <div class="nw-chip-group__title">DR</div>
                <div class="nw-links">
                  {% for item in bcp_dr %}
                    <a class="nw-link nw-link--red" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
                  {% endfor %}
                </div>
              </div>
              <div class="nw-chip-group">
                <div class="nw-chip-group__title">운영 요소</div>
                <div class="nw-links">
                  {% for item in bcp_ops %}
                    <a class="nw-link nw-link--strong" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
                  {% endfor %}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ④ IT 서비스 관리 -->
    <section class="biz-card">
      <div class="biz-card__header">④ IT 서비스 관리(ITSM)</div>
      <div class="biz-card__body">
        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/biz/04-itsm">ITSM</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in itsm_all %}
                <a class="nw-link nw-link--blue" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
            </div>
          </div>
        </div>
        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/biz/08-outsourcing">아웃소싱/컴플라이언스</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in out_all %}
                <a class="nw-link" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ⑤ 데이터 분석 -->
    <section class="biz-card">
      <div class="biz-card__header">⑤ 데이터 분석(마이닝/BI)</div>
      <div class="biz-card__body">
        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/biz/05-data-mining">데이터마이닝</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in mining_all %}
                <a class="nw-link nw-link--blue" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ⑥ 가치(시스템/서비스) -->
    <section class="biz-card">
      <div class="biz-card__header">⑥ 가치(시스템/서비스)</div>
      <div class="biz-card__body">
        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/biz/01-value-chain">가치사슬(Value Chain)</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in vc_all %}
                <a class="nw-link nw-link--strong" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
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
    <strong>외부 환경</strong>(ESG/정책/트렌드) → <strong>전략</strong>(도구/계획/성과) → <strong>거버넌스</strong> → <strong>위험관리</strong>(BCP/DR) → <strong>서비스 운영</strong>(ITSM/아웃소싱) → <strong>가치 실현</strong>(가치사슬/분석)
  </div>
</div>

