@echo off
cls
title Installer
py -3 -m pip install -r requirements.txt
pip install -U discord==1.7.3 
pip install -U discord.py==1.7.3
echo Finished!
pause
