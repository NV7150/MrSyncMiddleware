from .TopicHandler import TopicHandler

RESERVATION_TOPIC = ["subscribe", "unsubscribe", "publish", "pull"]


class TopicRouter:
    def __init__(self, client_man):
        self.handlers = {}
        self.client_man = client_man
        self.reserved = RESERVATION_TOPIC

    def register_topic(self, topic: str):
        if topic in self.reserved:
            raise Exception("tried to add reserved topic")
        self.handlers.setdefault(topic, TopicHandler(topic))

    def available_topics(self):
        return list(self.handlers.keys())

    def subscribe_return(self, idx):
        topic_name = f"return-{idx}"
        self.register_topic(topic_name)
        self.handlers[topic_name].subscribe(idx)
        self.reserved.append(topic_name)

    async def return_content(self, idx, content):
        await self.handlers[f"return-{idx}"](idx, content, self.client_man)

    async def handle(self, topic: str, idx: str, content):
        if topic == "subscribe":
            await self.handle_subscribe(idx, content)
            return True

        if topic == "unsubscribe":
            await self.handle_unsubscribe(idx, content)
            return True

        if topic in self.reserved:
            return False

        if topic not in self.handlers.keys():
            return False
        await self.handlers[topic](idx, content, self.client_man)
        return True

    async def handle_subscribe(self, idx: str, content):
        topic = content["topic"]

        if topic in RESERVATION_TOPIC:
            return False

        if topic not in self.handlers.keys():
            return False
        self.handlers[topic].subscribe(idx)
        return True

    async def handle_unsubscribe(self, idx: str, content):
        topic = content["topic"]

        if topic in RESERVATION_TOPIC:
            return False

        if topic not in self.handlers.keys():
            return False
        self.handlers[topic].unsubscribe(idx)
        return True



