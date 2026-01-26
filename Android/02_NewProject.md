# 创建项目

1. New Project
2. Phone and Tablet
3. Empty Activity

## 配置项目

1. `Name` 名称
2. `Package name` 包名
例如： `com.tencent.mobileqq` （腾讯QQ）
    - 全部使用小写字母。
    - 一级包名通常为`com`
    - 二级包名为xx（一般为公司或个人域名）
    - 三级包名根据应用进行命名
    - 四级包名为功能模块名
3. `Save location` 代码保存位置
4. `Minimum SDK` 指定可运行您应用的最低 Android 版本
5. `Build configuration language` 构建配置语言
    - `Kotlin DSL` Kotlin 静态类型语言
    - `Groovy DSL` Groovy 动态类型语言

## 目录结构

- `app/src` 顶级应用子项目/子项目源文件
    - `main` 主 源代码集
        - `AndroidManifest.xml` 应用元数据
        - `java` / `kotlin`
            - `<Package name>/MainActivity.kt` 源代码
        - `res` 资源文件
            - `layout/activity_main.xml` 布局文件 XML
            - `values/*.xml` 通用资源（文本/颜色/主题/样式）
            - `drawable` 图片文件
            - `menu` 菜单的XML文件
            - `xml` 通过调用 `Resources.getXML()` 读取任意的XML文件。

### 应用元数据

- 应用的包名（最终 ID）
- 使用哪些权限（网络、蓝牙、定位）
- 哪些 Activity / Service / Receiver 存在
- 应用的入口 Activity
- intent filter（如接收分享、深链）

任何组件不在 Manifest 注册，系统都不知道它存在。

### MainActivity.kt

应用入口的 UI 界面逻辑
设置 View / Fragment
创建生命周期方法 `onCreate()`

### 应用名称与图标

#### 应用名称

修改 `app/src/main/res/values/strings.xml`

```xml
<resources>
    <string name="app_name">我的应用</string>
</resources>
```

#### 应用图标

用 Android Studio 自动生成图标
右键点击 `app` → New > Image Asset

- Icon Type 选 Launcher Icons (Adaptive and Legacy)
- Foreground Layer：选择你的 PNG/SVG
- Background Layer：颜色或图片

Preview 下方会显示不同机型的效果，并自动更新 Manifest
