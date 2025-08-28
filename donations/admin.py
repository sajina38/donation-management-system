from django.contrib import admin
from .models import Donation, Event


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ("id", "donor", "amount", "method", "status", "event", "date", "posted_to_ledger")
    list_filter = ("method", "status", "event")
    search_fields = ("donor__name", "donor__email")


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("name", "start_date", "end_date")
