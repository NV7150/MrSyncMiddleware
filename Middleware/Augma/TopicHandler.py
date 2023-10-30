import asyncio

from . import TopicRouter, ClientManager

handlers = {}


def topic_handler(s):
    def _topic_handler(f):
        handlers.setdefault(s, TopicHandler(f))
        return f
    return _topic_handler


def register_handler(router: TopicRouter):
    router.register_handler_all(handlers)


class TopicHandler:
    def __init__(self, f):
        self.message_buffer = ""
        self.subscribers = []
        self.f = f

    def subscribe(self, idx):
        self.subscribers.append(idx)

    def unsubscribe(self, idx):
        if idx not in self.subscribers:
            return
        self.subscribers.remove(idx)

    def pull(self):
        return self.message_buffer

    async def __call__(self, idx: str, content: dict, client_man: ClientManager):
        message = self.f(idx, content)
        tasks = []
        for subscriber in self.subscribers:
            async def handle_task():
                result = await client_man.send(
                    subscriber,
                    message
                )
                if not result:
                    self.unsubscribe(subscriber)

            task = asyncio.create_task(handle_task())

            tasks.append(task)
        await asyncio.gather(*tasks)
        self.message_buffer = message

