from django.urls import path
#import views file
from . import views

urlpatterns = [
    #Core URLs
    path('', views.home, name="home",)
]