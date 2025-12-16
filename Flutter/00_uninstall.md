# 删除 Flutter SDK

## 删除安装目录

```sh
rm -rf ~/dev/flutter
```

## 清理安装和配置文件

删除 Flutter 配置目录

- `~/.flutter`
- `~/.flutter-devtools`
- `~/.flutter_settings`

```sh
rm -rf  ~/.flutter ~/.flutter-devtools ~/.flutter_settings
```

删除 Dart 配置目录

- `~/.dart`
- `~/.dart-tool`
- `~/.dartServer`

```sh
rm -rf  ~/.dart ~/.dart-tool ~/.dartServer
```

删除 pub 包目录

- `~/.pub-cache`

```sh
rm -rf ~/.pub-cache
```

删除镜像站信息

- `~/.zshrc`

```zshrc
# 删除这两行
export PUB_HOSTED_URL="https://mirrors.tuna.tsinghua.edu.cn/dart-pub"
export FLUTTER_STORAGE_BASE_URL="https://mirrors.tuna.tsinghua.edu.cn/flutter"
```

## 参考文献

- [Uninstall Flutter](https://docs.flutter.dev/install/uninstall)
