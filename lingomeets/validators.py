from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


validate_only_letters = RegexValidator(
    (
        '[^0-9]+'
    )
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


def validate_birthday(value):
    if value.year > 2004:
        raise ValidationError(
            'LingoMeets members must be over 18 to attend events.'
        )
    elif value.year < 1920:
        raise ValidationError(
            'Please enter a valid age.'
        )
    else:
        pass
