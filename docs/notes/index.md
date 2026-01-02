---
layout: default
title: 📚 학습노트
nav_order: 98
has_children: false
has_toc: false
permalink: /docs/notes
---

<style>
/* 노트 카드 그리드 */
.notes-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
  margin: 2rem 0;
}

.note-card {
  background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
  border: 1px solid #e2e8f0;
  border-radius: 16px;
  padding: 1.5rem;
  transition: transform 0.2s, box-shadow 0.2s;
}

.note-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 24px rgba(0,0,0,0.1);
}

.note-card__header {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  margin-bottom: 1rem;
}

.note-card__icon {
  font-size: 2rem;
}

.note-card__title {
  font-size: 1.25rem;
  font-weight: 700;
  color: #1e293b;
  margin: 0;
}

.note-card__desc {
  color: #64748b;
  font-size: 0.9rem;
  margin-bottom: 1rem;
  line-height: 1.5;
}

.note-card__link {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1rem;
  background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
  color: #fff !important;
  border-radius: 8px;
  text-decoration: none !important;
  font-weight: 600;
  font-size: 0.85rem;
  transition: all 0.2s;
}

.note-card__link:hover {
  background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%);
  transform: translateX(4px);
}

/* 최근 노트 섹션 */
.recent-notes {
  background: #fff;
  border: 1px solid #e2e8f0;
  border-radius: 16px;
  padding: 1.5rem;
  margin: 2rem 0;
}

.recent-notes__title {
  font-size: 1.1rem;
  font-weight: 700;
  color: #1e293b;
  margin-bottom: 1rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.recent-notes__list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.recent-notes__item {
  padding: 0.75rem 0;
  border-bottom: 1px solid #f1f5f9;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.recent-notes__item:last-child {
  border-bottom: none;
}

.recent-notes__item a {
  color: #3b82f6;
  text-decoration: none;
  font-weight: 500;
}

.recent-notes__item a:hover {
  text-decoration: underline;
}

.recent-notes__date {
  color: #94a3b8;
  font-size: 0.8rem;
}

/* 팁 박스 */
.tip-box {
  background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
  border: 1px solid #fcd34d;
  border-radius: 12px;
  padding: 1.25rem;
  margin: 2rem 0;
}

.tip-box__title {
  font-weight: 700;
  color: #92400e;
  margin-bottom: 0.5rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.tip-box__content {
  color: #78350f;
  font-size: 0.9rem;
  line-height: 1.6;
}
</style>

# 📚 학습노트
{: .fs-9 }

스터디 피드백, 멘토링 내용, 개인 학습 기록을 정리하는 공간
{: .fs-6 .fw-300 }

---

## 📂 영역별 학습노트

<div class="notes-grid">
  <div class="note-card">
    <div class="note-card__header">
      <span class="note-card__icon">🌐</span>
      <h3 class="note-card__title">DS (디지털서비스)</h3>
    </div>
    <p class="note-card__desc">
      DS 주간 모의고사 피드백, 멘토님 조언, 토픽별 학습 인사이트 정리
    </p>
    <a href="{{ site.baseurl }}/docs/ds/notes" class="note-card__link">
      노트 보기 →
    </a>
  </div>

  <div class="note-card">
    <div class="note-card__header">
      <span class="note-card__icon">💻</span>
      <h3 class="note-card__title">SW (소프트웨어공학)</h3>
    </div>
    <p class="note-card__desc">
      SW 영역 학습 기록, 감리/테스트/품질 관련 노트
    </p>
    <a href="{{ site.baseurl }}/docs/sw/notes" class="note-card__link" style="background: #94a3b8; pointer-events: none;">
      준비 중
    </a>
  </div>

  <div class="note-card">
    <div class="note-card__header">
      <span class="note-card__icon">🔐</span>
      <h3 class="note-card__title">SEC (보안)</h3>
    </div>
    <p class="note-card__desc">
      NW/보안 영역 학습 기록, 프레임워크/공격기법/대응방안 노트
    </p>
    <a href="{{ site.baseurl }}/docs/sec/notes" class="note-card__link">
      노트 보기 →
    </a>
  </div>

  <div class="note-card">
    <div class="note-card__header">
      <span class="note-card__icon">🤖</span>
      <h3 class="note-card__title">AI (인공지능)</h3>
    </div>
    <p class="note-card__desc">
      AI 영역 학습 기록, 모델/학습기법/윤리 관련 노트
    </p>
    <a href="{{ site.baseurl }}/docs/ai/notes" class="note-card__link" style="background: #94a3b8; pointer-events: none;">
      준비 중
    </a>
  </div>
</div>

---

## 🕐 최근 노트

<div class="recent-notes">
  <div class="recent-notes__title">📝 최근 기록</div>
  <ul class="recent-notes__list">
    <li class="recent-notes__item">
      <a href="{{ site.baseurl }}/docs/sec/notes">NW/보안 주간 모의고사 피드백</a>
      <span class="recent-notes__date">2025-12-14</span>
    </li>
    <li class="recent-notes__item">
      <a href="{{ site.baseurl }}/docs/ds/notes">DS 주간 모의고사 피드백</a>
      <span class="recent-notes__date">2025-12-07</span>
    </li>
  </ul>
</div>


