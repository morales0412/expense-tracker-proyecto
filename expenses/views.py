from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense, Category
from .forms import ExpenseForm
from django.contrib import messages
from django.db.models import Q, Sum, Count
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class ListarGastosView(LoginRequiredMixin, ListView):
    model = Expense
    template_name = "expenses/listar_gastos.html"
    context_object_name = "gastos"

    def get_queryset(self):
        queryset = super().get_queryset().filter(usuario=self.request.user)
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


class CrearGastoView(LoginRequiredMixin, CreateView):
    model = Expense
    template_name = "expenses/crear_gasto.html"
    form_class = ExpenseForm
    success_url = reverse_lazy("listar_gastos")

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)


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


class EditarGastoView(LoginRequiredMixin, UpdateView):
    model = Expense
    template_name = "expenses/editar_gasto.html"
    form_class = ExpenseForm
    success_url = reverse_lazy("listar_gastos")

    def get_queryset(self):
        return super().get_queryset().filter(usuario=self.request.user)


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


class EliminarGastoView(LoginRequiredMixin, DeleteView):
    model = Expense
    template_name = "expenses/eliminar_gasto.html"
    success_url = reverse_lazy("listar_gastos")
    context_object_name = "gasto"

    def get_queryset(self):
        return super().get_queryset().filter(usuario=self.request.user)


# def eliminar_gasto(request, gasto_id):
#     gasto = get_object_or_404(Expense, id=gasto_id)
#     if request.method == "POST":
#         gasto.delete()
#         messages.success(request, "Gasto eliminado con exito")
#         return redirect("listar_gastos")
#     return render(request, "expenses/eliminar_gasto.html", {"gasto": gasto})


@login_required
def dashboard(request):
    total = (
        Expense.objects.filter(usuario=request.user).aggregate(
            monto_total=Sum("monto")
        )["monto_total"]
        or 0
    )
    cantidad_gastos = Expense.objects.filter(usuario=request.user).count()
    print(request.user)
    gastos_por_categoria = Category.objects.filter(
        expense__usuario=request.user
    ).annotate(total_gastos=Sum("expense__monto"), cantidad=Count("expense"))
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
