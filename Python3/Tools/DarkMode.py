# 通用
# https://pypi.org/project/darkdetect/

# windows
import winreg

def get_windows_theme():
    try:
        # 打开注册表路径
        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize",
        )

        # 读取AppsUseLightTheme值，它决定了应用程序的主题是深色还是浅色
        # 0表示深色主题，1表示浅色主题
        theme_value = winreg.QueryValueEx(key, "AppsUseLightTheme")[0]
        winreg.CloseKey(key)

        if theme_value == 0:
            return "深色主题"
        else:
            return "浅色主题"
    except FileNotFoundError:
        return "无法获取主题信息"


theme = get_windows_theme()
print(theme)

# MAC
"""
from os import system

command = 'theme=$(defaults read -g AppleInterfaceStyle) && if [[ $theme == "Dark" ]]; then python3 -c "from color import ifdark; ifdark()"; else python3 -c "from color import iflight; iflight()"; fi'
theme = system(command)
"""

# Gnome
"""
import subprocess

def detectDarkModeGnome():
    getArgs = ["gsettings", "get", "org.gnome.desktop.interface", "gtk-theme"]

    currentTheme = (
        subprocess.run(getArgs, capture_output=True)
        .stdout.decode("utf-8")
        .strip()
        .strip("'")
    )

    darkIndicator = "-dark"
    if currentTheme.endswith(darkIndicator):
        return True
    return False
"""

# Kde-Plasma
"""
app = QApplication(sys.argv)
decide_theme(app.palette().base().color())

def decide_theme(color: QColor) -> None:
    theme: str = ""
    r, g, b, a = color.getRgb()
    hsp = math.sqrt((0.241 * r * r) + (0.691 * g * g) + (0.068 * b * b))
    if hsp > 127.5:
        theme = "light"
    else:
        theme = "dark"
"""
