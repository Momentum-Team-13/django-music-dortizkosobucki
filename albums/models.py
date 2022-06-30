from django.db import models


class Album(models.Model):
    title = models.CharField(max_length=300)
    artist = models.CharField(max_length=300)
    created_at = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.title}'

    # artist = models.ManyToManyField("Artist", on_delete=models.CASCADE, related_name="albums", null=True, blank=True)