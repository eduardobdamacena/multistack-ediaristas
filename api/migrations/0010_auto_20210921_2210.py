# Generated by Django 3.2.5 on 2021-09-22 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20210921_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diaria',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='diaria',
            name='valor_comissao',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
