from django.urls import path
from . import views

urlpatterns = [


    path("",views.home, name="home"),
    path("Historia/",views.about, name="about"),
    path("Servicios/",views.services, name="services"),
    path("Visitanos/",views.store, name="store"),
]