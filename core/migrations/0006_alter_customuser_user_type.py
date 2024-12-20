# Generated by Django 5.1.1 on 2024-11-20 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_customuser_phone_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[('business', 'Dueño de Negocio'), ('customer', 'Cliente')], default='customer', max_length=50),
        ),
    ]
