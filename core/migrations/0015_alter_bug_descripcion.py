# Generated by Django 5.1.1 on 2024-12-19 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_alter_bug_captura_alter_bug_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='descripcion',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
