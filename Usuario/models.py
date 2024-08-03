from django.db import models
from django.contrib.auth.models import AbstractUser

#SE EXTIENDE DE USUARIO QUE VIENE POR DEFECTO DE DJANGO
class Usuario(AbstractUser):
    domicilio = models.CharField(max_length=250, null=True, blank=True)
    nacionalidad = models.CharField(max_length=80, null=True, blank=True)
    nroTelefono = models.CharField(max_length=80, null=True, blank=True)
    correoElectronicoSecundario = models.CharField(max_length=250, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    fotoPerfil = models.ImageField(blank=True, upload_to='PONER NOMBRE DE LA CARPETA AQUI')

    def _str_(self):
        return self.username
    
class BilleteraVirtual(models.Model):
    monto = models.IntegerField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=None)