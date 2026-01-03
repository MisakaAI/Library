# Claude Code

## 安装

```sh
npm install -g @anthropic-ai/claude-code
claude --version

# zsh
echo 'export ANTHROPIC_AUTH_TOKEN="API Key"' >> ~/.zshrc
echo 'export ANTHROPIC_MODEL="claude-opus-4-5-20251101"' >> ~/.zshrc
```

## 配置

### settings.json

创建 `~/.claude/settings.json` 文件

```json
{
  "env": {
    "ANTHROPIC_AUTH_TOKEN": "API Key",
    "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": 1
  },
  "permissions": {
    "allow": [],
    "deny": []
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
