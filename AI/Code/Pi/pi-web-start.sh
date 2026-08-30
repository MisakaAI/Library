#!/usr/bin/env bash
set -Eeuo pipefail

ENV_FILE="${PI_WEB_ENV_FILE:-/etc/pi-web/pi-web.env}"

if [[ ! -r "$ENV_FILE" ]]; then
  echo "pi-web-start: cannot read environment file: $ENV_FILE" >&2
  exit 1
fi

# The env file is trusted local configuration and should be chmod 600.
set -a
# shellcheck source=/dev/null
. "$ENV_FILE"
set +a

: "${HTTP_PROXY:?HTTP_PROXY is required}"
: "${HTTPS_PROXY:?HTTPS_PROXY is required}"
: "${PI_WEB_PASSWORD:?PI_WEB_PASSWORD is required}"

# Keep local traffic away from the outbound HTTP proxy.
export NO_PROXY="${NO_PROXY:-localhost,127.0.0.1,::1}"
export no_proxy="${no_proxy:-$NO_PROXY}"
export http_proxy="${http_proxy:-$HTTP_PROXY}"
export https_proxy="${https_proxy:-$HTTPS_PROXY}"

# Security default: Pi Web itself is never exposed on a non-loopback address.
export PI_WEB_HOSTNAME="127.0.0.1"
export PORT="${PORT:-30141}"
export PI_WEB_NO_OPEN=1

# Set PI_WEB_BIN explicitly in pi-web.env when npm was installed through
# nvm/fnm/asdf or another non-system Node.js installation.
if [[ -z "${PI_WEB_BIN:-}" ]]; then
  PI_WEB_BIN="$(command -v pi-web || true)"
fi

if [[ -z "$PI_WEB_BIN" || ! -x "$PI_WEB_BIN" ]]; then
  echo "pi-web-start: pi-web executable not found." >&2
  echo "Set PI_WEB_BIN in $ENV_FILE to the output of: command -v pi-web" >&2
  exit 1
fi

# Important for npm globals installed via nvm/fnm: the pi-web shebang may use
# /usr/bin/env node, so make sure the directory containing node is on PATH.
PI_WEB_BIN_DIR="$(dirname "$PI_WEB_BIN")"
export PATH="$PI_WEB_BIN_DIR:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-}"

exec "$PI_WEB_BIN" \
  --hostname "$PI_WEB_HOSTNAME" \
  --port "$PORT" \
  --no-open
