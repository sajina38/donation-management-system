from django.urls import path
from . import views

urlpatterns = [
    path("record/", views.record_expense, name="record_expense"),
    path("list/", views.expense_list, name="expense_list"),
]
