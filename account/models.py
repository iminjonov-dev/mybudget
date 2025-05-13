from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True)
    otp_code = models.CharField(max_length=6, blank=True, null=True, unique=False)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username


