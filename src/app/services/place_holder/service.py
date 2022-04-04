from urllib.error import HTTPError

from app.services.place_holder.client import JsonReceivedClient
from app.services.place_holder.exceptions import PlaceHolderException


class JsonReceivedService:
    def __init__(self):
        self.client = JsonReceivedClient()

    def get_list_json_place_holder(self):
        try:
            response = self.client.get_json_place_holder()
            return response[:5]
        except HTTPError as exc:
            raise PlaceHolderException(exc)
