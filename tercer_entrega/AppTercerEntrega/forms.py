from django import forms


class Formulario_registro(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    email = forms.EmailField()
    contrasenia = forms.CharField(widget=forms.PasswordInput())
    es_profesor = forms.BooleanField()
    imagen = forms.ImageField(required=False)
