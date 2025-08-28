from django.db import models
from donors.models import Donor
from django.utils import timezone

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(max_length=255)
    created_at = models.DateField(null=True)
    end_date = models.DateField(null=True)
     
    def __str__(self):
        return self.name

class Donation:
    CASH_METHOD = "CASH"    # valid options banako
    BANK_METHOD = "BANK"    # to record people's payment_method
    ONLINE_METHOD = "Cash"   # and for using in models below
    METHOD_CHOICES = [
        (CASH_METHOD ,"Cash"),
        (BANK_METHOD ,"Bank"),
        (ONLINE_METHOD, "Online"),
    ]

    STATUS_PENDING = "PENDING"
    STATUS_CONFIRMED = "CONFIRMED"
    STATUS_CHOICES = [
        (STATUS_PENDING, "Pending"),
        (STATUS_CONFIRMED, "Confirmed"),
    ]


    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, null=True, blank=True, on_delete=models.SET_NULL)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    method = models.CharField(max_length=10, choices=METHOD_CHOICES)
    date = models.DateField(default=timezone.localdate)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=STATUS_PENDING)
    posted_to_ledger = models.BooleanField()
    receipt_pdf = models.FileField(upload_to="receipts/", blank=True, null=True)

    def __str__(self):
        return f"{self.donor.name} - {self.amount}"

    

