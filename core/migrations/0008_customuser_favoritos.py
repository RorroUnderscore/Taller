# Generated by Django 5.1.1 on 2024-11-21 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_local_dueño_alter_local_categoria_alter_local_imagen_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='favoritos',
            field=models.ManyToManyField(blank=True, related_name='favorito_de', to='core.local'),
        ),
    ]
