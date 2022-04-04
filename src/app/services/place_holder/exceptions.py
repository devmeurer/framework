from rest_framework import status
from rest_framework.exceptions import APIException


class PlaceHolderException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "placer_holder_get_json_error"
