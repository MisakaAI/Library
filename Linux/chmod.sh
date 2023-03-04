#!/bin/bash

#　.代表当前目录，按需改为需要修改权限的目录。

# 查找目录修改目录权限为755
# find . -type d -exec chmod 755 {} \;
find . -type d | xargs chmod 755

#　查找文件修改文件权限为644
# find . -type f -exec chmod 644 {} \;
find .  -type f | xargs chmod 644