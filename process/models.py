from django.db import models
#Importar catalogos
from catalogues.models import *

# Create your models here.

class Operators(models.Model):
    first_name = models.CharField(max_length=80, verbose_name='Nombre')
    last_name_p = models.CharField(max_length=80, verbose_name='Apellido paterno')
    last_name_m = models.CharField(max_length=80, verbose_name='Apellido materno')
    b_day = models.DateField(null=True, blank=True, verbose_name='Fecha de nacimiento')
    rfc = models.CharField(max_length=50, verbose_name='RFC')
    curp = models.CharField(max_length=50, verbose_name='CURP')
    id_state = models.ForeignKey(State, on_delete=models.CASCADE, verbose_name='Estado')
    id_town = models.ForeignKey(Town, on_delete=models.CASCADE, verbose_name='Municipio')
    id_marital_status = models.ForeignKey(Marital_status, on_delete=models.CASCADE, verbose_name='Estado civil')
    id_education_level = models.ForeignKey(Education_level, on_delete=models.CASCADE, verbose_name='Grado academico')
    id_status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name='Status')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Operador'
        verbose_name_plural = 'Operadores'
    
    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name_p)

class Operator_information(models.Model):
    id_operator = models.ForeignKey(Operators, on_delete=models.CASCADE, verbose_name='Operador')
    id_media = models.ForeignKey(Media, on_delete=models.CASCADE, verbose_name='Medio')
    id_mexa_interest = models.ForeignKey(Mexa_interest, on_delete=models.CASCADE, verbose_name='Interes')
    id_truck_type = models.ManyToManyField(Truck_type, verbose_name='Tipo de unidad')
    last_job = models.CharField(max_length=250, verbose_name = 'Ultimo trabajo')
    period_started = models.DateField(null=True, blank=True, verbose_name='Inicio')
    period_finished = models.DateField(null=True, blank=True, verbose_name='Termino')
    id_status_job = models.ForeignKey(Status_job, on_delete=models.CASCADE, verbose_name='¿Está trabajando ahora?')
    actual_job_where = models.CharField(max_length=250, verbose_name='¿Dónde?', null=True, blank=True)
    id_status_process = models.ForeignKey(Status_process, on_delete=models.CASCADE, verbose_name='¿Está llevando otro proceso?')
    actual_process_where = models.CharField(max_length=250, verbose_name='¿Dónde?', null=True, blank=True)
    id_status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name='Status')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Información de operación'
        verbose_name_plural = 'Informacion de operaciones'
    
    def __str__(self):
        return "%s" % (self.id_operator)

class Documentation(models.Model):
    id_operator = models.ForeignKey(Operators, on_delete=models.CASCADE, verbose_name='Operador')
    curp_file = models.FileField(upload_to="archivos/", null=True, blank=True)
    secure_number_file = models.FileField(upload_to="archivos/", null=True, blank=True)
    secure_number = models.CharField(max_length=250, verbose_name='Digita el número', null=True, blank=True)
    licence_file = models.FileField(upload_to="archivos/", null=True, blank=True)
    licence = models.CharField(max_length=250, verbose_name='Ingresa licencia', null=True, blank=True)
    licence_started = models.DateField(null=True, blank=True, verbose_name='Inicio')
    licence_finished = models.DateField(null=True, blank=True, verbose_name='Vencimiento')
    psicofisico_file = models.FileField(upload_to="archivos/", null=True, blank=True)
    recommendation_letter_file = models.FileField(upload_to="archivos/", null=True, blank=True)

    class Meta:
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'
    
    def __str__(self):
        return "%s" % (self.id_operator)