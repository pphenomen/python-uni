from django.shortcuts import get_object_or_404, redirect, render

from music_app.forms import ArtistForm

# Create your views here.
from .models import Artist

def artist_list(request):
    artists = Artist.objects.all()
    return render(request, 'music_app/artist_list.html', {'artists': artists})

def add_artist(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('artist_list')
    else:
        form = ArtistForm()
    return render(request, 'music_app/add_artist.html', {'form': form})


def artist_detail(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    return render(request, 'music_app/artist_detail.html', {'artist': artist})

