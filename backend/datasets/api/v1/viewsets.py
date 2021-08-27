from rest_framework import authentication
from datasets.models import DataSet, DataSetImage
from .serializers import DataSetSerializer, DataSetImageSerializer
from rest_framework import viewsets


class DataSetViewSet(viewsets.ModelViewSet):
    serializer_class = DataSetSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = DataSet.objects.all()


class DataSetImageViewSet(viewsets.ModelViewSet):
    serializer_class = DataSetImageSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = DataSetImage.objects.all()
