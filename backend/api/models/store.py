from django.utils import timezone
from django.db import models


class Store(models.Model):
    # id = models.IntegerField(primary_key=True)
    store_name = models.CharField(max_length=50)
    branch = models.CharField(max_length=50, null=True)
    area = models.CharField(max_length=50, null=True)
    tel = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=200, null=True)
    latitude = models.FloatField(max_length=10, null=True)
    longitude = models.FloatField(max_length=10, null=True)
    category = models.CharField(max_length=200, null=True)
    pictures = models.TextField(null=True,blank=True)
    group_seat = models.IntegerField(null=True)
    reservation = models.IntegerField(null=True)
    delivery = models.IntegerField(null=True)
    take_away = models.IntegerField(null=True)
    parking = models.IntegerField(null=True)

    @property
    def category_list(self):
        return self.category.split("|") if self.category else []
