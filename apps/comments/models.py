from django.db import models
from apps.posts.models import Posts
from apps.users.models import Users

# Create your models here.
class Comments(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'comments'