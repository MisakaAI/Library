# CodeX

## Install

```sh
# Install using npm
npm install -g @openai/codex
```

## Proxy

```sh
mkdir ~/.codex
touch ~/.codex/.env
echo -e 'HTTP_PROXY="http://127.0.0.1:7890"\nHTTPS_PROXY="http://127.0.0.1:7890"' > .codex/.env
```
