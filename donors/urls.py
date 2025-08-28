from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.donor_register, name="donor_register"),
    path("list/", views.donor_list, name="donor_list"),
]
