# Generated by Django 5.1.1 on 2024-12-18 20:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_customuser_favoritos'),
    ]

    operations = [
        migrations.AddField(
            model_name='valoracion',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='valoracion',
            name='comentario',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
