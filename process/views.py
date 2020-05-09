from django.shortcuts import render

# Create your views here.

def stepone(request):
    return render(request, "process/stepone.html")