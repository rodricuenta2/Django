from django.db import models

# CLASES DEL PROYECTO
# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.CharField ()
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre