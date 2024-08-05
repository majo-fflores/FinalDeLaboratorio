from django.db import models
from Usuario.models import Usuario

class BilleteraVirtual(models.Model):
    monto = models.IntegerField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=None)
