from django.urls import path
from . import views

urlpatterns = [
    path("", views.listar_categorias, name="listar_categorias"),
    path("crear/", views.crear_categoria, name="crear_categoria"),
    path("editar/<int:categoria_id>/", views.editar_categoria, name="editar_categoria"),
    path(
        "eliminar/<int:categoria_id>/",
        views.eliminar_categoria,
        name="eliminar_categoria",
    ),
]
