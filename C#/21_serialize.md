# 序列化和反序列化

## JSON 序列化

`System.Text.Json` 将对象转换为 JSON 字符串，或从 JSON 字符串还原对象。

```cs
using System;
using System.Text.Json;

public class Person
{
    public string Name { get; set; }
    public int Age { get; set; }
}

class Program
{
    static void Main()
    {
        var json = new Person { Name = "Misaka", Age = 30 };

        // 序列化对象为 JSON 字符串
        string jsonString = JsonSerializer.Serialize(json);
        Console.WriteLine(jsonString);

        // 反序列化 JSON 字符串为对象
        string String = "{\"Name\":\"Alice\",\"Age\":30}";
        Person p = JsonSerializer.Deserialize<Person>(String);
        Console.WriteLine($"Name: {p.Name}, Age: {p.Age}");
    }
}
```

## XML 序列化

`System.Xml.Serialization` 将对象序列化为 XML 格式。

```cs
using System;
using System.IO;
using System.Xml.Serialization;

[Serializable]
public class Person
{
    public string Name { get; set; }
    public int Age { get; set; }
}

class Program
{
    static void Main()
    {
        var person = new Person { Name = "Misaka", Age = 30 };
        // 创建 XmlSerializer 对象
        XmlSerializer serializer = new XmlSerializer(typeof(Person));

        // 序列化 输出到控制台
        serializer.Serialize(Console.Out, person);
        Console.WriteLine();

        // 序列化 保存到 output.xml 文件
        using (FileStream fileStream = new FileStream("output.xml", FileMode.Create))
        {
            serializer.Serialize(fileStream, person);
        }

        // 反序列化 output.xml 文件，读取到 Person 对象
        XmlSerializer deserialized = new XmlSerializer(typeof(Person));

        using (FileStream fileStream = new FileStream("output.xml", FileMode.Open))
        {
            Person d = (Person)deserialized.Deserialize(fileStream);
            // 输出反序列化的对象内容
            Console.WriteLine($"Name: {d.Name}");
            Console.WriteLine($"Age: {d.Age}");
        }
    }
}
```

`[Serializable]` 是一个用于标记类或结构体的特性（Attribute），它表明该类或结构体的实例可以被序列化。
序列化是将对象的状态（即其属性值）转换为一种可以存储或传输的格式的过程，反序列化则是将这种格式的数据重新转换回对象。
如果没有加上 `[Serializable]`，在某些序列化技术中（例如二进制序列化）将会抛出错误。
这个标记在 XML 序列化中并不是必要的。
