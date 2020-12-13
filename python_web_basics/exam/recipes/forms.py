from django import forms
from django.core.validators import MinValueValidator


class RecipeForm(forms.Form):
    title = forms.CharField(max_length=30)
    image_url = forms.URLField()
    description = forms.CharField(widget=forms.Textarea)
    ingredients = forms.CharField(max_length=250)
    time = forms.IntegerField(validators=(MinValueValidator(
        0,
        message='Time to cook can not be a negative number'),
        )
    )
