# Generated by Django 5.0.3 on 2024-04-01 04:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppTercerEntrega', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='curso',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='AppTercerEntrega.curso'),
        ),
    ]
