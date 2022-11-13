# OpenSSH 密钥管理

[密钥管理](https://learn.microsoft.com/zh-cn/windows-server/administration/openssh/openssh_keymanagement)

## 主机密钥生成

```PowerShell
# Set the sshd service to be started automatically
Get-Service -Name sshd | Set-Service -StartupType Automatic

# Now start the sshd service
Start-Service sshd
```

## 用户密钥生成

若要使用基于密钥的身份验证，首先需要为客户端生成公钥/私钥对。 ssh-keygen.exe 用于生成密钥文件，并且可以指定算法 DSA、RSA、ECDSA 或 Ed25519。 如果未指定算法，则使用 RSA。 应使用强算法和密钥长度，例如此示例中的 Ed25519。

若要使用 Ed25519 算法生成密钥文件，请从客户端上的 PowerShell 或 cmd 提示符运行以下命令

```PowerShell
ssh-keygen -t ed25519
```

请记住，私钥文件等效于密码，应当采用与保护密码相同的方式来保护它。 为了实现此目的，请使用 ssh-agent 来将私钥安全地存储在与你的 Windows 登录关联的 Windows 安全上下文中。 为执行该操作，请以管理员身份启动 ssh-agent 服务并使用 ssh-add 来存储私钥。

```PowerShell
# By default the ssh-agent service is disabled. Allow it to be manually started for the next step to work.
# Make sure you're running as an Administrator.
Get-Service ssh-agent | Set-Service -StartupType Manual

# Start the service
Start-Service ssh-agent

# This should return a status of Running
Get-Service ssh-agent

# Now load your key files into ssh-agent
ssh-add ~\.ssh\id_ed25519
```

## 部署公钥

若要使用上面创建的用户密钥，需要将公钥 (~\.ssh\id_ed25519.pub) 的内容放置在服务器上的一个文本文件中，其名称和位置取决于用户帐户是本地管理员组的成员还是标准用户帐户。

### 标准用户

公钥 (~\.ssh\id_ed25519.pub) 的内容需放置在服务器上的一个名为 authorized_keys 的文本文件中，该文件位于 C:\Users\username\.ssh\。 OpenSSH 客户端包括了 scp 来帮助实现此目的，这是一个安全的文件传输实用工具。

以下示例将公钥复制到服务器（其中“username”替换为你的用户名）。 最初，对于服务器，需要使用用户帐户的密码。

```PowerShell
# Make sure that the .ssh directory exists in your server's user account home folder
ssh username@domain1@contoso.com mkdir C:\Users\username\.ssh\

# Use scp to copy the public key file generated previously on your client to the authorized_keys file on your server
scp C:\Users\username\.ssh\id_ed25519.pub user1@domain1@contoso.com:C:\Users\username\.ssh\authorized_keys
```

### 管理用户

公钥 (~\.ssh\id_ed25519.pub) 的内容需放置在服务器上的一个名为 administrators_authorized_keys 的文本文件中，该文件位于 \。 OpenSSH 客户端包括了 scp 来帮助实现此目的，这是一个安全的文件传输实用工具。 此文件上的 ACL 需要配置为仅允许访问管理员和系统。

以下示例将公钥复制到服务器并配置 ACL（其中“username”替换为你的用户名）。 最初，对于服务器，需要使用用户帐户的密码。

> 此示例演示了创建 administrators_authorized_keys file 的步骤。 如果多次运行，则每次都会覆盖此文件。 若要为多个管理用户添加公钥，需将此文件附加到每个公钥。

```PowerShell
# Make sure that the .ssh directory exists in your server's user account home folder
ssh user1@domain1@contoso.com mkdir C:\ProgramData\ssh\

# Use scp to copy the public key file generated previously on your client to the authorized_keys file on your server
scp C:\Users\username\.ssh\id_ed25519.pub user1@domain1@contoso.com:C:\ProgramData\ssh\administrators_authorized_keys

# Appropriately ACL the authorized_keys file on your server
ssh --% user1@domain1@contoso.com icacls.exe "C:\ProgramData\ssh\administrators_authorized_keys" /inheritance:r /grant "Administrators:F" /grant "SYSTEM:F"ssh-add ~\.ssh\id_ed25519
```

这些步骤完成了对 Windows 上的 OpenSSH 使用基于密钥的身份验证所需的配置。 完成此项后，用户可以从具有私钥的任何客户端连接到 sshd 主机。
