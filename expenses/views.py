from django.shortcuts import render, redirect
from .models import Expense
from .forms import ExpenseForm
# Create your views here.

def record_expense(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("expense_list")
    else:
        form = ExpenseForm()
    return render(request, "expenses/record.html", {"form": form})

def expense_list(request):
    expenses = Expense.objects.all()
    return render(request, "expenses/list.html", {"expenses": expenses})
