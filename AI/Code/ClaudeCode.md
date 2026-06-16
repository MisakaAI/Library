# Claude Code

## 安装

```sh
curl -fsSL https://claude.ai/install.sh | bash
claude --version

# npm
npm install -g @anthropic-ai/claude-code

# zsh
echo 'export ANTHROPIC_AUTH_TOKEN="API Key"' >> ~/.zshrc
echo 'export ANTHROPIC_MODEL="claude-opus-4-5-20251101"' >> ~/.zshrc
```

## 配置

### settings.json

创建 `~/.claude/settings.json` 文件

#### 智谱 GLM

```json
{
  "env": {
    "ANTHROPIC_AUTH_TOKEN": "<API Key>",
    "ANTHROPIC_BASE_URL": "https://open.bigmodel.cn/api/anthropic",
    "API_TIMEOUT_MS": "3000000",
    "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": 1,
    "CLAUDE_CODE_AUTO_COMPACT_WINDOW": "1000000",
    "CLAUDE_CODE_EFFORT_LEVEL": "max",
    "ANTHROPIC_DEFAULT_OPUS_MODEL": "glm-5.2[1m]",
    "ANTHROPIC_DEFAULT_SONNET_MODEL": "glm-5.2[1m]",
    "ANTHROPIC_DEFAULT_HAIKU_MODEL": "glm-4.7"
  }
}
```

#### DeepSeek

```json
{
  "env": {
    "ANTHROPIC_AUTH_TOKEN": "<API Key>",
    "ANTHROPIC_BASE_URL": "https://api.deepseek.com/anthropic",
    "API_TIMEOUT_MS": "3000000",
    "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": 1,
    "CLAUDE_CODE_AUTO_COMPACT_WINDOW": "1000000",
    "ANTHROPIC_MODEL": "deepseek-v4-pro[1m]",
    "ANTHROPIC_DEFAULT_OPUS_MODEL": "deepseek-v4-pro[1m]",
    "ANTHROPIC_DEFAULT_SONNET_MODEL": "deepseek-v4-pro[1m]",
    "ANTHROPIC_DEFAULT_HAIKU_MODEL": "deepseek-v4-flash",
    "CLAUDE_CODE_SUBAGENT_MODEL": "deepseek-v4-flash",
  }
}
```

vscode 中插件使用，创建文件 `~/.claude/config.json`

```json
{
    "primaryApiKey": "fox"
}
```

### 验证方法

```sh
# macOS/Linux
echo $ANTHROPIC_BASE_URL
echo $ANTHROPIC_AUTH_TOKEN

# Windows PowerShell
echo $env:ANTHROPIC_BASE_URL
echo $env:ANTHROPIC_AUTH_TOKEN

# Windows CMD
echo %ANTHROPIC_BASE_URL%
echo %ANTHROPIC_AUTH_TOKEN%
```

## 命令

命令|说明
-|-
`/btw <question>` | 提出快速附加问题，无需添加到对话中
`/clear` | 使用空上下文启动新对话。
`/code-review [low\|medium\|high\|xhigh\|max]` | 审阅当前差异以查找正确性错误以及重用、简化和效率清理。
`/review` | 在当前会话中本地审阅 pull request。
`/security-review` | 分析当前分支上的待处理更改以查找安全漏洞。
`/export [filename]` | 将当前对话导出为纯文本。
`/goal [condition\|clear]` | 设置一个目标：Claude 在多个轮次中继续工作，直到满足条件。
`/init` | 使用 CLAUDE.md 指南初始化项目。
`/plugin` | 管理 Claude Code plugins
`/verify` | 通过构建您的项目应用、运行它并观察结果来确认代码更改是否按预期工作，而不是依赖测试或类型检查。
`/status` | 打开设置界面（状态选项卡），显示版本、模型、账户和连接性。
`/usage` | 显示会话成本、计划使用限制和活动统计。
`/skills` | 列出可用的 skills。

级别|何时使用
-|-
low|保留用于短期、范围有限、延迟敏感且不需要高智能的任务
medium|减少成本敏感工作的令牌使用，可以权衡一些智能
high|平衡令牌使用和智能。Opus 4.8、Opus 4.6 和 Sonnet 4.6 上的默认值
xhigh|更深入的推理，令牌支出更高。Opus 4.7 上的默认值
max|可以改进困难任务的性能，但可能显示收益递减，容易过度思考。在广泛采用前进行测试
ultracode|一个 Claude Code 设置，为每个实质性任务规划一个动态工作流，每条消息进行 xhigh 推理。仅限会话

## 交互
快捷键|描述
-|-
`Ctrl+C` | 中断，或清除输入
`Ctrl+D` | 退出 Claude Code 会话
`Ctrl+L` | 重绘屏幕
`Esc` | 断 Claude

## 权限模式

模式|无需询问即可运行的操作|最适合
-|-|-
default|仅读取|入门、敏感工作
acceptEdits|读取、文件编辑和常见文件系统命令（mkdir、touch、mv、cp 等）|迭代您正在审查的代码
plan|仅读取|在更改代码库前进行探索
auto|所有操作，带后台安全检查|长时间任务、减少提示疲劳
dontAsk|仅预先批准的工具|锁定的 CI 和脚本
bypassPermissions|所有操作，带后台安全检查|仅隔离容器和 VM
