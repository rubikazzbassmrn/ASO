from django.db import models

# Create your models here.

#Modelo STATUS
class Status(models.Model):
    status = models.CharField(max_length=25, verbose_name='Status')

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Status'

    def __str__(self):
        return self.status

#Modelo States
class State(models.Model):
    state_name = models.CharField(max_length=100, verbose_name='Estado')

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'

    def __str__(self):
        return self.state_name

#Modelo Towns
class Town(models.Model):
    town_name = models.CharField(max_length=50, verbose_name='Municipio')
    id_state = models.ForeignKey(State, on_delete=models.CASCADE, verbose_name='Id de estado')

    class Meta:
        verbose_name = 'Municipio'
        verbose_name_plural = 'Municipios'

    def __str__(self):
        return self.town_name

#Modelo Marital_status
class Marital_status(models.Model):
    marital_status = models.CharField(max_length=30, verbose_name='Estado civil')

    class Meta:
        verbose_name = 'Estado civil'
        verbose_name_plural = 'Estados civil'

    def __str__(self):
        return self.marital_status

#Modelo Education_level
class Education_level(models.Model):
    education_level = models.CharField(max_length=55, verbose_name='Grado academico')

    class Meta:
        verbose_name = 'Grado academico'
        verbose_name_plural = 'Grados academicos'

    def __str__(self):
        return self.education_level

#Modelo Media
class Media(models.Model):
    media = models.CharField(max_length=55, verbose_name='Medio')

    class Meta:
        verbose_name = 'Medio'
        verbose_name_plural = 'Medios'

    def __str__(self):
        return self.media

#Modelo Truck_type
class Truck_type(models.Model):
    truck_type = models.CharField(max_length=50, verbose_name='Tipo de tracto')

    class Meta:
        verbose_name = 'Tipo de tracto'
        verbose_name_plural = 'Tipos de tracto'

    def __str__(self):
        return self.truck_type

#Modelo Mexa_interest
class Mexa_interest(models.Model):
    interest = models.CharField(max_length=250, verbose_name='Interes')

    class Meta:
        verbose_name = 'Interes'
        verbose_name_plural = 'Intereses'

    def __str__(self):
        return self.interest

#Modelo Status_job
class Status_job(models.Model):
    status_job = models.CharField(max_length=25, verbose_name='Status job')

    class Meta:
        verbose_name = 'Status job'
        verbose_name_plural = 'Status job'

    def __str__(self):
        return self.status_job

#Modelo Status_process
class Status_process(models.Model):
    status_process = models.CharField(max_length=25, verbose_name='Status process')

    class Meta:
        verbose_name = 'Status process'
        verbose_name_plural = 'Status process'

    def __str__(self):
        return self.status_process