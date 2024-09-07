# 日期

`DataTime` 表示某个时刻，通常以日期和当天的时间表示。
`TimeSpan` 表示时间间隔，能够用于保存时间信息。

除上述类外，`.NET` 还提供以下支持处理时区的类型：

- `TimeZone` 使用此类处理系统的本地时区和协调世界时 (UTC) 区域。
- `TimeZoneInfo` 此类可用于处理系统上预定义的任何时区、创建新时区，以及将日期和时间从一个时区轻松转换成另一个时区。 对于新的开发，使用 `TimeZoneInfo` 类而不使用 `TimeZone` 类。
- `DateTimeOffset` 使用此结构处理已知 UTC 偏移量（或差值）的日期和时间。

从 `.NET 6` 开始，可用类型如下：

- `DateOnly` 只表示日期的值时，请使用此结构。该日期表示从一天开始到结束的一整天。
- `TimeOnly` 使用此结构来表示不含日期的时间。 此时间表示不含具体日期的小时、分钟和秒。

## 参考文献

[DateTime 结构](https://learn.microsoft.com/zh-cn/dotnet/api/system.datetime?view=net-8.0)
[TimeSpan 结构](https://learn.microsoft.com/zh-cn/dotnet/api/system.timespan?view=net-8.0)
