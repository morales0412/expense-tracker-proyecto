from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("lista/", views.ListarGastosView.as_view(), name="listar_gastos"),
    path("crear/", views.CrearGastoView.as_view(), name="crear_gasto"),
    path("editar/<int:pk>/", views.EditarGastoView.as_view(), name="editar_gasto"),
    path(
        "eliminar/<int:pk>/", views.EliminarGastoView.as_view(), name="eliminar_gasto"
    ),
]
