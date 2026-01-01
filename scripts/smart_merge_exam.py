#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
기존 링크/암기법을 유지하면서 새 문제만 추가하는 스마트 병합 스크립트
"""

import csv
import re
from pathlib import Path

# 도메인 매핑
DOMAIN_MAP = {
    '소공': 'SW', 'SW': 'SW', '인공지능': 'AI', 'AI': 'AI',
    '보안': 'SEC', 'SEC': 'SEC', 'DS': 'DS', 'NW': 'NW',
    '네트워크': 'NW', 'DB': 'DB', '데이터베이스': 'DB',
    'CA': 'CAOS', 'CAOS': 'CAOS', '경영': 'BIZ', 'BIZ': 'BIZ',
    '알고리즘': 'SW', '자료구조': 'SW',
}

def get_domain_code(category):
    if not category:
        return 'SW'
    return DOMAIN_MAP.get(category.strip(), 'SW')

def clean_question(text):
    if not text:
        return ""
    text = re.sub(r'^\d+\.\s*', '', text.strip())
    text = text.replace('\n', ' ').replace('\r', '')
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'\(\d{3}(관리|컴시응|정|컴)\)', '', text)
    return text.strip()

def get_short_question(full, max_len=100):
    if not full:
        return ""
    if ' 가.' in full or ' 가)' in full:
        parts = re.split(r'\s+가[\.\)]', full)
        short = parts[0].strip()
    else:
        short = full
    return short[:max_len] + '...' if len(short) > max_len else short

def parse_csv(csv_path):
    """CSV 파싱하여 문제 딕셔너리 반환"""
    questions = {}
    
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # 헤더 스킵
        
        current = None
        for row in reader:
            if len(row) < 7:
                if current and len(row) > 0:
                    current['full'] += ' ' + ' '.join(row)
                continue
            
            round_num, exam_type, period, num, question, obj, category = row[:7]
            
            if not round_num.strip().isdigit():
                if current:
                    current['full'] += ' ' + question
                continue
            
            if current:
                key = f"{current['round']}-{current['exam_type']}-{current['period']}-{current['num']}"
                questions[key] = current
            
            current = {
                'round': int(round_num.strip()),
                'exam_type': exam_type.strip(),
                'period': period.strip(),
                'num': num.strip(),
                'full': clean_question(question),
                'domain': get_domain_code(category)
            }
        
        if current:
            key = f"{current['round']}-{current['exam_type']}-{current['period']}-{current['num']}"
            questions[key] = current
    
    return questions

def parse_existing_rows(index_path):
    """기존 index.md에서 tr 행들 파싱"""
    existing = {}
    
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # tbody 내용 추출
    tbody_match = re.search(r'<tbody>(.*?)</tbody>', content, re.DOTALL)
    if not tbody_match:
        return existing, content
    
    tbody = tbody_match.group(1)
    
    # 각 tr 행 파싱
    for tr_match in re.finditer(r'<tr[^>]*>.*?</tr>', tbody, re.DOTALL):
        tr = tr_match.group(0)
        
        # 회차, 정/컴, 교시, 번호 추출
        td_matches = re.findall(r'<td[^>]*>(.*?)</td>', tr, re.DOTALL)
        if len(td_matches) >= 4:
            round_text = re.sub(r'<[^>]+>', '', td_matches[0]).strip()
            round_num = re.match(r'(\d+)', round_text)
            if round_num:
                exam_type = re.sub(r'<[^>]+>', '', td_matches[1]).strip()
                period = re.sub(r'<[^>]+>', '', td_matches[2]).strip()
                num = re.sub(r'<[^>]+>', '', td_matches[3]).strip()
                
                key = f"{round_num.group(1)}-{exam_type}-{period}-{num}"
                existing[key] = tr
    
    return existing, content

def generate_new_row(q):
    """새 문제에 대한 tr 행 생성"""
    domain_class = q['domain'].lower()
    short = get_short_question(q['full'])
    
    full_escaped = q['full'].replace('"', '&quot;').replace('<', '&lt;').replace('>', '&gt;')
    short_escaped = short.replace('<', '&lt;').replace('>', '&gt;')
    
    row = f'<tr data-domain="{q["domain"]}" data-full="{full_escaped}">'
    row += f'<td>{q["round"]}<span class="domain-badge {domain_class}">{q["domain"]}</span></td>'
    row += f'<td>{q["exam_type"]}</td>'
    row += f'<td>{q["period"]}</td>'
    row += f'<td>{q["num"]}</td>'
    row += f'<td class="question-cell">{short_escaped}</td>'
    row += '<td>-</td>'
    row += '</tr>'
    
    return row

def main():
    csv_path = Path('/Users/jaewoo.ryu/Downloads/전체 기출문제.csv')
    index_path = Path('/Users/jaewoo.ryu/woowa/dev/fantasio-dev.github.io/docs/exam/index.md')
    
    print("1. CSV 파싱 중...")
    csv_questions = parse_csv(csv_path)
    print(f"   CSV에서 {len(csv_questions)}개 문제 파싱됨")
    
    print("2. 기존 index.md 파싱 중...")
    existing_rows, full_content = parse_existing_rows(index_path)
    print(f"   기존 {len(existing_rows)}개 문제 보존")
    
    # 기존에 없는 새 문제들 찾기
    new_questions = []
    for key, q in csv_questions.items():
        if key not in existing_rows:
            new_questions.append(q)
    
    print(f"3. 새로 추가할 문제: {len(new_questions)}개")
    
    if len(new_questions) == 0:
        print("   추가할 새 문제가 없습니다.")
        return
    
    # 도메인별로 그룹화
    by_domain = {}
    for q in new_questions:
        domain = q['domain']
        if domain not in by_domain:
            by_domain[domain] = []
        by_domain[domain].append(q)
    
    # 정렬
    for domain in by_domain:
        by_domain[domain].sort(key=lambda x: (
            -x['round'],
            -int(x['period']) if x['period'].isdigit() else 0,
            -int(x['num']) if x['num'].isdigit() else 0
        ))
    
    # 새 행 생성
    new_rows = []
    domain_order = ['SW', 'AI', 'SEC', 'DS', 'NW', 'DB', 'CAOS', 'BIZ']
    
    for domain in domain_order:
        if domain in by_domain:
            new_rows.append(f'<!-- 추가된 {domain} 문제 ({len(by_domain[domain])}개) -->')
            for q in by_domain[domain]:
                new_rows.append(generate_new_row(q))
    
    # 기존 tbody에 새 행 추가
    tbody_match = re.search(r'(<tbody>)(.*?)(</tbody>)', full_content, re.DOTALL)
    if tbody_match:
        new_tbody = tbody_match.group(1) + tbody_match.group(2) + '\n' + '\n'.join(new_rows) + '\n' + tbody_match.group(3)
        new_content = full_content[:tbody_match.start()] + new_tbody + full_content[tbody_match.end():]
    else:
        print("   ERROR: tbody를 찾을 수 없습니다.")
        return
    
    # 회차 선택 옵션 업데이트
    all_rounds = set()
    for key in csv_questions:
        round_num = int(key.split('-')[0])
        all_rounds.add(round_num)
    for key in existing_rows:
        round_num = int(key.split('-')[0])
        all_rounds.add(round_num)
    
    round_options = ['<option value="">전체</option>']
    for r in sorted(all_rounds, reverse=True):
        round_options.append(f'<option value="{r}">{r}회</option>')
    
    new_select = '<select id="filterRound">\n        ' + '\n        '.join(round_options) + '\n      </select>'
    new_content = re.sub(r'<select id="filterRound">.*?</select>', new_select, new_content, flags=re.DOTALL)
    
    # 저장
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"4. 완료! {len(new_questions)}개 문제 추가됨")
    print(f"   총 문제 수: {len(existing_rows) + len(new_questions)}개")

if __name__ == '__main__':
    main()

