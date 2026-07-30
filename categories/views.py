from django.shortcuts import render, redirect, get_object_or_404
from .models import Category
from django.contrib import messages
from .forms import CategoriaForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class ListarCategoriasView(LoginRequiredMixin, ListView):
    model = Category
    template_name = "categories/listar_categorias.html"
    context_object_name = "categorias"

    def get_queryset(self):
        queryset = super().get_queryset().filter(usuario=self.request.user)
        busqueda = self.request.GET.get("busqueda", "")
        if busqueda:
            queryset = queryset.filter(
                nombre__icontains=busqueda, usuario=self.request.user
            )
        return queryset


# def listar_categorias(request):
#     categorias = Category.objects.all()
#     busqueda = request.GET.get("busqueda", "")
#     if busqueda:
#         categorias = categorias.filter(nombre__icontains=busqueda)
#     return render(
#         request,
#         "categories/listar_categorias.html",
#         {"categorias": categorias, "busqueda": busqueda},
#     )


class CrearCategoriaView(LoginRequiredMixin, CreateView):
    model = Category
    template_name = "categories/crear_categorias.html"
    form_class = CategoriaForm
    success_url = reverse_lazy("listar_categorias")

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)


# def crear_categoria(request):
#     if request.method == "POST":
#         form = CategoriaForm(request.POST)
#         if form.is_valid():
#             form.save()
#             print(request.POST["nombre"])
#             print(form.data)
#             messages.success(request, "Categoria creada exitosamente.")
#             return redirect("listar_categorias")
#         else:
#             messages.error(
#                 request, "Error al crear la categoria. Por favor , corrige los errores."
#             )
#     else:
#         form = CategoriaForm()
#     return render(request, "categories/crear_categorias.html", {"form": form})


class EditarCategoriaView(LoginRequiredMixin, UpdateView):
    model = Category
    template_name = "categories/editar_categoria.html"
    form_class = CategoriaForm
    success_url = reverse_lazy("listar_categorias")

    def get_queryset(self):
        return super().get_queryset().filter(usuario=self.request.user)


# def editar_categoria(request, categoria_id):
#     categoria = get_object_or_404(Category, id=categoria_id)
#     if request.method == "POST":
#         form = CategoriaForm(request.POST, instance=categoria)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Categoria editada exitosamente.")
#             return redirect("listar_categorias")
#         else:
#             messages.error(
#                 request, "Error al editar la categoria"
#             )  # Muestra que no es valido y luego renderiza el formulario con los valores que tenia en la request
#     else:
#         # se hace cuando se entra a la url y hace un GET
#         form = CategoriaForm(
#             instance=categoria
#         )  # crea un formulario prellenado con los datos de la categoria a editar
#     return render(
#         request, "categories/editar_categoria.html", {"form": form}
#     )  # Esto se ejecuta cuando se hace una solicitud GET para mostrar el formulario de edición con los datos actuales de la categoria o cuando los datos enviados en una solicitud POST no son validos y se quiere mostrar el formulario nuevamente con los errores y los datos ingresados por el usuario.


class EliminarCategoriaView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = "categories/eliminar_categoria.html"
    context_object_name = "categoria"
    success_url = reverse_lazy("listar_categorias")

    def get_queryset(self):
        return super().get_queryset().filter(usuario=self.request.user)


# def eliminar_categoria(request, categoria_id):
#     categoria = get_object_or_404(Category, id=categoria_id)
#     if request.method == "POST":
#         categoria.delete()
#         messages.success(request, "Categoria eliminada exitosamente.")
#         return redirect("listar_categorias")
#     return render(
#         request, "categories/eliminar_categoria.html", {"categoria": categoria}
#     )
