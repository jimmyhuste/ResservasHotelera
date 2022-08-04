from django.shortcuts import render,redirect
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
from HoteleraApp.models import Habitacion
from HoteleraApp.models import Reserva
from HoteleraApp.models import Cliente
from HoteleraApp.models import Hotel
from HoteleraApp.forms import ContactForm, ReservaForm

from django.conf import settings
#from django.http import HttpResponse
# Create your views here.

def Contacto(request):
    data={
        'form':ContactForm()
    }
    if request.method== 'POST':
        formulario= ContactForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Gracias!"
        else:  
            data["form"]= formulario
   
    return render(request, "Contacto.html", data)

def Quienes_somos(request):
    return render(request, "Quienes_somos.html", {})

def Inicio(request):
    return render(request, "Inicio.html", {})

def Habitaciones(request):
    habitaciones= Habitacion.objects.all()
    return render(request, "Habitaciones.html", {"habitaciones":habitaciones})

def Reserva(request):
    data={
        'form_reserva':ReservaForm()
    }
    if request.method== 'POST':
        formulario= ReservaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensage"] = "Gracias por elegir nuestro Hotel!"
        else:  
            data["form_reserva"]= formulario

    return render(request,"Reserva.html", data)
