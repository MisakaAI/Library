# Blender

[Blender](https://www.blender.org/)

## 安装

- [下载](https://www.blender.org/download/)

### Linux

```
# 解压
tar -xf blender-5.1.2-linux-x64.tar.xz -C /opt
mv /opt/blender-5.1.2-linux-x64 /opt/blender

# 桌面入口文件
cp /opt/blender/blender.desktop /usr/share/applications

# 图标
cp /opt/blender/blender.svg /usr/share/icons/hicolor/scalable/apps/blender.svg
sudo gtk-update-icon-cache -f /usr/share/icons/hicolor

# 更新菜单缓存
update-desktop-database

# 命令
ln -s /opt/blender/blender /usr/local/bin/blender
```

※ 最好安装在纯英文路径下。

## 目录

- [基本操作](01_BasicOperations.md)
- [坐标系](02_Coordinate.md)
- [吸附衰减](03_Adsorption.md)
- [物体模式](04_ObjectMode.md)
- [编辑模式](05_EditMode.md)
- [摄像机](06_Camera.md)
- [材质](07_Materials.md)
- [场景](08_Scene.md)

## 设置

### 语言

`Edit` `Preferences` `Interface` `Language` `Simplified Chinese`
`编辑` `偏好设置` `界面` `语言` `（简体中文）`

### 偏好设置

修改后在左下角保存用户设置

#### 界面

- 显示 分辨率缩放 （1.0）
- 编辑器 状态栏 （系统内存） （显示内存） （Blender版本）
- 语言 翻译 （新建数据） 取消勾选

#### 输入

- 模拟三键鼠标

#### 视图导航

- 旋转&平移 视轨灵敏度 围绕选择物体旋转
- 旋转&平移 自动 深度

#### 系统

- 内存&限额 撤销内存限制 全局撤销

#### 保存&加载

- 自动运行 Python 脚本

### 插件

- Node Wrangler （强大的节点工具）
- Rigify （自带的强大绑骨插件）
- Copy Attributes Menu （复制属性菜单）
- Modifier Tools (修改器工具)
- LoopTools （循环工具）
- Bool Tool （布尔工具）
- Magic UV （魔法UV）
- Export Autocad DXF Format (导出 .dxf)
- Extra Curve Objects （额外曲线）
- Extra Mesh Objects （额外网格）
- A.N.T.Landscape （简单地形制作）
- BoltFactory （添加螺栓）

## 参考文献

- [Blender 2.9-3.4黑铁骑士Ⅱ系统零基础入门教程](https://www.bilibili.com/video/BV1zh411Y7LX/) 只剩一瓶辣椒酱
    - [目录](BV1zh411Y7LX.md)