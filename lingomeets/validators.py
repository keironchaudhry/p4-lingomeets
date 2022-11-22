from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


validate_only_letters = RegexValidator(
    r'^[a-zA-Z]*$',
    'Only alphabetical letters allowed.'
)


def validate_textfields(value):
    if len(value) < 5:
        raise ValidationError(
            'You have entered less than 5 characters.'
        )
    elif len(value) > 250:
        raise ValidationError(
            'You have reached character limit of 250 characters.'
        )
    else:
        pass


def validate_age(age):
    if age < 17:
        return ''
    elif age > 101:
        return ''
    else:
        return True
