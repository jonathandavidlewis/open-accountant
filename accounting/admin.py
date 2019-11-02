from django.contrib import admin
from django import forms
from accounting.models import *
from django.contrib.admin import ModelAdmin
from django.contrib.admin import ModelAdmin, SimpleListFilter
from admin_views.admin import AdminViews
from django.db.models import Q

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

class TransactionFilter(SimpleListFilter):
  title = 'Scrape status' # a label for our filter
  parameter_name = 'account' # you can put anything here

  def lookups(self, request, model_admin):
    # This is where you create filter options; we have two:
    account_names = list(Account.objects.all().values_list("name", flat=True))
    return [(name, name) for name in account_names]
    return [
        ('scraped', 'Scraped'),
        ('not_scraped', 'Not scraped'),
    ]

  def queryset(self, request, queryset):
    if self.value() == None:
          return queryset.all()
    debits = Debit.objects.filter(account__name=self.value())
    credits = Credit.objects.filter(account__name=self.value())
    return queryset.filter(Q(credit__in=credits) | Q(debit__in=debits))
    # if self.value() == 'scraped':
        # Get websites that have at least one page.
        # credits = Credit.objects.filter(account__name=AccountType.INCOME.name)
        # credits = Credit.objects.filter(account__name=AccountType.INCOME.name)

    #
    # if self.value():
    #     # Get websites that don't have any pages.
    #     return queryset.distinct().filter(pages__isnull=True)


class WebsiteAdmin(AdminViews):
    list_display = ['url']
    search_fields = ['url']
    list_filter = (TransactionFilter,)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    inlines = [
        CreditInline, DebitInline
    ]
    formset = TransactionFormset
    list_filter = (TransactionFilter,)

# admin.site.register(TransactionAdmin)






