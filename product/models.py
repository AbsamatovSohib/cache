from django.db import models

class Product(models.Model):

    title = models.CharField(max_length=127)

    color = models.CharField(max_length=127, null=True, blank=True)

    price = models.PositiveIntegerField()
    amount = models.PositiveIntegerField(null=True, blank=True)

    objects = models.Manager

