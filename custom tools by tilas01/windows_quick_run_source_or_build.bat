@echo off
setlocal EnableDelayedExpansion

:askCompileOrRunSource
cls
echo ========================================
echo Would you like to:
echo   1) Compile the code
echo   2) Run from Python Source Code (faster)
echo ========================================
set /p userChoice1=Enter 1 or 2: 

if "%userChoice2%"=="1" (
    echo You chose to compile.
    goto done
) else if "%userChoice2%"=="2" (
    echo You chose to run from source (faster).
    goto RunFromSource
) else (
    echo Invalid choice. Please enter 1 or 2.
    pause >nul
    goto askRunCompiledOrSource
)

:CompileandAskRun
echo Compiling...
cd..
title Installing requirements for build...
echo Downloading all requirements required with pip to build or run this project with the python interpreter...
pip install -r requirements.txt
cls
title Building [EDOPro-HD-Card-Downloader] with pyinstaller...
pyinstaller main.py -y --distpath "bin" -F --specpath "bin" -n "EDOPro-HD-Downloader" -c --clean --workpath "workpath_pyinstaller"
title Copying Custom Tools into Binary Directory
echo Copying over custom exif tool this fork provides...
copy "custom tools by tilas01\exif_removal_tool_for_pics.py" bin
cls

:askRunCompiledOrSource
echo.
echo ========================================
echo Now, would you like to:
echo   1) Run the compiled binary
echo   2) Continue running from source (faster)
echo ========================================
set /p userChoice2=Enter 1 or 2: 

if "%userChoice2%"=="1" (
    echo You chose to run the compiled binary.
    goto RunCompiledBinary
) else if "%userChoice2%"=="2" (
    echo You chose to continue from source (faster).
    goto RunFromSource
) else (
    echo Invalid choice. Please enter 1 or 2.
    pause >nul
    goto askRunCompiledOrSource
)

:RunCompiledBinary
title Running built app [/bin/EDOPro-HD-Card-Downloader.exe]...
cd bin
echo EDOPro HD Card Downloader Built! Launching Now! Please Wait...
echo This build can be found and run inside the /bin directory as EDOPRO-HD-Downloader.exe
echo.
ping 127.0.0.1 >nul
ping 127.0.0.1 >nul
title EDOPro HD Card Downloader [EasyBuild]
EDOPro-HD-Downloader.exe

:RunFromSource
cd..
echo Running From Source (Faster)...
echo Python3 is Required. Please Install it if you have not.
python main.py


