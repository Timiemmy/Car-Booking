from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager



class CustomUser(AbstractUser):
    username = None
    email = models.EmailField('email address', unique=True)
    phone_number = models.IntegerField(null=True, blank=True    )
    address = models.CharField(max_length=255, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


    def __str__(self):
        return self.email