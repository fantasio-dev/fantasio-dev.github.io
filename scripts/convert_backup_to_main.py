#!/usr/bin/env python3
"""
AI 토픽 파일의 '기존 내용 (백업)' 섹션을 메인 콘텐츠로 변환하는 스크립트
"""

import os
import re

def extract_frontmatter(content):
    """YAML front matter 추출"""
    match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if match:
        return match.group(0), match.end()
    return '', 0

def extract_backup_content(content):
    """
    '기존 내용 (백업)' 섹션 내용 추출
    <details> 태그 안의 내용을 가져옴
    """
    # 수정된 패턴: <summary><h3>🗂️ 기존 내용 (백업)</h3></summary>
    pattern = r'<summary><h3[^>]*>🗂️ 기존 내용 \(백업\)</h3></summary>\s*(.*?)</details>'
    match = re.search(pattern, content, re.DOTALL)
    
    if match:
        backup_content = match.group(1).strip()
        return backup_content
    return None

def process_file(filepath):
    """파일 처리"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Front matter 추출
    frontmatter, fm_end = extract_frontmatter(content)
    if not frontmatter:
        print(f"  ⚠️ Front matter 없음: {os.path.basename(filepath)}")
        return False
    
    # 백업 내용 추출
    backup_content = extract_backup_content(content)
    if not backup_content:
        print(f"  ⚠️ 백업 섹션 없음: {os.path.basename(filepath)}")
        return False
    
    # 새 콘텐츠 구성: front matter + 백업 내용
    new_content = f"{frontmatter}\n{backup_content}\n"
    
    # 파일 저장
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"  ✅ 변환 완료: {os.path.basename(filepath)}")
    return True

def main():
    """메인 함수"""
    # 백업 양식이 있는 파일 목록 (supervised-learning.md 제외 - 이미 처리됨)
    files = [
        "/Users/jaewoo.ryu/woowa/dev/fantasio-dev.github.io/docs/ai/01-machine-learning/activation-function.md",
        "/Users/jaewoo.ryu/woowa/dev/fantasio-dev.github.io/docs/ai/01-machine-learning/data-labeling.md",
        "/Users/jaewoo.ryu/woowa/dev/fantasio-dev.github.io/docs/ai/01-machine-learning/dbscan.md",
        "/Users/jaewoo.ryu/woowa/dev/fantasio-dev.github.io/docs/ai/01-machine-learning/deep-learning-concept.md",
        "/Users/jaewoo.ryu/woowa/dev/fantasio-dev.github.io/docs/ai/01-machine-learning/k-means.md",
        "/Users/jaewoo.ryu/woowa/dev/fantasio-dev.github.io/docs/ai/01-machine-learning/knn.md",
        "/Users/jaewoo.ryu/woowa/dev/fantasio-dev.github.io/docs/ai/01-machine-learning/parameters.md",
        "/Users/jaewoo.ryu/woowa/dev/fantasio-dev.github.io/docs/ai/01-machine-learning/pca.md",
        "/Users/jaewoo.ryu/woowa/dev/fantasio-dev.github.io/docs/ai/01-machine-learning/perceptron.md",
        "/Users/jaewoo.ryu/woowa/dev/fantasio-dev.github.io/docs/ai/01-machine-learning/q-learning.md",
        "/Users/jaewoo.ryu/woowa/dev/fantasio-dev.github.io/docs/ai/01-machine-learning/reinforcement-learning.md",
        "/Users/jaewoo.ryu/woowa/dev/fantasio-dev.github.io/docs/ai/01-machine-learning/som.md",
        "/Users/jaewoo.ryu/woowa/dev/fantasio-dev.github.io/docs/ai/01-machine-learning/svm.md",
        "/Users/jaewoo.ryu/woowa/dev/fantasio-dev.github.io/docs/ai/01-machine-learning/unsupervised-learning.md",
        "/Users/jaewoo.ryu/woowa/dev/fantasio-dev.github.io/docs/ai/02-deep-learning/catastrophic-forgetting.md",
        "/Users/jaewoo.ryu/woowa/dev/fantasio-dev.github.io/docs/ai/02-deep-learning/cnn.md",
        "/Users/jaewoo.ryu/woowa/dev/fantasio-dev.github.io/docs/ai/02-deep-learning/dcgan.md",
        "/Users/jaewoo.ryu/woowa/dev/fantasio-dev.github.io/docs/ai/02-deep-learning/dropout.md",
        "/Users/jaewoo.ryu/woowa/dev/fantasio-dev.github.io/docs/ai/02-deep-learning/gan.md",
        "/Users/jaewoo.ryu/woowa/dev/fantasio-dev.github.io/docs/ai/02-deep-learning/lstm.md",
        "/Users/jaewoo.ryu/woowa/dev/fantasio-dev.github.io/docs/ai/02-deep-learning/overfitting-underfitting.md",
        "/Users/jaewoo.ryu/woowa/dev/fantasio-dev.github.io/docs/ai/02-deep-learning/pooling-layer.md",
        "/Users/jaewoo.ryu/woowa/dev/fantasio-dev.github.io/docs/ai/02-deep-learning/rnn.md",
        "/Users/jaewoo.ryu/woowa/dev/fantasio-dev.github.io/docs/ai/02-deep-learning/vanishing-gradient.md",
        "/Users/jaewoo.ryu/woowa/dev/fantasio-dev.github.io/docs/ai/03-neural-network/federated-learning.md",
        "/Users/jaewoo.ryu/woowa/dev/fantasio-dev.github.io/docs/ai/03-neural-network/gnn.md",
        "/Users/jaewoo.ryu/woowa/dev/fantasio-dev.github.io/docs/ai/04-nlp/chatgpt.md",
        "/Users/jaewoo.ryu/woowa/dev/fantasio-dev.github.io/docs/ai/04-nlp/electra.md",
        "/Users/jaewoo.ryu/woowa/dev/fantasio-dev.github.io/docs/ai/04-nlp/mrc.md",
        "/Users/jaewoo.ryu/woowa/dev/fantasio-dev.github.io/docs/ai/04-nlp/transformer.md",
        "/Users/jaewoo.ryu/woowa/dev/fantasio-dev.github.io/docs/ai/04-nlp/word-embedding.md",
        "/Users/jaewoo.ryu/woowa/dev/fantasio-dev.github.io/docs/ai/05-ai-ethics/adversarial-attack.md",
        "/Users/jaewoo.ryu/woowa/dev/fantasio-dev.github.io/docs/ai/05-ai-ethics/ai-ethics.md",
        "/Users/jaewoo.ryu/woowa/dev/fantasio-dev.github.io/docs/ai/05-ai-ethics/ai-security.md",
        "/Users/jaewoo.ryu/woowa/dev/fantasio-dev.github.io/docs/ai/05-ai-ethics/bias.md",
        "/Users/jaewoo.ryu/woowa/dev/fantasio-dev.github.io/docs/ai/06-ml-evaluation/confusion-matrix.md",
        "/Users/jaewoo.ryu/woowa/dev/fantasio-dev.github.io/docs/ai/06-ml-evaluation/precision-recall.md",
        "/Users/jaewoo.ryu/woowa/dev/fantasio-dev.github.io/docs/ai/06-ml-evaluation/roc-curve.md",
        "/Users/jaewoo.ryu/woowa/dev/fantasio-dev.github.io/docs/ai/07-ai-service/deep-view.md",
        "/Users/jaewoo.ryu/woowa/dev/fantasio-dev.github.io/docs/ai/07-ai-service/recommendation-system.md",
        "/Users/jaewoo.ryu/woowa/dev/fantasio-dev.github.io/docs/ai/07-learning-techniques/few-shot-learning.md",
        "/Users/jaewoo.ryu/woowa/dev/fantasio-dev.github.io/docs/ai/07-learning-techniques/meta-learning.md",
        "/Users/jaewoo.ryu/woowa/dev/fantasio-dev.github.io/docs/ai/08-ml-process/hyperparameters.md",
        "/Users/jaewoo.ryu/woowa/dev/fantasio-dev.github.io/docs/ai/11-ai-training-data/training-data-cost.md",
    ]
    
    print(f"\n🔄 AI 토픽 백업 양식 → 메인 양식 변환")
    print(f"📁 대상 파일: {len(files)}개\n")
    
    success = 0
    failed = 0
    
    for filepath in files:
        if os.path.exists(filepath):
            if process_file(filepath):
                success += 1
            else:
                failed += 1
        else:
            print(f"  ❌ 파일 없음: {os.path.basename(filepath)}")
            failed += 1
    
    print(f"\n📊 결과: 성공 {success}개 / 실패 {failed}개")
    return success, failed

if __name__ == "__main__":
    main()
