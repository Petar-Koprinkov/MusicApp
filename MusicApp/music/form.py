from django import forms

from MusicApp.music.models import Song, Album


class BaseAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'


class CreateAlbumForm(BaseAlbumForm):
    pass


class BaseSongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = '__all__'


class CreateSongForm(BaseSongForm):
    pass


class EditAlbumForm(BaseAlbumForm):
    pass


class DeleteAlbumForm(BaseAlbumForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].disabled = True


