# Generated by Django 5.0.4 on 2024-08-08 18:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Reseña', '0001_initial'),
        ('Usuario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reseña',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reseñas', to='Usuario.usuario'),
        ),
    ]
