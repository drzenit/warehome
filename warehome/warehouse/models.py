from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, default="not")
    season = models.CharField(max_length=20, default="not")
    qrCodePath = models.CharField(max_length=200)

    def __str__(self):
        return self.name
