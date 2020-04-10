from django.utils import timezone
from django.db import models


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    gender = models.CharField(max_length=50, null=True)
    born_year = models.IntegerField(null=True)
