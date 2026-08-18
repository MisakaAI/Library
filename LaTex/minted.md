# LaTeX 代码高亮

## 依赖

```sh
# 代码高亮
apt install python3-pygments
python3 -m pip install --user --break-system-packages latexminted
```

## 范例

- [minted](Example/minted.tex)

## 编译

```sh
latexmk minted.tex
```
