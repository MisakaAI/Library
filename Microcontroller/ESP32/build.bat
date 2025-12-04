@echo off
REM 激活 Python 虚拟环境
call .esp32\Scripts\activate.bat

REM 清空 dist 目录
if exist dist (
    echo Clearing dist directory...
    rmdir /s /q dist
)
mkdir dist

REM 检测 mpy-cross 是否安装
mpy-cross --version >nul 2>&1
if errorlevel 1 (
    echo mpy-cross not found, installing...
    pip install -q mpy-cross
) else (
    echo mpy-cross is installed
)

REM 检测 html-minifier-terser 是否安装
html-minifier-terser --version >nul 2>&1
if errorlevel 1 (
    echo html-minifier-terser not found, installing...
    npm install -g html-minifier-terser
) else (
    echo html-minifier-terser is installed
)

REM 编译 Python 文件
for %%f in (src\*.py) do (
    if exist "%%f" (
        echo Compiling %%f ...
        mpy-cross "%%f" -o "dist\%%~nf.mpy"
    )
)

REM 压缩 HTML
echo Compressing HTML...
html-minifier-terser src\index.html -o dist\index.html ^
--collapse-whitespace ^
--remove-comments ^
--remove-optional-tags ^
--remove-redundant-attributes ^
--remove-script-type-attributes ^
--remove-style-link-type-attributes ^
--minify-css true ^
--minify-js true

REM 删除 dist\boot.mpy
if exist dist\boot.mpy (
    echo Removing dist\boot.mpy
    del /f /q dist\boot.mpy
)

REM 复制 boot.py
if exist src\boot.py (
    echo Copying src\boot.py to dist\
    copy /y src\boot.py dist\boot.py >nul
)

echo Build completed successfully!
pause
