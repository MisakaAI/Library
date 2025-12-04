@echo off
REM ==========================
REM MicroPython ampy 文件上传
REM ==========================

REM --- 配置区 ---
set "AMPY_PORT=COM3"      REM ESP32 端口 (例如: COM3, COM4 等)
set "LOCAL_DIR=dist"      REM 要上传的本地目录名
set "REMOTE_ROOT=/"       REM 文件上传到板卡上的目标目录 (例如: /, /lib)
REM ----------------

REM 检查 ampy 命令是否存在
where ampy >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo 错误：找不到 ampy 命令。请确保 ampy 已安装并配置在系统 PATH 中。
    pause
    goto :eof
)

echo.
echo --- ampy 文件上传开始 ---
echo 本地目录: %LOCAL_DIR%
echo 目标端口: %AMPY_PORT%
echo 板卡目标路径: %REMOTE_ROOT%
echo --------------------------
echo.

REM 检查本地目录是否存在
if not exist "%LOCAL_DIR%" (
    echo 错误：本地目录 '%LOCAL_DIR%' 不存在！
    pause
    goto :eof
)

REM 确保 REMOTE_ROOT 格式正确 (如果不是 /，则确保末尾有 /)
if not "%REMOTE_ROOT%"=="\" if not "%REMOTE_ROOT:~-1%"=="/" (
    set "REMOTE_ROOT=%REMOTE_ROOT%/"
)

REM 使用 FOR 循环遍历 LOCAL_DIR 目录下的所有文件
REM %%f 是文件名变量
for %%f in ("%LOCAL_DIR%\*") do (
    REM 检查是否是文件 (跳过目录)
    if exist "%%f" (
        REM 获取文件名 (例如: dist\main.py -> main.py)
        set "local_file=%%f"

        REM %%~nxf 提取文件名和扩展名
        set "filename=%%~nxf"

        REM 完整的目标路径
        set "remote_file=%REMOTE_ROOT%%%~nxf"

        REM 延迟扩展，用于在循环内部使用 set 的变量
        call :UPLOAD_FILE
    )
)

echo.
echo --- 所有文件上传完成！ ---
pause
goto :eof


REM 子程序: 执行文件上传
:UPLOAD_FILE
    echo 上传文件: %local_file% -> %remote_file%

    REM 执行 ampy put 命令上传文件
    ampy -p "%AMPY_PORT%" put "%local_file%" "%remote_file%"

    if %ERRORLEVEL% neq 0 (
        echo 错误：文件上传失败：%local_file%。请检查端口或连接。
        pause
        exit /b %ERRORLEVEL%
    )
    goto :eof