from django.contrib import admin
#Importar modelos
from .models import *

# Register your models here.

admin.site.register(Operators)

admin.site.register(Operator_information)

admin.site.register(Documentation)