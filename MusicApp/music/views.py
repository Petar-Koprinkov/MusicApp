from django.http import HttpResponse
from django.shortcuts import render, redirect

from MusicApp.music.form import CreateAlbumForm, CreateSongForm, EditAlbumForm, DeleteAlbumForm
from MusicApp.music.models import Album, Song


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
        form = CreateSongForm(request.POST, request.FILES)

    if form.is_valid():
        form.save(request)
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


def serve_song(request, pk):
    song = Song.objects.get(pk=pk)
    if song:
        response = HttpResponse(song.music_file_data, content_type='audio/mpeg')
        response['Content-Disposition'] = f'inline; filename="{song.song_name}"'
        return response
    else:
        return HttpResponse('Song not found', status=404)


def play_song(request, pk):
    song = Song.objects.get(pk=pk)
    fav_songs = request.session.get('fav_songs')
    if fav_songs is not None:
        is_favourite = song.pk in fav_songs
    else:
        is_favourite = False

    context = {
        'song': song,
        'is_favourite': is_favourite

    }

    return render(request, 'songs/music-player.html', context)


def favourite_songs(request):
    if request.method == 'GET':
        fav_songs = request.session.get('fav_songs')
        context = {}

        if fav_songs is None or len(fav_songs) == 0:
            context['songs'] = []
            context['have_songs'] = False
        else:
            songs = Song.objects.filter(id__in=fav_songs)
            context['have_songs'] = True
            context['songs'] = songs

        return render(request, 'songs/favourite-songs.html', context)

    if request.method == 'POST':
        fav_songs = request.session.get('fav_songs')

        if fav_songs is None or len(fav_songs) == 0:
            fav_songs = []

        song_id = int(request.POST.get('song_id'))

        if song_id not in fav_songs:
            fav_songs.append(song_id)
        else:
            fav_songs.remove(song_id)
        request.session['fav_songs'] = fav_songs

        return redirect('index')
