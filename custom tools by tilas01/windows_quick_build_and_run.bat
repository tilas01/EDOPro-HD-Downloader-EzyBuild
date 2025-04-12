@echo off
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
title Running built app [/bin/EDOPro-HD-Card-Downloader.exe]...
cd bin
echo EDOPro HD Card Downloader Built! Launching Now! Please Wait...
echo This build can be found and run inside the /bin directory as EDOPRO-HD-Downloader.exe
echo.
ping 127.0.0.1 >nul
ping 127.0.0.1 >nul
title EDOPro HD Card Downloader [EasyBuild]
EDOPro-HD-Downloader.exe