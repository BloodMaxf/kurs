from django.db import models
from django.urls import reverse
# Create your models here.
class Personal_area(models.Model):

    title = models.CharField(max_length=255)
    key = models.CharField(max_length=255)
    user_id = models.ForeignKey('auth.User', on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.title
