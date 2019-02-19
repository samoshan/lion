@ECHO OFF
cd lion
IF NOT EXIST enabled mklink /D enabled cogs
python liond.py
PAUSE