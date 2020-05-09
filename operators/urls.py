from django.urls import path
#import views file
from . import views

urlpatterns = [
    #Operators URLs
    path('matriz', views.matriz, name="matriz",)
]