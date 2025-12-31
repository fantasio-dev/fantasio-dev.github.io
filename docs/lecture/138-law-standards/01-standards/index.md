---
layout: default
title: 1. 인증/표준/원칙/기타
parent: 138회 대비 법인가출 특강
grand_parent: 특강
nav_order: 1
has_children: true
has_toc: false
permalink: /docs/lecture/138-law-standards/01-standards
---

# 1. 인증 / 표준 / 원칙 / 기타
{: .fs-8 }

ISO, IEC 국제표준 및 인증 관련 핵심 정리 (32개 토픽)
{: .fs-6 .fw-300 }

---

> 💡 **Tip**: 표준이라고 하면 정해져있다. ISO, IEC, 윤리 관련.  
> 주의: 이전 기출이라고 안 챙기면 안된다. 반복해서 출제된다. (최근 3년치)

---

## 📋 토픽 목록

{% assign standards = site.pages | where: "parent", "1. 인증/표준/원칙/기타" | sort: "nav_order" %}

| No | 토픽 | 출제예상 |
|:--:|:-----|:--------:|
{% for page in standards %}| {{ page.nav_order }} | [{{ page.title }}]({{ page.url | relative_url }}) | {% if page.hot %}⭐{% endif %} |
{% endfor %}

---

## 🎯 출제 예상 토픽

**반드시 암기**: 3, 7, 13(벡터), 14, 15, 16(AI거버넌스), 21, 23, 30, 31


