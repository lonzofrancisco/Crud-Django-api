from django.db import models
from datetime import datetime, date


class Productos(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombreProducto = models.CharField(max_length=100,unique=True ) 
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return "COD" + str(self.codigo) +" ________ "+ str(self.nombreProducto)+ "________    $" + str(self.precio) + "__________  Cantidad disponible:  " + str(self.stock)

class Ventas(models.Model):
    venta = models.ForeignKey(Productos, null=False, blank=False, on_delete=models.PROTECT, db_constraint=False)
    fecha = models.DateField(auto_now=False, auto_now_add=False, blank=True, default=None)
    cantidad = models.PositiveIntegerField(default=1)
    monto = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return "  Venta:" + str(self.venta)+ " Fecha "+str(self.fecha)+ " Monto total de venta: " + str( self.cantidad)

# tengo que ver como se puede hacer que el 
# usuario solo pueda agregar a ventas productos que tiene en stock.
