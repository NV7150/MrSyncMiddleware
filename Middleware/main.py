import json
import os
import asyncio
import websockets
from Augma import TopicHandler, TopicRouter, ClientManager
import handlers.EventHandler

client_man = ClientManager()
router = TopicRouter(client_man)
TopicHandler.register_handler(router)


async def solve(websocket):
    register = client_man.register_client
    unregister = client_man.unregister_client
    idx = register(websocket)
    print("new websock connected")
    try:
        async for message in websocket:
            data = json.loads(message)
            print(f"payload delivered {data}")
            result = await router.handle(data["topic"], idx, data["content"])
            print(f"handle: {result}")
    finally:
        unregister(idx)

HOST = "0.0.0.0"
PORT = 8500


async def main():
    async with websockets.serve(solve, HOST, PORT):
        await asyncio.Future()

print("started program")
asyncio.run(main())
