@echo off
TITLE EdgeFix AI - Snapdragon Launch Console
color 0A
echo ===================================================
echo   Starting EdgeFix AI Environment...
echo ===================================================
if exist venv\Scripts\activate (
    call venv\Scripts\activate
)
python src\main.py
pause
