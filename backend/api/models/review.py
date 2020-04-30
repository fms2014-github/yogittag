from django.utils import timezone
from django.db import models
from .store import Store
from .user import User


class Review(models.Model):
    # id = models.IntegerField(primary_key=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField(null=True)
    content = models.TextField(null=True)
    reg_time = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['reg_time']

    def __str__(self):
        return self.content
