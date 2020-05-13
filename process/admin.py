from django.contrib import admin
#Importar modelos
from .models import *

# Register your models here.

admin.site.register(Operators)

admin.site.register(Last_job)

admin.site.register(Actual_job)

admin.site.register(Operator_information)