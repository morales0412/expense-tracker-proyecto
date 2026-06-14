from django import forms
from .models import Category


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["nombre", "descripcion"]
