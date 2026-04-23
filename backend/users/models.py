from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # contoh field tambahan
    phone_number = models.CharField(max_length=20, blank=True, null=True)

# Create your models here.
