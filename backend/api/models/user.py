from django.utils import timezone
from django.db import models
from datetime import datetime


class User(models.Model):
    # id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=10, null=True)
    nick_name = models.CharField(max_length=16, null=True)
    gender = models.CharField(max_length=5, null=True)
    birthday = models.CharField(max_length=5, null=True)
    profile_picture = models.CharField(max_length=300, null=True)
    cover_picture = models.CharField(max_length=300, null=True)
    born_year = models.CharField(max_length=5, null=True)
    followers = models.ManyToManyField("self", symmetrical=False)
    email = models.CharField(max_length=100, blank=True)
    google_refresh_token = models.CharField(max_length=200, null=True)
    naver_refresh_token = models.CharField(max_length=200, null=True)
    isCompleted = models.BooleanField(null = True)
