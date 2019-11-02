from django.db import models
from django.core.validators import MinValueValidator
from enum import Enum
import datetime


# Create your models here.

# Look into all the complete asset types - capture everything but be as efficient as possible.



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


class Transaction(models.Model):
    memo = models.CharField(max_length=200, blank=False)
    ref_number = models.CharField(max_length=200, blank=False)
    createdate = models.DateTimeField('date created', auto_now_add=True)
    transactiondate = models.DateField('transaction date', default=datetime.datetime.now())

    def __unicode__(self):
        return '{}'.format(self.memo)

    def __str__(self):
        return self.__unicode__()


class Category(models.Model):
    name = models.CharField(max_length=200, blank=False)

    def __unicode__(self):
        return '{}'.format(self.name)

    def __str__(self):
        return self.__unicode__()


class Credit(models.Model):
    value = models.DecimalField(max_digits=20, decimal_places=2, validators=[MinValueValidator(0)])
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)


class Debit(models.Model):
    value = models.DecimalField(max_digits=20, decimal_places=2, validators=[MinValueValidator(0)])
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)



