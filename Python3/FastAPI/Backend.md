# FastAPI 后端开发指南

从零创建 FastAPI + SQLModel + Alembic + SQLite 项目

## 最终目录结构

```
myapp/
├── main.py
├── pyproject.toml
├── alembic.ini
├── app.db                  # 迁移后自动生成
├── migrations/
│   ├── env.py
│   ├── script.py.mako
│   └── versions/
└── app/
    ├── __init__.py
    ├── db.py
    ├── models.py
    ├── schemas.py
    ├── security.py
    └── main.py
```

## 第 1 步:初始化项目

```bash
mkdir myapp && cd myapp
uv init
mkdir app && touch app/__init__.py
```

## 第 2 步:安装依赖

```bash
uv add "fastapi[standard]" sqlmodel alembic "pwdlib[argon2]"
```

- `fastapi[standard]` 已包含 uvicorn、`fastapi` 命令行和 `email-validator`(校验邮箱格式需要)
- `pwdlib[argon2]` 用于密码哈希,是 FastAPI 文档目前推荐的方案

## 第 3 步:数据库配置 `app/db.py`

```python
from sqlalchemy import event
from sqlmodel import Session, create_engine

DATABASE_URL = "sqlite:///app.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)


@event.listens_for(engine, "connect")
def set_sqlite_pragma(dbapi_conn, _):
    cur = dbapi_conn.cursor()
    cur.execute("PRAGMA foreign_keys=ON")   # SQLite 默认不强制外键
    cur.execute("PRAGMA journal_mode=WAL")  # 改善读写并发
    cur.close()


def get_session():
    with Session(engine) as session:
        yield session
```

`DATABASE_URL` 只在这里定义一次,Alembic 也会从这里读取。

## 第 4 步:模型 `app/models.py`

```python
import uuid

from sqlalchemy import MetaData
from sqlmodel import Field, SQLModel

# 约束命名规范:SQLite 的 batch 迁移需要约束有名字(必须在定义模型之前设置)
SQLModel.metadata = MetaData(
    naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }
)


class User(SQLModel, table=True):
    __tablename__ = "users"

    uid: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    username: str = Field(max_length=32, unique=True, index=True)
    email: str = Field(max_length=255, unique=True, index=True)
    nickname: str = Field(max_length=50)
    password_hash: str
```

UID 这里用 UUID,不会暴露用户数量,也不易被枚举。如果你更想要自增整数,改成 `uid: int | None = Field(default=None, primary_key=True)` 即可。

## 第 5 步:请求/响应模型 `app/schemas.py`

`table=True` 的模型不会做数据校验,所以校验用单独的 Pydantic 模型。同时,响应里**绝不能包含 `password_hash`**。

```python
import uuid

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserCreate(BaseModel):
    username: str = Field(min_length=3, max_length=32)
    email: EmailStr
    nickname: str = Field(min_length=1, max_length=50)
    password: str = Field(min_length=8, max_length=128)


class UserRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    uid: uuid.UUID
    username: str
    email: EmailStr
    nickname: str
```

## 第 6 步:密码哈希 `app/security.py`

```python
from pwdlib import PasswordHash

_password_hash = PasswordHash.recommended()  # 默认 Argon2


def hash_password(password: str) -> str:
    return _password_hash.hash(password)


def verify_password(password: str, hashed: str) -> bool:
    return _password_hash.verify(password, hashed)
```

## 第 7 步:初始化并配置 Alembic

```bash
uv run alembic init migrations
```

**(1)用下面的内容完整替换 `migrations/env.py`:**

```python
from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool
from sqlmodel import SQLModel

from app import models  # noqa: F401  必须导入,否则 metadata 是空的
from app.db import DATABASE_URL

config = context.config
config.set_main_option("sqlalchemy.url", DATABASE_URL)

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = SQLModel.metadata


def run_migrations_offline() -> None:
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        render_as_batch=True,  # SQLite 必需
    )
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            render_as_batch=True,  # SQLite 必需
        )
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
```

**(2)修改 `migrations/script.py.mako`**,在 `import sqlalchemy as sa` 下面加一行:

```python
import sqlalchemy as sa
import sqlmodel   # 新增:迁移脚本里会用到 sqlmodel.sql.sqltypes.AutoString
```

不加的话,运行迁移时会报 `NameError: name 'sqlmodel' is not defined`。

## 第 8 步:生成并执行迁移

```bash
uv run alembic revision --autogenerate -m "create users table"
```

生成后**打开 `migrations/versions/xxxx_create_users_table.py` 检查一遍**,应该能看到 `op.create_table('users', ...)` 以及 username、email 的唯一索引。确认无误后执行:

```bash
uv run alembic upgrade head
```

此时项目根目录会出现 `app.db`。

## 第 9 步:接口 `app/main.py`

```python
import uuid
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlmodel import Session

from app.db import get_session
from app.models import User
from app.schemas import UserCreate, UserRead
from app.security import hash_password

app = FastAPI()

SessionDep = Annotated[Session, Depends(get_session)]


@app.post("/users", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def create_user(data: UserCreate, session: SessionDep):
    user = User(
        username=data.username,
        email=data.email.lower(),
        nickname=data.nickname,
        password_hash=hash_password(data.password),
    )
    session.add(user)
    try:
        session.commit()
    except IntegrityError:
        session.rollback()
        raise HTTPException(status.HTTP_409_CONFLICT, "用户名或邮箱已存在")
    session.refresh(user)
    return user


@app.get("/users/{uid}", response_model=UserRead)
def get_user(uid: uuid.UUID, session: SessionDep):
    user = session.get(User, uid)
    if user is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "用户不存在")
    return user
```

这里依赖数据库的唯一约束来捕获重复,比先查再插入更可靠,不会有并发竞争问题。

## 第 10 步:运行并测试

```bash
uv run fastapi dev app/main.py
```

浏览器打开 http://127.0.0.1:8000/docs 可以直接测试,或者用 curl:

```bash
curl -X POST http://127.0.0.1:8000/users \
  -H "Content-Type: application/json" \
  -d '{"username":"alice","email":"alice@example.com","nickname":"Alice","password":"supersecret123"}'
```

返回示例:

```json
{
  "uid": "3f2b8c1e-....",
  "username": "alice",
  "email": "alice@example.com",
  "nickname": "Alice"
}
```

再用同样的数据请求一次,会得到 `409`。直接查看数据库,可以确认存的是哈希而不是明文:

```bash
sqlite3 app.db "SELECT uid, username, password_hash FROM users;"
```

## 以后改表结构的流程

1. 修改 `app/models.py`(比如给 `User` 加一个 `avatar_url` 字段)
2. `uv run alembic revision --autogenerate -m "add avatar_url"`
3. 检查生成的脚本
4. `uv run alembic upgrade head`

## 几个提醒

- 把 `app.db`、`app.db-wal`、`app.db-shm` 加进 `.gitignore`,`migrations/` 目录则要提交
- 不要再调用 `SQLModel.metadata.create_all()`,表结构统一由 Alembic 管理
- 新增模型文件后,记得在 `env.py` 里(或通过 `app/models.py`)导入,否则 autogenerate 看不到
- 如果有人手动改了 `app.db` 导致和迁移记录对不上,开发阶段最简单的办法是删掉 `app.db` 重新 `upgrade head`
