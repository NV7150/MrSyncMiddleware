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

    def handle(self, topic: str, content: dict):
        self.handlers[topic](content, self.client_man)
