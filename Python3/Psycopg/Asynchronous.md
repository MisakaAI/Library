# 异步操作

Psycopg Connection 和 Cursor 具有支持异步接口的对应项 AsyncConnection 和 AsyncCursor。
异步对象的设计与同步对象的设计基本相同，你只需要在各处使用 await 关键字。

```python
async with await psycopg.AsyncConnection.connect(
        "dbname=test user=postgres") as aconn:
    async with aconn.cursor() as acur:
        await acur.execute(
            "INSERT INTO test (num, data) VALUES (%s, %s)",
            (100, "abc'def"))
        await acur.execute("SELECT * FROM test")
        await acur.fetchone()
        # will return (1, 100, "abc'def")
        async for record in acur:
            print(record)
```
