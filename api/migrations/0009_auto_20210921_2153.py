# Generated by Django 3.2.5 on 2021-09-22 00:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_diaria_complemento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diaria',
            name='candidatos',
        ),
        migrations.AddField(
            model_name='diaria',
            name='candidatas',
            field=models.ManyToManyField(blank=True, related_name='candidatas', to=settings.AUTH_USER_MODEL),
        ),
    ]
