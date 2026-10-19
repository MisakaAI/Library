# 现代化前端开发指南

## 快速施法

```sh
# 创建 Vue 3 + TypeScript 项目
npm create vite@latest my-vue-app -- --template vue-ts

# 进入项目
cd my-vue-app
# 安装基础依赖
npm install

# 安装路由和状态管理
npm install vue-router
# 安装 UI 组件库
npm install element-plus # ArcoVue
npm install @arco-design/web-vue # Arco Design

# 安装 图标
npm install @remixicon/vue
# 安装 Tiptap 富文本编辑器
npm install @tiptap/vue-3 @tiptap/pm @tiptap/starter-kit
# 可视化图表库
npm install echarts
# 状态管理库
npm install pinia
# 日期处理
npm install dayjs
# 国际化多语言支持
npm install vue-i18n@11
# 网络请求库
npm install axios
# 数据验证
npm install zod

# 启动项目
npm run dev
# 编译生产版本
npm run build
# 本地预览编译结果
npm run preview
```

## 基础概念

- `Node.js`：让 JavaScript 可以在电脑上运行，不只待在浏览器里。
- `npm`：Node.js 自带的“应用商店 + 遥控器”。用它下载别人写好的代码包，也用它运行命令，比如 `npm run dev`。
- `npx` 是 npm 自带的“临时运行器”。npm 负责把包下载/安装到项目里；npx 负责“把包里的命令拿来跑一下”。可以理解成是临时工。
- `Yarn`、`pnpm`：也是“应用商店 + 遥控器”，和 npm 干的事差不多，可以替代 npm。有的更快，有的更省硬盘。
- `Vite`：是一个前端项目工具。你改代码，它马上帮你显示出来；项目做完，它帮你打包。
- `Vue`、`React`：用来做网页界面的工具，网页上的按钮、列表、输入框，都可以拆成一个个“小组件”。类似乐高积木。
- `TypeScript`（简称 TS）是 JavaScript 的超集，在 JS 基础上增加了静态类型系统。写代码时给变量、函数参数、返回值标注类型，编译器会在运行前就帮你检查出类型错误。
详细说明见 [TypeScript](TypeScript.md)

## 创建

```sh
npm create vite@latest my-vue-app -- --template vue

# 如果使用 TypeScript 则应该是：
# npm create vite@latest my-vue-app -- --template vue-ts

# Need to install the following packages:
# 需要安装以下软件包：
# create-vite@9.2.1
# 
# Ok to proceed? (y)
# 是否继续？(y)

# > npx
# > "create-vite" my-vue-app --template vue
# 
# │
# ◆  Install with npm and start now?
# ◆  是否现在用 npm 安装依赖并启动项目？
# │  ● Yes / ○ No
# └

# ◇  Scaffolding project in /home/Work/my-vue-app...
# ◇  正在 /home/Work/my-vue-app 中创建项目结构（生成项目脚手架）...
# │
# ◇  Installing dependencies with npm...
# ◇  正在使用 npm 安装依赖...

#   VITE v8.3.3  ready in 184 ms
# 
#   ➜  Local:   http://localhost:5173/
#   ➜  本地访问地址：http://localhost:5173/
#   ➜  Network: use --host to expose
#   ➜  网络访问：使用 --host 参数来对外暴露（让局域网内其他设备也能访问）
#   ➜  press h + enter to show help
#   ➜  按 h 键，然后按回车，显示帮助信息

# 按 Ctrl+C 停止

cd my-vue-app

npm install
npm run dev
```

## Vue Router

Vue Router 像“路标”，让页面之间切换，不用刷新整个网页。

```sh
# 安装
npm install vue-router
```

```js
// src/main.js
import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './router'

const app = createApp(App)
app.use(router)
app.mount('#app')
```

```html
<!-- src/App.vue -->
<template>
  <nav class="nav">
    <router-link to="/">Home</router-link>
    <router-link to="/editor">Editor</router-link>
  </nav>
  <router-view />
</template>

<style scoped>
.nav {
  display: flex;
  justify-content: center;
  gap: 1.5rem;
  padding: 1rem;
  background: #f0f0f0;
  border-bottom: 1px solid #ddd;
}
.nav a {
  text-decoration: none;
  color: #333;
}
.nav a.router-link-active {
  font-weight: bold;
  color: #42b883;
}
</style>
```

```html
<!-- src/views/Home.vue -->
<template>
  <HelloWorld />
</template>

<script setup>
import HelloWorld from '../components/HelloWorld.vue'
</script>
```

