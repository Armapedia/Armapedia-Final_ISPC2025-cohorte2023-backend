from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Arma(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    origen = models.CharField(max_length=50)
    año_produccion = models.IntegerField()
    fabricante = models.CharField(max_length=100)
    longitud_total = models.FloatField()
    longitud_cañon = models.FloatField()
    peso = models.FloatField()
    calibre = models.CharField(max_length=50)
    capacidad_cargador = models.IntegerField()
    velocidad_salida = models.FloatField()
    eventos_historicos = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
