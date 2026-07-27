from django.urls import path
from . import views

urlpatterns = [
    path("", views.ListarCategoriasView.as_view(), name="listar_categorias"),
    path("crear/", views.CrearCategoriaView.as_view(), name="crear_categoria"),
    path(
        "editar/<int:pk>/",
        views.EditarCategoriaView.as_view(),
        name="editar_categoria",
    ),
    path(
        "eliminar/<int:pk>/",
        views.EliminarCategoriaView.as_view(),
        name="eliminar_categoria",
    ),
]
