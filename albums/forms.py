from django import forms
from .models import Album, Favorite

class AlbumForm(forms.ModelForm):
    class Meta: 
        model = Album
        fields = [
            'title', 
            'artist', 
            'year',
            'cover',
        ]


class FavoriteForm(forms.ModelForm):
    class Meta:
        model = Favorite
        fields = [
            'user',
            'album',
        ]