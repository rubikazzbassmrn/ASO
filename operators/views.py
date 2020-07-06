from django.shortcuts import render
#Importar modelos process
from process.models import *
#Importar Q
from django.db.models import Q

# Create your views here.

def matriz(request):
    queryset_nom = request.GET.get("nombre")
    queryset_rfc = request.GET.get("rfc")
    queryset_curp = request.GET.get("curp")
    queryset_bday = request.GET.get("bday")

    operators = Operators.objects.all().filter(
        id_status__status='Activo'
    )

    if queryset_nom:
        operators = Operators.objects.filter(
            Q(first_name__icontains = queryset_nom)
        )
    elif queryset_rfc:
        operators = Operators.objects.filter(
            Q(rfc__icontains = queryset_rfc)
        )
    elif queryset_bday:
        operators = Operators.objects.filter(
            Q(b_day = queryset_bday)
        )
    elif queryset_curp:
        operators = Operators.objects.filter(
            Q(curp__icontains = queryset_curp)
        )

    return render(request, "operators/matriz.html",{'operators':operators})