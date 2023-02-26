@echo off
call %~dp0audio\venv\Scripts\activate
cd %~dp0audio

set ID=822738478
set TOKEN=6094016563:AAETk1shEsVojZ4CVFZTLke9dEl2OoWNei4
python main.py

pause
