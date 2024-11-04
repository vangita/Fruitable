from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.hashers import make_password
from django.utils import timezone

class User(AbstractUser):
    age = models.IntegerField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    city = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    last_active_datetime = models.DateTimeField(null=True, blank=True)

    # REQUIRED_FIELDS = ('email',)

    def update_last_active(self):
        self.last_active_datetime = timezone.now()
        self.save()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email