from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.

class Product(models.Model):

    title = models.CharField(max_length=255)
    cover = models.ImageField(upload_to='static/images/')
    price = models.IntegerField()
    key = models.CharField(max_length=255)

    def __str__(self):
        return self.title


