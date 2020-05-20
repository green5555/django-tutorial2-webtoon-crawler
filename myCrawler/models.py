from django.db import models

# Create your models here.
class Favorite(models.Model):
    title = models.CharField(blank=False, max_length=200, null=False, unique=True)
    url = models.TextField(blank=False, max_length=200, unique=True)
    service = models.CharField(blank=False, max_length=20)

class Episode(models.Model):
    title = models.CharField(blank=False, max_length=200, null=False)
    url = models.TextField(blank=False, max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    webtoon = models.ForeignKey('Favorite', on_delete=models.CASCADE)