from enum import Enum
import asyncio


class ClientTag(Enum):
    MR = 0
    DT = 1


class ClientManager:
    def __init__(self):
        self.mr_clients = []
        self.dt_clients = []

    def register_client(self, tag: ClientTag, client):
        if tag == ClientTag.MR:
            self.mr_clients.append(client)
        elif tag == ClientTag.DT:
            self.dt_clients.append(client)

    def unregister_client_mr(self, client):
        self.mr_clients.remove(client)

    def unregister_client_dt(self, client):
        self.dt_clients.remove(client)

    async def send_dt(self, payload):
        await asyncio.gather(*(dt.send(payload) for dt in self.dt_clients))

    async def send_mr(self, payload):
        await asyncio.gather(*(mr.send(payload) for mr in self.mr_clients))

