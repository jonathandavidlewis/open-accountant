from django.contrib import admin
from django import forms
from accounting.models import *

admin.site.register(Account)
# admin.site.register(Transaction)
# admin.site.register(Credit)
# admin.site.register(Debit)
admin.site.register(Category)


class CreditInline(admin.TabularInline):
    model = Credit
    extra = 0


class DebitInline(admin.TabularInline):
    model = Debit
    extra = 0


# todo: Allow only transactions with equal debit / credit totals to save.
class TransactionFormset(forms.models.BaseInlineFormSet):
    def clean(self):
        class Meta:
            model = Transaction

        count = 0
        for form in self.forms:
            try:
                if form.cleaned_data:
                    count += 1
            except AttributeError:
                # annoyingly, if a subform is invalid Django explicity raises
                # an AttributeError for cleaned_data
                pass
        if count < 1:
            raise forms.ValidationError('You must have at least one order')


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    inlines = [
        CreditInline, DebitInline
    ]
    formset = TransactionFormset

# admin.site.register(TransactionAdmin)
