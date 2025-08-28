from django.shortcuts import render, redirect
from .models import Donor
from .forms import DonorForm

# Create your views here.

def donor_register(request):
    if request.method == "POST":
        form = DonorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("donor_list")
    else:
        form = DonorForm()
    return render(request, "donors/register.html", {"form": form})

def donor_list(request):
    donors = Donor.objects.all()
    return render(request, "donors/list.html", {"donors": donors})