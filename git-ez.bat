@echo off
set repo=%1
set dir=%2
echo %repo% >> path.txt
echo %dir% >> path.txt
python main.py
