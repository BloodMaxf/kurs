from django.db import models
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):

    RPG ='RPG'
    Shooter = 'Shooter'
    Adventure = 'Adventure'
    SoulsLike = 'SoulsLike'
    Horror = 'Horror'
    Roguelike = 'Roguelike'

    CHOICE_GROUP = {
        (RPG, 'RPG'),
        (Shooter, 'Shooter'),
        (Adventure, "Adventure"),
        (SoulsLike, 'SoulsLike'),
        (Horror, 'Horror'),
        (Roguelike,'Roguelike')
    }

    title = models.CharField(max_length=255)
    cover = models.ImageField(upload_to='static/images/')
    price = models.IntegerField()
    body = models.TextField(default="")
    key = models.CharField(max_length=255, unique=True)
    Technical_desc = models.TextField(default="")
    group = models.CharField(max_length=20, choices=CHOICE_GROUP, default=RPG)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])

class Purchased_products(models.Model):

    title = models.CharField(max_length=255)
    key = models.CharField(max_length=255)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default='')
    def __str__(self):
        return str(self.title)

