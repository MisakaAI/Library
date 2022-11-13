# 安装 Git

## Linux

[Download for Linux and Unix](https://git-scm.com/download/linux)

```bash
# Debian / Ubuntu
sudo apt install git

# RHEL / Fedora
sudo dnf install git
```

还有一个合集的包叫 `git-all`，包括了下面几个软件包。

- **git-cvs**：git-cvs 互操作性
- **git-doc**：git 文档
- **git-email**：git 电子邮件 add-on
- **git-gui**：git GUI
- **git-mediawiki**：MediaWiki 远程助手
- **git-svn**：git-svn 互操作性
- **gitk**：git 版本树可视化器
- **gitweb**：git Web 界面

此外，还有两个简单的 git 仓库的服务，非常适合只读更新，即通过网络从 git 仓库拉取。

- **git-daemon-run**：一个简单的 git 仓库的服务器，比 git-daemon-sysvinit 更简单、更可靠，代价是对习惯于 sysvinit 的管理员来说不太熟悉。
- **git-daemon-sysvinit**：一个简单的 git 仓库的服务器，这个包为 git-daemon 提供了通常的 sysvinit 服务管理命令 `service git-daemon start/stop`

## Windows

[Download for Windows](https://git-scm.com/download/win)

下载，然后一直下一步就可以了。

范例：(2.38.1) 64-bit version

Additional icons
附加图标

On the Desktop
桌面上

Windows Explorer integration
Windows 资源管理器集成
    Git Bash Here
    Git GUI Here

Git LFS (Large File Support)
Git LFS（大文件支持）

Associate .git* configuration files with default text editor
将.git*配置文件与默认文本编辑器关联

Associate .sh file to be run with Bash
将.sh文件与Bash关联

Use a TrueType font in all console windows
在所有控制台窗口中使用TrueType字体

Check daily for Git for Windows updates
在Windows更新中每天检查Git更新

Scalar (Git add-on to manage large-scale repositories)
Scalar（用于管理大型存储库的Git插件）

Choosing the default editor used by Git
选择Git使用的默认编辑器

Use Vim (the ubiquitous text editor) as Git's default editor
使用Vim（无处不在的文本编辑器）作为Git的默认编辑器

The vim editor, while powerful, can be hard to use. Its user interface is unintuitive and its key bindings are awkward.
vim编辑器虽然功能强大，但很难使用。它的用户界面不直观，键绑定也很笨拙。

Note: Vim is the default editor of git for windows only for historical reasons, and it is highly recommended to switch to a modern GUI editor instead.
注：由于历史原因，Vim是git for windows的默认编辑器，强烈建议改为现代GUI编辑器。

Note: This will leave the 'core.editor' option unset, which will make Git fall back to the 'EDITOR' environment variable. The default editor is Vim - but you set it to some other editor of your choice.
注：这将使“core.editor”选项未设置，这将使Git返回到“EDITOR”环境变量。默认编辑器是Vim，但您可以将其设置为自己选择的其他编辑器。

Adjusting the name of the initial branch in new repositories
调整新存储库中初始分支的名称

what would you like Git to name the initial branch after "git init"
您希望Git在“git init”之后为初始分支命名什么

Let Git decide
让Git决定

Let Git usr its default branch name (currently:"master") for the initial branch in newly created repositories the Git project intends to change this default to a more inclusive name in the near future.
让Git使用它的默认分支名称（当前：“master”）作为新创建的存储库中的初始分支，Git项目打算在不久的将来将此默认名称更改为更具包容性的名称。

Override the default branch name for new repositories
覆盖新存储库的默认分支名称

NEW! Many teams already renamed their default branches;common choices are "main","trunk" and "development". Specify the name "git init" should use for the initial branch:
新许多团队已经重命名了他们的默认分支；常见的选择是“主要”、“主干”和“发展”。指定初始分支应使用的名称“git init”：

This setting does not affect exsiting repositories.
此设置不会影响现有存储库。

Adjusting your PATH environment
调整PATH环境

How would you like to use Git from the command link?
您希望如何从命令链接使用Git？

Use Git from Git Bash only
仅使用Git Bash中的Git

modified at all.You will only be able to use the Git command line tools from Git Bash.
这是最谨慎的选择，因为您的PATH根本不会被修改。您只能使用Git Bash中的Git命令行工具

Git from the command line and also from 3rd-party software
来自命令行和第三方软件的Git

(Recommended)THis option adds only some minimal Git wrappers to your PATH to avoid duttering your environment with optional Unix tools.
（推荐）此选项仅向您的PATH添加一些最小的Git封装器，以避免使用可选的Unix工具破坏您的环境。

You will be able to use Git from Git Bash, the Command Prompt and the Windows PowerShell as well as any third-party software looking for Git in PATH
您将能够从Git Bash、命令提示符和Windows PowerShell以及任何在PATH中查找Git的第三方软件中使用Git。

Use Git and optional Unix tools from the Command Prompt
从命令提示符使用Git和可选的Unix工具

Both Git and the optional Unix tools will be added to your PATH
Git和可选的Unix工具都将添加到您的PATH中

Warning:This will override Windows Tools like "find" and "stor",Only use this option if you understand the implications.
警告：这将覆盖Windows工具，如“find”和“stor”，只有当您了解其含义时才使用此选项。

Choosing the SSH executable
选择SSH可执行文件

Which Secure Shell client program would you like Git to use?
您希望Git使用哪个安全Shell客户端程序？

Use bundled OpenSSH
使用捆绑的OpenSSH

This uses ssh.exe that comes with Git.
在Git里使用ssh.exe

Use (Tortoise) Plink
使用(Tortoise) Plink

to use PuTTY, specify the path to and existing copy of (Tortoies) Plink.exe
要使用PuTTY，请指定（Tortoies）Plink.exe的路径和现有副本

Set ssh.variant for Tortoise Plink
设置(Tortoise) Plink的ssh.variant

Use external OpenSSH
使用外部OpenSSH

NEW! This uses an external ssh.exe. Git will not install its own OpenSSH (and related) binaries but use them as found on the PATH.
新！使用外部的ssh.exe。Git不会安装自己的OpenSSH（和相关的）二进制文件，而是使用PATH上的二进制文件。

Choosing HTTPS transport backend
选择HTTPS传输后端

Which SSL/TLS library would you like Git to use for HTTPS connections?
您希望Git将哪个SSL/TLS库用于HTTPS连接？

Use the OpenSSH library
使用OpenSSH库

Server certificates will be validated using the ca-bundle.crt file
将使用ca-bundle.crt验证服务器证书文件

Use the native Windows Secure Channel library
使用本机Windows安全通道库

Server certificates will be validated using Windows Certificate Stores.
将使用Windows证书存储验证服务器证书。

This option also allow you to use your company's internal Root CA certificates distributed e.g. via Active Directory Domain Services.
此选项还允许您使用通过Active Directory域服务分发的公司内部根CA证书

Configuring the ending conversions
配置结束转换

How should Git treat line andings in text files?
Git应该如何处理文本文件中的行号？

Checkout Windows-style,commit Unix-style line endings
检出Windows风格，提交Unix风格的行尾

Checkout as-is,commit Unix-style line endings
按原样检出，提交Unix风格的行尾

Checkout as-is,commit as-is
按原样检出，按原样提交

Configuring the terminal emulator to use with Git Bash
配置终端模拟器以与Git Bash一起使用

Which terminal emulator do you want to use with your Git Bash?
您想在GitBash中使用哪个终端仿真器？

Use MinTTY(the defalut terminal of MSYS2)
使用MinTTY（MSYS2的默认终端）

Git Bash will use MinTTY as terminal emulator, which sports a resizable window,non-rectangular selections and a Unicode font. Windows console programs (such as interactive Python)must be launched via `winpty` to work in MinTTY
GitBash将使用MinTTY作为终端模拟器，它支持可调整大小的窗口、非矩形选择和Unicode字体。Windows控制台程序（如交互式Python）必须通过“winpty”启动才能在MinTTY中运行

Use Windows default console window
使用Windows的默认控制台窗口

choose the default behavior of `git pull`
选择“git pull”的默认行为

What shoyld `git pull` do by default?
默认情况下，“git pull”会做什么？

Default(fast-forward or merge)
默认（快进或合并）

This is the standard behavior of `git pull`: fast-forward the current branch to the fetched branch when possible, otherwise create a merge commit.
这是“git pull”的标准行为：在可能的情况下，将当前分支快进到获取的分支，否则创建合并提交。

Rebase
重新定位

Rebasg the current branch onto the fetched branch. If there are no local commits to rebase, this is eqivlent to a fast-forward
将当前分支重新绑定到提取的分支。如果没有本地提交来重新设置基础，这相当于快速前进

Only ever fast-forward
永远快进

Fastward to the fetched branch. Fail if that is not possible.
快到提取的分支。如果不可能，则失败。

Choose a credential helper
选择凭据帮助程序

Which credential helper should be configured?
应该配置哪个凭据助手？

Git Credential Manager
Git凭据管理器

Use the cross-platform Git Credential Manager.
使用跨平台Git凭据管理器。

See mpre information about the future of Git Credential Manger here.
在此处查看有关Git凭证管理器未来的mpre信息。

None
无

Do not use a credential helper.
不要使用凭据帮助程序。

Configuring extra options
配置额外选项

Enable file system caching
启用文件系统缓存

File system data will be read in bulk and cached in memory for certain operations("core.fscache" is set to "true"). This provides a significant performance boost.
对于某些操作，文件系统数据将被批量读取并缓存在内存中（“core.fscache”设置为“true”）。这提供了显著的性能提升。

Enable symbolic links
启用符号链接

Enable symbolic links(requires the SeCreateSymbolicLink permission).
启用符号链接（需要SeCreateSymbolicLink权限）。

Please note that existiong repositories are unaffected by this setting.
请注意，现有存储库不受此设置的影响。

Configuring experimental options
配置实验选项

These features are developed actively. Would you like try them?
这些功能正在积极开发。你想尝尝吗？

Enable experimental support for pseudo consoles.
为伪控制台启用实验支持。

This allows running native console programs like Node or Python in a Git BAsh window without using winpty, but it still know bugs.
这允许在GitBAsh窗口中运行本地控制台程序，如Node或Python，而不使用winpty，但它仍然知道bug。

Enable experimental built-in file system monitor
启用实验性内置文件系统监视器

Automatically run a built-in file system watcher, to speed up common operations such as `git status`,`git add`, `git commit`,etc in worktrees containing many files.
自动运行内置文件系统观察器，以加快包含许多文件的工作树中的常见操作，如“git status”、“git add”、“git commit”等。

## Macos

[Download for macOS](https://git-scm.com/download/mac)

```sh
# Homebrew
brew install git
```
