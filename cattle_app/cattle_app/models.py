from django.db import models

class Usuario(models.Model):
    id_usuario = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    rol = models.CharField(max_length=20)
    email = models.CharField(unique=True, max_length=100)
    contrasena = models.CharField(max_length=100)
    finca_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        db_table = 'usuario'


class Ganado(models.Model):
    id_ganado = models.BigIntegerField(primary_key=True)
    tipo = models.CharField(max_length=50)
    raza = models.CharField(max_length=50, blank=True, null=True)
    peso = models.FloatField(blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    estado_salud = models.CharField(max_length=20, blank=True, null=True)
    finca = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'ganado'


class Alimentacion(models.Model):
    id_alimentacion = models.BigIntegerField(primary_key=True)
    ganado = models.ForeignKey(Ganado, on_delete=models.DO_NOTHING)
    tipo_alimento = models.CharField(max_length=100)
    cantidad_diaria = models.FloatField()
    frecuencia = models.BigIntegerField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'alimentacion'
