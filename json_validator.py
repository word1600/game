#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
JSON 파일 오탈자 검증 도구
UFO Word Game Unit 생성 전 JSON 파일 검증
"""

import json
import re
import sys
from pathlib import Path

def validate_json_structure(file_path):
    """JSON 파일 구조 검증"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if not isinstance(data, list):
            return False, "JSON 파일이 배열 형태가 아닙니다."
        
        return True, f"JSON 구조 정상. 총 {len(data)}개 단어"
    except json.JSONDecodeError as e:
        return False, f"JSON 형식 오류: {e}"
    except Exception as e:
        return False, f"파일 읽기 오류: {e}"

def validate_word_format(word_data, index):
    """개별 단어 데이터 형식 검증 - 오탈자만 확인"""
    errors = []
    
    # 필수 필드 확인
    required_fields = ['ko', 'en', 'pos']
    for field in required_fields:
        if field not in word_data:
            errors.append(f"필수 필드 '{field}' 누락")
    
    # 필드 타입 확인
    for field in required_fields:
        if field in word_data and not isinstance(word_data[field], str):
            errors.append(f"'{field}' 필드가 문자열이 아닙니다")
    
    # 빈 값 확인
    for field in required_fields:
        if field in word_data and not word_data[field].strip():
            errors.append(f"'{field}' 필드가 비어있습니다")
    
    # 영문 단어 오탈자 검증 (더 관대한 규칙)
    if 'en' in word_data and word_data['en']:
        en_word = word_data['en'].strip()
        # 연속된 공백만 확인 (오타 가능성)
        if '  ' in en_word:
            errors.append(f"연속된 공백 발견: '{en_word}'")
        
        # 숫자만 있는 경우만 오류로 판단
        if re.match(r'^\d+$', en_word):
            errors.append(f"숫자만 있는 단어: '{en_word}'")
    
    # 한글 단어 오탈자 검증 (더 관대한 규칙)
    if 'ko' in word_data and word_data['ko']:
        ko_word = word_data['ko'].strip()
        # 연속된 공백만 확인 (오타 가능성)
        if '  ' in ko_word:
            errors.append(f"연속된 공백 발견: '{ko_word}'")
    
    # 품사 형식 검증 (더 관대한 규칙)
    if 'pos' in word_data and word_data['pos']:
        pos = word_data['pos'].strip()
        # 빈 품사만 오류로 판단
        if not pos:
            errors.append(f"품사가 비어있습니다")
    
    return errors

def check_duplicates(data):
    """중복 단어 확인"""
    duplicates = {}
    for i, word in enumerate(data):
        key = f"{word.get('ko', '')}|{word.get('en', '')}"
        if key in duplicates:
            duplicates[key].append(i + 1)
        else:
            duplicates[key] = [i + 1]
    
    return {k: v for k, v in duplicates.items() if len(v) > 1}

def validate_json_file(file_path):
    """JSON 파일 전체 검증"""
    print(f"🔍 {file_path} 검증 시작...")
    print("=" * 50)
    
    # 1. JSON 구조 검증
    is_valid, message = validate_json_structure(file_path)
    if not is_valid:
        print(f"❌ {message}")
        return False
    
    print(f"✅ {message}")
    
    # 2. 파일 읽기
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 3. 개별 단어 검증
    total_errors = 0
    for i, word in enumerate(data):
        errors = validate_word_format(word, i)
        if errors:
            total_errors += len(errors)
            print(f"\n⚠️  단어 {i+1}번 오류:")
            for error in errors:
                print(f"   - {error}")
            print(f"   현재 데이터: {word}")
    
    # 4. 중복 확인
    duplicates = check_duplicates(data)
    if duplicates:
        print(f"\n⚠️  중복 단어 발견:")
        for word, indices in duplicates.items():
            print(f"   - '{word}': {indices}번째")
    
    # 5. 결과 요약
    print("\n" + "=" * 50)
    print(f"📊 검증 결과:")
    print(f"   - 총 단어 수: {len(data)}개")
    print(f"   - 오류 수: {total_errors}개")
    print(f"   - 중복 단어: {len(duplicates)}개")
    
    if total_errors == 0 and len(duplicates) == 0:
        print("🎉 모든 검증을 통과했습니다!")
        return True
    else:
        print("❌ 오류가 발견되었습니다. 수정 후 다시 검증해주세요.")
        return False

def main():
    """메인 함수"""
    if len(sys.argv) != 2:
        print("사용법: python json_validator.py <json_file_path>")
        print("예시: python json_validator.py data/unit9.json")
        return
    
    file_path = sys.argv[1]
    if not Path(file_path).exists():
        print(f"❌ 파일을 찾을 수 없습니다: {file_path}")
        return
    
    success = validate_json_file(file_path)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()

