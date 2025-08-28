

# Register your models here.
from django.contrib import admin
from .models import Expense

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ("category","amount","date","posted_to_ledger")
    list_filter = ("category","date")