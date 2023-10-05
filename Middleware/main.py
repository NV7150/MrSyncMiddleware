import json
import os
import asyncio
import websockets
from Auguma import TopicHanlder, TopicRouter, ClientManager

client_man = ClientManager()
router = TopicRouter(client_man)
TopicHanlder.register_handler(router)


async def solve(websocket, path, register, unregister):
    idx = register(websocket)
    try:
        async for message in websocket:
            data = json.loads(message)
            await router.handle(data["topic"], idx, data["content"])
    finally:
        unregister(idx)


async def solve_mr(websocket, path):
    await solve(websocket, path, client_man.register_client_mr, client_man.unregister_client_mr)


async def solve_dt(websocket, path):
    await solve(websocket, path, client_man.register_client_dt, client_man.unregister_client_dt)

HOST = os.environ.get("HOST", "localhost")
PORT_MR = int(os.environ.get("MR_PORT", 8785))
PORT_DT = int(os.environ.get("DT_PORT", 8786))

start_server_mr = websockets.serve(solve_mr, HOST, PORT_MR)
start_server_dt = websockets.serve(solve_dt, HOST, PORT_DT)
asyncio.get_event_loop().run_until_complete(start_server_mr)
asyncio.get_event_loop().run_until_complete(start_server_dt)

asyncio.get_event_loop().run_forever()
