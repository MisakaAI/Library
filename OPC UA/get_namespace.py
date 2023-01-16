# 获取命名空间索引

import asyncio
from asyncua import Client

url = ""

async def main():
    async with Client(url=url) as client:
        namespace = await client.get_namespace_array()
        nsidx = await client.get_namespace_index(namespace[0])
        print(f"Namespace Index for '{namespace[0]}': {nsidx}")

if __name__ == "__main__":
    asyncio.run(main())