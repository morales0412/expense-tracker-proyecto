from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
