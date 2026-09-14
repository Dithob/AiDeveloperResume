@echo off
setlocal
rem Thin launcher for package_overleaf.ps1 (double-click friendly).
rem Usage (from the repo root; root is resolved automatically either way):
rem   scripts\package_overleaf.bat                     package all four templates (default)
rem   scripts\package_overleaf.bat backend             package only main_backend.tex
rem   scripts\package_overleaf.bat algorithm -Sanitize package a desensitized copy (no real personal data)
rem The zip is written to <repo>\overleaf\ and is ready to be uploaded to Overleaf.
chcp 65001 >nul
cd /d "%~dp0.."
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0package_overleaf.ps1" %*
endlocal
