# django-ckeditor

```sh
pip install django-tinymce
```

在 `settings.py` 中进行以下配置

```py
INSTALLED_APPS = [
    ...
    'tinymce',
    ...
]

TINYMCE_DEFAULT_CONFIG = {
    "height": 800,  # 编辑器高度
    "width": 1200,  # 编辑器宽度
    "menubar": False,  # 禁用菜单
    "language": "zh-Hans",  # 设置为中文简体
    # 启用的插件
    "plugins": "anchor link autolink code charmap emoticons fullscreen"
    "help image lists advlist preview table visualblocks visualchars wordcount",
    # 工具栏按钮
    "toolbar": "undo redo | fontsize styles | "
    "bold italic underline |  forecolor backcolor | "
    "table visualblocks visualchars | bullist numlist | "
    "searchreplace  | link image | code preview | fullscreen help",
}
```

## 使用

在你的 `models.py` 中使用 `HTMLField`

```py
from django.db import models
from tinymce.models import HTMLField

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = HTMLField()  # 使用 TinyMCE 的 HTMLField

    def __str__(self):
        return self.title
```

## 配置

### plugins

- [Plugins for TinyMCE](https://www.tiny.cloud/docs/tinymce/latest/plugins/)

1. `anchor`：
    - 允许插入锚点（HTML `<a name="...">`），用于页面内跳转。
1. `link`：
    - 允许插入和编辑超链接，提供链接输入对话框。
1. `autolink`：依赖 `link`
    - 自动将输入的 URL 或邮箱地址转换为超链接。例如，输入 `https://example.com` 会自动变成可点击的链接。
1. `code`：
    - 启用 HTML 源代码编辑功能，点击后弹出窗口允许直接编辑 HTML。
1. `codesample`:
    - 启用代码编辑功能，插入和嵌入语法突出显示的代码段。
1. `charmap`：
    - 添加特殊字符表，允许插入符号（如 ©、∑ 等）。
1. `emoticons`：
    - 支持 emoji。
1. `fullscreen`：
    - 提供全屏模式，将编辑器扩展到整个屏幕。
1. `help`：
    - 添加帮助按钮，提供 TinyMCE 的使用说明或快捷键列表。
1. `insertdatetime`：
    - 允许插入当前日期和时间，支持自定义格式。
1. `importcss`：
    - 从`content_css`配置的CSS文件自动导入CSS样式的功能。
    - `"content_css": "/my-styles.css"`
1. `image`：
    - 启用图片插入功能，支持上传或输入图片 URL。
1. `lists`：
    - 提供基本的有序列表（编号）和无序列表（项目符号）功能。
1. `advlist`：依赖 `lists`
    - 增强列表功能，支持更复杂的编号和项目符号样式（如罗马数字、字母等）。
1. `media`：
    - 启用嵌入媒体功能（如视频、音频），支持插入 `<iframe>` 或 `<video>` 等标签。
1. `nonbreaking`：
    - 用于在当前插入符号位置（光标插入点）插入不间断的空格实体 `&nbsp;`
1. `pagebreak`：
    - 支持分页，允许用户在可编辑区域插入分页。
1. `preview`：
    - 提供预览功能，打开新窗口显示内容渲染效果。
1. `quickbars`:
    - 选择文本时显示，提供格式按钮。
    - 添加新行时显示，提供用于插入对象（如表格和图像）的按钮。
    - 选择图像或图形时显示，提供图像格式按钮，如对齐选项。
1. `searchreplace`：
    - 提供搜索和替换功能，支持在内容中查找和替换文本。
1. `table`：
    - 添加表格功能，支持插入、编辑和格式化表格。
1. `visualblocks`：
    - 显示内容中的 HTML 块元素（如 `<p>`、`<div>`）边框，便于可视化编辑。
1. `visualchars`
    - 在可编辑区域中查看不可见字符
1. `wordcount`：
    - 显示字数统计，通常在编辑器底部显示字符或单词计数。

### toolbar

- [Toolbar Buttons Available for TinyMCE](https://www.tiny.cloud/docs/tinymce/latest/available-toolbar-buttons/)
