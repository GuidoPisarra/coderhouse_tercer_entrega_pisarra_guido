from django.shortcuts import render
from AppTercerEntrega.models import *
from AppTercerEntrega.forms import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.db.models import Q

# Create your views here.


# Vista para el home
def home(request):
    return render(request, "base.html")


# Ingresar como usuario
def user_login(request):

    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                usuario = Usuario.objects.get(user=user)
                if usuario.es_profesor:
                    cursos = usuario.cursos.all()

                    return render(
                        request,
                        "profesor.html",
                        {"cursos": cursos, "usuario": user, "imagen": usuario.imagen},
                    )
                else:
                    cursos = usuario.cursos.all()
                    cursos_disponibles = Curso.objects.all()

                    return render(
                        request,
                        "alumno.html",
                        {
                            "cursos": cursos,
                            "cursos_disponibles": cursos_disponibles,
                            "usuario": user,
                            "imagen": usuario.imagen,
                        },
                    )
            else:
                return render(
                    request,
                    "login.html",
                    {
                        "form": form,
                        "error": ["Usuario o contraseña incorrectos."],
                        "mensaje": [],
                    },
                )
        else:
            return render(
                request,
                "login.html",
                {
                    "form": form,
                    "error": ["Usuario o contraseña incorrectos."],
                    "mensaje": [],
                },
            )
    else:
        form = AuthenticationForm()
        return render(
            request,
            "login.html",
            {
                "form": form,
                "error": [],
                "mensaje": [],
            },
        )


# Registrar usuario
def register(request):
    if request.method == "POST":
        mi_formulario = Formulario_registro(request.POST, request.FILES)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            nuevo_usuario = User.objects.create_user(
                username=datos["email"],
                email=datos["email"],
                password=datos["password"],
            )
            nuevo_usuario.first_name = datos["nombre"]
            nuevo_usuario.last_name = datos["apellido"]
            nuevo_usuario.save()

            # Crear instancia UserProfile asociada al nuevo usuario
            nuevo_userprofile = Usuario.objects.create(user=nuevo_usuario)

            # Asignar imagen si se proporcionó
            imagen = mi_formulario.cleaned_data.get("imagen")
            if imagen:
                nuevo_userprofile.imagen = imagen
                nuevo_userprofile.save()

            return render(request, "login.html")
        else:
            # Manejar el caso en que el formulario no sea válido
            print("Formulario inválido")
            print("Errores:", mi_formulario.errors)
            print("Datos:", mi_formulario.cleaned_data)
            return render(
                request,
                "register.html",
                {
                    "error": ["Ocurrió un error al registrar el usuario."],
                    "mensaje": [],
                },
            )
    else:
        return render(request, "register.html", {"form": Formulario_registro()})


# Agregar curso, con el decorador @login_required me aseguro que el usuario este logueado
@login_required
def agregar_curso(request):
    if request.method == "POST":
        mi_formulario = Formulario_agregar_curso(request.POST, request.FILES)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            nuevo_curso = Curso(nombre=datos["nombre_curso"], camada=datos["camada"])
            nuevo_curso.save()

            # Obtener el usuario autenticado
            usuario = request.user.usuario

            # Agregar el nuevo curso al usuario
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
                {
                    "error": ["Ocurrió un error al registrar el curso."],
                },
            )
    else:
        return render(request, "profesor.html")


# ver del detalle del curso desde profesor
def detalle_curso_profesor(request, id):
    curso = Curso.objects.get(id=id)

    usuarios_inscritos = Usuario.objects.filter(cursos=curso)
    usuarios_auth_user = User.objects.filter(usuario__in=usuarios_inscritos)

    return render(
        request,
        "detalle_curso_profesor.html",
        {"curso": curso, "usuarios_inscritos": usuarios_auth_user},
    )


# inscripcion del alumno a un curso
def curso_inscripcion(request, id):
    curso = Curso.objects.get(id=id)
    cursos_totales = Curso.objects.all()
    usuario = request.user.usuario
    # Agregar el nuevo curso al usuario
    usuario.cursos.add(curso)
    cursos = usuario.cursos.all()
    return render(
        request,
        "alumno.html",
        {
            "usuario": usuario,
            "cursos": cursos,
            "cursos_totales": cursos_totales,
        },
    )


# desloguear al usuario
def custom_logout(request):
    logout(request)
    return render(request, "base.html")


def calificar(request):
    if request.method == "POST":
        mi_formulario = Formulario_calificar(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso = Curso.objects.get(nombre=datos["curso"])
            usuarios_inscritos = Usuario.objects.filter(cursos=curso.id)
            usuarios_auth_user = User.objects.filter(usuario__in=usuarios_inscritos)
            datos = mi_formulario.cleaned_data
            curso = Curso.objects.get(nombre=datos["curso"])
            usuario = Usuario.objects.get(id=datos["id_alumno"])
            calificacion = datos["calificacion"]
            nueva_calificacion = Calificacion(
                curso=curso,
                usuario=usuario,
                descripcion="",
                calificacion=calificacion,
            )
            nueva_calificacion.save()
            texto = "La calificacción fue guardada con éxito."
            return render(
                request,
                "detalle_curso_profesor.html",
                {
                    "curso": curso,
                    "usuarios_inscritos": usuarios_auth_user,
                    "error": [],
                    "mensaje": [texto],
                },
            )
        else:
            usuarios_inscritos = Usuario.objects.filter(cursos=curso)
            usuarios_auth_user = User.objects.filter(usuario__in=usuarios_inscritos)
            curso = Curso.objects.get(nombre=request.POST["curso"])
            return render(
                request,
                "detalle_curso_profesor.html",
                {
                    "curso": curso,
                    "usuarios_inscritos": usuarios_auth_user,
                    "error": ["Ocurrió un error al calificar al alumno."],
                    "mensaje": [],
                },
            )
    else:
        usuarios_inscritos = Usuario.objects.filter(cursos=curso)
        usuarios_auth_user = User.objects.filter(usuario__in=usuarios_inscritos)
        curso = Curso.objects.get(nombre=curso)
        return render(
            request,
            "detalle_curso_profesor.html",
            {"curso": curso, "usuarios_inscritos": usuarios_auth_user},
        )


def buscar_alumno(request):
    if request.GET["alumno"]:
        name = request.GET["alumno"]
        alumno = User.objects.filter(
            Q(first_name__icontains=name) | Q(last_name__icontains=name)
        )

        if alumno is not None:
            print(alumno)
        return render(request, "resultado_busqueda_alumno.html", {"alumnos": alumno})
