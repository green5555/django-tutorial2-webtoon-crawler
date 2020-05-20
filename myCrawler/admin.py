from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Episode, Favorite

@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'service')

@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'created_at', 'webtoon')