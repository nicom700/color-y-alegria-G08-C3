from django.db import models
from apps.posts.models import Posts

# Create your models here.
class Media(models.Model):
    path = models.CharField(max_length=255)
    filename = models.CharField(max_length=255)
    original_filename = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    is_first = models.BooleanField(default=False)
    post = models.ForeignKey(Posts, on_delete=models.RESTRICT)

    class Meta:
        managed = True
        db_table = 'media'