@echo off
setlocal

REM llama.cpp Windows Server：Ryzen 9 7945HS / RTX 4060 Laptop / 64GB RAM / Qwen3.8-27B Q4_K_M。
set "LLAMA_DIR=%~dp0"
set "MODEL=%~dp0Qwen3.8-27B-ABLITERATED-Q4_K_M.gguf"

REM HOST：127.0.0.1 仅本机；0.0.0.0 允许局域网访问（需配置 --api-key，勿暴露公网）。PORT 冲突时可改为 8081/8088/18080。
set "HOST=127.0.0.1"
set "PORT=8080"

REM CTX：8192 为当前配置的推荐起点；资源紧张改 4096，长文可改 16384/32768；0 使用模型原生最大值。
set "CTX=8192"

REM GPU_LAYERS：8GB 显存运行 27B Q4 建议从 20/24 起步并保留 0.5-1.5GB；显存不足时降低；0 纯 CPU，all 尽可能全放 GPU。
set "GPU_LAYERS=24"

REM THREADS：生成线程，7945HS 建议 16，可测试 12/20/24，线程越多不一定越快。
set "THREADS=16"

REM THREADS_BATCH：Prompt/Batch 阶段线程，通常可高于 THREADS；当前 24，温度或卡顿时降至 20/16。
set "THREADS_BATCH=24"

REM FLASH_ATTN：auto 为推荐值，也可测试 on/off。
set "FLASH_ATTN=auto"

REM PARALLEL：并发 slot，单用户设 1，多客户端可设 2；8GB 显存不建议一开始设为 4 或更高。
set "PARALLEL=1"

echo.
echo ===== llama.cpp Server =====
echo Model         : %MODEL%
echo Host          : %HOST%
echo Port          : %PORT%
echo Context       : %CTX%
echo GPU Layers    : %GPU_LAYERS%
echo CPU Threads   : %THREADS%
echo Batch Threads : %THREADS_BATCH%
echo Flash Attn    : %FLASH_ATTN%
echo Parallel      : %PARALLEL%
echo =============================
echo.

cd /d "%LLAMA_DIR%"
if errorlevel 1 (
    echo [ERROR] Cannot enter directory: %LLAMA_DIR%
    pause
    exit /b 1
)

if not exist "%MODEL%" (
    echo [ERROR] Model file not found: %MODEL%
    pause
    exit /b 1
)

REM Web UI：http://127.0.0.1:8080；OpenAI API：http://127.0.0.1:8080/v1/chat/completions；局域网访问时请将 HOST 改为 0.0.0.0 并配置 --api-key。
llama.exe serve -m "%MODEL%" -c %CTX% -ngl %GPU_LAYERS% -t %THREADS% -tb %THREADS_BATCH% -fa %FLASH_ATTN% -np %PARALLEL% --host %HOST% --port %PORT%

echo.
echo ===== llama.cpp server stopped. =====
pause
endlocal
