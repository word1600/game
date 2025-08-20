#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit 4 생성 전용 스크립트
"""

import json
from pathlib import Path
from unit_generator import UFOGameGenerator

def main():
    """Unit 4 생성"""
    print("🚀 Unit 4 생성 시작...")
    
    # Unit 4 단어 데이터 로드
    data_path = Path("data") / "unit4.json"
    if not data_path.exists():
        print(f"❌ Unit 4 데이터를 찾을 수 없습니다: {data_path}")
        return
    
    with open(data_path, 'r', encoding='utf-8') as f:
        unit4_data = json.load(f)
    
    print(f"📚 Unit 4 단어 데이터 로드 완료: {len(unit4_data)}개 단어")
    
    # Unit 4 생성
    generator = UFOGameGenerator()
    if generator.generate_unit(4, unit4_data):
        print("🎉 Unit 4 생성 완료!")
        print("🌐 접속 URL: http://localhost:8000/unit4/")
    else:
        print("❌ Unit 4 생성 실패")

if __name__ == "__main__":
    main()





