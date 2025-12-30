#!/usr/bin/env python3
"""
핵심 암기 (Quick Reference) 섹션이 없는 파일에 추가하는 스크립트
기존 내용(정의, 키워드)을 기반으로 Quick Reference 생성
"""

import os
import re
import glob

def extract_frontmatter(content):
    """YAML front matter 추출"""
    match = re.match(r'^(---\n.*?\n---\n)', content, re.DOTALL)
    if match:
        return match.group(1), content[match.end():]
    return '', content

def extract_title(frontmatter):
    """제목 추출"""
    match = re.search(r'title:\s*(.+)', frontmatter)
    return match.group(1).strip() if match else "Unknown"

def extract_keywords(content):
    """핵심 키워드 추출"""
    # ## 핵심 키워드 다음 줄에서 백틱 키워드 추출
    pattern = r'##\s*핵심 키워드\s*\n+`([^`]+)`\s*`([^`]+)`\s*`([^`]+)`'
    match = re.search(pattern, content)
    if match:
        return [match.group(1), match.group(2), match.group(3)]
    
    # 다른 패턴 시도
    pattern2 = r'##\s*핵심 키워드\s*\n+([^\n]+)'
    match2 = re.search(pattern2, content)
    if match2:
        keywords = re.findall(r'`([^`]+)`', match2.group(1))
        if keywords:
            return keywords[:3]
    
    return None

def extract_definition(content):
    """정의/개념 추출"""
    # ## 정의/개념 다음 줄
    pattern = r'##\s*정의/개념\s*\n+([^\n#]+)'
    match = re.search(pattern, content)
    if match:
        return match.group(1).strip()
    
    # 대안: 첫 번째 문장 추출
    pattern2 = r'#[^#\n]+\n[^\n]*\n+---\n+([^\n]+)'
    match2 = re.search(pattern2, content)
    if match2:
        return match2.group(1).strip()
    
    return None

def extract_mnemonic(content):
    """암기법 추출 (있으면)"""
    # 구성요소 `암기법` 패턴
    pattern = r'##\s*구성요소[^\n]*`([^`]+)`'
    match = re.search(pattern, content)
    if match:
        return match.group(1)
    
    # 다른 암기법 패턴
    pattern2 = r'`([가-힣]{2,6})`'
    matches = re.findall(pattern2, content)
    if matches:
        # 가장 많이 나오는 것 선택
        return matches[0]
    
    return None

def has_quick_reference(content):
    """핵심 암기 섹션이 있는지 확인"""
    return '핵심 암기' in content or 'Quick Reference' in content

def create_quick_reference(title, definition, keywords, mnemonic):
    """Quick Reference 섹션 생성"""
    # 키워드 문자열
    kw_str = ', '.join(keywords) if keywords else ''
    
    # 기본 템플릿
    qr = f'''## 🎯 기술사 수준 설명

### 📌 핵심 암기 (Quick Reference)

{{: .highlight }}
> **{title}**: {definition if definition else '[정의 필요]'}
'''
    
    # 암기법이 있으면 추가
    if mnemonic:
        qr += f'> - (구성) `{mnemonic}`\n'
    
    # 키워드 추가
    if keywords:
        qr += f'> - (키워드) {kw_str}\n'
    
    qr += '\n---\n'
    
    return qr

def process_file(filepath):
    """파일 처리"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 이미 핵심 암기가 있으면 스킵
    if has_quick_reference(content):
        return 'skip', '이미 있음'
    
    # Front matter 분리
    frontmatter, body = extract_frontmatter(content)
    if not frontmatter:
        return 'error', 'Front matter 없음'
    
    # 정보 추출
    title = extract_title(frontmatter)
    keywords = extract_keywords(body)
    definition = extract_definition(body)
    mnemonic = extract_mnemonic(body)
    
    if not definition and not keywords:
        return 'no_info', '정의/키워드 없음'
    
    # Quick Reference 생성
    qr_section = create_quick_reference(title, definition, keywords, mnemonic)
    
    # 삽입 위치 찾기: 첫 번째 --- 다음
    # 패턴: 제목 + 레이블 + --- 다음에 삽입
    insert_pattern = r'(#[^#\n]+.*?\{:\s*\.label[^\n]*\}\s*\n+---\s*\n+)'
    match = re.search(insert_pattern, body, re.DOTALL)
    
    if match:
        insert_pos = match.end()
        new_body = body[:insert_pos] + qr_section + body[insert_pos:]
    else:
        # 대안: 첫 번째 ## 앞에 삽입
        first_h2 = body.find('\n## ')
        if first_h2 > 0:
            new_body = body[:first_h2+1] + qr_section + body[first_h2+1:]
        else:
            return 'no_insert', '삽입 위치 없음'
    
    # 저장
    new_content = frontmatter + new_body
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return 'success', title[:30]

def main():
    """메인 함수"""
    print("\n🔄 핵심 암기 (Quick Reference) 섹션 추가")
    
    # 대상 파일 수집
    files = []
    for i in range(0, 12):
        pattern = f'/Users/jaewoo.ryu/woowa/dev/fantasio-dev.github.io/docs/ai/{i:02d}-*/*.md'
        files.extend(glob.glob(pattern))
    
    # index.md 제외
    files = [f for f in files if not f.endswith('index.md')]
    
    print(f"📁 대상 파일: {len(files)}개\n")
    
    results = {'success': [], 'skip': [], 'no_info': [], 'no_insert': [], 'error': []}
    
    for filepath in sorted(files):
        status, msg = process_file(filepath)
        filename = os.path.basename(filepath)
        results[status].append(filename)
        
        if status == 'success':
            print(f"  ✅ {filename}")
        elif status == 'no_info':
            print(f"  ⚠️ {filename}: {msg}")
        elif status == 'error':
            print(f"  ❌ {filename}: {msg}")
    
    print(f"\n📊 결과:")
    print(f"  ✅ 추가 완료: {len(results['success'])}개")
    print(f"  ⏭️ 이미 있음: {len(results['skip'])}개")
    print(f"  ⚠️ 정보 없음: {len(results['no_info'])}개")
    print(f"  ➖ 삽입 불가: {len(results['no_insert'])}개")
    print(f"  ❌ 오류: {len(results['error'])}개")
    
    return results

if __name__ == "__main__":
    main()



