# Generated by Django 5.0.7 on 2024-11-19 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_rename_rol_historicaluser_role_rename_rol_user_role'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicaluser',
            old_name='firstname',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='firstname',
            new_name='name',
        ),
    ]
