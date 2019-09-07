from django.db import models
from enum import Enum

# Create your models here.


class AccountType(Enum):
    INCOME = "Income"
    EXPENSE = "Expense"
    ASSET = "Asset"
    LIABILILTY = "Liability"
    EQUITY = "Equity"
    COGS = "COGS"


class Account(models.Model):
    name = models.CharField(max_length=200, blank=False)
    type = models.CharField(
        max_length=12,
        choices=[(act_type.name, act_type.value) for act_type in AccountType]
    )
    createdate = models.DateTimeField('date created', auto_now_add=True)

    def __unicode__(self):
        return '{}'.format(self.name)

    def __str__(self):
        return self.__unicode__()
