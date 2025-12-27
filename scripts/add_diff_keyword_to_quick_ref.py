#!/usr/bin/env python3
"""
핵심 암기 (Quick Reference) 섹션에 차별점 키워드 추가 스크립트
"""

import os
import re
import glob

def extract_diff_keyword(content):
    """차별점 키워드 내용 추출"""
    # 패턴 1: ### ⭐ 차별점 키워드 다음 줄
    pattern1 = r'###\s*⭐\s*차별점 키워드\s*\n+[-\*]\s*\*\*([^*]+)\*\*[:\s]*([^\n]+)'
    match1 = re.search(pattern1, content)
    
    # 패턴 2: ## ⭐ 차별점 키워드 (가산점 포인트) 다음 important 블록
    pattern2 = r'##\s*⭐\s*차별점 키워드.*?\n+\{:\s*\.important\s*\}\s*\n>\s*\*\*([^*]+)\*\*[:\s]*([^\n]+)'
    match2 = re.search(pattern2, content, re.DOTALL)
    
    if match1:
        keyword = match1.group(1).strip()
        desc = match1.group(2).strip()
        return f"{keyword}: {desc}"
    elif match2:
        keyword = match2.group(1).strip()
        desc = match2.group(2).strip()
        return f"{keyword}: {desc}"
    
    # 패턴 3: 간단한 형태
    pattern3 = r'차별점.*?[-\*]\s*\*\*([^*]+)\*\*[:\s–-]*([^\n]+)'
    match3 = re.search(pattern3, content)
    if match3:
        keyword = match3.group(1).strip()
        desc = match3.group(2).strip()
        return f"{keyword}: {desc}"
    
    return None

def has_diff_in_quick_ref(content):
    """핵심 암기 섹션에 이미 차별점이 있는지 확인"""
    # 핵심 암기 섹션 찾기
    quick_ref_pattern = r'###\s*📌\s*핵심 암기.*?\n(.*?)(?=\n---|\n##|\n<div|\Z)'
    match = re.search(quick_ref_pattern, content, re.DOTALL)
    if match:
        quick_ref_content = match.group(1)
        return '차별점' in quick_ref_content
    return False

def add_diff_to_quick_ref(content, diff_keyword):
    """핵심 암기 섹션에 차별점 키워드 추가"""
    # 핵심 암기 블록 찾기: {: .highlight } > 로 시작하는 블록
    # 마지막 > 줄 다음에 새 줄 추가
    
    # 패턴: 핵심 암기 섹션의 마지막 > 줄 찾기
    pattern = r'(###\s*📌\s*핵심 암기[^\n]*\n+\{:\s*\.highlight\s*\}\s*\n(?:>[^\n]*\n)+)'
    
    def add_diff_line(match):
        block = match.group(1)
        # 마지막 > 줄 뒤에 차별점 추가
        if not block.endswith('\n'):
            block += '\n'
        # 이미 차별점이 있으면 추가하지 않음
        if '차별점' in block:
            return block
        return block.rstrip('\n') + f'\n> - ⭐ **차별점**: {diff_keyword}\n'
    
    new_content = re.sub(pattern, add_diff_line, content, count=1)
    return new_content

def process_file(filepath):
    """파일 처리"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 이미 핵심 암기에 차별점이 있으면 스킵
    if has_diff_in_quick_ref(content):
        return 'skip', '이미 차별점 있음'
    
    # 차별점 키워드 추출
    diff_keyword = extract_diff_keyword(content)
    if not diff_keyword:
        return 'no_diff', '차별점 키워드 없음'
    
    # 핵심 암기 섹션에 추가
    new_content = add_diff_to_quick_ref(content, diff_keyword)
    
    if new_content == content:
        return 'no_change', '핵심 암기 섹션 없거나 변경 없음'
    
    # 저장
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return 'success', diff_keyword[:50]

def main():
    """메인 함수"""
    print("\n🔄 핵심 암기 (Quick Reference)에 차별점 키워드 추가")
    
    # 기출문제 파일
    exam_files = glob.glob('/Users/jaewoo.ryu/woowa/dev/fantasio-dev.github.io/docs/ai/exam/*.md')
    exam_files = [f for f in exam_files if 'index.md' not in f]
    
    # 기본 토픽 파일 (01-machine-learning ~ 11-ai-training-data)
    topic_files = []
    for i in range(1, 12):
        pattern = f'/Users/jaewoo.ryu/woowa/dev/fantasio-dev.github.io/docs/ai/{i:02d}-*/*.md'
        topic_files.extend(glob.glob(pattern))
    
    all_files = exam_files + topic_files
    
    print(f"📁 대상 파일: 기출 {len(exam_files)}개 + 토픽 {len(topic_files)}개 = {len(all_files)}개\n")
    
    results = {'success': [], 'skip': [], 'no_diff': [], 'no_change': []}
    
    for filepath in sorted(all_files):
        status, msg = process_file(filepath)
        filename = os.path.basename(filepath)
        results[status].append(filename)
        
        if status == 'success':
            print(f"  ✅ {filename}: {msg}")
        elif status == 'skip':
            pass  # 이미 있는 건 조용히 스킵
    
    print(f"\n📊 결과:")
    print(f"  ✅ 추가 완료: {len(results['success'])}개")
    print(f"  ⏭️ 이미 있음: {len(results['skip'])}개")
    print(f"  ⚠️ 차별점 없음: {len(results['no_diff'])}개")
    print(f"  ➖ 변경 없음: {len(results['no_change'])}개")

if __name__ == "__main__":
    main()

