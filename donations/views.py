
from django.shortcuts import render, redirect
from .models import Donation
from .forms import DonationForm
from expenses.models import Expense

# Create your views here.

def home(request):
    return render(request, "donations/home.html")
 
def record_donation(request):
    if request.method == "POST":
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("donation_list")
    else:
        form = DonationForm()
    return render(request, "donations/record.html", {"form": form})

def donation_list(request):
    donations = Donation.objects.all()
    return render(request, "donations/list.html", {"donations": donations})


def reports(request):
    total_donations = Donation.objects.all().aggregate(sum_amount=models.Sum("amount"))["sum_amount"] or 0
    total_expenses = Expense.objects.all().aggregate(sum_amount=models.Sum("amount"))["sum_amount"] or 0
    remaining = total_donations - total_expenses

    context = {
        "total_donations": total_donations,
        "total_expenses": total_expenses,
        "remaining": remaining,
    }
    return render(request, "reports/dashboard.html", context)