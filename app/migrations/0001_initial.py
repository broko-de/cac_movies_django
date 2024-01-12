# Generated by Django 4.2.9 on 2024-01-11 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Titulo')),
                ('director', models.CharField(max_length=150, verbose_name='Director')),
                ('release_date', models.DateField(null=True, verbose_name='Fecha de lanzamiento')),
                ('banner', models.URLField(max_length=255, null=True, verbose_name='Portada')),
            ],
        ),
    ]
