import requests

from api.settings import PLACE_HOLDER_URL


class JsonReceivedClient:
    def __init__(self):
        self.url = PLACE_HOLDER_URL

    def get_json_place_holder(self):
        response = requests.get(self.url)
        payload = response.json()

        return payload
