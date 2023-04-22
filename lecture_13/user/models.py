from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    bio = models.CharField(null=False, blank=True, default='', max_length=255)
    owner = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', max_length=1000, null=True)
    resume = models.FileField(upload_to='files/', max_length=1000, null=True)



