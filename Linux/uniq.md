# 统计重复项

```sh
lsof /dev/sdb1 | awk 'NR>1 {print $1}' | sort | uniq -c | sort -nr
```

- `lsof /dev/sdb1` 命令
- `awk 'NR>1` 跳过首行
- `awk '{print $1}'` 提取第一列
- `sort` 将所有相同命令排列在一起，使 `uniq -c` 能正确统计
- `uniq -c` 统计重复项
- `sort -nr` 按次数倒序排列

## 扩展用法

- `head -n3` 仅显示前三行
