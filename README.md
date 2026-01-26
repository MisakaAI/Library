# 图书馆

“奶奶曾经说过：我的进化速度比光还要快”

这里是一个简单的知识库，在学习新的技能时，用来记一点笔记。

## 目录

同时也是一个技能树。

- [AI](./AI/README.md) 人工智能
  - [PyTorch](./AI/PyTorch/README.md)
  - [Ollama](./AI/LLM/Ollama.md)
- [Blender](./Blender/README.md) 三维建模
- [C#](./C#/README.md) 编程语言
- [C++](./C++/README.md) 编程语言
- [Computer Science](./CS/README.md) 计算机科学
- [Docker](./Docker/README.md) 容器
- [Flutter](./Flutter/README.md) 跨平台应用开发框架
- [Git](./Git/README.md) 版本控制
- [HTML](./HTML/index.html) 网页
- [JavaScript](./JavaScript/README.md) 编程语言
- [Microcontroller](./Microcontroller/README.md) 单片机
- [OPC UA](./OPC%20UA/README.md) 工业通信协议
- [Python3](./Python3/README.md) 编程语言
- [RaspberryPi](./RaspberryPi/README.md) 树莓派
- [Software](./Software/README.md) 软件
- [SQL](./SQL/README.md) 数据库

### 操作系统

- [Windows](./Windows/README.md)
- [Linux](./Linux/README.md)
- [macOS](./macOS/README.md)
- [Android](./Android/README.md) 安卓

## 其他

- [Life](./Life/README.md) 生活指南
- [Other](.//Other/README.md) 其他

## Q&A

Q: 为什么要学编程?  
A: **Just for fun.**

Q: 学会编程能干什么?  
A: 创造一个属于自己的世界。

Q: 我英语/数学不好，能学编程吗?  
A: 肯定是有丰富的数学知识，英语又好的程序员牛逼。  
但是英语/数学不好，并不意味着不能写程序。  
你看，变量名可以用汉语拼音啊，看英文的文档可以用 Google Translate 啊。  
我也因为不会英语，数学不好，被某个在美帝留过学的程序员嘲笑过。  
但是管他呢，我敲代码就是兴趣使然，享受编程带给我的乐趣。  
（更新）现在还可以面向 GPT 编程。

Q: 关于操作系统的选择？  
A: 珍爱生命，远离折腾。

> **Windows**  
9102年了，请使用 *Windows 10*  
2022年了，*Windows11* 就是垃圾，请使用 *Windows 10*  
（更新）2025年了，*Windows11* 也能凑合用一下，但是出于稳定性考虑，依然推荐使用 *Windows 10 LTSC*
\
**Linux**  
入门选一个倾向于稳定的 Linux 发行版即可。(包括但不仅限于 *Ubuntu* / *Debian* / *Fedora* / *OpenSUSE* / *Manjaro*)  
通常情况下，*WSL*（*适用于 Linux 的 Windows 子系统*）也是不错的选择。  
不喜欢用 *RedHat* / *CentOS* 的原因是，官方源里的软件可能是上个世纪的，折腾第三方源又很麻烦，自己编译更麻烦。  
那我为什么不直接用官方源软件版本比较新的发行版呢？（注：与 *CentOS 8* 同时推出的 *CentOS Stream* 在一定程度上解决了该问题。）  
当然，*RedHat* / *CentOS* 仍是优秀的操作系统，且很多 Linux 教程都是以 *CentOS* 为基础进行教学的。  
有一定基础以后就可以根据自己的需求来选择发行版了，比如喜欢折腾的同学可以试试 *Arch Linux* 或者直接 *LFS*。  
但是不要在发行版的选择中浪费太多时间，人生苦短。  
（2024更新）*Debian* / *Ububtu Lts*  
（2025更新）*Linux Mint*  
但就是想体验一下不同的发行版怎么办？请妥善使用虚拟机。
\
**macOS**  
目前主力机：Mac mini (M4 芯片机型) 16GB 统一内存 / 256GB 固态硬盘  
并夕夕只要¥2999，还要什么自行车？  
性价比超高的好吧！！

Q: 与时俱进  
A: 如果你要学一个新的技术，应当从最新的版本开始学。

选择思路应该是：

1. Stable(稳定版)
2. Latest(最新版)

不要相信部分过气教程里，支持 Python 2 的库比 Python 3 要多的鬼话，那种情况只存在于 Python 3 刚问世的时候。  
现在还不支持 Python 3 的库大多是常年无人维护的东西了。（Python 的核心团队计划在 2020 年停止支持 Python 2。）

Q: 关于学习资料  
A: 大部分情况下，能从互联网上找到各种免费的教程。  
(比如 [*w3cschool*](https://www.w3school.com.cn/)、[*菜鸟教程*](https://www.runoob.com/)、[*哔哩哔哩*](https://www.bilibili.com)、[*阿里云大学*](https://edu.aliyun.com) 等。  
京东、当当、亚马逊有活动的时候也买了一些实体书（收藏用）。  
官方文档永远值得信赖，例如：[Python](https://docs.python.org/zh-cn/3/)
同时也请善用 *Google*、*Bing* 等搜索引擎，但是最好屏蔽 *CSDN* -> [uBlacklist](https://chromewebstore.google.com/detail/ublacklist/pncfbmialoiaghdehhbnbhkkgmjanfhe)。  
（2025更新）善用AI，例如：*ChatGPT*、*Grok*、*DeepSeek*

Q: 党争？

- Neovim
- Visual Studio Code
- Tab = 4 Space
- Linux Mint

```c
// C/C++
#include <iostream>
using namespace std;

int main() {
    cout << "Hello World!" << endl;
    return 0;
}
```

```css
/* CSS */
html {
    font-size: 1rem;
}
```

```js
// JavaScript
for ( let i = 0; i < 10; i++) {
    console.log(i)
}
```

```python
# Python3
print("Hello World!")
```
