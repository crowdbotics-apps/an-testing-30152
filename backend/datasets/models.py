from django.conf import settings
from django.db import models


class DataSet(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=256,
    )
    description = models.CharField(
        max_length=256,
    )


class DataSetImage(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=256,
    )
    mime_type = models.CharField(
        max_length=256,
    )
    width = models.IntegerField()
    height = models.IntegerField()
    data_set = models.ForeignKey(
        "datasets.DataSet",
        on_delete=models.CASCADE,
        related_name="datasetimage_data_set",
    )


# Create your models here.
