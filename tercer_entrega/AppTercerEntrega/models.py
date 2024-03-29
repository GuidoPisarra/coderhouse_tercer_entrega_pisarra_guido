from django.db import models
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.

from django.db import models


class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Camada: {self.camada}"


class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    contrasenia = models.CharField(max_length=128)  # Encripta si el objeto es nuevo
    cursos = models.ManyToManyField(Curso)
    es_profesor = models.BooleanField(default=False)
    imagen = models.FileField(upload_to="files/imagenes")

    def save(self, *args, **kwargs):
        if not self.pk:  # Encripta la contraseña si el objeto es nuevo
            self.contrasenia = make_password(self.contrasenia)
        super().save(*args, **kwargs)

    def validar_contraseña(self, contrasenia_texto_plano):
        return check_password(contrasenia_texto_plano, self.contrasenia)

    def __str__(self):
        return self.nombre


class Calificacion(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=100)
    calificacion = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.alumno} - Curso: {self.curso.nombre} - Calificación: {self.calificacion}"
