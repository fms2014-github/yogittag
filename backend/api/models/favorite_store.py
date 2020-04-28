from django.db import models
from .favorite_list import FavoriteList
from .store import Store
from .user import User


class FavoriteStore(models.Model):
    # id = models.IntegerField(primary_key=True)
    favorite_list_id = models.ForeignKey(
        FavoriteList, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
