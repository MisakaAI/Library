# UV

一个用 Rust 编写的极速 Python 包和项目管理工具。

## 安装

```sh
# Linux
# curl -LsSf https://astral.sh/uv/install.sh | sh
export ALL_PROXY="socks5://127.0.0.1:7890"
export http_proxy="socks5://127.0.0.1:7890"
export https_proxy="socks5://127.0.0.1:7890"

git config --global http.proxy 'socks5://127.0.0.1:7890'
git config --global https.proxy 'socks5://127.0.0.1:7890'

curl -x http://127.0.0.1:7890 -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## 使用

```sh
# 设置全局默认 Python 版本
uv python default 3.12

# 查看可用的 Python 版本
uv python list
uv python list 3.14

# 安装 Python 版本
uv python install 3.14.0

# 初始化
uv init example-app

# 添加依赖项
uv add httpx

# 删除依赖项
uv remove httpx

# 在项目中运行命令
uv run python -c "import example"

# 锁文件
# 锁文件会自动创建，但也可以手动创建或更新锁文件
uv lock

# 同步环境
# 环境会自动同步，但也可以手动同步：
uv sync
```

## 配置文件

系统级 `/etc/uv/uv.toml`
用户级 `~/.config/uv/uv.toml`
项目级 `./pyproject.toml`

项目级配置优先于用户级配置，用户级配置优先于系统级配置。

```uv.toml
[[index]]
url = "https://test.pypi.org/simple"
default = true
```

```pyproject.toml
[[tool.uv.index]]
url = "https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple/"
default = true
```

## 范例

项目级配置

```pyproject.toml
[project]
name = "example-app"
version = "0.1.0"
description = "Example APP"
readme = "README.md"
requires-python = ">=3.13"
dependencies = [
    "ruff>=0.14.6",
    "fastapi>=0.121.3",
    "psycopg[binary]>=3.2.13",
    "uvicorn[standard]>=0.38.0",
]

[[tool.uv.index]]
url = "https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple/"
default = true

[tool.ruff]
line-length = 120
target-version = "py313"
exclude = [".git", ".venv", "node_modules", "build", "dist", "__pycache__"]

[tool.ruff.format]
quote-style = "double"
indent-style = "space"
skip-magic-trailing-comma = false
line-ending = "lf"

[tool.ruff.lint]
select = ["E", "F", "I", "UP",]
ignore = ["E501"]
```
