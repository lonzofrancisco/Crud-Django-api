# Generated by Django 3.1.5 on 2021-01-13 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0010_auto_20210113_1202'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productos',
            old_name='cantidad',
            new_name='stock',
        ),
        migrations.RemoveField(
            model_name='ventas',
            name='nombreProducto',
        ),
        migrations.RemoveField(
            model_name='ventas',
            name='precio',
        ),
        migrations.AddField(
            model_name='ventas',
            name='cantidad',
            field=models.IntegerField(default=1),
        ),
    ]