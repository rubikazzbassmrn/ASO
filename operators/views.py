from django.shortcuts import render
#Importar modelos process
from process.models import *

# Create your views here.

def matriz(request):
    operators = Operators.objects.all()
    return render(request, "operators/matriz.html",{'operators':operators})