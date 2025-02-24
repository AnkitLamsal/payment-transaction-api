from django.db import models
from django.contrib.auth.models import  AbstractUser
# Create your models here.

class User(AbstractUser):
    is_staff = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    