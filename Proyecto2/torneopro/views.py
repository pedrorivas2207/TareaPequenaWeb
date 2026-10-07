from django.shortcuts import render
from .models import Equipo, Jugador, Torneo


def equipos(request):
    equipos = Equipo.objects.all()
    return render(request, 'equipos.html', {'equipos': equipos})


def jugadores(request):
    jugadores = Jugador.objects.all()
    return render(request, 'jugadores.html', {'jugadores': jugadores})


def torneos(request):
    torneos = Torneo.objects.all()
    return render(request, 'torneos.html', {'torneos': torneos})