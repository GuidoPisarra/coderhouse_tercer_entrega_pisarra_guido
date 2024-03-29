from django.shortcuts import render
from AppTercerEntrega.models import *
from django.http import HttpResponse
from django.template import loader

from AppTercerEntrega.forms import *


# Create your views here.


# Vista para el home
def home(request):
    return render(request, "base.html")


# Ingresar como usuario
def login(request):
    if request.method == "POST":
        mi_formulario = Formulario_ingreso(request.POST)

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            try:
                usuario = Usuario.objects.get(email__iexact=datos["email"])
            except Usuario.DoesNotExist:
                usuario = None
            if usuario and usuario.validar_contraseña(datos["contrasenia"]):
                cursos = usuario.cursos.all()
                if usuario.es_profesor:
                    return render(
                        request,
                        "profesor.html",
                        {"usuario": usuario, "cursos": cursos},
                    )
                else:
                    cursos_totales = Curso.objects.all()
                    return render(
                        request,
                        "alumno.html",
                        {
                            "usuario": usuario,
                            "cursos": cursos,
                            "cursos_totales": cursos_totales,
                        },
                    )
            else:
                return render(
                    request,
                    "login.html",
                    {"error": ["Usuario o contraseña incorrectos."]},
                )
    else:
        return render(request, "login.html")


# Creación de usuario
def register(request):
    if request.method == "POST":
        mi_formulario = Formulario_registro(request.POST, request.FILES)
        if mi_formulario.is_valid():
            print("Formulario válido")
            datos = mi_formulario.cleaned_data
            print("Datos recibidos:", datos)
            usuario = Usuario(
                nombre=datos["nombre"],
                apellido=datos["apellido"],
                email=datos["email"],
                contrasenia=datos["contrasenia"],
                es_profesor=datos["es_profesor"],
                imagen=request.FILES.get("imagen"),
            )
            usuario.save()
            return render(request, "login.html")
        else:
            print("Formulario inválido")
            print("Errores:", mi_formulario.errors)
            print("Datos:", mi_formulario.cleaned_data)
            return render(
                request,
                "register.html",
                {"error": ["Ocurrió un error al registrar el usuario."]},
            )
    else:
        return render(request, "register.html")


def agregar_curso(request):
    if request.method == "POST":
        mi_formulario = Formulario_agregar_curso(request.POST, request.FILES)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            nuevo_curso = Curso(nombre=datos["nombre_curso"], camada=datos["camada"])
            nuevo_curso.save()
            usuario = Usuario.objects.get(email__iexact=datos["email"])
            usuario.cursos.add(nuevo_curso)
            cursos = usuario.cursos.all()

            return render(request, "profesor.html", {"cursos": cursos})
        else:
            print("Formulario inválido")
            print("Errores:", mi_formulario.errors)
            print("Datos:", mi_formulario.cleaned_data)
            return render(
                request,
                "profesor.html",
                {"error": ["Ocurrió un error al registrar el curso."]},
            )
    else:
        return render(request, "profesor.html", {"cursos": usuario.cursos})


def detalle_curso_profesor(request, id, email):
    curso = Curso.objects.get(id=id)
    usuario = Usuario.objects.get(email=email)
    alumnos_en_curso = curso.usuario_set.all()

    """ cursos = Curso.objects.all()
    diccionario = {"cursos": cursos}
    plantilla = loader.get_template("cursos.html")
    documento = plantilla.render(diccionario)
    return HttpResponse(documento) """

    print(curso)
    print(usuario)
    print(alumnos_en_curso)

    return render(
        request,
        "detalle_curso_profesor.html",
    )


def curso_inscripcion(request, id, email):
    curso = Curso.objects.get(id=id)
    usuario = Usuario.objects.get(email=email)
    cursos = usuario.cursos.all()
    cursos_totales = Curso.objects.all()

    print(curso)
    print(usuario)
    usuario.cursos.add(curso)
    return render(
        request,
        "alumno.html",
        {
            "usuario": usuario,
            "cursos": cursos,
            "cursos_totales": cursos_totales,
        },
    )
