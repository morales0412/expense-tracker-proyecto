from django import forms
from .models import Expense


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ["nombre", "monto", "categoria", "fecha"]
        labels = {
            "nombre": "Nombre del gasto",
            "monto": "Monto del gasto",
            "categoria": "Categoria del gasto",
            "fecha": "Fecha del gasto",
        }
        help_texts = {
            "nombre": "Ingrese el nombre del gasto (maximo 100 caracteres).",
            "monto": "Ingrese el monto del gasto.",
            "categoria": "Seleccione la categoria del gasto.",
            "fecha": "Ingrese la fecha del gasto.",
        }
        error_messages = {
            "nombre": {
                "max_length": "El nombre del gasto no puede exceder los 100 caracteres.",
                "required": "El nombre del gasto es obligatorio.",
            },
            "monto": {"required": "El monto del gasto es obligatorio."},
            "categoria": {"required": "La categoria del gasto es obligatoria."},
            "fecha": {"required": "La fecha del gasto es obligatoria."},
        }
