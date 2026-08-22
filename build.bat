@echo off
setlocal EnableDelayedExpansion
rem Build script: outputs each template into .preview\<template-name>\ (already gitignored),
rem keeping the repo root clean.
rem Usage:
rem   build.bat                         show menu, compile one template (default main_algorithm)
rem   build.bat main_algorithm.tex      compile a specific template
rem   build.bat --all                   compile all main_*.tex

cd /d %~dp0

rem If xelatex is not on PATH, fall back to the common MiKTeX install location.
where xelatex >nul 2>nul
if errorlevel 1 (
    if exist "%LOCALAPPDATA%\Programs\MiKTeX\miktex\bin\x64" (
        set "PATH=%LOCALAPPDATA%\Programs\MiKTeX\miktex\bin\x64;%PATH%"
    )
)

if /i "%~1"=="--all" goto :compile_all
if not "%~1"=="" (
    call :compile "%~1"
    if errorlevel 1 exit /b 1
    echo.
    echo Done. PDF is in .preview\%~n1\
    goto :eof
)

:menu
echo.
echo Select a template to compile:
echo   1) main_algorithm.tex   (AI / Algorithm / Agent)
echo   2) main_backend.tex     (Java Backend)
echo   3) main_frontend.tex    (Frontend / Web)
echo   4) main_testdevelop.tex (Test Development)
echo.
set "choice="
set /p choice="Enter number 1-4 and press Enter (default: 1): "
if "!choice!"=="" set choice=1

if "!choice!"=="1" (
    call :compile "main_algorithm.tex"
    if errorlevel 1 exit /b 1
    echo.
    echo Done. PDF is in .preview\main_algorithm\
    goto :eof
)
if "!choice!"=="2" (
    call :compile "main_backend.tex"
    if errorlevel 1 exit /b 1
    echo.
    echo Done. PDF is in .preview\main_backend\
    goto :eof
)
if "!choice!"=="3" (
    call :compile "main_frontend.tex"
    if errorlevel 1 exit /b 1
    echo.
    echo Done. PDF is in .preview\main_frontend\
    goto :eof
)
if "!choice!"=="4" (
    call :compile "main_testdevelop.tex"
    if errorlevel 1 exit /b 1
    echo.
    echo Done. PDF is in .preview\main_testdevelop\
    goto :eof
)

echo Invalid choice. Please enter 1-4.
goto :menu

:compile_all
echo Compiling all main_*.tex into .preview\...
for %%f in (main_*.tex) do (
    call :compile "%%f"
    if errorlevel 1 exit /b 1
)
echo.
echo Done.
goto :eof

:compile
set "fname=%~n1"
set "outdir=.preview\%fname%"
if not exist "%outdir%" mkdir "%outdir%"
echo.
echo === Compiling %~1 into %outdir%\ ===
xelatex -interaction=nonstopmode -synctex=1 -output-directory="%outdir%" %~1
if errorlevel 1 (
    echo [ERROR] %~1 failed on first pass.
    exit /b 1
)
xelatex -interaction=nonstopmode -synctex=1 -output-directory="%outdir%" %~1
if errorlevel 1 (
    echo [ERROR] %~1 failed on second pass.
    exit /b 1
)
goto :eof
