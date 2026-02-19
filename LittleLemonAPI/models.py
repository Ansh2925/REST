from django.db import models

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    inventory = models.SmallIntegerField()