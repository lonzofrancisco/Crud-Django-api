# Generated by Django 3.1.5 on 2021-01-13 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0018_auto_20210113_1243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ventas',
            name='montoVenta',
        ),
    ]