from django.db import models
from django.utils import timezone


class CategoriaProducto(models.Model):
    nombre_categoria = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre_categoria


class Producto(models.Model):
    codigo_de_barras = models.CharField(max_length=30)
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    categoria = models.ForeignKey(CategoriaProducto, on_delete=models.DO_NOTHING)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_ultima_modificacion = models.DateTimeField(default=timezone.now)

    def actualizar(self):
        self.fecha_ultima_modificacion = timezone.now()
        self.save()

    def __str__(self):
        return self.nombre


class MovimientoLibro(models.Model):
    fecha_movimiento = models.DateTimeField(default=timezone.now)
    producto = models.ForeignKey(Producto, on_delete=models.DO_NOTHING)
    cantidad = models.PositiveIntegerField(help_text="Sólo números positivos")
    egreso = models.BooleanField(default=True)

    def __str__(self):

        return ("Egreso" if self.egreso else "Ingreso") + " de " + self.producto.nombre + ", fecha: " + self.fecha_movimiento
