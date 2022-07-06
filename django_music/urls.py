"""django_music URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from albums import views as album_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', album_views.list_albums, name='list_albums'),
    path('albums/add/', album_views.add_album, name='add_album'),
    path('albums/<int:pk>/individual', album_views.album_details, name="album_details"),
    path('albums/<int:pk>/edit/', album_views.edit_album, name='edit_album'),
    path('albums/<int:pk>/delete/',album_views.delete_album,name='delete_album'),
    path('albums/<int:pk>/add_fav', album_views.add_favorite, name='add_favorite'),
    path('albums/<int:pk>/delete_fav', album_views.delete_favorite, name='delete_favorite'),
]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
