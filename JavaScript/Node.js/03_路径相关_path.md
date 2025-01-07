# 路径

## 当前文件所在目录

`__dirname` 

```node
console.log(__dirname)
```

## path 模块

使用 path 模块处理路径。

```node
var path = require("path")

// 格式化路径
path.normalize(path)

// 连接路径
path.join([path1][, path2][, ...])

// 将 to 参数解析为绝对路径
path.resolve([from ...], to)

// 是否为绝对路径
path.isAbsolute(path)

// 将绝对路径转为相对路径，返回从 from 到 to 的相对路径
path.relative(from, to)

// 返回路径中代表文件夹的部分，同 Unix 的dirname 命令类似
path.dirname(path)

// 返回路径中的最后一部分。同 Unix 命令 bashname 类似。
path.basename(path[, ext])

// 返回路径中文件的后缀名
path.extname(path)

// 返回路径字符串的对象
path.parse(pathString)

// 从对象中返回路径字符串，和 path.parse 相反
path.format(pathObject)
```

### 属性


属性|描述
-|-
path.sep | 平台的文件路径分隔符，'\\' 或 '/'。
path.delimiter | 平台的分隔符, ';' or ':'
path.posix | 提供上述 path 的方法，不过总是以 posix 兼容的方式交互。
path.win32 | 提供上述 path 的方法，不过总是以 win32 兼容的方式交互。

