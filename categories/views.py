from django.shortcuts import render, redirect, get_object_or_404
from .models import Category
from django.contrib import messages
from .forms import CategoriaForm
# Create your views here.


def listar_categorias(request):
    categorias = Category.objects.all()
    return render(
        request,
        "categories/listar_categorias.html",
        {"categorias": categorias},
    )


def crear_categoria(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Categoria creada exitosamente.")
            return redirect("listar_categorias")
        else:
            messages.error(
                request, "Error al crear la categoria. Por favor , corrige los errores."
            )
    else:
        form = CategoriaForm()
    return render(request, "categories/crear_categoria.html", {"form": form})


def editar_categoria(request, categoria_id):
    categoria = get_object_or_404(Category, id=categoria_id)
    if request.method == "POST":
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, "Categoria editada exitosamente.")
            return redirect("listar_categorias")
        else:
            messages.error(
                request, "Error al editar la categoria"
            )  # Muestra que no es valid y luego renderiza el formulario con los valores que tenia en la request
    else:
        # se hace cuando se entra a la url y hace un GET
        form = CategoriaForm(
            instance=categoria
        )  # crea un formulario prellenado con los datos de la categoria a editar
    return render(
        request, "categories/editar_categoria.html", {"form": form}
    )  # Esto se ejecuta cuando se hace una solicitud GET para mostrar el formulario de edición con los datos actuales de la categoria


def eliminar_categoria(request, categoria_id):
    categoria = get_object_or_404(Category, id=categoria_id)
    if request.method == "POST":
        categoria.delete()
        messages.success(request, "Categoria eliminada exitosamente.")
        return redirect("listar_categorias")
    return render(
        request, "categories/eliminar_categoria.html", {"categoria": categoria}
    )
