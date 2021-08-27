from rest_framework import serializers
from datasets.models import DataSet


class DataSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSet
        fields = "__all__"
