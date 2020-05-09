from django.shortcuts import render

# Create your views here.

def matriz(request):
    return render(request, "operators/matriz.html")