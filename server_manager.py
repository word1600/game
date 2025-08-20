#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UFO Word Game 로컬 서버 관리 도구
자동으로 포트를 찾고 서버를 시작/관리합니다.
"""

import os
import sys
import time
import socket
import subprocess
import threading
from pathlib import Path

class ServerManager:
    def __init__(self):
        self.base_ports = [8000, 8001, 8002, 8003, 8004, 8005]
        self.server_process = None
        self.current_port = None
        
    def find_available_port(self):
        """사용 가능한 포트 찾기"""
        for port in self.base_ports:
            if self.is_port_available(port):
                return port
        return None
    
    def is_port_available(self, port):
        """포트 사용 가능 여부 확인"""
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('localhost', port))
                return True
        except OSError:
            return False
    
    def start_server(self, port=None):
        """서버 시작"""
        if port is None:
            port = self.find_available_port()
            
        if port is None:
            print("❌ 사용 가능한 포트를 찾을 수 없습니다.")
            return False
            
        self.current_port = port
        
        print(f"🚀 포트 {port}에서 서버를 시작합니다...")
        print(f"📍 접속 URL: http://localhost:{port}/")
        print()
        print("🎮 게임 접속 방법:")
        print(f"   - Unit 1: http://localhost:{port}/")
        print(f"   - Unit 2: http://localhost:{port}/unit2/")
        print(f"   - Unit 3: http://localhost:{port}/unit3/")
        print(f"   - Unit 4: http://localhost:{port}/unit4/")
        print(f"   - Unit 5: http://localhost:{port}/unit5/")
        print()
        print("⚠️  서버를 중지하려면 Ctrl+C를 누르세요.")
        print()
        
        try:
            # 서버 시작
            self.server_process = subprocess.Popen(
                [sys.executable, '-m', 'http.server', str(port)],
                cwd=Path.cwd()
            )
            
            print("✅ 서버가 성공적으로 시작되었습니다!")
            print(f"🌐 http://localhost:{port}/ 에서 게임을 즐겨보세요!")
            
            # 서버 프로세스 모니터링
            while self.server_process.poll() is None:
                time.sleep(1)
                
        except KeyboardInterrupt:
            print("\n🛑 서버를 중지합니다...")
            self.stop_server()
        except Exception as e:
            print(f"❌ 서버 시작 중 오류 발생: {e}")
            return False
            
        return True
    
    def stop_server(self):
        """서버 중지"""
        if self.server_process:
            self.server_process.terminate()
            self.server_process.wait()
            print("✅ 서버가 중지되었습니다.")
    
    def check_server_status(self):
        """서버 상태 확인"""
        if self.current_port and self.is_port_available(self.current_port):
            print(f"❌ 포트 {self.current_port}에서 서버가 실행되지 않고 있습니다.")
            return False
        else:
            print(f"✅ 포트 {self.current_port}에서 서버가 정상 실행 중입니다.")
            return True
    
    def restart_server(self):
        """서버 재시작"""
        print("🔄 서버를 재시작합니다...")
        self.stop_server()
        time.sleep(2)
        return self.start_server()

def main():
    """메인 함수"""
    print("🛸 UFO Word Game 서버 관리 도구")
    print("=" * 50)
    
    manager = ServerManager()
    
    # 사용 가능한 포트 확인
    available_port = manager.find_available_port()
    if available_port:
        print(f"✅ 사용 가능한 포트: {available_port}")
    else:
        print("❌ 사용 가능한 포트가 없습니다.")
        return
    
    try:
        # 서버 시작
        manager.start_server()
    except KeyboardInterrupt:
        print("\n👋 프로그램을 종료합니다.")

if __name__ == "__main__":
    main()






