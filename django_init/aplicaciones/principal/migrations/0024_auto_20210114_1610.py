# Generated by Django 3.1.5 on 2021-01-14 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0023_auto_20210113_1256'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ventas',
            name='venta',
        ),
        migrations.AddField(
            model_name='ventas',
            name='idVenta',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='principal.productos'),
        ),
        migrations.AlterField(
            model_name='productos',
            name='nombreProducto',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='productos',
            name='stock',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='ventas',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='ventas',
            name='monto',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
