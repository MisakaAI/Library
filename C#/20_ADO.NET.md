# ADO.NET

ADO.NET 用于对数据库进行访问和操作。

> ADO (ActiveX Data Objects)

## 主要组件

- **Connection 对象**
用于管理与数据源的连接。
常用的连接类包括 `SqlConnection`（用于 SQL Server）、`OleDbConnection`（用于 OLE DB 数据源），以及 `MySqlConnection` 等。
- **Command 对象**
用于执行 SQL 语句或存储过程。
`SqlCommand` 是最常用的命令类，它允许你发送查询或命令到数据库，并可以通过它来获取查询结果或执行更新操作。
- **DataReader 对象**
提供从数据库读取数据的前向只读流。
适用于一次性读取大量数据但不需要修改的场景。
它通过低内存消耗的方式，逐行读取数据。
- **DataSet 和 DataTable**
`DataSet` 是一个离线的数据缓存，用于存储从数据库中检索的数据。
它可以包含多个 `DataTable`，即数据库表的内存表示形式。
`DataSet` 支持断开连接的操作模式，可以对数据进行修改、删除、更新操作，并在后续与数据库同步。
- **DataAdapter 对象**
用于在数据源和 `DataSet` 之间填充数据，并提供将 `DataSet` 中的修改提交回数据库的功能。
`DataAdapter` 允许你通过批量操作来提高数据处理的效率。
- **Transaction**
支持数据库事务操作，通过 `SqlTransaction` 或 `DbTransaction` 对象管理事务的开始、提交和回滚，确保数据操作的原子性和一致性。

## 特点

- **断开连接的操作模式**
ADO.NET 可以通过 `DataSet` 在离线模式下操作数据，这减少了与数据库的持续连接，提升了系统的性能和扩展性。
- **面向对象的访问方式**
ADO.NET 采用类库形式，将数据访问抽象为对象，开发人员可以通过面向对象的方式进行数据操作。
- **数据提供者模型**
ADO.NET 支持多种数据库，通过不同的“数据提供者”类库（如 `SqlClient`、`OleDbClient`）来实现与特定数据库的通信。

## 使用

### SQL Server

