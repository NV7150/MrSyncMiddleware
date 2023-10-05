from enum import Enum
import asyncio
import uuid


class ClientManager:
    def __init__(self):
        self.mr_clients = {}
        self.dt_clients = {}

    @staticmethod
    def register_client(client_dict, client):
        idx = str(uuid.uuid4())
        client_dict.setdefault(idx, client)
        return idx

    @staticmethod
    def unregister_client(client_dict, idx):
        del client_dict[idx]

    def register_client_mr(self, client):
        return self.register_client(self.mr_clients, client)

    def unregister_client_mr(self, idx):
        self.unregister_client(self.mr_clients, idx)

    def register_client_dt(self, client):
        return self.register_client(self.dt_clients, client)

    def unregister_client_dt(self, idx):
        self.unregister_client(self.dt_clients, idx)

    async def send_dt(self, payload):
        await asyncio.gather(*(dt.send(payload) for dt in self.dt_clients))

    async def send_mr(self, payload):
        await asyncio.gather(*(mr.send(payload) for mr in self.mr_clients))

