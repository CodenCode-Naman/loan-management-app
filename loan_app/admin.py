from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Customer)
admin.site.register(models.AccountTransaction)
admin.site.register(models.Loan)
admin.site.register(models.LoanDetail)
admin.site.register(models.Transaction)
