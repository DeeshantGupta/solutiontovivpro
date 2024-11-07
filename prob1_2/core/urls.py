from django.urls import path
from . import views

urlpatterns = [
    path('songs/', views.SongListView.as_view(), name='songList'),
    path('song/<str:title>/', views.get_song_by_title, name='details'),
    path('rate/<str:title>/', views.rate_song, name='rating')
]
