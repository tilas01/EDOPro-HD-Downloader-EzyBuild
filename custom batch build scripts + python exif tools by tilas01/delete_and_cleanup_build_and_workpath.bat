@echo off

cd..
rmdir /s /q bin
echo Bin directory attempted to be removed...
rmdir /s /q workpath_pyinstaller
echo workpath_pyinstaller attempted to be removed...
echo.
echo Complete.
pause >nul