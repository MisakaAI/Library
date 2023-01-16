# 获取指定 Node 下所有 Node 节点

# Get node using NodeId object or a string representing a NodeId.
# https://opcua-asyncio.readthedocs.io/en/latest/api/asyncua.client.html
# get_node(nodeid)

import asyncio
from asyncua import Client

url = ""

async def main():
    async with Client(url=url) as client:
        n = client.nodes.objects
        var = await client.get_node(n).get_children()
        for i in var:
            print(i)

if __name__ == "__main__":
    asyncio.run(main())
