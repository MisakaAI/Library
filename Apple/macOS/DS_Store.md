# .DS_Store

删除烦人的 .DS_Store 文件

## .gitignore

```.gitignore
# Windows
[Dd]esktop.ini
Thumbs.db
$RECYCLE.BIN/

# macOS
.DS_Store
.fseventsd
.Spotlight-V100
.TemporaryItems
.Trashes
```

## 查找 & 删除

当前目录

```sh
# 查找
find . -name "*.DS_Store" -type f -print
# 删除
find . -name "*.DS_Store" -type f -delete
```
