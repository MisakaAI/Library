# Rust

## 安装 Rust

- [Rustup](https://rust-lang.org/learn/get-started/)

```sh
# 清华大学开源软件镜像站
echo 'export RUSTUP_UPDATE_ROOT=https://mirrors.tuna.tsinghua.edu.cn/rustup/rustup' >> ~/.zshrc
echo 'export RUSTUP_DIST_SERVER=https://mirrors.tuna.tsinghua.edu.cn/rustup' >> ~/.zshrc
source ~/.zshrc

curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
. "$HOME/.cargo/env"
rustc --version
cargo --version

# 自动加载环境
printf '\n# Rust\n. "$HOME/.cargo/env"\n' >> ~/.zshrc

# Rust crates.io 稀疏索引
mkdir -vp ${CARGO_HOME:-$HOME/.cargo}

cat << EOF | tee -a ${CARGO_HOME:-$HOME/.cargo}/config.toml
[source.crates-io]
replace-with = 'mirror'

[source.mirror]
registry = "sparse+https://mirrors.tuna.tsinghua.edu.cn/crates.io-index/"

[registries.mirror]
index = "sparse+https://mirrors.tuna.tsinghua.edu.cn/crates.io-index/"
EOF
```

## 编译 & 运行

```sh
cargo new hello
cd hello

cargo check
cargo run
cargo build --release
./target/release/hello
```

## 跨平台编译

### ARM64

```sh
sudo apt update
sudo apt install gcc-aarch64-linux-gnu
aarch64-linux-gnu-gcc --version

rustup target add aarch64-unknown-linux-gnu
rustup target list --installed

mkdir -p .cargo
cat > .cargo/config.toml <<EOF
[target.aarch64-unknown-linux-gnu]
linker = "aarch64-linux-gnu-gcc"
EOF

# 编译
cargo build --release --target aarch64-unknown-linux-gnu

# 验证
file target/aarch64-unknown-linux-gnu/release/hello

# 输出类似：
# ELF 64-bit LSB pie executable, ARM aarch64, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux-aarch64.so.1, BuildID[sha1]=a64b7f9ec3e4fcd67f657c8f3d58567fabc60eb0, for GNU/Linux 3.7.0, not stripped

# 运行
#target/aarch64-unknown-linux-gnu/release/hello
```

### Cross

```sh
# 安装
cargo install cross

# 需要 Docker 或 Podman
docker --version

# 静态链接，编译为 musl
rustup target add aarch64-unknown-linux-musl

# 编译
cross build --release --target aarch64-unknown-linux-musl

# 验证
file target/aarch64-unknown-linux-musl/release/hello

# 输出类似：
# ELF 64-bit LSB executable, ARM aarch64, version 1 (SYSV), statically linked, not stripped

# 运行
#target/aarch64-unknown-linux-musl/release/hello
```

- `aarch64-unknown-linux-gnu`    ARM64（glibc，动态链接）
- `aarch64-unknown-linux-musl`   ARM64（musl，静态链接）

- `x86_64-unknown-linux-gnu`     Linux x64（glibc，默认目标）
- `x86_64-unknown-linux-musl`    Linux x64（musl，静态链接）

- `x86_64-pc-windows-gnu`        Windows x64（MinGW，支持交叉编译）
- `x86_64-pc-windows-gnullvm`    Windows x64（LLVM + GNU Runtime）
- `x86_64-pc-windows-msvc`       Windows x64（MSVC，微软官方 ABI）

- `aarch64-apple-darwin`         macOS Apple Silicon（M1/M2/M3/M4）

- `wasm32-unknown-unknown`       WebAssembly（浏览器 / Wasm Runtime）

## 基础语法

## 参考文献

- [学习 Rust](https://rust-lang.org/zh-CN/learn/)
- [《Rust 程序设计语言》](https://kaisery.github.io/trpl-zh-cn/)
