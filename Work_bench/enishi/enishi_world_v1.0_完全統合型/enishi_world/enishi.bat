@chcp 65001 > nul
python main.py
pause
@echo off
cd /d "%~dp0"
python main.py
pause
