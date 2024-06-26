# Generated by Django 5.0.3 on 2024-04-01 04:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('camada', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('es_profesor', models.BooleanField(default=False)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='files/imagenes')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppTercerEntrega.curso')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Calificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100)),
                ('calificacion', models.DecimalField(decimal_places=2, max_digits=5)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppTercerEntrega.curso')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppTercerEntrega.usuario')),
            ],
        ),
    ]
