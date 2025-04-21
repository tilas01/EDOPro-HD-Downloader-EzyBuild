@echo off
setlocal EnableDelayedExpansion

rem Function to ask the first question
:askCompileOrRunSource
cls
echo ========================================
echo Would you like to:
echo   1) Compile the code
echo   2) Run from Python Source Code (faster)
echo ========================================
set /p userChoice1=Enter 1 or 2: 

if "%userChoice1%"=="1" (
    echo You chose to compile.
    goto CompileAndAskRun
) else if "%userChoice1%"=="2" (
    echo You chose to run from source (faster).
    goto RunFromSource
) else (
    echo Invalid choice. Please enter 1 or 2.
    pause >nul
    goto askCompileOrRunSource
)

rem Function to compile the code and ask whether to run compiled or from source
:CompileAndAskRun
cls
echo Compiling...
cd ..
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
goto askRunCompiledOrSource

rem Function to ask whether to run compiled binary or continue from source
:askRunCompiledOrSource
cls
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

rem Function to run the compiled binary
:RunCompiledBinary
cls
echo Running built app [/bin/EDOPro-HD-Card-Downloader.exe]...
cd bin
echo EDOPro HD Card Downloader Built! Launching Now! Please Wait...
echo This build can be found and run inside the /bin directory as EDOPRO-HD-Downloader.exe
timeout /t 3 /nobreak >nul
EDOPro-HD-Downloader.exe
goto askCompileOrRunSource

rem Function to run from source
:RunFromSource
cls
echo Running From Source (Faster)...
echo Python3 is Required. Please Install it if you have not.
cd ..
python main.py
goto askCompileOrRunSource

rem Function to confirm exit
:ConfirmExit
cls
echo Are you sure you want to quit?
echo   1) Yes
echo   2) No
set /p userChoiceExit=Enter 1 or 2: 

if "%userChoiceExit%"=="1" (
    exit
) else if "%userChoiceExit%"=="2" (
    goto askCompileOrRunSource
) else (
    echo Invalid choice. Please enter 1 or 2.
    pause >nul
    goto ConfirmExit
)
