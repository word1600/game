#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UFO Word Game 자동화 생성 도구
Unit 1을 템플릿으로 사용하여 Unit N을 자동 생성합니다.
"""

import os
import shutil
import json
import re
from pathlib import Path

class UFOGameGenerator:
    def __init__(self):
        self.template_dir = "unit1"  # 원본 템플릿 폴더
        self.base_dir = "."  # 현재 작업 디렉토리
        
    def create_unit_template(self, unit_number):
        """Unit 1을 템플릿으로 복사하여 Unit N 생성"""
        unit_name = f"unit{unit_number}"
        unit_dir = Path(self.base_dir) / unit_name
        
        # 기존 폴더가 있으면 삭제
        if unit_dir.exists():
            shutil.rmtree(unit_dir)
        
        # Unit 1을 템플릿으로 복사
        template_path = Path(self.base_dir) / self.template_dir
        if not template_path.exists():
            print(f"❌ 템플릿 폴더를 찾을 수 없습니다: {template_path}")
            return False
            
        shutil.copytree(template_path, unit_dir)
        print(f"✅ {unit_name} 폴더 생성 완료")
        
        # 파일 수정
        self.modify_index_html(unit_dir, unit_number)
        self.modify_game_js(unit_dir, unit_number)
        
        return True
    
    def modify_index_html(self, unit_dir, unit_number):
        """index.html의 Unit 번호 수정"""
        index_path = unit_dir / "index.html"
        if not index_path.exists():
            print(f"❌ index.html을 찾을 수 없습니다: {index_path}")
            return
            
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # "Unit 1" → "Unit N" 변경
        content = re.sub(r'Unit 1', f'Unit {unit_number}', content)
        
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"✅ index.html Unit 번호 수정 완료: Unit {unit_number}")
    
    def modify_game_js(self, unit_dir, unit_number):
        """game.js의 selectedUnit 및 loadWords 함수 수정"""
        game_js_path = unit_dir / "game.js"
        if not game_js_path.exists():
            print(f"❌ game.js를 찾을 수 없습니다: {game_js_path}")
            return
            
        with open(game_js_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # selectedUnit = 'unit1' → selectedUnit = 'unitN' 변경
        content = re.sub(r"selectedUnit = 'unit1'", f"selectedUnit = 'unit{unit_number}'", content)
        
        # loadWords 함수 수정: 각 Unit이 자신의 데이터 파일을 로드하도록
        # 하드코딩된 경로를 동적으로 변경
        old_load_words = r"const file = 'data/unit1\.json';"
        new_load_words = f"const file = 'data/unit{unit_number}.json';"
        content = re.sub(old_load_words, new_load_words, content)
        
        # unit2.json 경로도 수정 (혹시 있을 경우)
        old_load_words2 = r"const file = 'data/unit2\.json';"
        new_load_words2 = f"const file = 'data/unit{unit_number}.json';"
        content = re.sub(old_load_words2, new_load_words2, content)
        
        with open(game_js_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"✅ game.js selectedUnit 및 loadWords 수정 완료: unit{unit_number}")
    
    def create_unit_data(self, unit_number, word_data):
        """Unit N의 단어 데이터 JSON 파일 생성"""
        unit_name = f"unit{unit_number}"
        unit_dir = Path(self.base_dir) / unit_name
        data_dir = unit_dir / "data"
        
        # data 폴더가 없으면 생성
        data_dir.mkdir(exist_ok=True)
        
        # JSON 파일 생성
        json_path = data_dir / f"unit{unit_number}.json"
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(word_data, f, ensure_ascii=False, indent=2)
            
        print(f"✅ {json_path} 단어 데이터 생성 완료 ({len(word_data)}개 단어)")
    
    def generate_unit(self, unit_number, word_data):
        """Unit N 완전 생성"""
        print(f"\n🚀 Unit {unit_number} 생성 시작...")
        
        # 1. 템플릿 복사 및 수정
        if not self.create_unit_template(unit_number):
            return False
        
        # 2. 단어 데이터 생성
        self.create_unit_data(unit_number, word_data)
        
        print(f"🎉 Unit {unit_number} 생성 완료!")
        return True

def load_existing_unit_data(unit_number):
    """기존 Unit 데이터 로드 (테스트용)"""
    # Unit 1은 Unit1.json, 나머지는 unitN.json
    if unit_number == 1:
        data_path = Path("data") / "Unit1.json"
    else:
        data_path = Path("data") / f"unit{unit_number}.json"
    
    if data_path.exists():
        with open(data_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def main():
    """메인 실행 함수"""
    print("🛸 UFO Word Game 자동화 생성 도구")
    print("=" * 50)
    
    generator = UFOGameGenerator()
    
    # Unit 1을 템플릿으로 설정
    if not Path("unit1").exists():
        print("📁 Unit 1을 템플릿으로 설정 중...")
        
        # 현재 파일들을 unit1 폴더로 복사
        unit1_dir = Path("unit1")
        unit1_dir.mkdir(exist_ok=True)
        
        # 필요한 파일들 복사
        files_to_copy = [
            "index.html", "game.js", "style.css", "README.md"
        ]
        
        for file_name in files_to_copy:
            if Path(file_name).exists():
                shutil.copy2(file_name, unit1_dir / file_name)
        
        # assets 폴더 복사
        if Path("assets").exists():
            shutil.copytree("assets", unit1_dir / "assets", dirs_exist_ok=True)
        
        # data 폴더 복사
        if Path("data").exists():
            shutil.copytree("data", unit1_dir / "data", dirs_exist_ok=True)
        
        print("✅ Unit 1 템플릿 설정 완료")
        
        # Unit 1 생성 (템플릿 설정 후)
        print("\n🧪 Unit 1 생성...")
        unit1_data = load_existing_unit_data(1)
        if unit1_data:
            generator.generate_unit(1, unit1_data)
        else:
            print("❌ Unit 1 데이터를 찾을 수 없습니다.")
    
    # 테스트: Unit 2 생성
    print("\n🧪 Unit 2 테스트 생성...")
    unit2_data = load_existing_unit_data(2)
    if unit2_data:
        generator.generate_unit(2, unit2_data)
    else:
        print("❌ Unit 2 데이터를 찾을 수 없습니다.")
    
    # Unit 3 생성 (실제 unit3.json 사용)
    print("\n🧪 Unit 3 생성 (실제 unit3.json)...")
    unit3_data = load_existing_unit_data(3)
    if unit3_data:
        generator.generate_unit(3, unit3_data)
    else:
        print("❌ Unit 3 데이터를 찾을 수 없습니다.")
    
    # Unit 6 생성 (실제 unit6.json 사용)
    print("\n🧪 Unit 6 생성 (실제 unit6.json)...")
    unit6_data = load_existing_unit_data(6)
    if unit6_data:
        generator.generate_unit(6, unit6_data)
    else:
        print("❌ Unit 6 데이터를 찾을 수 없습니다.")
    
    print("\n🎯 자동화 도구 개발 완료!")
    print("이제 generate_unit(unit_number, word_data) 함수를 사용하여")
    print("수십, 수백 개의 Unit을 자동 생성할 수 있습니다.")

if __name__ == "__main__":
    main() 