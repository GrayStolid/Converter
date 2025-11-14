import asyncio
from websockets.asyncio.client import connect


async def hello():
    async with connect("ws://192.168.43.90:8765") as websocket:
        await websocket.send("Hello world!")

if __name__ == "__main__":
    asyncio.run(hello())
