from rest_framework.routers import DefaultRouter

from app.viewsets import JsonReceivedViewSet

router = DefaultRouter()
router.register("json/", JsonReceivedViewSet, basename="json")
