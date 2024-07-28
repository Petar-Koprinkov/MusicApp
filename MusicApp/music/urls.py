from django.urls import path, include
from MusicApp.music import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create-song/', views.create_song, name='create-song'),
    path('create-album/', views.create_album, name='create-album'),
    path('<int:pk>/', include([
        path('album-details/', views.album_details, name='album-details'),
        path('delete-album/', views.delete_album, name='delete-album'),
        path('edit-album/', views.edit_album, name='edit-album'),
    ]))
]