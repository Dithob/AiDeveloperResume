@echo off
setlocal

cd /d "%~dp0"

where py >nul 2>nul
if not errorlevel 1 (
    py -3 "%~dp0scripts\build.py" %*
    exit /b %errorlevel%
)

where python >nul 2>nul
if not errorlevel 1 (
    python "%~dp0scripts\build.py" %*
    exit /b %errorlevel%
)

echo [ERROR] Python 3 was not found. Install Python 3 and try again.
exit /b 1
