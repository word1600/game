@echo off
cd unit6-github\unit6
echo Starting Unit 6 server on http://localhost:8000
echo Press Ctrl+C to stop the server
python -m http.server 8000
pause

