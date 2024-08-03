from django.db import models
from Usuario.models import Usuario

class Carrito(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name = 'carritos')
    cantidad = models.SmallIntegerField(default=0, null=True, blank=True)
    total = models.BigIntegerField(default=0, null=True, blank=True)
    titulo = models.TextField(max_length=250)

    def _str_(self):
        return f'Carrito de {self.usuario.username if self.usuario else "Desconocido"}'
       
