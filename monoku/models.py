from django.db import models


class Tipo_producto(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Galguerias(models.Model):
    nombre_producto = models.CharField(max_length=200)
    tipo = models.ForeignKey(Tipo_producto, on_delete=models.CASCADE)
    fecha_vencimiento = models.DateField()
    cantidad_producto = models.PositiveIntegerField(default=0)


    def __str__(self):
        return '{0} {1} {2}'.format(self.tipo, self.nombre_producto, self.cantidad_producto)


class Personas(models.Model):
    nombre_persona = models.CharField(max_length=200)
    edad = models.PositiveIntegerField(default=0)
    cargo = models.CharField(max_length=200)

    def __str__(self):
        return '{0}'.format(self.nombre_persona)


class Preferecias_galguerias(models.Model):
    persona = models.ForeignKey(Personas, on_delete=models.CASCADE)
    producto = models.ForeignKey(Galguerias, on_delete=models.CASCADE)
    cantidad_consumido = models.PositiveIntegerField(default=0)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{0} consumio {1} {2}'.format(self.persona.nombre_persona, self.cantidad_consumido,  self.producto.nombre_producto)