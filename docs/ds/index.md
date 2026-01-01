---
layout: default
title: DS (Digital Service)
nav_order: 2
has_children: true
has_toc: false
permalink: /docs/ds
---

# DS (Digital Service)


---

{% assign ds_root = page.title %}

{% assign cloud_all = site.pages | where: "parent", "1. 클라우드" | where: "grand_parent", ds_root | sort: "nav_order" %}
{% assign api_all = site.pages | where: "parent", "13. API" | where: "grand_parent", ds_root | sort: "nav_order" %}
{% assign web_all = site.pages | where: "parent", "24. 웹 기술/검색엔진" | where: "grand_parent", ds_root | sort: "nav_order" %}
{% assign uiux_all = site.pages | where: "parent", "12. UI/UX" | where: "grand_parent", ds_root | sort: "nav_order" %}
{% assign xr_all = site.pages | where: "parent", "2. 가상융합/XR/메타버스" | where: "grand_parent", ds_root | sort: "nav_order" %}
{% assign dist_all = site.pages | where: "parent", "11. 분산 컴퓨팅" | where: "grand_parent", ds_root | sort: "nav_order" %}
{% assign virt_all = site.pages | where: "parent", "7. 가상화/컨테이너" | where: "grand_parent", ds_root | sort: "nav_order" %}
{% assign spatial_all = site.pages | where: "parent", "14. 공간정보" | where: "grand_parent", ds_root | sort: "nav_order" %}
{% assign blockchain_all = site.pages | where: "parent", "3. 블록체인" | where: "grand_parent", ds_root | sort: "nav_order" %}

{% assign auto_all = site.pages | where: "parent", "4. 스마트카/자율주행" | where: "grand_parent", ds_root | sort: "nav_order" %}
{% assign factory_all = site.pages | where: "parent", "5. 스마트공장" | where: "grand_parent", ds_root | sort: "nav_order" %}
{% assign grid_all = site.pages | where: "parent", "6. 스마트그리드/에너지" | where: "grand_parent", ds_root | sort: "nav_order" %}
{% assign virt_infra_all = site.pages | where: "parent", "23. 인프라스트럭처" | where: "grand_parent", ds_root | sort: "nav_order" %}
{% assign iot_all = site.pages | where: "parent", "8. IoT" | where: "grand_parent", ds_root | sort: "nav_order" %}
{% assign drone_all = site.pages | where: "parent", "9. 드론/UAM" | where: "grand_parent", ds_root | sort: "nav_order" %}
{% assign health_all = site.pages | where: "parent", "10. 디지털 헬스케어" | where: "grand_parent", ds_root | sort: "nav_order" %}
{% assign robot_all = site.pages | where: "parent", "19. 로봇/자동화" | where: "grand_parent", ds_root | sort: "nav_order" %}
{% assign reco_all = site.pages | where: "parent", "20. 추천 시스템" | where: "grand_parent", ds_root | sort: "nav_order" %}
{% assign vision_all = site.pages | where: "parent", "21. 영상처리/영상보안" | where: "grand_parent", ds_root | sort: "nav_order" %}
{% assign finops_all = site.pages | where: "parent", "22. 디지털 지갑/FinOps" | where: "grand_parent", ds_root | sort: "nav_order" %}

{% assign egov_all = site.pages | where: "parent", "16. 전자정부" | where: "grand_parent", ds_root | sort: "nav_order" %}
{% assign design_all = site.pages | where: "parent", "15. 디자인씽킹" | where: "grand_parent", ds_root | sort: "nav_order" %}
{% assign etc_all = site.pages | where: "parent", "18. DS 기타" | where: "grand_parent", ds_root | sort: "nav_order" %}
{% assign gartner_all = site.pages | where: "parent", "17. 가트너 전략" | where: "grand_parent", ds_root | sort: "nav_order" %}

