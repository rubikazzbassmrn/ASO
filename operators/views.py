from django.shortcuts import render
#Importar modelos process
from process.models import *

# Create your views here.

def matriz(request):
    general_informations = General_information.objects.all()
    return render(request, "operators/matriz.html",{'general_informations':general_informations})