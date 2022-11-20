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


def validate_age(age):
    if age < 17:
        ValidationError(
            'Age cannot be validated. Please try again.'
        )
    elif age > 101:
        ValidationError(
            'Please enter a valid age. Try again.'
        )
    else:
        return True
