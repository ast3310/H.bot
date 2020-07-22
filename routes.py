from app import app, controler
from flask import request
import json
import config
from core.types import EventType
from core.data import EventData


@app.route('/', methods=['GET', 'POST'])
def index():
    data = json.loads(request.data.decode("utf-8"))

    if data['type'] == EventType.CONFIRMATION:
        return config.VkConfig.RETURN_STR
    else:
        event = EventData.from_raw(data)
        controler.recognition(event)

        return 'ok'
