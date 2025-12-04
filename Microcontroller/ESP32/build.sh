#!/bin/bash
source .esp32/bin/activate

# 清空 dist 目录
if [ -d "dist" ]; then
    echo "Clearing dist directory..."
    rm -rf dist
fi
mkdir -p dist

# 检测 mpy-cross 是否安装
mpy-cross --version
if [ $? -ne 0 ]; then
    echo "mpy-cross not found, installing..."
    pip install -q mpy-cross
else
    echo "mpy-cross is installed"
fi

# 检测 html-minifier-terser 是否安装
html-minifier-terser --version
if [ $? -ne 0 ]; then
    echo "html-minifier-terser not found, installing..."
    npm install -g html-minifier-terser
else
    echo "html-minifier-terser is installed"
fi

# 编译并直接输出到 dist 目录
for f in src/*.py; do
    if [ -f "$f" ]; then
        echo "Compiling $f"
        mpy-cross -O3 "$f" -o "dist/$(basename "$f" .py).mpy"
    fi
done

# 压缩 HTML
echo "Compressing src/index.html"
html-minifier-terser src/index.html -o dist/index.html \
--collapse-whitespace \
--remove-comments \
--remove-optional-tags \
--remove-redundant-attributes \
--remove-script-type-attributes \
--remove-style-link-type-attributes \
--minify-css true \
--minify-js true

# 删除编译出的 boot.mpy
if [ -f "dist/boot.mpy" ]; then
    echo "Removing dist/boot.mpy (keeping boot.py uncompiled)"
    rm dist/boot.mpy
fi

# 复制 boot.py 到 dist
if [ -f "src/boot.py" ]; then
    echo "Copying src/boot.py to dist/"
    cp src/boot.py dist/boot.py
fi

echo "Build completed successfully!"
