from django.db import models

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    inventory = models.SmallIntegerField()

    def __str__(self)-> str:
        return self.title


class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255)

    def __str__(self)-> str:
        return self.title