from django.urls import path, include
from MusicApp.music import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create-song/', views.create_song, name='create-song'),
    path('create-album/', views.create_album, name='create-album'),
    path('album-details/<int:pk>/', views.album_details, name='album-details'),
    path('delete-album/<int:pk>/', views.delete_album, name='delete-album'),
    path('edit-album/<int:pk>/', views.edit_album, name='edit-album'),
    path('serve-song/<int:pk>/', views.serve_song, name='serve-song'),
    path('play-song/<int:pk>/', views.play_song, name='play-song'),
    path('favourite-songs/', views.favourite_songs, name='favourite-songs'),
]
