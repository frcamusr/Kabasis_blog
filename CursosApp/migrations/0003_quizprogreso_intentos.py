# Generated by Django 4.2.6 on 2024-01-30 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CursosApp', '0002_alter_quizprogreso_porcentaje'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizprogreso',
            name='intentos',
            field=models.IntegerField(default=0),
        ),
    ]
