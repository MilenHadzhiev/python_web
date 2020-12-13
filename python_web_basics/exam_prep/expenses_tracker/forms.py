from django import forms
from django.core.validators import MinValueValidator


class ProfileForm(forms.Form):
    first_name = forms.CharField(max_length=15, required=True)
    last_name = forms.CharField(max_length=15, required=True)
    budget = forms.IntegerField(validators=
    [MinValueValidator(
        1,
        message='The budget must be a positive number'
    )
    ],
        required=True
    )


class ExpenseForm(forms.Form):
    title = forms.CharField(max_length=50, required=True)
    image_url = forms.URLField(required=True)
    description = forms.CharField(widget=forms.Textarea(), required=True)
    price = forms.FloatField(validators=[
        MinValueValidator(1,
                          message='The price must be a positive number'
                          )
    ],
        required=True)
