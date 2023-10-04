import json
from ..Auguma import TopicHanlder, ClientManager


@TopicHanlder.topic_handler("event")
async def handle_event(content: dict, client_man: ClientManager):
    event_name = content["name"]
    await client_man.send_dt(json.dumps({
        "topic": "event",
        "content": {
            "name": event_name
        }
    }))

