from enum import Enum
import asyncio
import uuid


class ClientManager:
    def __init__(self):
        self.clients = {}

    def register_client(self, client):
        idx = str(uuid.uuid4())
        self.clients.setdefault(idx, client)
        return idx

    def unregister_client(self, idx):
        del self.clients[idx]

    def send(self, idx, payload):
        if idx not in self.clients.keys():
            return False
        self.clients[idx].send(payload)
        return True

    async def send_all(self, payload):
        await asyncio.gather(*(cl.send(payload) for cl in self.clients.values()))


