# Generated by Django 3.1.5 on 2021-01-13 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0020_ventas_montoxd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ventas',
            name='Montoxd',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
