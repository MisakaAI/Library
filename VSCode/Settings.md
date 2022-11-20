# Settings 设置

```json
{
    "workbench.iconTheme": "vscode-icons",
    "workbench.colorTheme": "One Dark Pro",
    "editor.fontSize": 22,
    "editor.fontFamily": "'Source Code Pro','Inconsolata','思源黑体 Light'",
    "editor.fontLigatures": true,
    "terminal.integrated.fontSize": 22,
    "terminal.integrated.fontFamily": "'Source Code Pro','Inconsolata','思源黑体 Light'",
    "workbench.startupEditor": "newUntitledFile",
    "vsicons.dontShowNewVersionMessage": true,
    "editor.minimap.enabled": false,
    "breadcrumbs.enabled": false,
    "files.eol": "\n",
    "[markdown]": {
        "editor.wordWrap": "off"
    },
    "security.workspace.trust.enabled": false,
    "terminal.integrated.profiles.windows": {
        "PowerShell": {
            "source": "PowerShell",
            "icon": "terminal-powershell"
        },
        "Command Prompt": {
            "path": [
                "${env:windir}\\Sysnative\\cmd.exe",
                "${env:windir}\\System32\\cmd.exe"
            ],
            "args": [],
            "icon": "terminal-cmd"
        },
        "Git Bash": {
            "source": "Git Bash"
        },
        "Ubuntu (WSL)": {
            "path": "C:\\Windows\\System32\\wsl.exe",
            "args": [
                "-d",
                "Ubuntu"
            ]
        }
    },
    "terminal.integrated.defaultProfile.windows": "Ubuntu (WSL)",
}
```