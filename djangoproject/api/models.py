# Create your models here.
from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class SNT(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class User_snt(AbstractBaseUser):
    username = None
    last_name = models.CharField(max_length=30, blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    middle_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=15, blank=True)
    password = models.CharField(max_length=255)
    snt_id = models.ForeignKey(SNT, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)
    is_gover = models.BooleanField(default=False)
    is_verif = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
