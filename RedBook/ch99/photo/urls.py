from django.urls import path
from django.views.generic import ListView, DetailView
from photo.models import Album, Photo

app_name = 'photo'
urlpatterns = [
    # Example: /photo/
    path('', ListView.as_view(model=Album), name='index'),

    # Example: /photo/album/, same as /photo/
    path('album', ListView.as_view(model=Album), name='album_list'),

    # Example: /photo/album/99/
    path('album/<int:pk>/', DetailView.as_view(model=Album), name='album_detail'),

    # Example: /photo/photo/99/
    path('photo/<int:pk>/', DetailView.as_view(model=Photo), name='photo_detail'),
]