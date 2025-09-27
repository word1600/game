#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
강화된 Unit 데이터 검증 도구
- 기본 JSON 검증
- 한글-영어 의미 일치성 검증
- 품사 일치성 검증
- 특수 케이스 검증
"""

import json
import re
import sys
import os

def validate_basic_structure(data):
    """기본 JSON 구조 검증"""
    errors = []
    
    for i, word in enumerate(data):
        # 필수 필드 존재 확인
        if 'ko' not in word or 'en' not in word or 'pos' not in word:
            errors.append(f"Line {i+1}: 필수 필드 누락 (ko, en, pos)")
            continue
        
        # 빈 값 확인
        if not word['ko'].strip() or not word['en'].strip() or not word['pos'].strip():
            errors.append(f"Line {i+1}: 빈 값 발견")
        
        # 영문 단어 형식 검증 (품사 표시 허용)
        if not re.match(r'^[a-zA-Z\s\-\'().]+$', word['en']):
            errors.append(f"Line {i+1}: 영문 단어 형식 오류: {word['en']}")
        
        # 한글 단어 형식 검증
        if not re.match(r'^[가-힣a-zA-Z0-9\s,()!]+$', word['ko']):
            errors.append(f"Line {i+1}: 한글 단어 형식 오류: {word['ko']}")
        
        # 품사 형식 검증
        valid_pos = ['n.', 'v.', 'adj.', 'adv.', 'prep.', 'conj.', 'interj.', 'int.', 'phr.', 'pron.', 'past', 's', 'ing', 'to inf.']
        pos_valid = any(word['pos'].startswith(p) for p in valid_pos)
        if not pos_valid:
            errors.append(f"Line {i+1}: 품사 형식 오류: {word['pos']}")
    
    return errors

def validate_word_meaning_consistency(data):
    """한글-영어 의미 일치성 검증"""
    errors = []
    
    # 특정 단어들의 의미 검증
    meaning_checks = {
        'puddle': ['물웅덩이', '웅덩이', '물고인 곳'],
        'darn it': ['젠장', '이런', '아'],
        'assignment': ['과제', '임무', '숙제'],
        'task': ['임무', '과제', '작업'],
        'writing': ['쓰기', '글쓰기', '작문'],
        'soldier': ['군인', '병사', '전사'],
        'art': ['미술', '예술', '아트'],
        'elevator': ['승강기', '엘리베이터'],
        'restroom': ['화장실', '세면실', '화장실'],
        'weather': ['날씨', '기상'],
        'lunch': ['점심', '점심식사'],
        'earth': ['지구', '흙', '땅'],
        'street': ['거리', '도로', '길']
    }
    
    for i, word in enumerate(data):
        en_word = word['en'].lower().strip()
        ko_word = word['ko'].strip()
        
        if en_word in meaning_checks:
            valid_meanings = meaning_checks[en_word]
            if not any(valid in ko_word for valid in valid_meanings):
                errors.append(f"Line {i+1}: '{en_word}'의 한글 뜻 '{ko_word}'가 부적절함. 올바른 뜻: {valid_meanings}")
    
    return errors

def validate_pos_consistency(data):
    """품사 일치성 검증"""
    errors = []
    
    # 감탄사 단어들
    interjection_words = ['darn it', 'oh no', 'wow', 'oh my', 'gee', 'gosh']
    
    for i, word in enumerate(data):
        en_word = word['en'].lower().strip()
        pos = word['pos'].strip()
        
        # 감탄사 단어 검증
        if en_word in interjection_words:
            if 'int.' not in pos and 'interj.' not in pos:
                errors.append(f"Line {i+1}: '{en_word}'는 감탄사인데 품사가 '{pos}'로 표기됨")
        
        # 명사 단어 검증
        if en_word in ['puddle', 'assignment', 'task', 'writing', 'soldier', 'art', 'elevator', 'restroom', 'weather', 'lunch', 'earth', 'street']:
            if 'n.' not in pos:
                errors.append(f"Line {i+1}: '{en_word}'는 명사인데 품사가 '{pos}'로 표기됨")
    
    return errors

def validate_special_cases(data):
    """특수 케이스 검증"""
    errors = []
    
    for i, word in enumerate(data):
        en_word = word['en'].strip()
        ko_word = word['ko'].strip()
        
        # puddle 특별 검증
        if en_word == 'puddle':
            if ko_word not in ['물웅덩이', '웅덩이', '물고인 곳']:
                errors.append(f"Line {i+1}: puddle의 한글 뜻 '{ko_word}'가 부적절함. 올바른 뜻: 물웅덩이")
        
        # darn it 특별 검증
        if en_word == 'darn it':
            if '젠장' not in ko_word and '이런' not in ko_word:
                errors.append(f"Line {i+1}: darn it의 한글 뜻 '{ko_word}'가 부적절함. 올바른 뜻: 아,이런!, 젠장")
        
        # 연속된 공백 확인
        if '  ' in ko_word or '  ' in en_word:
            errors.append(f"Line {i+1}: 연속된 공백 발견")
    
    return errors

def check_duplicates(data):
    """중복 단어 확인"""
    errors = []
    seen_words = set()
    
    for i, word in enumerate(data):
        word_key = f"{word['en']}|{word['ko']}"
        if word_key in seen_words:
            errors.append(f"Line {i+1}: 중복 단어 발견: {word['en']} - {word['ko']}")
        seen_words.add(word_key)
    
    return errors

def enhanced_validate_unit_data(file_path):
    """강화된 Unit 데이터 검증"""
    print(f"🔍 {file_path} 강화 검증 시작...")
    print("=" * 50)
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"❌ 파일을 찾을 수 없습니다: {file_path}")
        return False
    except json.JSONDecodeError as e:
        print(f"❌ JSON 형식 오류: {e}")
        return False
    
    errors = []
    
    # 1. 기본 구조 검증
    print("📋 기본 구조 검증 중...")
    errors.extend(validate_basic_structure(data))
    
    # 2. 중복 확인
    print("🔄 중복 단어 확인 중...")
    errors.extend(check_duplicates(data))
    
    # 3. 의미 일치성 검증
    print("🎯 의미 일치성 검증 중...")
    errors.extend(validate_word_meaning_consistency(data))
    
    # 4. 품사 일치성 검증
    print("📝 품사 일치성 검증 중...")
    errors.extend(validate_pos_consistency(data))
    
    # 5. 특수 케이스 검증
    print("⚠️ 특수 케이스 검증 중...")
    errors.extend(validate_special_cases(data))
    
    # 결과 출력
    print("=" * 50)
    print(f"📊 검증 결과:")
    print(f"   - 총 단어 수: {len(data)}개")
    print(f"   - 오류 수: {len(errors)}개")
    
    if errors:
        print(f"❌ {len(errors)}개의 오류가 발견되었습니다:")
        for i, error in enumerate(errors, 1):
            print(f"   {i}. {error}")
        print("\n🔧 오류를 수정한 후 다시 검증해주세요.")
        return False
    else:
        print("🎉 모든 검증을 통과했습니다!")
        return True

def main():
    if len(sys.argv) != 2:
        print("사용법: python enhanced_validator.py <unit_json_file>")
        print("예시: python enhanced_validator.py data/unit11.json")
        sys.exit(1)
    
    file_path = sys.argv[1]
    
    if not os.path.exists(file_path):
        print(f"❌ 파일이 존재하지 않습니다: {file_path}")
        sys.exit(1)
    
    success = enhanced_validate_unit_data(file_path)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
