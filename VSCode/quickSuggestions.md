# 代码片段

快速插入一段代码，可以节约很多时间。

## 常用片段

### html

`文件` > `首选项` > `配置用户代码片段` > `html.json`

```json
{
    "Print to console": {
        "prefix": "!", // 快捷键
        "body": [
            "<!DOCTYPE html>",
            "<html lang=\"zh-cmn-Hans\">\n",
            "<head>",
            "\t<meta charset=\"UTF-8\">",
            "\t<meta name=\"viewport\" content=\"width=device-width,initial-scale=1.0,user-scalable=no\">",
            "\t<meta http-equiv=\"X-UA-Compatible\" content=\"ie=edge,chrome=1\">",
            "\t<link rel=\"stylesheet\" href=\"style.css\">",
            "\t<title></title>",
            "</head>\n",
            "<body>",
            "\t<div id=\"app\">\n\t\t$0",
            "\t</div>",
            "</body>",
            "</html>",
        ],
        "description": "常用的 HTML5 模板" // 模板描述
    }
}
```

`$0` 代表退出代码片段，以及最后光标停留的位置。



## 参考文献

- [VS Code 代码片段完全入门指南](https://www.freecodecamp.org/chinese/news/definitive-guide-to-snippets-visual-studio-code/)