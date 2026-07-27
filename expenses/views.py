from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense, Category
from .forms import ExpenseForm
from django.contrib import messages
from django.db.models import Q, Sum, Count
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.


class ListarGastosView(ListView):
    model = Expense
    template_name = "expenses/listar_gastos.html"
    context_object_name = "gastos"

    def get_queryset(self):
        queryset = super().get_queryset()
        busqueda = self.request.GET.get("busqueda", "")
        if busqueda:
            queryset = queryset.filter(
                Q(nombre__icontains=busqueda) | Q(categoria__nombre__icontains=busqueda)
            )
        print(queryset)
        return queryset


# def listar_gastos(request):
#     gastos = Expense.objects.all()
#     busqueda = request.GET.get("busqueda", "")
#     total = Expense.objects.annotate(monto_total=Sum("monto"))
#     if busqueda:
#         gastos = gastos.filter(
#             Q(nombre__icontains=busqueda) | Q(categoria__nombre__icontains=busqueda)
#         )
#     return render(
#         request, "expenses/listar_gastos.html", {"gastos": gastos, "busqueda": busqueda}
#     )


class CrearGastoView(CreateView):
    model = Expense
    template_name = "expenses/crear_gasto.html"
    form_class = ExpenseForm
    success_url = reverse_lazy("listar_gastos")


# def crear_gasto(request):
#     if request.method == "POST":
#         form = ExpenseForm(request.POST)
#         if form.is_valid():
#             print(request.POST.get("fecha"))
#             form.save()
#             messages.success(request, "Gasto creado con exito")
#             return redirect("listar_gastos")
#         else:
#             messages.error(
#                 request, "Error al crear el gasto. Por favor, corrige los errores."
#             )
#     else:
#         form = ExpenseForm()
#     return render(request, "expenses/crear_gasto.html", {"form": form})


class EditarGastoView(UpdateView):
    model = Expense
    template_name = "expenses/editar_gasto.html"
    form_class = ExpenseForm
    success_url = reverse_lazy("listar_gastos")


# def editar_gasto(request, gasto_id):
#     gasto = get_object_or_404(Expense, id=gasto_id)
#     if request.method == "POST":
#         form = ExpenseForm(request.POST, instance=gasto)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Gasto editado con exito")
#             return redirect("listar_gastos")
#         else:
#             messages.error(
#                 request, "Error al editar el gasto. Por favor, corrige los errores."
#             )
#     else:
#         form = ExpenseForm(instance=gasto)
#     return render(request, "expenses/editar_gasto.html", {"form": form})


class EliminarGastoView(DeleteView):
    model = Expense
    template_name = "expenses/eliminar_gasto.html"
    success_url = reverse_lazy("listar_gastos")
    context_object_name = "gasto"


# def eliminar_gasto(request, gasto_id):
#     gasto = get_object_or_404(Expense, id=gasto_id)
#     if request.method == "POST":
#         gasto.delete()
#         messages.success(request, "Gasto eliminado con exito")
#         return redirect("listar_gastos")
#     return render(request, "expenses/eliminar_gasto.html", {"gasto": gasto})


def dashboard(request):
    total = Expense.objects.aggregate(monto_total=Sum("monto"))["monto_total"] or 0
    print(total)
    cantidad_gastos = Expense.objects.count()
    gastos_por_categoria = Category.objects.annotate(
        total_gastos=Sum("expense__monto"), cantidad=Count("expense")
    )
    print(gastos_por_categoria)
    return render(
        request,
        "expenses/dashboard.html",
        {
            "total": total,
            "cantidad_gastos": cantidad_gastos,
            "gastos_por_categoria": gastos_por_categoria,
        },
    )
