---
layout: default
title: NW (네트워크)
nav_order: 6
has_children: true
permalink: /docs/nw
---

# NW (네트워크)
{: .fs-9 }

네트워크 관련 학습 자료입니다. 총 **85개** 항목
{: .fs-6 .fw-300 }

{% assign nw_root = page.title %}

<div class="nw-matrix">
  <div class="nw-matrix__grid">
    <!-- ① 네트워크 기본 -->
    <section class="nw-card nw-card--a">
      <div class="nw-card__header">① 네트워크 기본</div>
      <div class="nw-card__body">
        <div class="nw-sub">
          <div class="nw-sub__title">
            <a href="{{ site.baseurl }}/docs/nw/03-fundamentals">네트워크 기본 개념</a>
          </div>
          <div class="nw-sub__content">
            <div class="nw-chips">
              {% assign basic_items = site.pages | where: "parent", "3. 네트워크 기본" | where: "grand_parent", nw_root | sort: "nav_order" %}
              {% for item in basic_items %}
                <a href="{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a>
              {% endfor %}
            </div>
          </div>
        </div>

        <div class="nw-sub">
          <div class="nw-sub__title">
            <a href="{{ site.baseurl }}/docs/nw/07-osi-layer">네트워크 기본 모델 (OSI 7 Layer)</a>
            <span class="nw-badge-hot">🔥</span>
          </div>
          <div class="nw-sub__content">
            <div class="nw-chips">
              {% assign osi_items = site.pages | where: "parent", "7. OSI 7 Layer" | where: "grand_parent", nw_root | sort: "nav_order" %}
              {% for item in osi_items %}
                <a href="{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a>
              {% endfor %}
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ② 네트워크(통신) 기술 -->
    <section class="nw-card nw-card--b">
      <div class="nw-card__header">② 네트워크(통신) 기술</div>
      <div class="nw-card__body">
        <div class="nw-sub">
          <div class="nw-sub__title">
            유선 통신 기술 (선)
          </div>
          <div class="nw-sub__content">
            <div class="nw-chips">
              {% assign nw_topics = site.pages | where: "grand_parent", nw_root %}
              {% assign wired_core = nw_topics | where_exp: "p", "p.url contains '/03-fundamentals/line-control' or p.url contains '/03-fundamentals/switching' or p.url contains '/03-fundamentals/multiplexing' or p.url contains '/03-fundamentals/multiple-access'" %}
              {% assign wired_infra = nw_topics | where_exp: "p", "p.url contains '/04-infrastructure/reverse-proxy' or p.url contains '/04-infrastructure/forward-proxy' or p.url contains '/04-infrastructure/load-balancer'" %}
              {% assign wired_etc = nw_topics | where_exp: "p", "p.url contains '/10-etc/gslb' or p.url contains '/10-etc/smb-protocol'" %}
              {% assign wired = wired_core | concat: wired_infra | concat: wired_etc | uniq %}

              <a class="nw-chip--primary" href="{{ site.baseurl }}/docs/nw/03-fundamentals">기본(유선)</a>
              <a class="nw-chip--primary" href="{{ site.baseurl }}/docs/nw/04-infrastructure">구성요소</a>
              {% for item in wired %}
                <a href="{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a>
              {% endfor %}
            </div>
          </div>
        </div>

        <div class="nw-sub">
          <div class="nw-sub__title">
            무선 통신 기술 (주파수)
          </div>
          <div class="nw-sub__content">
            <div class="nw-chips">
              {% assign mobile_items = site.pages | where: "parent", "8. 이동통신" | where: "grand_parent", nw_root | sort: "nav_order" %}
              {% assign wlan_items = nw_topics | where_exp: "p", "p.url contains '/04-infrastructure/wlan-architecture' or p.url contains '/04-infrastructure/wifi7'" %}
              {% assign radio_infra = nw_topics | where_exp: "p", "p.url contains '/04-infrastructure/o-ran' or p.url contains '/04-infrastructure/5g-' or p.url contains '/04-infrastructure/ps-lte' or p.url contains '/04-infrastructure/leo-mobile' or p.url contains '/04-infrastructure/ran-sharing' or p.url contains '/04-infrastructure/6g'" %}
              {% assign wireless = mobile_items | concat: wlan_items | concat: radio_infra | uniq %}

              <a class="nw-chip--primary" href="{{ site.baseurl }}/docs/nw/08-mobile">이동통신</a>
              <a class="nw-chip--primary" href="{{ site.baseurl }}/docs/nw/04-infrastructure">WLAN/구축</a>
              {% for item in wireless %}
                <a href="{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a>
              {% endfor %}
            </div>
          </div>
        </div>

        <div class="nw-sub">
          <div class="nw-sub__title">분야 별 통신기술</div>
          <div class="nw-sub__content">
            <div class="nw-chips">
              {% assign iot_items = site.pages | where: "parent", "1. IoT" | where: "grand_parent", nw_root | sort: "nav_order" %}
              {% for item in iot_items %}
                <a href="{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a>
              {% endfor %}

              {% assign adhoc_items = site.pages | where: "parent", "2. 드론 (Ad-hoc)" | where: "grand_parent", nw_root | sort: "nav_order" %}
              {% for item in adhoc_items %}
                <a href="{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a>
              {% endfor %}

              {% assign loc_items = site.pages | where: "parent", "9. 위치 측위" | where: "grand_parent", nw_root | sort: "nav_order" %}
              {% for item in loc_items %}
                <a href="{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a>
              {% endfor %}

              {% assign etc_domain = nw_topics | where_exp: "p", "p.url contains '/10-etc/wireless-charging'" %}
              {% for item in etc_domain %}
                <a href="{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a>
              {% endfor %}
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ③ 네트워크 품질(QoS), 라우터 -->
    <section class="nw-card nw-card--c">
      <div class="nw-card__header">③ 네트워크 품질(QoS), 라우터 <span class="nw-badge-hot">🔥</span></div>
      <div class="nw-card__body">
        <div class="nw-sub">
          <div class="nw-sub__title">
            <a href="{{ site.baseurl }}/docs/nw/05-qos">QoS / QoE / 망성능</a>
          </div>
          <div class="nw-sub__content">
            <div class="nw-chips">
              {% assign qos_items = site.pages | where: "parent", "5. 네트워크 품질 (QoS)" | where: "grand_parent", nw_root | sort: "nav_order" %}
              {% for item in qos_items %}
                <a href="{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a>
              {% endfor %}
            </div>
          </div>
        </div>

        <div class="nw-sub">
          <div class="nw-sub__title">
            라우터 / 라우팅
          </div>
          <div class="nw-sub__content">
            <div class="nw-chips">
              {% assign osi_all = site.pages | where: "parent", "7. OSI 7 Layer" | where: "grand_parent", nw_root | sort: "nav_order" %}
              {% assign routing_items = osi_all | where_exp: "p", "p.url contains '/routing' or p.url contains '/bgp' or p.url contains '/distance-vector' or p.url contains '/link-state'" %}
              {% for item in routing_items %}
                <a href="{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a>
              {% endfor %}
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ④ 네트워크 가상화(SDE) -->
    <section class="nw-card nw-card--d">
      <div class="nw-card__header">④ 네트워크 가상화 (SDE)</div>
      <div class="nw-card__body">
        <div class="nw-sub">
          <div class="nw-sub__title">가상화 기술</div>
          <div class="nw-sub__content">
            <div class="nw-chips">
              {% assign mgmt_all = site.pages | where: "parent", "6. 네트워크 관리" | where: "grand_parent", nw_root | sort: "nav_order" %}
              {% assign sde_items = mgmt_all | where_exp: "p", "p.url contains '/sdn' or p.url contains '/openflow' or p.url contains '/nfv' or p.url contains '/sddc' or p.url contains '/sd-wan' or p.url contains '/sdx'" %}
              {% for item in sde_items %}
                <a href="{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a>
              {% endfor %}
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- (표 느낌용) 빈 칸 -->
    <div class="nw-spacer" aria-hidden="true"></div>

    <!-- 네트워크 관리 / 정책 -->
    <section class="nw-card nw-card--e">
      <div class="nw-card__header">네트워크 관리 / 정책</div>
      <div class="nw-card__body">
        <div class="nw-sub">
          <div class="nw-sub__title">
            <a href="{{ site.baseurl }}/docs/nw/06-management">관리</a>
          </div>
          <div class="nw-sub__content">
            <div class="nw-chips">
              {% for item in mgmt_all %}
                <a href="{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a>
              {% endfor %}
            </div>
          </div>
        </div>

        <div class="nw-sub">
          <div class="nw-sub__title">
            정책
          </div>
          <div class="nw-sub__content">
            <div class="nw-chips">
              <a href="{{ site.baseurl }}/docs/nw/10-etc/network-neutrality">망중립성</a>
              <a class="nw-chip--primary" href="{{ site.baseurl }}/docs/nw/exam">📝 기출문제 (62문제)</a>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</div>

---

[📝 기출문제 (62문제)]({{ site.baseurl }}/docs/nw/exam){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 }

