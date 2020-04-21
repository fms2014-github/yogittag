from django.utils import timezone
from django.db import models
from datetime import datetime


class User(models.Model):
    # id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, null=True)
    nick_name = models.CharField(max_length=50, null=True)
    gender = models.CharField(max_length=50, null=True)
    birthday = models.CharField(max_length=50, null=True)
    address = models.TextField(null=True)
    profile_picture = models.TextField(null=True)
    cover_picture = models.TextField(null=True)
    born_year = models.IntegerField(null=True)
    followers = models.ManyToManyField("self")
