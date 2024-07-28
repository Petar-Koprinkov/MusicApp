from django.shortcuts import render, redirect

from MusicApp.music.form import CreateAlbumForm, CreateSongForm, EditAlbumForm, DeleteAlbumForm
from MusicApp.music.models import Album


def index(request):
    albums = Album.objects.all()

    context = {
        'albums': albums
    }
    return render(request, 'common/index.html', context)


def create_song(request):
    if request.method == 'GET':
        form = CreateSongForm()
    else:
        form = CreateSongForm(request.POST)

    if form.is_valid():
        form.save()
        return redirect('index')

    context = {
        'form': form
    }
    return render(request, 'songs/create-song.html', context)


def create_album(request):
    if request.method == 'GET':
        form = CreateAlbumForm()
    else:
        form = CreateAlbumForm(request.POST)

    if form.is_valid():
        form.save()
        return redirect('index')

    context = {
        'form': form
    }



    return render(request, 'albums/create-album.html', context)


def album_details(request, pk):
    album = Album.objects.get(pk=pk)

    context = {
        'album': album
    }
    return render(request, 'albums/album-details.html', context)


def edit_album(request, pk):
    album = Album.objects.get(pk=pk)

    if request.method == 'GET':
        form = EditAlbumForm(instance=album)
    else:
        form = EditAlbumForm(request.POST, instance=album)

    if form.is_valid():
        form.save()
        return redirect('index')

    context = {
        'form': form,
        'album': album
    }
    return render(request, 'albums/edit-album.html', context)


def delete_album(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'GET':
        form = DeleteAlbumForm(instance=album)
    else:
        form = DeleteAlbumForm(request.POST, instance=album)

    if form.is_valid():
        album.delete()
        return redirect('index')

    context = {
        'form': form,
        'album': album
    }
    return render(request, 'albums/delete-album.html', context)

