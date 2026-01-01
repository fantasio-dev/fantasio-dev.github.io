#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
기출문제 CSV를 파싱하여 exam/index.md 에 추가하는 스크립트
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
    """문제 텍스트 정리 - 번호 제거 및 클린업"""
    if not question_text:
        return ""
    # 앞의 번호(예: "1.", "2.") 제거
    question_text = re.sub(r'^\d+\.\s*', '', question_text.strip())
    # 줄바꿈을 공백으로
    question_text = question_text.replace('\n', ' ').replace('\r', '')
    # 연속 공백 제거
    question_text = re.sub(r'\s+', ' ', question_text)
    # 회차 표시 제거 (137관리), (137컴시응) 등
    question_text = re.sub(r'\(\d{3}(관리|컴시응|정|컴)\)', '', question_text)
    return question_text.strip()

def get_short_question(full_question):
    """긴 문제를 짧게 요약"""
    if not full_question:
        return ""
    # 가. 나. 다. 등이 있으면 앞부분만
    if ' 가.' in full_question or ' 가)' in full_question:
        parts = re.split(r'\s+가[\.\)]', full_question)
        short = parts[0].strip()
    elif '. ' in full_question[:100]:
        # 첫 문장만
        short = full_question.split('. ')[0] + '.'
    else:
        short = full_question[:80] + '...' if len(full_question) > 80 else full_question
    return short

def parse_csv(csv_path):
    """CSV 파일 파싱"""
    questions = []
    
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)  # 헤더 스킵
        
        current_question = None
        
        for row in reader:
            if len(row) < 7:
                # 불완전한 행은 이전 문제의 연속일 수 있음
                if current_question and len(row) > 0:
                    # 멀티라인 문제 이어붙이기
                    current_question['full'] += ' ' + ' '.join(row)
                continue
            
            round_num, exam_type, period, num, question, obj, category = row[:7]
            
            # 회차가 숫자가 아니면 이전 문제의 연속
            if not round_num.strip().isdigit():
                if current_question:
                    current_question['full'] += ' ' + question
                continue
            
            # 이전 문제 저장
            if current_question:
                questions.append(current_question)
            
            # 새 문제
            current_question = {
                'round': int(round_num.strip()),
                'exam_type': exam_type.strip(),  # 관리/컴시응
                'period': period.strip(),  # 교시
                'num': num.strip(),  # 번호
                'full': clean_question(question),
                'category': category.strip(),
                'domain': get_domain_code(category)
            }
        
        # 마지막 문제 저장
        if current_question:
            questions.append(current_question)
    
    return questions

def generate_table_row(q):
    """테이블 행 HTML 생성"""
    domain_class = q['domain'].lower()
    short_question = get_short_question(q['full'])
    
    # HTML 이스케이프
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

def main():
    csv_path = Path('/Users/jaewoo.ryu/Downloads/전체 기출문제.csv')
    output_path = Path('/Users/jaewoo.ryu/woowa/dev/fantasio-dev.github.io/docs/exam/new_questions.html')
    
    print(f"CSV 파싱 중: {csv_path}")
    questions = parse_csv(csv_path)
    print(f"총 {len(questions)}개 문제 파싱됨")
    
    # 도메인별로 그룹화
    by_domain = {}
    for q in questions:
        domain = q['domain']
        if domain not in by_domain:
            by_domain[domain] = []
        by_domain[domain].append(q)
    
    # 각 도메인별로 회차 내림차순 정렬
    for domain in by_domain:
        by_domain[domain].sort(key=lambda x: (-x['round'], -int(x['period']) if x['period'].isdigit() else 0, -int(x['num']) if x['num'].isdigit() else 0))
    
    # HTML 생성
    html_parts = []
    domain_order = ['SW', 'AI', 'SEC', 'DS', 'NW', 'DB', 'CAOS', 'BIZ']
    
    for domain in domain_order:
        if domain in by_domain:
            html_parts.append(f'<!-- {domain} 영역 기출문제 ({len(by_domain[domain])}개) -->')
            for q in by_domain[domain]:
                html_parts.append(generate_table_row(q))
    
    # 파일 저장
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(html_parts))
    
    print(f"HTML 저장됨: {output_path}")
    
    # 통계 출력
    print("\n=== 도메인별 문제 수 ===")
    for domain in domain_order:
        if domain in by_domain:
            print(f"{domain}: {len(by_domain[domain])}개")
    
    # 회차별 통계
    rounds = sorted(set(q['round'] for q in questions))
    print(f"\n=== 회차 범위 ===")
    print(f"{min(rounds)}회 ~ {max(rounds)}회 (총 {len(rounds)}개 회차)")

if __name__ == '__main__':
    main()

