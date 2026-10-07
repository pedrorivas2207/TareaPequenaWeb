from django.urls import path
from . import views

urlpatterns = [
    path('equipos/', views.equipos, name='equipos'),
    path('jugadores/', views.jugadores, name='jugadores'),
    path('torneos/', views.torneos, name='torneos'),
]