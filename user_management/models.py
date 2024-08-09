from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.base_user import  AbstractBaseUser

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    class Meta:
        db_table = 'user_management'

    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)    
    email = models.CharField(max_length=100, unique=True)
    phone = models.CharField(max_length=255, default=False)
    date_activated = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=255, default=False)
    last_name = models.CharField(max_length=255, default=False)
    first_name = models.CharField(max_length=255, default=False)
    country_code = models.CharField(max_length=255, choices=country_code_choices, default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserModuleManager()