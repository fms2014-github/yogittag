from django.db import models


# Create your models here.
class User(models.Model):
    email = models.CharField(primary_key=True, max_length=50)
    password = models.CharField(max_length=15)
    birthday = models.DateField(null=True, blank=True)
    lasted_login = models.DateTimeField(null=True, blank=True)


# Create your models here.
class Bhour(models.Model):
    id = models.AutoField(primary_key=True)
    store = models.IntegerField()
    type = models.IntegerField()
    week_type = models.IntegerField()
    mon = models.IntegerField()
    tue = models.IntegerField()
    wed = models.IntegerField()
    thu = models.IntegerField()
    fri = models.IntegerField()
    sat = models.IntegerField()
    sun = models.IntegerField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    etc = models.TextField()


# Create your models here.
class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    menu_name = models.TextField()
    price = models.IntegerField()
    store_id = models.IntegerField()


# Create your models here.
class Review(models.Model):
    id = models.IntegerField(primary_key=True)
    store_id = models.IntegerField()
    content = models.TextField()
    user_id = models.IntegerField()
    score = models.IntegerField()
    reg_time = models.DateTimeField()


# Create your models here.
class Store(models.Model):
    id = models.IntegerField(primary_key=True)
    store_name = models.CharField(max_length=50)
    branch = models.CharField(max_length=50, null=True)
    area = models.CharField(max_length=50, null=True)
    tel = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=200, null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    category = models.CharField(max_length=200)
    review_cnt = models.IntegerField()

