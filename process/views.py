from django.shortcuts import render, redirect
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

    
    #Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        #Creamos un formulario vacio
        form = OperatorForm()
        #Añadimos los datos recibidos al formulario
        form = OperatorForm(request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            form = form.save(commit=False)
            # Guardamos la instancia
            form.save()
            # Después de guardar redireccionamos a la lista
            return redirect('steptwo')
    else:
        form = OperatorForm()
    return render(request, "process/stepone.html", {'form':form, 'states':states, 'towns':towns, 'maritals_status':maritals_status, 'education_levels':education_levels})

def steptwo(request):
    #Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        #Creamos un formulario vacio
        form = OpinfoForm()
        #Añadimos los datos recibidos al formulario
        form = OpinfoForm(request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            form = form.save(commit=False)
            # Guardamos la instancia
            form.save()
            # Después de guardar redireccionamos a la lista
            return redirect('stepthree')
    else:
        form = OpinfoForm()
    return render(request, "process/steptwo.html", {'form':form})

def stepthree(request):
    form = DocumentsForm()
    if request.method == "POST":
        form = DocumentsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('matriz')
    else:
        form = DocumentsForm()
    return render(request, "process/stepthree.html", {'form':form})