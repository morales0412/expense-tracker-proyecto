from django.urls import path
from . import views

urlpatterns = [
    path("", views.listar_gastos, name="listar_gastos"),
    path("crear/", views.crear_gasto, name="crear_gasto"),
    path("editar/<int:gasto_id>/", views.editar_gasto, name="editar_gasto"),
    path("eliminar/<int:gasto_id>/", views.eliminar_gasto, name="eliminar_gasto"),
]
