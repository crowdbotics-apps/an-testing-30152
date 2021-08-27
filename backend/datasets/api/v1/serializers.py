from rest_framework import serializers
from datasets.models import DataSet, DataSetImage


class DataSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSet
        fields = "__all__"


class DataSetImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSetImage
        fields = "__all__"
