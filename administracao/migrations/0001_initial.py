# Generated by Django 3.2.5 on 2021-07-30 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('valor_minimo', models.FloatField()),
                ('qtd_horas', models.IntegerField()),
                ('porcentagem_comissao', models.FloatField()),
                ('horas_quarto', models.IntegerField()),
                ('valor_quarto', models.FloatField()),
                ('horas_sala', models.IntegerField()),
                ('valor_sala', models.FloatField()),
                ('horas_banheiro', models.IntegerField()),
                ('valor_banheiro', models.FloatField()),
                ('horas_cozinha', models.IntegerField()),
                ('valor_cozinha', models.FloatField()),
                ('horas_quintal', models.IntegerField()),
                ('valor_quintal', models.FloatField()),
                ('horas_outros', models.IntegerField()),
                ('valor_outros', models.FloatField()),
                ('icone', models.CharField(choices=[('twf-cleaning-1', 'twf-cleaning-1'), ('twf-cleaning-2', 'twf-cleaning-2'), ('twf-cleaning-3', 'twf-cleaning-3')], max_length=14)),
                ('posicao', models.IntegerField()),
            ],
        ),
    ]
