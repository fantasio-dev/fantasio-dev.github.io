#!/usr/bin/env python3
"""
핵심 암기 섹션에 차별점 키워드 플레이스홀더 추가
"""

import os
import re
import glob

def has_diff_keyword(content):
    """차별점 키워드가 있는지 확인"""
    return '⭐ **차별점**' in content

def add_diff_placeholder(content):
    """핵심 암기 블록 끝에 차별점 플레이스홀더 추가"""
    # 패턴: highlight 블록의 마지막 > 줄 찾기
    # > - (키워드) ... 또는 > - (구성) ... 다음에 추가
    
    pattern = r'(###\s*📌\s*핵심 암기[^\n]*\n+\{:\s*\.highlight\s*\}\s*\n(?:>[^\n]*\n)+)'
    
    def add_diff_line(match):
        block = match.group(1).rstrip('\n')
        # 이미 차별점이 있으면 그대로
        if '차별점' in block:
            return match.group(1)
        return block + '\n> - ⭐ **차별점**: [TODO: 다른 기술과 구별되는 핵심 특징]\n'
    
    new_content = re.sub(pattern, add_diff_line, content, count=1)
    return new_content

def process_file(filepath):
    """파일 처리"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 핵심 암기 섹션이 없으면 스킵
    if '핵심 암기' not in content:
        return 'no_qr', '핵심 암기 없음'
    
    # 이미 차별점이 있으면 스킵
    if has_diff_keyword(content):
        return 'skip', '이미 있음'
    
    # 차별점 추가
    new_content = add_diff_placeholder(content)
    
    if new_content == content:
        return 'no_change', '변경 없음'
    
    # 저장
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return 'success', os.path.basename(filepath)

def main():
    """메인 함수"""
    print("\n🔄 차별점 키워드 플레이스홀더 추가")
    
    # 대상 파일 수집
    files = []
    for i in range(0, 12):
        pattern = f'/Users/jaewoo.ryu/woowa/dev/fantasio-dev.github.io/docs/ai/{i:02d}-*/*.md'
        files.extend(glob.glob(pattern))
    
    # index.md 제외
    files = [f for f in files if not f.endswith('index.md')]
    
    print(f"📁 대상 파일: {len(files)}개\n")
    
    results = {'success': [], 'skip': [], 'no_qr': [], 'no_change': []}
    
    for filepath in sorted(files):
        status, msg = process_file(filepath)
        filename = os.path.basename(filepath)
        results[status].append(filename)
        
        if status == 'success':
            print(f"  ✅ {filename}")
    
    print(f"\n📊 결과:")
    print(f"  ✅ 추가 완료: {len(results['success'])}개")
    print(f"  ⏭️ 이미 있음: {len(results['skip'])}개")
    print(f"  ⚠️ 핵심암기 없음: {len(results['no_qr'])}개")
    print(f"  ➖ 변경 없음: {len(results['no_change'])}개")

if __name__ == "__main__":
    main()

