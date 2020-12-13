from django.contrib.auth.models import User
from django.db import models


class Python(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)


class UserProfile(models.Model):
    date_of_birth = models.DateTimeField()
    profile_image = models.ImageField(
        upload_to='profile_pics/'
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
