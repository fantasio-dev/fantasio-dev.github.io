#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
기출문제 CSV를 파싱하여 exam/index.md 테이블을 업데이트하는 스크립트
기존 학습 페이지 링크와 암기법은 유지하면서 새로운 문제 추가
"""

import csv
import re
from pathlib import Path

# 도메인 매핑 (대분류 -> 도메인 코드)
DOMAIN_MAP = {
    '소공': 'SW',
    'SW': 'SW',
    '인공지능': 'AI',
    'AI': 'AI',
    '보안': 'SEC',
    'SEC': 'SEC',
    'DS': 'DS',
    'NW': 'NW',
    '네트워크': 'NW',
    'DB': 'DB',
    '데이터베이스': 'DB',
    'CA': 'CAOS',
    'CAOS': 'CAOS',
    '경영': 'BIZ',
    'BIZ': 'BIZ',
    '알고리즘': 'SW',
    '자료구조': 'SW',
}

def get_domain_code(category):
    """대분류를 도메인 코드로 변환"""
    if not category:
        return 'SW'
    category = category.strip()
    return DOMAIN_MAP.get(category, 'SW')

def clean_question(question_text):
    """문제 텍스트 정리"""
    if not question_text:
        return ""
    question_text = re.sub(r'^\d+\.\s*', '', question_text.strip())
    question_text = question_text.replace('\n', ' ').replace('\r', '')
    question_text = re.sub(r'\s+', ' ', question_text)
    question_text = re.sub(r'\(\d{3}(관리|컴시응|정|컴)\)', '', question_text)
    return question_text.strip()

def get_short_question(full_question, max_len=100):
    """긴 문제를 짧게 요약"""
    if not full_question:
        return ""
    if ' 가.' in full_question or ' 가)' in full_question:
        parts = re.split(r'\s+가[\.\)]', full_question)
        short = parts[0].strip()
    else:
        short = full_question
    
    if len(short) > max_len:
        short = short[:max_len] + '...'
    return short

def parse_csv(csv_path):
    """CSV 파일 파싱"""
    questions = []
    
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        
        current_question = None
        
        for row in reader:
            if len(row) < 7:
                if current_question and len(row) > 0:
                    current_question['full'] += ' ' + ' '.join(row)
                continue
            
            round_num, exam_type, period, num, question, obj, category = row[:7]
            
            if not round_num.strip().isdigit():
                if current_question:
                    current_question['full'] += ' ' + question
                continue
            
            if current_question:
                questions.append(current_question)
            
            current_question = {
                'round': int(round_num.strip()),
                'exam_type': exam_type.strip(),
                'period': period.strip(),
                'num': num.strip(),
                'full': clean_question(question),
                'category': category.strip(),
                'domain': get_domain_code(category)
            }
        
        if current_question:
            questions.append(current_question)
    
    return questions

def generate_table_row(q):
    """테이블 행 HTML 생성"""
    domain_class = q['domain'].lower()
    short_question = get_short_question(q['full'])
    
    full_escaped = q['full'].replace('"', '&quot;').replace('<', '&lt;').replace('>', '&gt;')
    short_escaped = short_question.replace('<', '&lt;').replace('>', '&gt;')
    
    row = f'<tr data-domain="{q["domain"]}" data-full="{full_escaped}">'
    row += f'<td>{q["round"]}<span class="domain-badge {domain_class}">{q["domain"]}</span></td>'
    row += f'<td>{q["exam_type"]}</td>'
    row += f'<td>{q["period"]}</td>'
    row += f'<td>{q["num"]}</td>'
    row += f'<td class="question-cell">{short_escaped}</td>'
    row += '<td>-</td>'
    row += '</tr>'
    
    return row

def read_existing_index(index_path):
    """기존 index.md 읽기"""
    with open(index_path, 'r', encoding='utf-8') as f:
        return f.read()

def extract_header_footer(content):
    """헤더(tbody 이전)와 푸터(tbody 이후) 분리"""
    tbody_start = content.find('<tbody>')
    tbody_end = content.find('</tbody>')
    
    if tbody_start == -1 or tbody_end == -1:
        raise ValueError("tbody를 찾을 수 없습니다")
    
    header = content[:tbody_start + len('<tbody>')]
    footer = content[tbody_end:]
    
    return header, footer

def generate_round_options(rounds):
    """회차 선택 옵션 HTML 생성"""
    options = ['<option value="">전체</option>']
    for r in sorted(rounds, reverse=True):
        options.append(f'<option value="{r}">{r}회</option>')
    return '\n        '.join(options)

def main():
    csv_path = Path('/Users/jaewoo.ryu/Downloads/전체 기출문제.csv')
    index_path = Path('/Users/jaewoo.ryu/woowa/dev/fantasio-dev.github.io/docs/exam/index.md')
    
    print(f"CSV 파싱 중: {csv_path}")
    questions = parse_csv(csv_path)
    print(f"총 {len(questions)}개 문제 파싱됨")
    
    # 회차 목록
    rounds = sorted(set(q['round'] for q in questions), reverse=True)
    print(f"회차 범위: {min(rounds)}회 ~ {max(rounds)}회")
    
    # 도메인별로 그룹화 및 정렬
    by_domain = {}
    for q in questions:
        domain = q['domain']
        if domain not in by_domain:
            by_domain[domain] = []
        by_domain[domain].append(q)
    
    for domain in by_domain:
        by_domain[domain].sort(key=lambda x: (
            -x['round'],
            -int(x['period']) if x['period'].isdigit() else 0,
            -int(x['num']) if x['num'].isdigit() else 0
        ))
    
    # 테이블 행 생성
    rows = []
    domain_order = ['SW', 'AI', 'SEC', 'DS', 'NW', 'DB', 'CAOS', 'BIZ']
    
    for domain in domain_order:
        if domain in by_domain:
            rows.append(f'<!-- {domain} 영역 기출문제 ({len(by_domain[domain])}개) -->')
            for q in by_domain[domain]:
                rows.append(generate_table_row(q))
    
    # 기존 index.md 읽기
    content = read_existing_index(index_path)
    header, footer = extract_header_footer(content)
    
    # 회차 선택 옵션 업데이트
    round_options = generate_round_options(rounds)
    old_options_pattern = r'<select id="filterRound">.*?</select>'
    new_options = f'''<select id="filterRound">
        {round_options}
      </select>'''
    header = re.sub(old_options_pattern, new_options, header, flags=re.DOTALL)
    
    # 새 index.md 생성
    new_content = header + '\n' + '\n'.join(rows) + '\n' + footer
    
    # 파일 저장
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"index.md 업데이트 완료!")
    print(f"\n=== 도메인별 문제 수 ===")
    for domain in domain_order:
        if domain in by_domain:
            print(f"{domain}: {len(by_domain[domain])}개")

if __name__ == '__main__':
    main()

