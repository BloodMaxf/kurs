from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.

class Product(models.Model):

    RPG ='RPG'
    Shooter = 'Shooter'
    Adventure = 'Adventure'
    SoulsLike = 'SoulsLike'
    Horror = 'Horror'

    CHOICE_GROUP = {
        (RPG, 'RPG'),
        (Shooter, 'Shooter'),
        (Adventure, "Adventure"),
        (SoulsLike, 'SoulsLike'),
        (Horror, 'Horror')
    }

    title = models.CharField(max_length=255)
    cover = models.ImageField(upload_to='static/images/')
    price = models.IntegerField()
    genre = models.CharField(max_length=30, default="")
    body = models.TextField(default="")
    key = models.CharField(max_length=255, unique=True)
    Technical_desc = models.TextField(default="")
    availability = models.BooleanField(default=True)
    group = models.CharField(max_length=20, choices=CHOICE_GROUP, default=RPG)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])


