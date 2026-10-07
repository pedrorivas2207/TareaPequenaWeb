from django.shortcuts import render
from .models import Animal, Protectora, Colaborador


def animales(request):
    animales = Animal.objects.all()
    return render(request, 'animales.html', {'animales': animales})


def protectoras(request):
    protectoras = Protectora.objects.all()
    return render(request, 'protectoras.html', {'protectoras': protectoras})


def colaboradores(request):
    colaboradores = Colaborador.objects.all()
    return render(request, 'colaboradores.html', {'colaboradores': colaboradores})