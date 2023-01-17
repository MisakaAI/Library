# 获取指定 Node 节点的数据

# https://opcua-asyncio.readthedocs.io/en/latest/api/asyncua.html
# uaread --url=opc.tcp://{IP}:{Port} -n '{Node ID}'

import asyncio
from asyncua import Client

url = ""
NodeID = ""

async def main():
    async with Client(url=url) as client:
        node = client.get_node(NodeID)
        value = await node.read_value()
        print(value)

if __name__ == "__main__":
    asyncio.run(main())
