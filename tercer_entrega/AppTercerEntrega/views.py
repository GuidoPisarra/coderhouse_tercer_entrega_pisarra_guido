from django.shortcuts import render
from AppTercerEntrega.models import *
from django.http import HttpResponse
from django.template import loader

from AppTercerEntrega.forms import Formulario_registro


# Create your views here.
def home(request):
    return render(request, "base.html")


def login(request):
    return render(request, "register.html")


def register(request):
    return render(request, "register.html")


def register_user(request):
    if request.method == "POST":
        mi_formulario = Formulario_registro(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            usuario = Usuario(
                nombre=datos["nombre"],
                apellido=datos["apellido"],
                email=datos["email"],
                contrasenia=datos[
                    "contrasenia"
                ],  # Corregido el acceso al campo de contraseña
                es_profesor=datos["es_profesor"],
                imagen=request.FILES.get("imagen"),
            )
            usuario.save()
    else:
        mi_formulario = Formulario_registro()

    return render(request, "base.html", {"mi_formulario": mi_formulario})
