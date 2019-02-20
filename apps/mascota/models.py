from django.db import models
from django.urls import reverse_lazy, reverse
# Create your models here.
from apps.adopcion.models import Persona

class Vacuna(models.Model):
	nombre = models.CharField(max_length=50)

	def __str__(self): #esta funcion nos trae el valor del objeto en vez del nombre del objeto cuando es llave foranea o forekeing
		return '{}'.format(self.nombre)	

class Mascota(models.Model):
	#folio = models.CharField(max_length=10, primary_key=True)
	nombre = models.CharField(max_length=50)
	sexo = models.CharField(max_length=10)
	edad_aproximada = models.IntegerField()
	fecha_rescate = models.DateField()
	persona = models.ForeignKey(Persona, null=True, blank=True, on_delete= models.CASCADE)
	vacuna = models.ManyToManyField(Vacuna, blank=True)

	def get_absolute_url(self):
	    return reverse('index')



