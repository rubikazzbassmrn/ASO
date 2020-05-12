from django.db import models

# Create your models here.

#Modelo Status_process
class Operators(models.Model):
    first_name = models.CharField(max_length=80, verbose_name='Nombre')
    last_name_p = models.CharField(max_length=80, verbose_name='Apellido paterno')
    last_name_m = models.CharField(max_length=80, verbose_name='Apellido materno')
    b_day = models.DateTimeField(null=True, blank=True, verbose_name='Fecha de nacimiento')
    rfc = models.CharField(max_length=50, verbose_name='RFC')
    curp = models.CharField(max_length=50, verbose_name='CURP')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Operador'
        verbose_name_plural = 'Operadores'

    def __str__(self):
        return "%s %s %s %s" % (self.first_name, self.last_name_p, self.last_name_m, self.curp)