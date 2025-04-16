#!/usr/bin/env python3
# pip install openai

import os
from openai import OpenAI

os.environ["http_proxy"] = "http://127.0.0.1:7890"
os.environ["https_proxy"] = "http://127.0.0.1:7890"

model = "grok-2-latest"
XAI_API_KEY = ""

client = OpenAI(
    api_key=XAI_API_KEY,
    base_url="https://api.x.ai/v1",
)

def chat(msg):
    try:
        completion = client.chat.completions.create(
            model=model,
            messages=msg,
        )
        return completion.choices[0].message
    except Exception as e:
        return f"错误: {str(e)}"

print(f"[system] 当前模型为 {model}")
messages = []
msg = input('[{}] >>> '.format(len(messages)+1))

while True:
    if msg == 'exit':
        print("[system] 再见！")
        break
    elif msg == 'newchat':
        print("\n" + "-"*30)
        messages = []
        msg = input('\n[{}] >>> '.format(int(len(messages)/2)+1))
    else:
        messages.append({"role": "user", "content": "{}".format(msg)})
        r = chat(messages)
        print(f"[{model}]: {r.content}")
        messages.append(r)
        msg = input('\n[{}] >>> '.format(int(len(messages)/2)+1))
