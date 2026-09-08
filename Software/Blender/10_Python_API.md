# Blender Python API

用 Python 程序控制 Blender 的场景、建模、材质、动画、渲染和文件处理能力。

- [官方文档](https://docs.blender.org/api/current/index.html)

## Blender Python API 主要能做什么

最核心的模块是：

```python
import bpy
```

可以把常用 API 粗略理解成下面几层：

| API           | 作用              | 示例                         |
| ------------- | --------------- | -------------------------- |
| `bpy.data`    | 直接访问 Blender 数据 | Mesh、Object、Material、Image |
| `bpy.context` | 当前场景和上下文        | 当前 Object、Scene、Collection |
| `bpy.ops`     | 执行 Blender 操作   | 创建 Cube、删除物体、应用 Modifier   |
| `bpy.types`   | Blender 类型系统    | Object、Operator、Panel      |
| `bpy.props`   | 自定义属性           | Add-on 参数                  |
| `mathutils`   | 3D 数学           | Vector、Matrix、Quaternion   |

例如：

```python
bpy.ops.mesh.primitive_cube_add()
```

基本就相当于在 Blender UI 里：

**Add → Mesh → Cube**

而：

```python
cube = bpy.context.object
cube.location.z = 2
```

相当于把刚创建的 Cube 在 Z 轴移动到 `2`。

所以它特别适合做：

- 程序化建模 / Procedural Modeling
- 批量生成模型
- 自动配置材质
- 自动布置 Camera / Light
- 自动创建动画
- 批量渲染
- `.blend` / OBJ / FBX / glTF 等资产处理
- Blender Pipeline 自动化
- 写 Blender Add-on
- 用参数生成家具、建筑、商品模型等

对于独立开发、自动化资产生成甚至搭建一个“输入 JSON → 输出 3D 模型”的服务都很有用。

## 例子：用 Python 创建马克杯

[10_Example.py](10_Example.py)这个脚本会：

1. 清空 Blender 场景中的所有物体。
2. 创建白色釉面陶瓷材质，加入清漆和细微凹凸效果。
3. 加载印花图片，创建印花材质并处理透明区域。
4. 创建外圆柱作为杯体。
5. 创建内圆柱，通过布尔差集挖空杯体并保留杯底。
6. 给杯体增加倒角、平滑着色和白色陶瓷材质。
7. 使用贝塞尔曲线创建杯把，并赋予白色陶瓷材质。
8. 创建贴合杯壁的弧形印花网格，为其生成 UV 并应用图片。
9. 创建暖灰色地面，用于接收阴影。
10. 设置主光、补光和轮廓光。
11. 创建略微俯视的三分之四视角相机。
12. 设置 Eevee、AgX 色彩管理和 720×720 PNG 输出。
13. 渲染并保存 mug.png。
14. 保存完整场景为 mug.blend。

代码只使用 Blender 自带 API，不需要额外安装 Python 包。

使用方法为：

```sh
blender -b -P 10_Example.py
```

- `b`, `--background` 在后台运行渲染（通常用于无需UI的渲染）。
- `-P`, `--python <filepath>` 运行指定的 Python 脚本文件。
