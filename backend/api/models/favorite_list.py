from django.db import models
from .user import User


class FavoriteList(models.Model):
    # id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField(null=True)
