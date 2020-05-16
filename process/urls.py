from django.urls import path
#import views file
from . import views

urlpatterns = [
    #Process URLs
    path('stepone', views.stepone, name="stepone"),
    path('steptwo', views.steptwo, name="steptwo"),
    path('stepthree', views.stepthree, name="stepthree")

]