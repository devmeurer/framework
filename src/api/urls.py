from django.urls import include, path

from api.routers import router as router_v1

urlpatterns = [
    path("api/", include(router_v1.urls)),
]
