from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import DataSetViewSet

router = DefaultRouter()
router.register("dataset", DataSetViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
