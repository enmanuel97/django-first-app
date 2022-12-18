 
from django.db import models
from django.utils import timezone
 
# Creación de campos de la tabla 'clientes' 
class Cliente(models.Model):
    codigo 		        = models.CharField(max_length=100, default='DEFAULT VALUE')
    nombre 		        = models.CharField(max_length=100, default='DEFAULT VALUE')
    anio_nacimiento 	= models.CharField(max_length=20, default='DEFAULT VALUE')
 
    class Meta:
        db_table = 'clientes' # Le doy de nombre 'clientes' a nuestra tabla en la Base de Datos