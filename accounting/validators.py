from django.core.exceptions import ValidationError


def validate_debit_credit_zero_sum(value):
    if value % 2 != 0:
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': value},
        )
