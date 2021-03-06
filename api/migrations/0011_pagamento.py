# Generated by Django 3.2.5 on 2021-09-28 02:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20210921_2210'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=20)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=5)),
                ('transacao_id', models.CharField(max_length=50)),
                ('created_at', models.DateField(auto_now_add=True, null=True)),
                ('updated_at', models.DateField(auto_now=True, null=True)),
                ('diaria', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.diaria')),
            ],
        ),
    ]
