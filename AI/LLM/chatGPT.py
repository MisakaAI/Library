# pip install openai

import openai

openai.organization = ""
openai.api_key = ""

messages = []
msg = input('[{}] >>> '.format(len(messages)+1))

while True:
    if msg == 'exit':
        break
    elif msg == 'newchat':
        print("\n" + "-"*30)
        messages = []
        msg = input('\n[{}] >>> '.format(int(len(messages)/2)+1))
    else:
        messages.append({"role": "user", "content": "{}".format(msg)})
        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        print("AI: ",end='')
        print(completion.choices[0].message.content)
        messages.append(completion.choices[0].message)
        msg = input('\n[{}] >>> '.format(int(len(messages)/2)+1))
