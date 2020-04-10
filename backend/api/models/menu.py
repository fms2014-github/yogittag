from django.utils import timezone
from django.db import models
from .store import Store


class Menu(models.Model):
    # id = models.IntegerField(primary_key=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    menu_name = models.TextField(null=True)
    price = models.IntegerField(null=True)
