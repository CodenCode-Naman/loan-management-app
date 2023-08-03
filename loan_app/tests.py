from django.test import TestCase
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Customer, Loan, LoanDetail, AccountTransaction, Transaction
from django.urls import reverse
from rest_framework import status


# Create your tests here.

class ModelTestCase(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(
            name="Naman Bhatia",
            email_id="naman@gmail.com",
            credit_score=750,
            aadhar_id="a78c4437-3bf4-4ad2-85e5-e0c9b33d4786",
            annual_income=50000.00,
        )

        self.loan = Loan.objects.create(
            loan_type="personal",
            principal_amount=10000,
            interest_rate=5.0,
            loan_term=12,
            customer=self.customer,
        )

        self.loan_detail = LoanDetail.objects.create(
            loan=self.loan,
            last_transaction_date=timezone.now(),
            next_emi_date=timezone.now(),
            next_emi_amount=1000.00,
            is_active=True,
            initial_emi_amounts="[1000, 1000, 1000]",
            total_emis_left=3,
        )

        self.transaction = Transaction.objects.create(
            payment=1000.00,
            loan=self.loan,
            customer=self.customer,
            payment_date=timezone.now(),
        )

    def test_customer_model(self):
        self.assertEqual(str(self.customer), "Naman Bhatia")

    def test_loan_model(self):
        self.assertEqual(str(self.loan), "Naman Bhatia - personal Loan")

    def test_loan_detail_model(self):
        self.assertEqual(self.loan_detail.get_initial_emi_amounts(), [1000, 1000, 1000])

    def test_transaction_model(self):
        self.assertEqual(self.transaction.payment, 1000.00)
        self.assertEqual(self.transaction.loan, self.loan)
        self.assertEqual(self.transaction.customer, self.customer)

    def test_transaction_date_auto_add(self):
        account_transaction = AccountTransaction.objects.create(
            transaction_type="debit",
            amount=200.00,
            aadhar_id=self.customer.aadhar_id,
        )
        self.assertIsNotNone(account_transaction.transaction_date)

    def test_transaction_date_auto_now(self):
        transaction = Transaction.objects.create(
            payment=200.00,
            loan=self.loan,
            customer=self.customer,
        )
        self.assertIsNotNone(transaction.payment_date)

    def test_transaction_date_auto_now_add(self):
        transaction = Transaction.objects.create(
            payment=200.00,
            loan=self.loan,
            customer=self.customer,
        )
        self.assertIsNotNone(transaction.payment_date)

    def test_loan_transaction_customer_relations(self):
        self.assertEqual(self.loan.loan_transactions.count(), 1)
        self.assertEqual(self.customer.customer_transactions.count(), 1)

        transaction = self.customer.customer_transactions.first()
        self.assertEqual(transaction.loan, self.loan)

        loan_transaction = self.loan.loan_transactions.first()
        self.assertEqual(loan_transaction.customer, self.customer)

    
    def test_loan_str(self):
        loan_str = str(self.loan)
        expected_str = f"{self.customer.name} - {self.loan.loan_type} Loan"
        self.assertEqual(loan_str, expected_str)

