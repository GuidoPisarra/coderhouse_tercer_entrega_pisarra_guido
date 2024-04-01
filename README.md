# coderhouse_tercer_entrega_pisarra_guido

Tercer entrega Coderhouse Django
python -m django startproject tercer_entrega

python manage.py migrate

python manage.py runserver

python manage.py startapp AppTercerEntrega

en settings.py del proyecto agregar a INSTALLEDAPPS el nombre de mi app

##revisa la app
python manage.py check AppTercerEntrega

# generar migracion

python manage.py makemigrations

## bbdd

python manage.py sqlmigrate AppTercerEntrega 0001
python manage.py migrate

### ADMIN

desde terminal:
python manage.py createsuperuser
guido - coderhouse123

se ingresa al panel:
http://127.0.0.1:8000/admin

### Explicación

Dentro de models tenemos los tres modelos :

- Usuario --> todos los usuarios de la aplicación
- Curso --> los cursos disponibles
- Calificacion --> las calificaciones que se le han dado a los alumnos

Dentro de usuario implemente "validar_contraseña" que será utilizado al momento del login, además
dobrecargue el método save() para poder guardar la contraeña encriptadad, ya que en clase no se explicó como guardar los usuarios
en la tabla de usuarios que viene por defecto en Django.

##USUARIOS :

guidito10@gmail.com , pass --> guido (alumno)
eldiez@gmail.com , pass --> diego (profesor)

##PROFESOR
El profesor puede crear materias y calificar alumnos.
Para esto ultimo, deberá ingresar en el listado de mis cursos, seleccionar una materia.
Una vez hecho esto aparecera un listado de alumnos, los cuales podrá calificar poniendo la nota en el input y presionando calificar
También podrá buscar alumnos por apellido desde la barra de buscar alumnos.

##ALUMNO
El alumno podrá ver su lista de cursos asignados, donde podrá inscribirse a un curso.
