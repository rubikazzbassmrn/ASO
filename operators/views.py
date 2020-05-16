from django.shortcuts import render
#Importar modelos process
from process.models import *

# Create your views here.

def matriz(request):
    operators = Operators.objects.all().filter(id_status__status='Activo')
    return render(request, "operators/matriz.html",{'operators':operators})