# Generated by Django 3.1.5 on 2021-01-13 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0017_auto_20210113_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ventas',
            name='montoVenta',
            field=models.IntegerField(),
        ),
    ]