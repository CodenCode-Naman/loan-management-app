from django.db import models
from utils.abstract_models import PrimaryKeyModel
import json
# Create your models here.

# Customer Model
class Customer(PrimaryKeyModel):
    name = models.CharField(max_length=100)
    email_id = models.EmailField()
    credit_score = models.IntegerField(null=True, blank=True)
    aadhar_id = models.UUIDField(unique=True)
    annual_income = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

# AccountTransaction Model
# to store customers account balance and transactions
class AccountTransaction(models.Model):
    TRANSACTION_CHOICES = [
        ("credit", "CREDIT"),
        ("debit", "DEBIT"),
    ]
    transaction_type = models.CharField(choices=TRANSACTION_CHOICES, max_length=20)
    transaction_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    aadhar_id = models.UUIDField(editable=False)

    def __str__(self):
        return self.transaction_type + " - " + self.amount