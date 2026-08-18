# 完整安装（约 7~8 GB）
# apt install texlive-full

# 基础 LaTeX
apt install texlive

# 中文支持（ctex、中文字体等）
apt install texlive-lang-chinese

# XeLaTeX（编译）
apt install texlive-xetex

# latexmk（自动编译）
apt install latexmk

# latexindent（代码格式化）
apt-get install texlive-extra-utils

# 参考文献（biblatex 推荐）
apt install biber

# 字体（推荐）
apt install fonts-lmodern fonts-noto fonts-noto-cjk

# 代码高亮
apt install python3-pygments
python3 -m pip install --user --break-system-packages latexminted
