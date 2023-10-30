import json
from Augma import TopicHandler, ClientManager


@TopicHandler.topic_handler("position")
async def handle_position(idx: str, content: dict):
    return json.dumps({
        "topic": "position",
        "content": {
            "cid": idx,
            "position": content["position"],
            "rotation": content["rotation"],
            "originLat": content["originLat"],
            "originLon": content["originLon"]
        }
    })
