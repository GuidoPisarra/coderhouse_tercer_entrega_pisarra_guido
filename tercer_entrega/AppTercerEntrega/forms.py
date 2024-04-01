from django import forms


class Formulario_registro(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    es_profesor = forms.ChoiceField(choices=[("True", "Profesor"), ("False", "Alumno")])
    imagen = forms.ImageField(required=False)


class Formulario_ingreso(forms.Form):
    username = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())


class Formulario_agregar_curso(forms.Form):
    nombre_curso = forms.CharField(max_length=100)
    camada = forms.IntegerField()
    email = forms.EmailField()
