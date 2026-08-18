cat > "$HOME/.latexmkrc" <<'EOF'
# 使用 XeLaTeX
$xelatex = 'xelatex -shell-escape %O %S';

# 默认使用 XeLaTeX
$pdf_mode = 5;

# 编译成功后自动清理中间文件
$cleanup_includes_cusdep_generated = 1;
$clean_ext .= ' %R.run.xml %R.bbl %R.bcf';
EOF