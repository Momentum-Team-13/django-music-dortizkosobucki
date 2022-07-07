import re
from django.shortcuts import render, redirect, get_object_or_404
from .models import Favorite, Album 
from .forms import AlbumForm, FavoriteForm 
from webbrowser import get

def list_albums(request):
    albums = Album.objects.all()
    favorite_albums = [album for album in albums if album.check_is_user_favorite(request.user)]
    return render(request, "albums/list_albums.html", {"albums":albums, "favorite_albums":favorite_albums})

def add_album(request):
    if request.method == 'GET':
        form = AlbumForm()
    else: 
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(to='list_albums')
    return render(request, "albums/add_album.html", {"form": form})

def album_details(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'GET':
        return render(request, "albums/album_details.html", {"album":album})

def edit_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'GET':
        form = AlbumForm(instance=album)
    else:
        form = AlbumForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect(to='list_albums')
    return render(request, "albums/edit_album.html", {"form": form, "album": album})

def delete_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        album.delete()
        return redirect(to='list_albums')
    return render(request, "albums/delete_album.html", {"album": album})


def add_favorite(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == "GET":
        form = FavoriteForm
    else:
        form = FavoriteForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_albums')
    return render(request, "albums/add_favorite.html", {"form":form, "album":album})

def delete_favorite(request, pk):
    album = get_object_or_404(Album, pk=pk) 
    favorite = album.favorites.get(user=request.user)
    if request.method == 'GET':
        return render(request, "albums/delete_favorite.html", {"album":album, "pk":pk})
    if request.method == 'POST':
        favorite.delete()
        return redirect(to='list_albums')
    return render(request, "albums/delete_favorite.html", {"album":album})