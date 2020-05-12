from django.db import models
#Importar modelo Operators
from operators.models import Operators
#Importar catalogos
from catalogues.models import *

# Create your models here.

class General_information(models.Model):
    id_operator = models.ForeignKey(Operators, on_delete=models.CASCADE, verbose_name='Operador')
    id_state = models.ForeignKey(State, on_delete=models.CASCADE, verbose_name='Estado')
    id_town = models.ForeignKey(Town, on_delete=models.CASCADE, verbose_name='Municipio')
    id_marital_status = models.ForeignKey(Marital_status, on_delete=models.CASCADE, verbose_name='Estado civil')
    id_education_level = models.ForeignKey(Education_level, on_delete=models.CASCADE, verbose_name='Grado academico')
    id_status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name='Status')
    
    class Meta:
        verbose_name = 'Información general'
        verbose_name_plural = 'Información general'
    
    def __str__(self):
        return "%s %s %s" % (self.id_operator, self.id_marital_status, self.id_status)

class Last_job(models.Model):
    id_operator = models.ForeignKey(Operators, on_delete=models.CASCADE, verbose_name='Operador')
    last_job = models.CharField(max_length=250, verbose_name='Ultimo trabajo')
    start_date = models.DateTimeField(null=True, blank=True, verbose_name='Fecha de inicio')
    fishined_date = models.DateTimeField(null=True, blank=True, verbose_name='Fecha de termino')

    class Meta:
        verbose_name = 'Ultimo trabajo'
        verbose_name_plural = 'Ultimos trabajos'
    
    def __str__(self):
        return "%s %s" % (self.id_operator, self.last_job)

class Actual_job(models.Model):
    id_operator = models.ForeignKey(Operators, on_delete=models.CASCADE, verbose_name='Operador')
    actual_job = models.CharField(max_length=250, verbose_name='Trabajo actual')
    start_date = models.DateTimeField(null=True, blank=True, verbose_name='Fecha de inicio')

    class Meta:
        verbose_name = 'Trabajo actual'
        verbose_name_plural = 'Trabajos actuales'
    
    def __str__(self):
        return "%s %s" % (self.id_operator, self.actual_job_job)

class Operator_information(models.Model):
    id_gi = models.ForeignKey(General_information, on_delete=models.CASCADE, verbose_name='Informacion G')
    id_media = models.ForeignKey(Media, on_delete=models.CASCADE, verbose_name='Medio')
    id_truck_type = models.ForeignKey(Truck_type, on_delete=models.CASCADE, verbose_name='Tipo de unidad')
    id_last_job = models.ForeignKey(Last_job, on_delete=models.CASCADE, verbose_name = 'Ultimo trabajo')
    id_mexa_interest  = models.ForeignKey(Mexa_interest, on_delete=models.CASCADE, verbose_name='Interes')
    id_status_job = models.ForeignKey(Status_job, on_delete=models.CASCADE, verbose_name='Estatus job')
    id_status_process  = models.ForeignKey(Status_process, on_delete=models.CASCADE, verbose_name='Estatus process')

    class Meta:
        verbose_name = 'Información de operador'
        verbose_name_plural = 'Informacion de operador'
    
    def __str__(self):
        return "%s" % (self.id_gi)