# Generated by Django 4.0.4 on 2022-04-18 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banco_origem', models.TextField(max_length=100)),
                ('agencia_origem', models.TextField(max_length=15)),
                ('conta_origem', models.IntegerField()),
                ('banco_destino', models.TextField(max_length=100)),
                ('agencia_destino', models.TextField(max_length=15)),
                ('conta_destino', models.IntegerField()),
                ('valor_transacao', models.FloatField()),
                ('data', models.DateField()),
            ],
        ),
    ]
