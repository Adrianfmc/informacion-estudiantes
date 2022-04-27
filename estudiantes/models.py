from django.conf import settings
from django.db import models
from django.utils import timezone

UNIVERSIDAD_OP = (
    (1, 'Ibero León'),
    (2,'Ibero Tijuana')
)

ASIGNATURA_OP = (
    (1, 'Interculturalidad'),
    (2, 'Persona y Humanismo')
)

CICLO_OP = (
    (1, 'Primavera 2022'),
    (2, 'Otro'),
)
class Alumnx(models.Model):
    nombre = models.CharField(max_length=100, help_text="Ingrese el nombre del alumnx")
    num_cuenta = models.CharField(max_length=200, help_text="Ingrese el número de cuenta del alumnx")
    email = models.EmailField(max_length=200, help_text="Ingrese el email del alumnx")
    universidad = models.IntegerField(default=1, choices = UNIVERSIDAD_OP)
    asignatura = models.IntegerField(default=1, choices = ASIGNATURA_OP)
    ciclo = models.IntegerField(default=1, choices = CICLO_OP)

    def __str__(self):
        return self.nombre

class Primer_parcial(models.Model):
    nombre = models.ForeignKey('Alumnx', on_delete=models.CASCADE,related_name='primer_par')
    calif_mono = models.DecimalField(max_digits=3, decimal_places=1)
    calif_expo_1er = models.DecimalField(max_digits=3, decimal_places=1)
    participacion_1er = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return str(self.nombre)
    
    def promedio(self):
        prom = float(self.calif_mono)*.6 + float(self.calif_expo_1er)*.1 + float(self.participacion_1er)*.3
        return prom

class Segundo_parcial(models.Model):
    nombre = models.ForeignKey('Alumnx', on_delete=models.CASCADE, related_name='segundo_par')
    calif_ensay_2do = models.DecimalField(max_digits=3, decimal_places=1, help_text="Ingrese la calificación del ensayo (2do parcial)")
    calif_expo_2do = models.DecimalField(max_digits=3, decimal_places=1, help_text="Ingrese la calificación de la exposición (2do parcial)")
    participacion_2do = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return str(self.nombre)
    
    def promedio_2do(self):
        prom_2do = float(self.calif_ensay_2do)*.6 + float(self.calif_expo_2do)*.1 + float(self.participacion_2do)*.3
        return prom_2do

class Final(models.Model):
    nombre = models.ForeignKey('Alumnx', on_delete=models.CASCADE, related_name='final_par')
    calif_ensay_final = models.DecimalField(max_digits=3, decimal_places=1, help_text="Ingrese la calificación del ensayo (3er parcial)")
    calif_expo_final = models.DecimalField(max_digits=3, decimal_places=1, help_text="Ingrese la calificación de la exposición (3er parcial)")
    participacion_final = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return self.nombre
    
    def promedio_final(self):
        prom_final = float(self.calif_ensay_final)*.6 + float(self.calif_expo_final)*.1 + float(self.participacion_final)*.3
        return prom_final

class Autobiografia(models.Model):
    nombre = models.ForeignKey('Alumnx', on_delete=models.CASCADE, related_name='autobio')
    autobiografia = models.DecimalField(max_digits=3, decimal_places=1, help_text="Ingrese la calificación de la autobiografía")

    def __str__(self):
        return str(self.nombre)
