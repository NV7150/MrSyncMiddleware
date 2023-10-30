import json
import asyncio
from Augma import TopicHandler, ClientManager


@TopicHandler.topic_handler("event")
def handle_event(idx: str, content: dict):
    return json.dumps(
        {
            "topic": "handlers",
            "content": {
                "name": content["name"]
            }
        })

