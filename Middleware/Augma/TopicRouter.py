from typing import Callable
import websockets


class TopicRouter:
    def __init__(self, client_man):
        self.handlers = {}
        self.client_man = client_man

    def register_handler(self, topic: str, handler):
        self.handlers[topic] = handler

    def register_handler_all(self, handlers: dict):
        self.handlers.update(handlers)

    def available_topics(self):
        return list(self.handlers.keys())

    async def handle(self, topic: str, idx: str, content: dict):
        if topic not in self.handlers.keys():
            return False
        await self.handlers[topic](idx, content, self.client_man)
        return True
