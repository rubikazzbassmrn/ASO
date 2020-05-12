from django.shortcuts import render
#Importar catálogos
from catalogues.models import *

# Create your views here.

def stepone(request):
    states = State.objects.all()
    towns = Town.objects.all()
    maritals_status = Marital_status.objects.all()
    education_levels = Education_level.objects.all()
    return render(request, "process/stepone.html", {'states':states, 'towns':towns, 'maritals_status':maritals_status, 'education_levels':education_levels})