[适用于 SQL Server 和 Azure SQL 数据库的 Microsoft ADO.NET](https://learn.microsoft.com/zh-cn/sql/connect/ado-net/microsoft-ado-net-sql-server?view=sql-server-ver16)

#### 安装 SQL Server

```sh
dotnet add package Microsoft.Data.SqlClient
```

#### 使用 SQL Server

```cs
using System;
using DT = System.Data;
using QC = Microsoft.Data.SqlClient;

namespace ProofOfConcept_SQL_CSharp
{
    public class Program
    {
        static public void Main()
        {
            using (var connection = new QC.SqlConnection(
                "Server=tcp:YOUR_SERVER_NAME_HERE.database.windows.net,1433;" +
                "Database=AdventureWorksLT;User ID=YOUR_LOGIN_NAME_HERE;" +
                "Password=YOUR_PASSWORD_HERE;Encrypt=True;" +
                "TrustServerCertificate=False;Connection Timeout=30;"
                ))
            {
                connection.Open();
                Console.WriteLine("Connected successfully.");

                Program.SelectRows(connection);

                Console.WriteLine("Press any key to finish...");
                Console.ReadKey(true);
            }
        }

        static public void SelectRows(QC.SqlConnection connection)
        {
            using (var command = new QC.SqlCommand())
            {
                command.Connection = connection;
                command.CommandType = DT.CommandType.Text;
                command.CommandText = @"
SELECT
    TOP 5
        COUNT(soh.SalesOrderID) AS [OrderCount],
        c.CustomerID,
        c.CompanyName
    FROM
                        SalesLT.Customer         AS c
        LEFT OUTER JOIN SalesLT.SalesOrderHeader AS soh
            ON c.CustomerID = soh.CustomerID
    GROUP BY
        c.CustomerID,
        c.CompanyName
    ORDER BY
        [OrderCount] DESC,
        c.CompanyName; ";

                QC.SqlDataReader reader = command.ExecuteReader();

                while (reader.Read())
                {
                    Console.WriteLine("{0}\t{1}\t{2}",
                        reader.GetInt32(0),
                        reader.GetInt32(1),
                        reader.GetString(2));
                }
            }
        }
    }
}
```

### PostgreSQL

- [Npgsql](https://www.npgsql.org/index.html)

#### 安装 Npgsql

使用 Npgsql 的最佳方法是安装其 [nuget](https://www.nuget.org/packages/Npgsql/) 包。

```sh
dotnet add package Npgsql
```

#### 使用 Npgsql

```cs
using Npgsql;
class Program
{
    static async Task Main()
    {
        var connectionString = "Host=localhost;Port=5432;Username=yourusername;Password=yourpassword;Database=yourdatabase";
        await using var dataSource = NpgsqlDataSource.Create(connectionString);
        // 创建库 CREATE DATABASE csharp;
        // 创建表 CREATE TABLE test (id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY, name TEXT, age TEXT);
        // 删除表 DROP TABLE IF EXISTS test;

        // 插入表
        // ($1), ($2)：表示插入多行，每行插入一个值。
        // ($1, $2)：表示插入一行，每行插入两个值。
        await using (var cmd = dataSource.CreateCommand("INSERT INTO test (name, age) VALUES ($1, $2)"))
        {
            cmd.Parameters.Add(new() { Value = "Misaka" }); // 构造一个 NpgsqlParameter 对象并将其添加到 cmd.Parameters 集合中
            cmd.Parameters.AddWithValue(18); // 快速添加值到参数集合中
            await cmd.ExecuteNonQueryAsync();
            // ExecuteNonQueryAsync 执行不返回任何结果的SQL，通常是INSERT、UPDATE或DELETE语句。返回受影响的行数。
        }

        // 查询表
        await using (var cmd = dataSource.CreateCommand("SELECT COUNT(id) FROM test"))
        {
            var reader = await cmd.ExecuteScalarAsync();
            Console.WriteLine("COUNT: " + reader);
        }
        // ExecuteScalarAsync 执行SQL，返回单个的结果。
        // 如果查询返回的结果为空，ExecuteScalarAsync 会返回 null。
        // 如果查询的结果集中有多行，ExecuteScalarAsync 只会返回第一行第一列的值，其余的行和列将被忽略。

        await using (var cmd = dataSource.CreateCommand("SELECT id, name, age FROM test"))
        await using (var reader = await cmd.ExecuteReaderAsync())
        // ExecuteReaderAsync 执行SQL，返回完整的结果集。
        {
            // 显示 字段名称
            int fieldCount = reader.FieldCount;
            for (int i = 0; i < fieldCount; i++)
            {
                string fieldName = reader.GetName(i);
                if (i == fieldCount - 1)
                {
                    Console.WriteLine(fieldName);
                }
                else
                {
                    Console.Write(fieldName + " | ");
                }
            }
            // 显示 查询结果
            while (await reader.ReadAsync())
            {
                Console.Write(reader.GetInt32(0) + " | ");
                Console.Write(reader.GetString(1) + " | ");
                Console.WriteLine(reader.GetString(2));
            }
        }
        // 修改表
        await using (var cmd = dataSource.CreateCommand("UPDATE test SET name = @name WHERE id = @id;"))
        {
            cmd.Parameters.AddWithValue("@name", "xNove");
            cmd.Parameters.AddWithValue("@id", 1);
            await cmd.ExecuteNonQueryAsync();
        }
        // 删除表
        string tableName = "test";
        await using (var cmd = dataSource.CreateCommand($"DELETE FROM {tableName} WHERE id = $1;"))
        {
            cmd.Parameters.AddWithValue(1);
            await cmd.ExecuteNonQueryAsync();
        }
    }
}
```

### SQLite3

- [Microsoft.Data.Sqlite](https://learn.microsoft.com/zh-cn/dotnet/standard/data/sqlite/?tabs=netcore-cli) 是用于 `SQLite` 的轻型 `ADO.NET` 提供程序。

#### 安装 Sqlite

```sh
dotnet add package Microsoft.Data.Sqlite
```

#### 使用 Sqlite

```cs
using System;
using Microsoft.Data.Sqlite;

namespace HelloWorldSample
{
    class Program
    {
        static void Main()
        {
            using (var connection = new SqliteConnection("Data Source=hello.db"))
            {
                connection.Open();
                var command = connection.CreateCommand();

                // 创建表
                command.CommandText =
                @"
                    CREATE TABLE IF NOT EXISTS user (
                        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL
                    );
                ";
                command.ExecuteNonQuery();

                 // 插入数据
                Console.Write("Name: ");
                var name = Console.ReadLine();

                #region snippet_Parameter
                command.CommandText =
                @"
                    INSERT INTO user (name)
                    VALUES ($name)
                ";
                command.Parameters.AddWithValue("$name", name);
                #endregion
                command.ExecuteNonQuery();

                // 查询数据
                // 查询最后一次插入操作的ID
                command.CommandText =
                @"
                    SELECT last_insert_rowid()
                ";
                var newId = (long)command.ExecuteScalar();
                Console.WriteLine($"Your new user ID is {newId}.");
                // 查询 newId 的 name
                command.CommandText =
                @"
                    SELECT name
                    FROM user
                    WHERE id = $id
                ";
                command.Parameters.AddWithValue("$id", newId);

                using (var reader = command.ExecuteReader())
                {
                    while (reader.Read())
                    {
                        var reader_name = reader.GetString(0);

                        Console.WriteLine($"Hello, {reader_name}!");
                    }
                }

            }
        }
    }
}
```
