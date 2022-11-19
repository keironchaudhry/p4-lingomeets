from django.core.exceptions import ValidationError


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
