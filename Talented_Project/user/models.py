from django.db import models


class User(models.Model):

    username = models.CharField(max_length=100)
    password = models.CharField(max_length=200)
    trackid = models.CharField(max_length=30)