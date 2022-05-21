# Generated by Django 4.0.4 on 2022-05-07 00:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('controller', '0011_alter_importacaorealizada_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='transacao',
            name='usuario',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]