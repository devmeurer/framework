import datetime
import logging

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from app.services.place_holder.service import JsonReceivedService

logger = logging.getLogger(__name__)


class JsonReceivedViewSet(viewsets.GenericViewSet):
    http_method_names = ["get"]

    @action(detail=True, url_name="json-payload", url_path="json/payload")
    def json_received(self):
        logger.warning("API was called" + str(datetime.datetime.now()) + " hours!")
        payload = JsonReceivedService().get_list_json_place_holder()
        return Response({"payload": payload}, status=status.HTTP_200_OK)
