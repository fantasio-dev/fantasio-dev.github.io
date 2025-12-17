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

<div class="topic-map">
  <div class="topic-map__sections">
    {% assign sections = site.pages | where: "parent", page.title | sort: "nav_order" %}
    {% for section in sections %}
      {% if section.title != "📝 기출문제" %}
        {% assign parts = section.title | split: ". " %}
        <div class="topic-map__section">
          <div class="topic-map__section-header">
            <a class="topic-map__section-link" href="{{ site.baseurl }}{{ section.url }}">
              {% if parts.size > 1 %}{{ parts[1] }}{% else %}{{ section.title }}{% endif %}
            </a>
          </div>
          <div class="topic-map__chips">
            {% assign items = site.pages | where: "parent", section.title | where: "grand_parent", page.title | sort: "nav_order" %}
            {% for item in items %}
              <a class="topic-map__chip" href="{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a>
            {% endfor %}
          </div>
        </div>
      {% endif %}
    {% endfor %}
    <div class="topic-map__section">
      <div class="topic-map__section-header">
        <a class="topic-map__section-link" href="{{ site.baseurl }}/docs/nw/exam">기출문제</a>
      </div>
      <div class="topic-map__chips">
        <a class="topic-map__chip topic-map__chip--primary" href="{{ site.baseurl }}/docs/nw/exam">📝 기출문제 (62문제)</a>
      </div>
    </div>
  </div>
</div>

---

[📝 기출문제 (62문제)]({{ site.baseurl }}/docs/nw/exam){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 }

