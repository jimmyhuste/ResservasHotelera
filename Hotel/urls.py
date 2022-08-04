"""Hotel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from HoteleraApp import views
from HoteleraApp.views import Contacto
from HoteleraApp.views import Quienes_somos
from HoteleraApp.views import Inicio
from HoteleraApp.views import Habitaciones
from HoteleraApp.views import Reserva


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Reserva/',Reserva),
    path('Contacto/',Contacto),
    path('Quienes_somos/',Quienes_somos),
    path('Inicio/',Inicio),
    path('Habitaciones/',Habitaciones),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)




# echo "# ResservasHotelera" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/jimmyhuste/ResservasHotelera.git
# git push -u origin main

# …or push an existing repository from the command line
# git remote add origin https://github.com/jimmyhuste/ResservasHotelera.git
# git branch -M main
# git push -u origin main