# 状态码

- 100 及以上状态码用于「消息」响应。你很少直接使用它们。具有这些状态代码的响应不能带有响应体。
- 200 及以上状态码用于「成功」响应。这些是你最常使用的。
  - 200 是默认状态代码，它表示一切「正常」。
  - 另一个例子会是 201，「已创建」。它通常在数据库中创建了一条新记录后使用。
  - 一个特殊的例子是 204，「无内容」。此响应在没有内容返回给客户端时使用，因此该响应不能包含响应体。
- 300 及以上状态码用于「重定向」。具有这些状态码的响应可能有或者可能没有响应体，但 304「未修改」是个例外，该响应不得含有响应体。
- 400 及以上状态码用于「客户端错误」响应。这些可能是你第二常使用的类型。
  - 一个例子是 404，用于「未找到」响应。
  - 对于来自客户端的一般错误，你可以只使用 400。
- 500 及以上状态码用于服务器端错误。你几乎永远不会直接使用它们。当你的应用程序代码或服务器中的某些部分出现问题时，它将自动返回这些状态代码之一。

## 参考文献

- [MDN 关于 HTTP 状态码](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)