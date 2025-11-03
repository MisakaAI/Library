# PyInstaller auto build for PowerShell

param(
    [string]$ScriptName = "main.py",
    [string]$AppName = "main",
    [string]$IconFile = "",
    [switch]$OneFile = $false
)

# 设置控制台编码为 UTF-8
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$OutputEncoding = [System.Text.Encoding]::UTF8

# 设置标题
$Host.UI.RawUI.WindowTitle = "打包工具 - $AppName"

Write-Host "=== PyInstaller 打包工具 ===" -ForegroundColor Cyan
Write-Host "应用程序: $AppName" -ForegroundColor Yellow
Write-Host "主脚本: $ScriptName" -ForegroundColor Yellow
if ($IconFile -ne "") {
    Write-Host "图标文件: $IconFile" -ForegroundColor Yellow
}
Write-Host "时间: $(Get-Date)" -ForegroundColor Gray
Write-Host ""

# 检测 pyinstaller 是否可用
if (-not (Get-Command pyinstaller -ErrorAction SilentlyContinue)) {
    Write-Host "错误: 未找到 PyInstaller，请确认已安装 (pip install pyinstaller)" -ForegroundColor Red
    pause
    exit 1
}

# 检查主脚本是否存在
if (-not (Test-Path $ScriptName)) {
    Write-Host "错误: 找不到文件 '$ScriptName'" -ForegroundColor Red
    pause
    exit 1
}

# 检查图标文件是否存在（如果指定了）
if ($IconFile -ne "" -and -not (Test-Path $IconFile)) {
    Write-Host "警告: 找不到图标文件 '$IconFile'，将不使用图标" -ForegroundColor Yellow
    $IconFile = ""
}

# 构建 PyInstaller 命令
$PyInstallerArgs = @(
    "--windowed",
    "--clean",
    "--noconfirm",
    "--name=$AppName"
)

# 添加图标参数（如果指定了且文件存在）
if ($IconFile -ne "") {
    $PyInstallerArgs += "--icon=$IconFile"
}

if ($OneFile) {
    $PyInstallerArgs += "--onefile"
    Write-Host "模式: 单文件模式" -ForegroundColor Green
} else {
    Write-Host "模式: 目录模式" -ForegroundColor Green
}

$PyInstallerArgs += $ScriptName

Write-Host "开始打包过程..." -ForegroundColor Green
Write-Host "命令: pyinstaller $($PyInstallerArgs -join ' ')" -ForegroundColor Gray

# 执行打包命令
try {
    $process = Start-Process -FilePath "pyinstaller" -ArgumentList $PyInstallerArgs -Wait -PassThru -NoNewWindow

    if ($process.ExitCode -eq 0) {
        Write-Host "`n打包成功完成!" -ForegroundColor Green
        Write-Host "输出目录: .\dist\$AppName\" -ForegroundColor Yellow

        # 显示生成的文件
        if (Test-Path ".\dist\$AppName") {
            Write-Host "`n生成的文件:" -ForegroundColor Cyan
            Get-ChildItem ".\dist\$AppName" | ForEach-Object {
                Write-Host "  - $($_.Name)" -ForegroundColor White
            }
        }

        # ===== 复制模型文件到输出目录 =====
        Write-Host "`n正在复制模型文件..." -ForegroundColor Cyan

        # 设置输出目录
        $outputDir = Join-Path "dist" $AppName

        # 确保输出目录存在
        if (-not (Test-Path $outputDir)) {
            Write-Host "    创建输出目录: $outputDir" -ForegroundColor Yellow
            New-Item -ItemType Directory -Path $outputDir -Force | Out-Null
        }

        # 查找所有 .pt 和 .pth 文件
        Write-Host "    搜索模型文件..." -ForegroundColor Gray
        $modelFiles = @()

        $ptFiles = Get-ChildItem -Path "." -Filter "*.pt" -File
        $pthFiles = Get-ChildItem -Path "." -Filter "*.pth" -File

        if ($ptFiles) { $modelFiles += $ptFiles }
        if ($pthFiles) { $modelFiles += $pthFiles }

        if ($modelFiles.Count -gt 0) {
            foreach ($file in $modelFiles) {
                # 复制文件到输出目录
                $targetPath = Join-Path $outputDir $file.Name
                Copy-Item $file.FullName $targetPath -Force
                Write-Host "    复制: $($file.Name)" -ForegroundColor Green
            }
            Write-Host "    成功复制 $($modelFiles.Count) 个模型文件到输出目录" -ForegroundColor Green
        } else {
            Write-Host "    未找到任何 .pt 或 .pth 文件" -ForegroundColor Yellow
        }
        # ===== 复制完成 =====


        # ===== 使用 7-Zip 打包输出目录 =====
        Write-Host "`n正在使用 7-Zip 打包输出目录..." -ForegroundColor Cyan

        # 指定 7-Zip 路径
        $sevenZipExe = "C:\Program Files\7-Zip\7z.exe"

        if (-not (Test-Path $sevenZipExe)) {
            Write-Host "错误: 找不到 7-Zip，请确认已安装 7-Zip" -ForegroundColor Red
        } else {
            # 创建压缩文件名
            $zipFileName = "$AppName-$(Get-Date -Format 'yyyyMMdd-HHmmss').7z"
            $zipFilePath = Join-Path "dist" $zipFileName

            # 使用 7-Zip 压缩目录（最高压缩率）
            Write-Host "创建压缩文件: $zipFilePath" -ForegroundColor Gray

            # 切换到 dist\$AppName 目录
            Push-Location "dist\$AppName"

            # 直接使用命令行语法
            $command = "& '$sevenZipExe' a -t7z -r -mx=5 -y '..\$zipFileName' *"
            Write-Host "执行命令: $command" -ForegroundColor Gray

            try {
                Invoke-Expression $command

                if ($LASTEXITCODE -eq 0) {
                    Write-Host "    成功创建压缩文件: $zipFileName" -ForegroundColor Green
                    # 显示压缩文件信息
                    $zipFile = Get-Item $zipFilePath -ErrorAction SilentlyContinue
                    if ($zipFile) {
                        $sizeInMB = [math]::Round($zipFile.Length / 1MB, 2)
                        Write-Host "文件大小: $sizeInMB MB" -ForegroundColor Gray
                    }
                } else {
                    Write-Host "    创建压缩文件失败，错误代码: $LASTEXITCODE" -ForegroundColor Red
                }
            }
            catch {
                Write-Host "    执行 7-Zip 时出错: $($_.Exception.Message)" -ForegroundColor Red
            }
            finally {
                Pop-Location
            }
        }
        # ===== 7-Zip 打包完成 =====

    } else {
        Write-Host "`n打包失败，错误代码: $($process.ExitCode)" -ForegroundColor Red
    }
}
catch {
    Write-Host "`n执行错误: $($_.Exception.Message)" -ForegroundColor Red
}

# 完成提示
Write-Host "`n操作完成。" -ForegroundColor Cyan

pause

# 打包结束后自动打开输出目录
if (Test-Path "dist") {
    Start-Process explorer.exe "dist"
}
