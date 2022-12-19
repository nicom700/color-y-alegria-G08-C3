from django.db import models
from apps.posts.models import Posts

# Create your models here.
class Media(models.Model):
    photo = models.ImageField(upload_to='posts', null=True, blank=True, default=None)
    is_first = models.BooleanField(default=False)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='photos')

    class Meta:
        managed = True
        db_table = 'media'