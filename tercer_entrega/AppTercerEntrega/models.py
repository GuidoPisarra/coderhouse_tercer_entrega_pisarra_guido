from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User

# Create your models here.

from django.db import models


class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Camada: {self.camada}"


class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    es_profesor = models.BooleanField(default=False)
    imagen = models.ImageField(upload_to="files/imagenes", blank=True, null=True)
    cursos = models.ManyToManyField(Curso, related_name="alumnos", blank=True)

    def save(self, *args, **kwargs):
        # Actualizar el campo es_profesor según si el usuario es superusuario
        self.es_profesor = self.user.is_superuser
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Id: {self.id} Nombre: {self.nombre} Apellido: {self.apellido} Email {self.email} Profesor {self.es_profesor} Cursos: {self.cursos} Imagen: {self.imagen}"


class Calificacion(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=100)
    calificacion = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.usuario} - Curso: {self.curso.nombre} - Calificación: {self.calificacion}"
