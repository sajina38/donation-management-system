from django.db import models

# Create your models here.
class Donor(models.Model):
    name = models.CharField(max_length=255)
    email= models.EmailField(unique=True)
    contact= models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return f"{self.name} {self.email}"

