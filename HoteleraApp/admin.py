from HoteleraApp.models import Cliente,Habitacion,Hotel,Reserva,Agente,Contacto
from django.contrib import admin


class Admin(admin.ModelAdmin):
    '''Admin View for '''
    list_display = ('nombre',)
    list_filter = ('nombre',)
    search_fields=('nombre','apellido',)

class AdminH(admin.ModelAdmin):
    '''Admin View for '''
    list_display = ('tipo',)
    list_filter = ('precio','tipo',)
    search_fields=('tipo',)
    

class AdminR(admin.ModelAdmin):
    '''Admin View for '''
    list_filter=('fecha_entrada','fecha_salida',) 
    list_display = ('nombre','apellido',) 
    search_fields=('nombre', 'apellido',) 

class AdminContacto(admin.ModelAdmin):
    list_display = ('nombre', 'apellido')

#registramos las clases aquí
admin.site.register(Cliente,Admin)
admin.site.register(Habitacion,AdminH)
admin.site.register(Hotel)
admin.site.register(Reserva,AdminR) 
admin.site.register(Agente)
admin.site.register(Contacto,AdminContacto)

