from django.urls import path
from . import views

urlpatterns = [
    path("record/", views.record_donation, name="record_donation"),
    path("list/", views.donation_list, name="donation_list"),
    path("reports/", views.reports, name="reports"),
]
