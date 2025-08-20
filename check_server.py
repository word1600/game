#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
서버 상태 확인 및 자동 재시작 도구
"""

import socket
import subprocess
import sys
import time

def check_server(port=8000):
    """서버 상태 확인"""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex(('localhost', port))
            return result == 0
    except:
        return False

def start_server(port=8000):
    """서버 시작"""
    print(f"🚀 포트 {port}에서 서버를 시작합니다...")
    try:
        subprocess.Popen([sys.executable, '-m', 'http.server', str(port)])
        print(f"✅ 서버가 시작되었습니다!")
        print(f"🌐 접속 URL: http://localhost:{port}/")
        return True
    except Exception as e:
        print(f"❌ 서버 시작 실패: {e}")
        return False

def main():
    """메인 함수"""
    port = 8000
    
    print("🔍 UFO Word Game 서버 상태 확인 중...")
    
    if check_server(port):
        print(f"✅ 포트 {port}에서 서버가 정상 실행 중입니다!")
        print(f"🌐 접속 가능: http://localhost:{port}/")
    else:
        print(f"❌ 포트 {port}에서 서버가 실행되지 않고 있습니다.")
        print("🔄 서버를 자동으로 시작합니다...")
        
        if start_server(port):
            print("🎉 서버가 성공적으로 시작되었습니다!")
            print("🎮 이제 게임을 즐길 수 있습니다!")
        else:
            print("💡 수동으로 서버를 시작해주세요:")
            print(f"   python -m http.server {port}")

if __name__ == "__main__":
    main()






