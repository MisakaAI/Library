# TypeScript

TypeScript（简称 TS）是 JavaScript 的超集，在 JS 基础上增加了静态类型系统。
写代码时给变量、函数参数、返回值标注类型，编译器在编译时会检查出类型错误。

## 使用

### 创建时直接声明

```sh
npm create vite@latest my-vue-app -- --template vue-ts
```

### 创建时未声明，后期引入

#### 安装依赖

```sh
npm install -D typescript vue-tsc @types/node
```

#### 对旧文件进行修改

- 新增 `tsconfig.json`
- 新增 `tsconfig.node.json`，专门给 `vite.config.ts` 使用。
- 新增 `src/env.d.ts` 让 TS 认识 `.vue` 文件，`import App from './App.vue'` 才不会报错。
- `vite.config.js` 改为 `vite.config.ts`
- `index.html` 把入口脚本改成 .ts：`<script type="module" src="/src/main.ts"></script>`
- `src/main.js` 改为 `src/main.ts`
- 其他需要修改的地方，如`src/router/index.js`改为`src/router/index.ts`
- `.vue` 文件本身不改名，只是把 `<script setup>` 改成 `<script setup lang="ts">`。