<div class="ds-matrix">
  <div class="ds-matrix__grid">
    <!-- ① 웹/UX -->
    <section class="ds-card">
      <div class="ds-card__header">① 웹/UX</div>
      <div class="ds-card__body">
        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/ds/24-web">웹 기술/검색엔진</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in web_all %}
                <a class="nw-link nw-link--blue" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
            </div>
          </div>
        </div>
        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/ds/12-ui-ux">UI/UX</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in uiux_all %}
                <a class="nw-link" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ② 연동/API -->
    <section class="ds-card">
      <div class="ds-card__header">② 연동/API</div>
      <div class="ds-card__body">
        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/ds/13-api">API</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in api_all %}
                <a class="nw-link nw-link--blue" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
            </div>
          </div>
        </div>
        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/ds/23-infra">인프라 자동화</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in virt_infra_all %}
                <a class="nw-link nw-link--strong" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ③ XR/메타버스 -->
    <section class="ds-card">
      <div class="ds-card__header">③ XR/메타버스</div>
      <div class="ds-card__body">
        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/ds/02-xr-metaverse">가상융합/XR/메타버스</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in xr_all %}
                <a class="nw-link nw-link--red" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ④ 컴퓨팅/분산 -->
    <section class="ds-card">
      <div class="ds-card__header">④ 컴퓨팅/분산</div>
      <div class="ds-card__body">
        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/ds/11-distributed">분산 컴퓨팅</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in dist_all %}
                <a class="nw-link" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ⑤ 클라우드 -->
    <section class="ds-card">
      <div class="ds-card__header">⑤ 클라우드</div>
      <div class="ds-card__body">
        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/ds/01-cloud">클라우드</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in cloud_all %}
                <a class="nw-link nw-link--blue" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ⑥ 가상화/컨테이너 -->
    <section class="ds-card">
      <div class="ds-card__header">⑥ 가상화/컨테이너</div>
      <div class="ds-card__body">
        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/ds/07-virtualization">가상화/컨테이너</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in virt_all %}
                <a class="nw-link nw-link--strong" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ⑦ 위치/공간 -->
    <section class="ds-card">
      <div class="ds-card__header">⑦ 위치/공간</div>
      <div class="ds-card__body">
        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/ds/14-spatial">공간정보</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in spatial_all %}
                <a class="nw-link" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ⑧ 블록체인 -->
    <section class="ds-card">
      <div class="ds-card__header">⑧ 블록체인</div>
      <div class="ds-card__body">
        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/ds/03-blockchain">블록체인</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in blockchain_all %}
                <a class="nw-link nw-link--blue" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ⑨ 서비스별(응용) -->
    <section class="ds-card">
      <div class="ds-card__header">⑨ 서비스별(응용)</div>
      <div class="ds-card__body">
        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/ds/04-autonomous">스마트카/자율주행</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in auto_all %}
                <a class="nw-link nw-link--red" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
            </div>
          </div>
        </div>
        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/ds/05-smart-factory">스마트공장</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in factory_all %}
                <a class="nw-link" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
            </div>
          </div>
        </div>
        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/ds/06-smart-grid">스마트그리드/에너지</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in grid_all %}
                <a class="nw-link" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
            </div>
          </div>
        </div>
        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/ds/08-iot">IoT</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in iot_all %}
                <a class="nw-link" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
            </div>
          </div>
        </div>
        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/ds/09-drone-uam">드론/UAM</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in drone_all %}
                <a class="nw-link" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
            </div>
          </div>
        </div>
        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/ds/10-healthcare">디지털 헬스케어</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in health_all %}
                <a class="nw-link" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
            </div>
          </div>
        </div>
        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/ds/19-robot">로봇/자동화</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in robot_all %}
                <a class="nw-link" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
            </div>
          </div>
        </div>
        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/ds/20-recommendation">추천 시스템</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in reco_all %}
                <a class="nw-link" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
            </div>
          </div>
        </div>
        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/ds/21-vision">영상처리/영상보안</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in vision_all %}
                <a class="nw-link" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
            </div>
          </div>
        </div>
        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/ds/22-finops">디지털 지갑/FinOps</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in finops_all %}
                <a class="nw-link nw-link--blue" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ⑩ 설계/거버넌스 -->
    <section class="ds-card">
      <div class="ds-card__header">⑩ 설계/거버넌스</div>
      <div class="ds-card__body">
        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/ds/16-e-gov">전자정부</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in egov_all %}
                <a class="nw-link" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
            </div>
          </div>
        </div>
        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/ds/15-design-thinking">디자인씽킹</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in design_all %}
                <a class="nw-link" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
            </div>
          </div>
        </div>
        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/ds/18-etc">DS 기타</a></div>
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

    <!-- ⑪ 전략 -->
    <section class="ds-card">
      <div class="ds-card__header">⑪ 전략</div>
      <div class="ds-card__body">
        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/ds/17-gartner">가트너 전략</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in gartner_all %}
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
    <strong>사용자 접점</strong>(웹/UX) → <strong>연동</strong>(API/자동화) → <strong>기반</strong>(분산/클라우드/가상화) → <strong>기능 축</strong>(공간/블록체인) → <strong>응용 서비스</strong> → <strong>거버넌스/전략</strong>
  </div>
</div>

