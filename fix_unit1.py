#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit 1 수정 스크립트
"""

import json
from pathlib import Path
from unit_generator import UFOGameGenerator

def load_unit1_data():
    """Unit 1 데이터 로드"""
    data_path = Path("data") / "Unit1.json"
    if data_path.exists():
        with open(data_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def main():
    """Unit 1 수정"""
    print("🔧 Unit 1 수정 시작...")
    
    # Unit 1 데이터 로드
    unit1_data = load_unit1_data()
    if not unit1_data:
        print("❌ Unit 1 데이터를 찾을 수 없습니다.")
        return
    
    # Unit 1 재생성
    generator = UFOGameGenerator()
    success = generator.generate_unit(1, unit1_data)
    
    if success:
        print("✅ Unit 1 수정 완료!")
    else:
        print("❌ Unit 1 수정 실패!")

if __name__ == "__main__":
    main() 