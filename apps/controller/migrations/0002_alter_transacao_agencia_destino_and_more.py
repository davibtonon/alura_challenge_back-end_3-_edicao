# Generated by Django 4.0.4 on 2022-04-18 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controller', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transacao',
            name='agencia_destino',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='transacao',
            name='agencia_origem',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='transacao',
            name='banco_destino',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='transacao',
            name='banco_origem',
            field=models.CharField(max_length=100),
        ),
    ]
