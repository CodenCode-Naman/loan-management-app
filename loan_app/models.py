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


# Loan Model
# to store Loan details against customer
class Loan(PrimaryKeyModel):
    LOAN_CATEGORIES = [
        ("car", "car"),
        ("home", "home"),
        ("education", "education"),
        ("personal", "personal"),
    ]

    loan_type = models.CharField(max_length=25, choices=LOAN_CATEGORIES)
    principal_amount = models.PositiveIntegerField()
    interest_rate = models.DecimalField(decimal_places=2, max_digits=5)
    loan_term = models.PositiveIntegerField()
    disbursal_date = models.DateTimeField(auto_now=True)
    start_date = models.DateField(auto_now=True)
    end_date = models.DateField(null=True, blank=True)
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="loan_customers"
    )
    remaining_amount = models.PositiveIntegerField(default=20)

    def __str__(self):
        return self.customer.name + " - " + self.loan_type + " Loan"


# LoanDetail Model
# to store loan transaction against loan
class LoanDetail(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE, related_name="loan")
    last_transaction_date = models.DateTimeField(blank=True, null=True)
    next_emi_date = models.DateField(blank=True, null=True)
    next_emi_amount = models.DecimalField(
        decimal_places=2, max_digits=10, blank=True, null=True
    )
    is_active = models.BooleanField(default=True)
    initial_emi_amounts = models.CharField(max_length=1000)
    total_emis_left = models.IntegerField()

    def set_adjusted_emi_amounts(self, lst):
        self.adjusted_emi_amounts = json.dumps(lst)

    def get_adjusted_emi_amounts(self):
        return json.loads(self.adjusted_emi_amounts)

    def set_initial_emi_amounts(self, lst):
        self.initial_emi_amounts = json.dumps(lst)

    def get_initial_emi_amounts(self):
        return json.loads(self.initial_emi_amounts)


# Transaction Model
# to store emi details against loan
class Transaction(models.Model):
    payment = models.DecimalField(max_digits=10, decimal_places=2)
    loan = models.ForeignKey(
        Loan, on_delete=models.CASCADE, related_name="loan_transactions"
    )
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="customer_transactions"
    )
   
    payment_date = models.DateTimeField(auto_now=True)