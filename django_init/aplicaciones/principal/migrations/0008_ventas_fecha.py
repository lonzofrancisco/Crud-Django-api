# Generated by Django 3.1.5 on 2021-01-13 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0007_auto_20210113_1148'),
    ]

    operations = [
        migrations.AddField(
            model_name='ventas',
            name='fecha',
            field=models.DateField(blank=True, default=None),
        ),
    ]
