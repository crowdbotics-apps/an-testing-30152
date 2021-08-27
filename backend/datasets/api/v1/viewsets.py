from rest_framework import authentication
from datasets.models import DataSet
from .serializers import DataSetSerializer
from rest_framework import viewsets


class DataSetViewSet(viewsets.ModelViewSet):
    serializer_class = DataSetSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = DataSet.objects.all()
