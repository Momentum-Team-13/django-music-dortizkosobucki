from django.db import models
import datetime

class Album(models.Model):
    title = models.CharField(max_length=300)
    artist = models.CharField(max_length=300)
    year = models.CharField(max_length=300, null=True, blank=True)
    cover = models.ImageField(upload_to='images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'
