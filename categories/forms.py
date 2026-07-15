from django import forms
from .models import Category


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["nombre", "descripcion"]
        labels = {
            "nombre": "Nombre de la categoria",
            "descripcion": "Descripcion de la categoria",
        }
        help_texts = {
            "nombre": "Ingrese el nombre de la categoria (maximo 100 caracteres).",
            "descripcion": "Ingrese una descripcion para la categoria (opcional).",
        }
        error_messages = {
            "nombre": {
                "max_length": "El nombre de la categoria no puede exceder los 100 caracteres.",
                "required": "El nombre de la categoria es obligatorio.",
            },
            "descripcion": {
                "max_length": "La descripcion de la categoria no puede exceder los 200 caracteres",
            },
        }
