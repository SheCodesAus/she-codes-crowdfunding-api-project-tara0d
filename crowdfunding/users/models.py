from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):

    email = models.EmailField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    developer = models.BooleanField(default=False)    #Need to add way for admin to make created accounts developers ones
    bio = models.CharField(max_length=300)
    is_creator = models.BooleanField(default=False)

    def __str__(self):
        return self.username

        
