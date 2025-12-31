---
layout: default
title: CAOS (컴퓨터구조/OS)
nav_order: 9
has_children: true
has_toc: false
permalink: /docs/caos
---

# CAOS (컴퓨터구조/OS) <span class="page-title-with-cta__ctas"><a class="exam-top-cta" href="{{ site.baseurl }}/docs/caos/daily">🃏 데일리 암기 덱</a><a class="exam-top-cta" href="{{ site.baseurl }}/docs/caos/exam">📝 기출문제</a></span>
{: .fs-9 .page-title-with-cta }


---

{% assign caos_root = page.title %}

{% assign computer_all = site.pages | where: "parent", "0. Computer" | where: "grand_parent", caos_root | sort: "nav_order" %}
{% assign cpu_sched_all = site.pages | where: "parent", "1. CPU 스케줄링" | where: "grand_parent", caos_root | sort: "nav_order" %}
{% assign sync_all = site.pages | where: "parent", "2. 동기화" | where: "grand_parent", caos_root | sort: "nav_order" %}
{% assign deadlock_all = site.pages | where: "parent", "3. 교착상태" | where: "grand_parent", caos_root | sort: "nav_order" %}
{% assign vm_all = site.pages | where: "parent", "4. 가상메모리" | where: "grand_parent", caos_root | sort: "nav_order" %}
{% assign cache_all = site.pages | where: "parent", "5. 캐시메모리" | where: "grand_parent", caos_root | sort: "nav_order" %}
{% assign raid_all = site.pages | where: "parent", "6. RAID" | where: "grand_parent", caos_root | sort: "nav_order" %}
{% assign process_all = site.pages | where: "parent", "7. 프로세스" | where: "grand_parent", caos_root | sort: "nav_order" %}
{% assign pipe_all = site.pages | where: "parent", "8. 파이프라인" | where: "grand_parent", caos_root | sort: "nav_order" %}
{% assign memory_all = site.pages | where: "parent", "9. 메모리" | where: "grand_parent", caos_root | sort: "nav_order" %}
{% assign irq_all = site.pages | where: "parent", "10. 인터럽트" | where: "grand_parent", caos_root | sort: "nav_order" %}
{% assign os_all = site.pages | where: "parent", "11. 운영체제" | where: "grand_parent", caos_root | sort: "nav_order" %}
{% assign semi_all = site.pages | where: "parent", "12. 반도체" | where: "grand_parent", caos_root | sort: "nav_order" %}
{% assign cpugpu_all = site.pages | where: "parent", "13. CPU/GPU" | where: "grand_parent", caos_root | sort: "nav_order" %}
{% assign ca_etc_all = site.pages | where: "parent", "14. CA 기타" | where: "grand_parent", caos_root | sort: "nav_order" %}

<div class="caos-matrix">
  <div class="caos-matrix__grid">
    <!-- ① CA (Computer Architecture) -->
    <section class="caos-card">
      <div class="caos-card__header">① CA (Computer Architecture)</div>
      <div class="caos-card__body">
        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/caos/00-computer">CA 일반</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in computer_all %}
                <a class="nw-link nw-link--blue" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
            </div>
          </div>
        </div>

        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/caos/13-cpu-gpu">CPU/GPU · 병렬처리</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in cpugpu_all %}
                <a class="nw-link nw-link--strong" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
            </div>
          </div>
        </div>

        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/caos/05-cache-memory">캐시</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in cache_all %}
                <a class="nw-link" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
            </div>
          </div>
        </div>

        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/caos/08-pipeline">파이프라인</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in pipe_all %}
                <a class="nw-link" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
            </div>
          </div>
        </div>

        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/caos/09-memory">메모리(신기술)</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in memory_all %}
                <a class="nw-link nw-link--blue" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
              {% for item in ca_etc_all %}
                <a class="nw-link" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
            </div>
          </div>
        </div>

        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/caos/12-semiconductor">반도체</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in semi_all %}
                <a class="nw-link nw-link--red" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ② OS (Operation System) -->
    <section class="caos-card">
      <div class="caos-card__header">② OS (Operation System)</div>
      <div class="caos-card__body">
        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/caos/11-os">운영체제</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in os_all %}
                <a class="nw-link nw-link--blue" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
            </div>
          </div>
        </div>

        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/caos/07-process">프로세스/스레드</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in process_all %}
                <a class="nw-link" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
            </div>
          </div>
        </div>

        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/caos/01-cpu-scheduling">CPU 스케줄링</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in cpu_sched_all %}
                <a class="nw-link nw-link--strong" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
            </div>
          </div>
        </div>

        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/caos/02-synchronization">동기화</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in sync_all %}
                <a class="nw-link" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
            </div>
          </div>
        </div>

        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/caos/03-deadlock">교착상태</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in deadlock_all %}
                <a class="nw-link nw-link--red" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
            </div>
          </div>
        </div>

        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/caos/04-virtual-memory">가상메모리</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in vm_all %}
                <a class="nw-link nw-link--blue" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
            </div>
          </div>
        </div>

        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/caos/06-raid">저장장치</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in raid_all %}
                <a class="nw-link" href="{{ site.baseurl }}{{ item.url }}">{{ item.title | split: "(" | first | strip }}</a>
              {% endfor %}
            </div>
          </div>
        </div>

        <div class="nw-sub">
          <div class="nw-sub__title"><a href="{{ site.baseurl }}/docs/caos/10-interrupt">인터럽트</a></div>
          <div class="nw-sub__content">
            <div class="nw-links">
              {% for item in irq_all %}
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
    <strong>CA</strong>(구성요소·성능) → <strong>OS</strong>(프로세스·스케줄링·동기화) → <strong>메모리</strong>(가상/캐시) → <strong>I/O</strong>(인터럽트/저장) → <strong>하드웨어 트렌드</strong>(가속기/반도체)
  </div>
</div>

