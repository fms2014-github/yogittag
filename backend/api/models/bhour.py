from django.utils import timezone
from django.db import models
from .store import Store


class BHour(models.Model):
    # id = models.IntegerField(primary_key=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    type = models.IntegerField(null=True)
    week_type = models.IntegerField(null=True)
    mon = models.CharField(max_length=10, null=True)
    tue = models.CharField(max_length=10, null=True)
    wed = models.CharField(max_length=10, null=True)
    thu = models.CharField(max_length=10, null=True)
    fri = models.CharField(max_length=10, null=True)
    sat = models.CharField(max_length=10, null=True)
    sun = models.CharField(max_length=10, null=True)
    start_time = models.CharField(max_length=50, null=True)
    end_time = models.CharField(max_length=50, null=True)
    etc = models.TextField(null=True)
