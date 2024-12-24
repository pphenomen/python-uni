from django.urls import path
from . import views

urlpatterns = [
    path('', views.artist_list, name='artist_list'),
    path('<int:pk>/', views.artist_detail, name='artist_detail'),
]

urlpatterns += [
    path('add/', views.add_artist, name='add_artist'),
]