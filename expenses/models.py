from django.db import models

# Create your models here.

class Expense(models.Model):
    CATEGORY_PROGRAM = "PROGRAM"
    CATEGORY_ADMIN = "ADMIN"
    CATEGORY_OTHER = "OTHER"
    CATEGORY_CHOICES = [
        (CATEGORY_PROGRAM, "Program"),
        (CATEGORY_ADMIN, "Admin"),
        (CATEGORY_OTHER, "Other"),
    ]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.CharField(max_length=255, blank=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    posted_to_ledger = models.BooleanField()

    def __str__(self):
        return f"{self.category} - {self.amount}"