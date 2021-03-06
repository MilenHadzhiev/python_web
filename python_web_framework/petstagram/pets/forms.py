from django import forms

from pets.models import Pet, Comment


class PetCreateForm(forms.ModelForm):
    class Meta:
        model = Pet
        exclude = ('type', 'user')


class CommentForm(forms.Form):
    comment = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control rounded-2'
            }
        )
    )
