# Generated by Django 3.1.5 on 2021-01-13 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0005_remove_stock_cantidadisponible'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='cantidad',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
