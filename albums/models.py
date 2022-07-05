from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime

class Album(models.Model):
    title = models.CharField(max_length=300)
    artist = models.CharField(max_length=300)
    year = models.CharField(max_length=300, null=True, blank=True)
    cover = models.ImageField(upload_to='images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'
    
    def check_is_user_favorite(self, user):
        for favorite in self.favorites.all():
            if favorite.album == self:
                return True


class User(AbstractUser):
    pass


class Favorite(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="favorites", null=True, blank=True)
    album = models.ForeignKey("Album", on_delete=models.CASCADE, related_name="favorites", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

