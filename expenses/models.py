from django.db import models
from categories.models import Category
# Create your models here.


class Expense(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(Category, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre
