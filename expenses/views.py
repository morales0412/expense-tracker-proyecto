from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense
from .forms import ExpenseForm
from django.contrib import messages
# Create your views here.


def listar_gastos(request):
    gastos = Expense.objects.all()
    return render(request, "expenses/listar_gastos.html", {"gastos": gastos})


def crear_gasto(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Gasto creado con exito")
            return redirect("listar_gastos")
        else:
            messages.error(
                request, "Error al crear el gasto. Por favor, corrige los errores."
            )
    else:
        form = ExpenseForm()
    return render(request, "expenses/crear_gasto.html", {"form": form})


def editar_gasto(request, gasto_id):
    gasto = get_object_or_404(Expense, id=gasto_id)
    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=gasto)
        if form.is_valid():
            form.save()
            messages.success(request, "Gasto editado con exito")
            return redirect("listar_gastos")
        else:
            messages.error(
                request, "Error al editar el gasto. Por favor, corrige los errores."
            )
    else:
        form = ExpenseForm(instance=gasto)
    return render(request, "expenses/editar_gasto.html", {"form": form})


def eliminar_gasto(request, gasto_id):
    gasto = get_object_or_404(Expense, id=gasto_id)
    if request.method == "POST":
        gasto.delete()
        messages.success(request, "Gasto eliminado con exito")
        return redirect("listar_gastos")
    return render(request, "expenses/eliminar_gasto.html", {"gasto": gasto})
