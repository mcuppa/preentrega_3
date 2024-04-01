from django.db import models

# Create your models here.
class Pinturas(models.Model):
    name = models.CharField(max_length=200)
    color = models.CharField(max_length=20)
    litros = models.IntegerField()
    
    def __str__(self):
        return self.name
    
class Accesorios(models.Model):
    description = models.CharField(max_length=200)
    brand = models.CharField(max_length=40)
    type = models.CharField(max_length=30)
    material = models.CharField(max_length=30)
    
    def __str__(self):
        return self.description
        
class Clientes(models.Model):
    CONDICIONES = (
        ('consumidor_final', 'Consumidor final'),
        ('monotributista', 'Monotributista'),
        ('responsable_inscripto', 'Responsable inscripto'),
        ('exento', 'Exento'),

    )

    name = models.CharField(max_length=200)
    adress = models.CharField(max_length=200)
    condition = models.CharField(max_length=30, choices=CONDICIONES)
    location = models.CharField(max_length=200)
