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
{% assign nw_topics = site.pages | where: "grand_parent", nw_root %}

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
            {% assign f_core = nw_topics | where_exp: "p", "p.url contains '/03-fundamentals/line-control' or p.url contains '/03-fundamentals/switching'" %}
            {% assign f_multi = nw_topics | where_exp: "p", "p.url contains '/03-fundamentals/multiplexing' or p.url contains '/03-fundamentals/multiple-access' or p.url contains '/03-fundamentals/access-control'" %}
            {% assign f_addr = nw_topics | where_exp: "p", "p.url contains '/03-fundamentals/nat'" %}
            {% assign f_ip = nw_topics | where_exp: "p", "p.url contains '/03-fundamentals/ipv4-ipv6' or p.url contains '/03-fundamentals/ipv6-detail'" %}

            <div class="nw-chip-groups">
              <div class="nw-chip-group">
                <div class="nw-chip-group__title">교환/회선</div>
                <div class="nw-links">
                  {% for item in f_core %}
                    <a class="nw-link" href="{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a>
                  {% endfor %}
                </div>
              </div>

              <div class="nw-chip-group">
                <div class="nw-chip-group__title">접근/다중화</div>
                <div class="nw-links">
                  {% for item in f_multi %}
                    <a class="nw-link" href="{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a>
                  {% endfor %}
                </div>
              </div>

              <div class="nw-chip-group">
                <div class="nw-chip-group__title">주소 변환</div>
                <div class="nw-links">
                  {% for item in f_addr %}
                    <a class="nw-link nw-link--blue" href="{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a>
                  {% endfor %}
                </div>
              </div>

              <div class="nw-chip-group">
                <div class="nw-chip-group__title">인터넷 구조</div>
                <div class="nw-links">
                  {% for item in f_ip %}
                    <a class="nw-link nw-link--blue" href="{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a>
                  {% endfor %}
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="nw-sub">
          <div class="nw-sub__title">
            <a href="{{ site.baseurl }}/docs/nw/07-osi-layer">네트워크 기본 모델 (OSI 7 Layer)</a>
            <span class="nw-badge-hot">🔥</span>
          </div>
          <div class="nw-sub__content">
            {% assign osi_all = site.pages | where: "parent", "7. OSI 7 Layer" | where: "grand_parent", nw_root | sort: "nav_order" %}
            {% assign osi_overview = osi_all | where_exp: "p", "p.url contains '/osi-7-layers'" %}
            {% assign osi_layers = osi_all | where_exp: "p", "p.url contains '/application-layer' or p.url contains '/transport-layer' or p.url contains '/network-layer' or p.url contains '/datalink-layer'" %}
            {% assign osi_transport = osi_all | where_exp: "p", "p.url contains '/tcp' or p.url contains '/udp' or p.url contains '/sctp' or p.url contains '/mptcp'" %}
            {% assign osi_routing = osi_all | where_exp: "p", "p.url contains '/distance-vector' or p.url contains '/link-state' or p.url contains '/bgp' or p.url contains '/routing-'" %}
            {% assign osi_error = osi_all | where_exp: "p", "p.url contains '/error-control' or p.url contains '/fec-bec' or p.url contains '/arq' or p.url contains '/h-arq' or p.url contains '/hamming-code' or p.url contains '/crc'" %}
            {% assign osi_app = osi_all | where_exp: "p", "p.url contains '/http3' or p.url contains '/quic' or p.url contains '/ftp' or p.url contains '/tls' or p.url contains '/dns'" %}

            <div class="nw-chip-groups">
              <div class="nw-chip-group">
                <div class="nw-chip-group__title">OSI 개요</div>
                <div class="nw-links">
                  {% for item in osi_overview %}
                    <a class="nw-link nw-link--red" href="{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a>
                  {% endfor %}
                </div>
              </div>

              <div class="nw-chip-group">
                <div class="nw-chip-group__title">계층</div>
                <div class="nw-links">
                  {% for item in osi_layers %}
                    <a class="nw-link nw-link--strong" href="{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a>
                  {% endfor %}
                </div>
              </div>

              <div class="nw-chip-group">
                <div class="nw-chip-group__title">전송계층 프로토콜</div>
                <div class="nw-links">
                  {% for item in osi_transport %}
                    <a class="nw-link{% if item.url contains '/tcp' %} nw-link--red{% elsif item.url contains '/udp' %} nw-link--blue{% endif %}" href="{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a>
                  {% endfor %}
                </div>
              </div>

              <div class="nw-chip-group">
                <div class="nw-chip-group__title">라우팅</div>
                <div class="nw-links">
                  {% for item in osi_routing %}
                    <a class="nw-link{% if item.url contains '/bgp' %} nw-link--red{% else %} nw-link--blue{% endif %}" href="{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a>
                  {% endfor %}
                </div>
              </div>

              <div class="nw-chip-group">
                <div class="nw-chip-group__title">오류 제어</div>
                <div class="nw-links">
                  {% for item in osi_error %}
                    <a class="nw-link" href="{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a>
                  {% endfor %}
                </div>
              </div>

              <div class="nw-chip-group">
                <div class="nw-chip-group__title">응용 프로토콜</div>
                <div class="nw-links">
                  {% for item in osi_app %}
                    <a class="nw-link{% if item.url contains '/quic' or item.url contains '/http3' %} nw-link--red{% elsif item.url contains '/dns' %} nw-link--blue{% endif %}" href="{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a>
                  {% endfor %}
                </div>
              </div>
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
            <div class="nw-chip-groups">
              {% assign wired_core = nw_topics | where_exp: "p", "p.url contains '/03-fundamentals/line-control' or p.url contains '/03-fundamentals/switching' or p.url contains '/03-fundamentals/multiplexing' or p.url contains '/03-fundamentals/multiple-access'" %}
              {% assign wired_infra = nw_topics | where_exp: "p", "p.url contains '/04-infrastructure/reverse-proxy' or p.url contains '/04-infrastructure/forward-proxy' or p.url contains '/04-infrastructure/load-balancer'" %}
              {% assign wired_etc = nw_topics | where_exp: "p", "p.url contains '/10-etc/gslb' or p.url contains '/10-etc/smb-protocol'" %}
              {% assign wired = wired_core | concat: wired_infra | concat: wired_etc | uniq | sort: "title" %}

              <div class="nw-chip-group">
                <div class="nw-chip-group__title">기본(유선)</div>
                <div class="nw-links">
                  {% for item in wired_core %}
                    <a class="nw-link" href="{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a>
                  {% endfor %}
                </div>
              </div>

              <div class="nw-chip-group">
                <div class="nw-chip-group__title">구성요소</div>
                <div class="nw-links">
                  {% for item in wired_infra %}
                    <a class="nw-link" href="{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a>
                  {% endfor %}
                </div>
              </div>

              <div class="nw-chip-group">
                <div class="nw-chip-group__title">기타</div>
                <div class="nw-links">
                  {% for item in wired_etc %}
                    <a class="nw-link" href="{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a>
                  {% endfor %}
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="nw-sub">
          <div class="nw-sub__title">
            무선 통신 기술 (주파수)
          </div>
          <div class="nw-sub__content">
            {% assign mobile_items = site.pages | where: "parent", "8. 이동통신" | where: "grand_parent", nw_root | sort: "nav_order" %}
            {% assign wlan_items = nw_topics | where_exp: "p", "p.url contains '/04-infrastructure/wlan-architecture' or p.url contains '/04-infrastructure/wifi7'" %}
            {% assign radio_infra = nw_topics | where_exp: "p", "p.url contains '/04-infrastructure/o-ran' or p.url contains '/04-infrastructure/5g-' or p.url contains '/04-infrastructure/ps-lte' or p.url contains '/04-infrastructure/leo-mobile' or p.url contains '/04-infrastructure/ran-sharing' or p.url contains '/04-infrastructure/6g'" %}

            <div class="nw-chip-groups">
              <div class="nw-chip-group">
                <div class="nw-chip-group__title">이동통신</div>
                <div class="nw-links">
                  {% for item in mobile_items %}
                    <a class="nw-link{% if item.url contains '/network-slicing' or item.url contains '/mec-fog' %} nw-link--blue{% elsif item.url contains '/6g' %} nw-link--red{% endif %}" href="{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a>
                  {% endfor %}
                </div>
              </div>

              <div class="nw-chip-group">
                <div class="nw-chip-group__title">WLAN</div>
                <div class="nw-links">
                  {% for item in wlan_items %}
                    <a class="nw-link nw-link--blue" href="{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a>
                  {% endfor %}
                </div>
              </div>

              <div class="nw-chip-group">
                <div class="nw-chip-group__title">망 구축(무선 인프라)</div>
                <div class="nw-links">
                  {% for item in radio_infra %}
                    <a class="nw-link{% if item.url contains '/o-ran' %} nw-link--red{% elsif item.url contains '/ps-lte' or item.url contains '/leo-mobile' %} nw-link--blue{% endif %}" href="{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a>
                  {% endfor %}
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="nw-sub">
          <div class="nw-sub__title">분야 별 통신기술</div>
          <div class="nw-sub__content">
            {% assign iot_items = site.pages | where: "parent", "1. IoT" | where: "grand_parent", nw_root | sort: "nav_order" %}
            {% assign adhoc_items = site.pages | where: "parent", "2. 드론 (Ad-hoc)" | where: "grand_parent", nw_root | sort: "nav_order" %}
            {% assign loc_items = site.pages | where: "parent", "9. 위치 측위" | where: "grand_parent", nw_root | sort: "nav_order" %}
            {% assign etc_domain = nw_topics | where_exp: "p", "p.url contains '/10-etc/wireless-charging'" %}

            <div class="nw-chip-groups">
              <div class="nw-chip-group">
                <div class="nw-chip-group__title">IoT</div>
                <div class="nw-links">
                  {% for item in iot_items %}
                    <a class="nw-link" href="{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a>
                  {% endfor %}
                </div>
              </div>

              <div class="nw-chip-group">
                <div class="nw-chip-group__title">Ad-hoc / 드론</div>
                <div class="nw-links">
                  {% for item in adhoc_items %}
                    <a class="nw-link nw-link--blue" href="{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a>
                  {% endfor %}
                </div>
              </div>

              <div class="nw-chip-group">
                <div class="nw-chip-group__title">위치 측위</div>
                <div class="nw-links">
                  {% for item in loc_items %}
                    <a class="nw-link" href="{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a>
                  {% endfor %}
                </div>
              </div>

              <div class="nw-chip-group">
                <div class="nw-chip-group__title">기타(도메인성)</div>
                <div class="nw-links">
                  {% for item in etc_domain %}
                    <a class="nw-link" href="{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a>
                  {% endfor %}
                </div>
              </div>
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
            {% assign qos_items = site.pages | where: "parent", "5. 네트워크 품질 (QoS)" | where: "grand_parent", nw_root | sort: "nav_order" %}
            {% assign qos_basic = qos_items | where_exp: "p", "p.url contains '/qos' and p.url contains '/05-qos/qos'" %}
            {% assign qos_metrics = qos_items | where_exp: "p", "p.url contains '/qos-metrics'" %}
            {% assign qos_queue = qos_items | where_exp: "p", "p.url contains '/queue-management'" %}
            {% assign qos_control = qos_items | where_exp: "p", "p.url contains '/traffic-shaping' or p.url contains '/traffic-policing' or p.url contains '/tcp-congestion'" %}
            {% assign qos_guarantee = qos_items | where_exp: "p", "p.url contains '/qos-guarantee'" %}

            <div class="nw-chip-groups">
              <div class="nw-chip-group">
                <div class="nw-chip-group__title">개요</div>
                <div class="nw-links">
                  {% for item in qos_basic %}
                    <a class="nw-link nw-link--red" href="{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a>
                  {% endfor %}
                  {% for item in qos_metrics %}
                    <a class="nw-link nw-link--blue" href="{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a>
                  {% endfor %}
                </div>
              </div>

              <div class="nw-chip-group">
                <div class="nw-chip-group__title">관리(큐/제어)</div>
                <div class="nw-links">
                  {% for item in qos_queue %}
                    <a class="nw-link nw-link--blue" href="{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a>
                  {% endfor %}
                  {% for item in qos_control %}
                    <a class="nw-link" href="{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a>
                  {% endfor %}
                </div>
              </div>

              <div class="nw-chip-group">
                <div class="nw-chip-group__title">보장</div>
                <div class="nw-links">
                  {% for item in qos_guarantee %}
                    <a class="nw-link nw-link--red" href="{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a>
                  {% endfor %}
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="nw-sub">
          <div class="nw-sub__title">
            라우터 / 라우팅
          </div>
          <div class="nw-sub__content">
            {% assign osi_all2 = site.pages | where: "parent", "7. OSI 7 Layer" | where: "grand_parent", nw_root | sort: "nav_order" %}
            {% assign routing_items = osi_all2 | where_exp: "p", "p.url contains '/distance-vector' or p.url contains '/link-state' or p.url contains '/bgp' or p.url contains '/routing-'" %}
            <div class="nw-links">
              {% for item in routing_items %}
                <a class="nw-link{% if item.url contains '/bgp' %} nw-link--red{% else %} nw-link--blue{% endif %}" href="{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a>
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
            {% assign mgmt_all = site.pages | where: "parent", "6. 네트워크 관리" | where: "grand_parent", nw_root | sort: "nav_order" %}
            {% assign sdx_items = mgmt_all | where_exp: "p", "p.url contains '/sdx' or p.url contains '/sddc' or p.url contains '/sd-wan'" %}
            {% assign sdn_items = mgmt_all | where_exp: "p", "p.url contains '/sdn' or p.url contains '/openflow'" %}
            {% assign nfv_items = mgmt_all | where_exp: "p", "p.url contains '/nfv'" %}

            <div class="nw-chip-groups">
              <div class="nw-chip-group">
                <div class="nw-chip-group__title">SDx / SDDC / SD-WAN</div>
                <div class="nw-links">
                  {% for item in sdx_items %}
                    <a class="nw-link nw-link--blue" href="{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a>
                  {% endfor %}
                </div>
              </div>

              <div class="nw-chip-group">
                <div class="nw-chip-group__title">SDN / OpenFlow</div>
                <div class="nw-links">
                  {% for item in sdn_items %}
                    <a class="nw-link nw-link--red" href="{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a>
                  {% endfor %}
                </div>
              </div>

              <div class="nw-chip-group">
                <div class="nw-chip-group__title">NFV</div>
                <div class="nw-links">
                  {% for item in nfv_items %}
                    <a class="nw-link nw-link--red" href="{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a>
                  {% endfor %}
                </div>
              </div>
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
            {% assign mgmt_sdx = mgmt_all | where_exp: "p", "p.url contains '/sdx' or p.url contains '/sdn' or p.url contains '/openflow' or p.url contains '/sd-wan' or p.url contains '/sddc'" %}
            {% assign mgmt_nfv = mgmt_all | where_exp: "p", "p.url contains '/nfv'" %}
            {% assign mgmt_addr = mgmt_all | where_exp: "p", "p.url contains '/subnetting'" %}

            <div class="nw-chip-groups">
              <div class="nw-chip-group">
                <div class="nw-chip-group__title">관리(제어/자동화)</div>
                <div class="nw-links">
                  {% for item in mgmt_sdx %}
                    <a class="nw-link{% if item.url contains '/openflow' %} nw-link--red{% elsif item.url contains '/sdn' %} nw-link--red{% else %} nw-link--blue{% endif %}" href="{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a>
                  {% endfor %}
                </div>
              </div>

              <div class="nw-chip-group">
                <div class="nw-chip-group__title">가상화/운영</div>
                <div class="nw-links">
                  {% for item in mgmt_nfv %}
                    <a class="nw-link nw-link--blue" href="{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a>
                  {% endfor %}
                  {% for item in mgmt_addr %}
                    <a class="nw-link nw-link--blue" href="{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a>
                  {% endfor %}
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="nw-sub">
          <div class="nw-sub__title">
            정책
          </div>
          <div class="nw-sub__content">
            <div class="nw-links">
              <a class="nw-link nw-link--red" href="{{ site.baseurl }}/docs/nw/10-etc/network-neutrality">망중립성</a>
              <a class="nw-link nw-link--blue nw-link--strong" href="{{ site.baseurl }}/docs/nw/exam">📝 기출문제 (62문제)</a>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</div>

---

[📝 기출문제 (62문제)]({{ site.baseurl }}/docs/nw/exam){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 }

