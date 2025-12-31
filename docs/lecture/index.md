---
layout: default
title: 특강
nav_order: 99
has_children: true
has_toc: false
permalink: /docs/lecture
---

# 📚 특강
{: .fs-9 }

기술사 시험 준비를 위한 특강 자료 모음입니다.
{: .fs-6 .fw-300 }

---

## 특강 목록

{% assign lectures = site.pages | where: "parent", "특강" | sort: "nav_order" %}

<div class="lecture-grid">
{% for lecture in lectures %}
  <div class="lecture-card">
    <a href="{{ lecture.url | relative_url }}">
      <h3>{{ lecture.title }}</h3>
      {% if lecture.description %}
      <p>{{ lecture.description }}</p>
      {% endif %}
    </a>
  </div>
{% endfor %}
</div>

{% if lectures.size == 0 %}
<div class="empty-state">
  <p>📝 아직 등록된 특강이 없습니다.</p>
  <p>특강 페이지를 추가하려면 <code>docs/lecture/</code> 폴더에 마크다운 파일을 생성하세요.</p>
</div>
{% endif %}

<style>
.lecture-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 1rem;
  margin-top: 1.5rem;
}

.lecture-card {
  border: 1px solid #e5e7eb;
  border-radius: 12px;
  padding: 1.25rem;
  transition: all 0.2s;
  background: #fafafa;
}

.lecture-card:hover {
  border-color: #3b82f6;
  box-shadow: 0 4px 12px rgba(59, 130, 246, 0.15);
  transform: translateY(-2px);
}

.lecture-card a {
  text-decoration: none;
  color: inherit;
}

.lecture-card h3 {
  margin: 0 0 0.5rem 0;
  color: #1e40af;
  font-size: 1.1rem;
}

.lecture-card p {
  margin: 0;
  color: #6b7280;
  font-size: 0.9rem;
}

.empty-state {
  text-align: center;
  padding: 3rem;
  background: #f9fafb;
  border-radius: 12px;
  color: #6b7280;
}

.empty-state code {
  background: #e5e7eb;
  padding: 0.2rem 0.5rem;
  border-radius: 4px;
  font-size: 0.85rem;
}
</style>

