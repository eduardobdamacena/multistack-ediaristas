# Generated by Django 3.2.5 on 2021-09-15 00:10

import django.contrib.auth.models
from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_usuario_username'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='usuario',
            managers=[
                ('diarista_objects', django.db.models.manager.Manager()),
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]