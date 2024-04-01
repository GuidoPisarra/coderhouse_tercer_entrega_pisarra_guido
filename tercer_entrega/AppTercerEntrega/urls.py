from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.home, name="home"),
    path("register", views.register, name="register"),
    path("user_login", views.user_login, name="user_login"),
    path("agregar_curso", views.agregar_curso, name="agregar_curso"),
    path("buscar_alumno", views.buscar_alumno, name="buscar_alumno"),
    path(
        "curso_inscripcion/<int:id>",
        views.curso_inscripcion,
        name="curso_inscripcion",
    ),
    path(
        "detalle_curso_profesor/<int:id>",
        views.detalle_curso_profesor,
        name="detalle_curso_profesor",
    ),
    path("logout/", views.custom_logout, name="logout"),
    path("calificar", views.calificar, name="calificar"),
]
