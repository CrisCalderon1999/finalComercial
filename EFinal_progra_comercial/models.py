from django.db import models

class Continente(models.Model):
    nombre = models.CharField(max_length=255)

    class Meta:
        db_table = 'Continentes'

    def __str__(self):
        return self.nombre

class Pais(models.Model):
    nombre = models.CharField(max_length=255)
    codigo = models.CharField(max_length=5, unique=True)
    continente = models.ForeignKey(Continente, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Paises'

    def __str__(self):
        return self.nombre

class Pasaporte(models.Model):
    id_pasaporte = models.AutoField(primary_key=True)
    numero_pasaporte = models.CharField(unique=True, max_length=20)
    nombre = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=10)
    fecha_emision = models.DateField()
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Pasaportes'

    def __str__(self):
        return self.numero_pasaporte
