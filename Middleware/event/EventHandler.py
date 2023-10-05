import json
from ..Auguma import TopicHanlder, ClientManager


@TopicHanlder.topic_handler("event")
async def handle_event(idx: str, content: dict, client_man: ClientManager):
    event_name = content["name"]
    await client_man.send_dt(json.dumps({
        "topic": "event",
        "content": {
            "name": event_name
        }
    }))


@TopicHanlder.topic_handler("position")
async def handle_position(idx: str, content: dict, client_man: ClientManager):
    await client_man.send_dt(json.dumps({
        "topic": "position",
        "content": {
            "cid": idx,
            "position": content["position"],
            "rotation": content["rotation"]
        }
    }))
