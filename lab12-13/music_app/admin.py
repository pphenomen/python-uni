from django.contrib import admin

# Register your models here.
from .models import Artist, Album, Song

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'genre', 'birth_date')
    search_fields = ('name', 'genre')
    list_filter = ('genre',)


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'artist')
    list_filter = ('release_date',)
    search_fields = ('title',)


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration', 'album')
    list_filter = ('album',)
    search_fields = ('title',)