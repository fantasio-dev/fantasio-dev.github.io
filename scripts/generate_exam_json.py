#!/usr/bin/env python3
"""
각 도메인별 exam.json 파일을 생성하는 스크립트
- docs/{domain}/exam/*.md 파일들을 스캔
- title, url, nav_order, exam_type(1교시형/2교시형) 추출
- docs/{domain}/exam.json 파일로 저장
"""

import os
import json
import re
from pathlib import Path

DOMAINS = ['ai', 'sw', 'ds', 'sec', 'nw', 'db', 'caos', 'biz']
BASE_DIR = Path(__file__).parent.parent
DOCS_DIR = BASE_DIR / 'docs'

def extract_front_matter(content):
    """YAML front matter 추출"""
    if not content.startswith('---'):
        return {}
    
    end_idx = content.find('---', 3)
    if end_idx == -1:
        return {}
    
    fm_text = content[3:end_idx]
    result = {}
    
    for line in fm_text.split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            result[key.strip()] = value.strip()
    
    return result

def detect_exam_type(content):
    """1교시형인지 2교시형인지 감지"""
    if '1교시형' in content:
        return '1'
    elif '2교시형' in content:
        return '2'
    # 파일명에서 교시 번호 추출
    return '1'  # 기본값

def parse_title_info(title):
    """제목에서 회차, 교시, 번호 추출"""
    # 137회-1교시-5번 GNN... 형태
    match = re.match(r'(\d+)회-(\d+)교시-(\d+)번\s*(.*)', title)
    if match:
        return {
            'round': int(match.group(1)),
            'session': int(match.group(2)),
            'number': int(match.group(3)),
            'topic': match.group(4).strip()
        }
    return None

def generate_exam_json(domain):
    """특정 도메인의 exam.json 생성"""
    exam_dir = DOCS_DIR / domain / 'exam'
    if not exam_dir.exists():
        print(f"  {domain}: exam 폴더 없음")
        return []
    
    exam_files = list(exam_dir.glob('*.md'))
    if not exam_files:
        print(f"  {domain}: 기출문제 파일 없음")
        return []
    
    items = []
    for md_file in exam_files:
        content = md_file.read_text(encoding='utf-8')
        fm = extract_front_matter(content)
        
        title = fm.get('title', '')
        permalink = fm.get('permalink', '')
        nav_order = fm.get('nav_order', '0')
        
        if not title or not permalink:
            continue
        
        exam_type = detect_exam_type(content)
        title_info = parse_title_info(title)
        
        item = {
            'title': title,
            'url': permalink,
            'nav_order': int(nav_order) if nav_order.isdigit() else 0,
            'exam_type': exam_type,  # "1" 또는 "2"
        }
        
        if title_info:
            item['round'] = title_info['round']
            item['session'] = title_info['session']
            item['number'] = title_info['number']
            item['topic'] = title_info['topic']
        
        items.append(item)
    
    # nav_order로 정렬
    items.sort(key=lambda x: x.get('nav_order', 0), reverse=True)
    
    return items

def main():
    print("기출문제 JSON 생성 시작...")
    
    for domain in DOMAINS:
        items = generate_exam_json(domain)
        
        if items:
            output_file = DOCS_DIR / domain / 'exam.json'
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(items, f, ensure_ascii=False, indent=2)
            print(f"  {domain}: {len(items)}개 항목 → {output_file}")
        else:
            print(f"  {domain}: 생성할 항목 없음")
    
    print("완료!")

if __name__ == '__main__':
    main()

