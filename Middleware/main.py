import json
import os
import asyncio
import websockets
from Auguma import TopicHanlder, TopicRouter, ClientManager, ClientTag

client_man = ClientManager()
router = TopicRouter(client_man)
TopicHanlder.register_handler(router)


async def solve_mr(websocket, path):
    client_man.register_client(ClientTag.MR, websocket)
    try:
        async for message in websocket:
            data = json.loads(message)
            router.handle(data["topic"], data["content"])
    finally:
        client_man.unregister_client(websocket)


async def solve_dt(websocket, path):
    client_man.register_client(ClientTag.DT, websocket)
    try:
        async for message in websocket:
            data = json.loads(message)
            router.handle(data["topic"], data["content"])
    finally:
        client_man.unregister_client(websocket)


HOST = os.environ.get("HOST", "localhost")
PORT_MR = int(os.environ.get("MR_PORT", 8785))
PORT_DT = int(os.environ.get("DT_PORT", 8786))

start_server_mr = websockets.serve(solve_mr, HOST, PORT_MR)
start_server_dt = websockets.serve(solve_dt, HOST, PORT_DT)
asyncio.get_event_loop().run_until_complete(start_server_mr)
asyncio.get_event_loop().run_until_complete(start_server_dt)

asyncio.get_event_loop().run_forever()
