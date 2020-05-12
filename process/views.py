from django.shortcuts import render
#Importar catálogos
from catalogues.models import *
#Importar form
from .forms import *

# Create your views here.

def stepone(request):
    states = State.objects.all()
    towns = Town.objects.all()
    maritals_status = Marital_status.objects.all()
    education_levels = Education_level.objects.all()

    #Creamos un formulario vacio
    form = GeneralForm()

    #Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        #Añadimos los datos recibidos al formulario
        form = GeneralForm(request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
            # así conseguiremos una instancia para manejarla
            instancia = form.save(comit=False)
            # Podemos guardarla cuando queramos
            instancia.save()
            # Después de guardar redireccionamos a la lista
            return redirect('matriz')
    return render(request, "process/stepone.html", {'form':form, 'states':states, 'towns':towns, 'maritals_status':maritals_status, 'education_levels':education_levels})

def steptwo(request):
    return render(request, "process/steptwo.html")