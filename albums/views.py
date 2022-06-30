from django.shortcuts import render, redirect, get_object_or_404
from .models import Album
from .forms import AlbumForm

def list_albums(request):
    albums = Album.objects.all()
    return render(request, "albums/list_albums.html", {"albums":albums})

def add_album(request):
    if request.method == 'GET':
        form = AlbumForm()
    else: 
        form = AlbumForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_albums')
    return render(request, "albums/add_album.html", {"form": form})

def album_details(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'GET':
        return render(request, "albums/album_details.html", {"album":album})



# Create your views here.
