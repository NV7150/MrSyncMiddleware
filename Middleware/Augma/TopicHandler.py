import asyncio

from . import TopicRouter, ClientManager


class TopicHandler:
    def __init__(self, topic):
        self.topic = topic
        self.message_buffer = ""
        self.subscribers = []

    def subscribe(self, idx):
        self.subscribers.append(idx)

    def unsubscribe(self, idx):
        if idx not in self.subscribers:
            return
        self.subscribers.remove(idx)

    def pull(self):
        return self.message_buffer

    async def __call__(self, idx: str, content, client_man: ClientManager):
        message = {
            "topic": self.topic,
            "idx": idx,
            "content": content
        }
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

