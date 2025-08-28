from django.contrib import admin
from .models import Donor
# Register your models here.


@admin.register(Donor)
class DonorAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "contact", "created_at")
    search_fields = ("name", "email")
