from django.db import models
from apps.categories.models import Categories
from apps.users.models import Users

# Create your models here.
class Posts(models.Model):
    slug = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    body = models.TextField()
    is_published = models.BooleanField(default=False)
    allow_comments = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(Users, on_delete=models.RESTRICT)
    category = models.ForeignKey(Categories, on_delete=models.RESTRICT)
    
    class Meta:
        managed = True
        db_table = 'posts'