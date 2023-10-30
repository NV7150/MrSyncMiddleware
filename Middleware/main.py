import json
import os
import asyncio
import websockets
from Augma import TopicHandler, TopicRouter, ClientManager
import event.EventHandler

client_man = ClientManager()
router = TopicRouter(client_man)
TopicHandler.register_handler(router)


async def solve(websocket, register, unregister):
    idx = register(websocket)
    print("new websock connected")
    try:
        async for message in websocket:
            data = json.loads(message)
            print(f"payload delivered {data}")
            await router.handle(data["topic"], idx, data["content"])
    finally:
        unregister(idx)


async def solve_mr(websocket):
    await solve(websocket, client_man.register_client_mr, client_man.unregister_client_mr)


async def solve_dt(websocket):
    await solve(websocket, client_man.register_client_dt, client_man.unregister_client_dt)

HOST = "0.0.0.0"
PORT_MR = 8500
PORT_DT = 8501


async def mr_start():
    print("ready mr")
    async with websockets.serve(solve_mr, HOST, PORT_MR):
        await asyncio.Future()


async def dt_start():
    print("ready dt")
    async with websockets.serve(solve_dt, HOST, PORT_DT):
        await asyncio.Future()


async def main():
    print(f"topics: {router.available_topics()} is available")
    await asyncio.gather(dt_start(), mr_start())

print("started program")
asyncio.run(main())
