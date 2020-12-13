from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, EmailValidator, MinLengthValidator


def validate_name(value):
    if value[0].islower():
        raise ValidationError('The name must start with an uppercase letter.')
    if len(value) < 6:
        raise ValidationError('The name must have at least 6 characters.')


def validate_age(value):
    if MinValueValidator(value):
        raise ValidationError('The age cannot be less than zero.')


def validate_email(value):
    if EmailValidator(value):
        raise ValidationError('Enter a valid email.')