```html
<!-- src/views/EditorPage.vue -->
<template>
  <div class="page">
    <h1>编辑器页面（普通文本框版）</h1>

    <!-- 普通文本输入框，先用 v-model 双向绑定 -->
    <textarea
      v-model="content"
      class="plain-input"
      placeholder="在这里输入内容..."
    ></textarea>

    <!-- 实时预览输出 -->
    <div class="output">
      <h3>实时输出：</h3>
      <pre>{{ content }}</pre>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const content = ref('Hello! 先试试普通文本框输入吧...')
</script>

<style scoped>
.page {
  max-width: 800px;
  margin: 2rem auto;
  padding: 0 1rem;
}
.plain-input {
  width: 100%;
  min-height: 150px;
  padding: 1rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 16px;
  font-family: inherit;
  outline: none;
  resize: vertical;
  box-sizing: border-box;
}
.plain-input:focus {
  border-color: #42b883;
}
.output {
  margin-top: 2rem;
  padding: 1rem;
  background-color: #f5f5f5;
  border-radius: 4px;
}
.output pre {
  white-space: pre-wrap;
  word-break: break-all;
  margin: 0;
}
</style>
```

```js
// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import EditorPage from '../views/EditorPage.vue'

const routes = [
    { path: '/', name: 'Home', component: Home },
    { path: '/editor', name: 'Editor', component: EditorPage }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router
```

## Tiptap 富文本输入框

Tiptap 是一个第三方富文本编辑器，像简化版 Word，可以加粗、斜体等。

```sh
# 安装
npm install @tiptap/vue-3 @tiptap/pm @tiptap/starter-kit
```

创建组件封装 Tiptap，对外暴露 `v-model`

```html
<!-- src/components/TiptapEditor.vue -->
<template>
  <div class="editor-container">
    <editor-content :editor="editor" class="editor-content" />
  </div>
</template>

<script setup>
import { useEditor, EditorContent } from '@tiptap/vue-3'
import StarterKit from '@tiptap/starter-kit'
import { watch } from 'vue'

const props = defineProps({
  modelValue: {
    type: String,
    default: ''
  }
})
const emit = defineEmits(['update:modelValue'])

// 创建编辑器实例
const editor = useEditor({
  content: props.modelValue,
  extensions: [StarterKit],
  onUpdate: ({ editor }) => {
    // 内容变化时，把 HTML 抛给父组件
    emit('update:modelValue', editor.getHTML())
  }
})

// 父组件内容变化时，反向同步到编辑器
watch(
  () => props.modelValue,
  (newValue) => {
    if (editor.value && editor.value.getHTML() !== newValue) {
      // emitUpdate: false，避免触发 onUpdate 造成死循环
      editor.value.commands.setContent(newValue, false)
    }
  }
)
</script>

<style scoped>
.editor-container {
  border: 1px solid #ccc;
  border-radius: 4px;
  padding: 1rem;
  background: #fff;
}
.editor-content :deep(.ProseMirror) {
  min-height: 150px;
  outline: none;
  font-size: 16px;
  font-family: inherit;
}
.editor-content :deep(.ProseMirror p) {
  margin: 0.5em 0;
}
.editor-content :deep(.ProseMirror:focus) {
  outline: none;
}
/* 让编辑区获得焦点时容器有绿色边框 */
.editor-container:focus-within {
  border-color: #42b883;
}
</style>
```

修改 `src/views/EditorPage.vue`，把 `<textarea>` 换成 `<TiptapEditor>`，其他几乎不动。

```html
<!-- src/views/EditorPage.vue -->
<template>
  <div class="page">
    <h1>编辑器页面（Tiptap 版）</h1>

    <!-- 用 Tiptap 组件替换原来的 textarea -->
    <TiptapEditor v-model="content" />

    <!-- 实时预览输出 -->
    <div class="output">
      <h3>实时输出 (HTML)：</h3>
      <pre>{{ content }}</pre>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import TiptapEditor from '../components/TiptapEditor.vue'

const content = ref('<p>Hello Tiptap! 开始输入吧...</p>')
</script>

<style scoped>
.page {
  max-width: 800px;
  margin: 2rem auto;
  padding: 0 1rem;
}
.output {
  margin-top: 2rem;
  padding: 1rem;
  background-color: #f5f5f5;
  border-radius: 4px;
}
.output pre {
  white-space: pre-wrap;
  word-break: break-all;
  margin: 0;
}
</style>
```

## Remix Icon 图标库

```sh
# 安装
npm install @remixicon/vue
```

