from django.db import models
from Usuario.models import Usuario

class Estado(models.TextChoices):
    PENDIENTE = 'P', 'Pendiente'
    ENVIADO = 'N', 'Enviado'
    CANCELADO = 'C', 'Cancelado'

class Pedido(models.Model):
    monto = models.IntegerField()
    fecha = models.DateField(auto_now_add=True)
    origen = models.CharField(max_length=20)
    estado = models.CharField(max_length=1, choices=Estado.choices)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='pedidos')