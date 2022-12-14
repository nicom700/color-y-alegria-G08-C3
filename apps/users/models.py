from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Users(AbstractUser):
    photo = models.CharField(max_length=255, default=None, null=True)
    is_admin = models.BooleanField(default=False)

    class Meta:
        managed = True
        db_table = 'users'