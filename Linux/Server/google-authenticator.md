# 启用双因素认证(2FA)

## 安装

```sh
apt update
apt install libpam-google-authenticator
```

## 配置

```sh
google-authenticator
```

Do you want authentication tokens to be time-based (y/n)
是否希望身份验证令牌基于时间 (y/n)

Warning: pasting the following URL into your browser exposes the OTP secret to Google:
警告：将以下 URL 粘贴到您的浏览器中会将 OTP 密钥暴露给 Google：

Your new secret key is:
您的新密钥是：

Enter code from app (-1 to skip):
输入应用程序中的代码（-1 跳过）

代码已确认
Code confirmed

您的紧急暂存代码是：
Your emergency scratch codes are:

您是否希望我更新您的“/root/.google_authenticator”文件？(y/n)
Do you want me to update your "/root/.google_authenticator" file? (y/n)

Do you want to disallow multiple uses of the same authentication
token? This restricts you to one login about every 30s, but it increases
your chances to notice or even prevent man-in-the-middle attacks (y/n)
您是否要禁止多次使用同一个身份验证令牌？
这会限制您大约每 30 秒登录一次，但这会增加您注意到甚至阻止中间人攻击的机会 (y/n)

By default, a new token is generated every 30 seconds by the mobile app.
In order to compensate for possible time-skew between the client and the server,
we allow an extra token before and after the current time. This allows for a
time skew of up to 30 seconds between authentication server and client. If you
experience problems with poor time synchronization, you can increase the window
from its default size of 3 permitted codes (one previous code, the current
code, the next code) to 17 permitted codes (the 8 previous codes, the current
code, and the 8 next codes). This will permit for a time skew of up to 4 minutes
between client and server.
Do you want to do so? (y/n)
默认情况下，移动应用程序每 30 秒生成一个新令牌。
为了补偿客户端和服务器之间可能出现的时间偏差，
我们允许在当前时间之前和之后生成一个额外的令牌。
这允许身份验证服务器和客户端之间的时间偏差最多为 30 秒。
如果您遇到时间同步不佳的问题，可以将窗口从默认的 3 个允许代码（一个前一个代码、当前代码、下一个代码）增加到 17 个允许代码（8 个前一个代码、当前代码和 8 个下一个代码）。
这将允许客户端和服务器之间的时间偏差最多为 4 分钟。
你想这样做吗？(y/n)

If the computer that you are logging into isn't hardened against brute-force
login attempts, you can enable rate-limiting for the authentication module.
By default, this limits attackers to no more than 3 login attempts every 30s.
Do you want to enable rate-limiting? (y/n)
如果您登录的计算机没有针对暴力登录尝试进行强化，您可以为身份验证模块启用速率限制。
默认情况下，这会将攻击者的登录尝试次数限制为每 30 秒不超过 3 次。
是否要启用速率限制？(y/n)

### 本地登录

编辑 `/etc/pam.d/login`

```conf
auth required pam_google_authenticator.so
```

### 远程登录

编辑 `/etc/pam.d/sshd`

nullok: 未创建密钥的用户可以正常登录

```conf
# 注释掉 @include common-auth 可以只使用 2FA 登录
auth required pam_google_authenticator.so nullok
```

编辑 `/etc/ssh/sshd_config`

```conf
# ChallengeResponseAuthentication yes
KbdInteractiveAuthentication yes
UsePAM yes
```
