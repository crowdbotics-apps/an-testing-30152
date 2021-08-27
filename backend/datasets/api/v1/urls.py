from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import DataSetViewSet, DataSetImageViewSet

router = DefaultRouter()
router.register("dataset", DataSetViewSet)
router.register("datasetimage", DataSetImageViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
