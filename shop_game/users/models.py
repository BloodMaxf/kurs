from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
class Personal_area(models.Model):

    title = models.CharField(max_length=255)
    key = models.CharField(max_length=255)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    def __str__(self):
        return str(self.user_id)
