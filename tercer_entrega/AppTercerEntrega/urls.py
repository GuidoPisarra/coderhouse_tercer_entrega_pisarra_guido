from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("agregar_curso", views.agregar_curso, name="agregar_curso"),
    path(
        "curso_inscripcion/<int:id>/<str:email>",
        views.curso_inscripcion,
        name="curso_inscripcion",
    ),
    path(
        "detalle_curso_profesor/<int:id>/<str:email>",
        views.detalle_curso_profesor,
        name="detalle_curso_profesor",
    ),
]
