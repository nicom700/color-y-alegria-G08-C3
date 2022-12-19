from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Users(AbstractUser):
    photo = models.ImageField(upload_to='users', null=True, blank=True, default=None)
    is_admin = models.BooleanField(default=False)

    class Meta:
        managed = True
        db_table = 'users'