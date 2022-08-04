from django.db import models
# Create your models here.
class Hotel(models.Model):
    nombre_hotel = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=50)
    piscina = models.BooleanField()
    gimnasio = models.BooleanField()
    restaurante = models.BooleanField()
    aforo_max = models.IntegerField()

    class Meta:
        verbose_name='Hotel'
        verbose_name_plural='Hoteles'
        db_table='Hotel'
    def __str__(self):
        return self.nombre_hotel   

class Habitacion(models.Model):
    tipo= models.CharField(max_length=50)
    aforo_max = models.IntegerField()
    precio = models.IntegerField(blank=True, null=True)
    descripcion= models.TextField()
    piscina = models.BooleanField(null=True)
    gimnasio = models.BooleanField(null=True)
    restaurante = models.BooleanField(null=True)
    imagen= models.ImageField(upload_to='reservas', null=True)
    #Cliente_Reservado= models.ForeignKey(Cliente, blank=True, null=True, on_delete=models.CASCADE)
    habitacion= models.ForeignKey(Hotel, blank=True, null=True, on_delete=models.CASCADE) 
    
    class Meta:
        verbose_name='Habitacion'
        verbose_name_plural='Habitaciones'
        db_table='Habitacion'

    def __str__(self):
        return self.tipo

class Cliente(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    rut = models.CharField(max_length=10)
    correo = models.EmailField()
    Habitacion_reservada= models.ForeignKey(Habitacion, blank=True, null=True, on_delete=models.CASCADE) 

 
    
    class Meta:
        verbose_name='Cliente'
        verbose_name_plural='Clientes'
        db_table='Cliente'   

    #aqui personalizo el nombre en la base de datos para que no se me cambia por defecto.
    def __str__(self):
        return self.nombre

class Reserva(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    rut = models.CharField(max_length=10)
    correo = models.EmailField()
    telefono = models.CharField(max_length=11)
    fecha_entrada = models.DateTimeField()
    fecha_salida = models.DateTimeField()
    Habitacion_reservada= models.ForeignKey(Habitacion, blank=True, null=True, on_delete=models.CASCADE) 
    Cliente_Reservado= models.ForeignKey(Cliente, blank=True, null=True, on_delete=models.CASCADE)
    #Agente_Reservado= models.ForeignKey(Agente, blank=True, null=True, on_delete=models.CASCADE) 


    class Meta:
            verbose_name='Reserva'
            verbose_name_plural='Reservas'
            db_table='Reserva' 

class Agente(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    rut = models.CharField(max_length=10)
    correo = models.EmailField()
    cargo= models.CharField(max_length=50)
    Hotel= models.ForeignKey(Hotel, blank=True, null=True, on_delete=models.CASCADE) 

    class Meta:
            verbose_name='Agente'
            verbose_name_plural='Agentes'
            db_table='Agente'
    def __str__(self):
            return self.nombre



class Contacto(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    telefono = models.CharField(max_length=12)
    correo = models.EmailField()
    direccion= models.CharField(max_length=100)
    comentario= models.TextField()
    

    class Meta:
            verbose_name='Contacto'
            verbose_name_plural='Contactos'
            db_table='Contacto'
    def __str__(self):
            return self.nombre
# Create your models here.
