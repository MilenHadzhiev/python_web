from django import forms

from todo_app.validators import validate_name


class TodoForm(forms.Form):
    title = forms.CharField(
        label='Title',
        max_length=20,
        validators=(
            validate_name,
        ),
    )
    description = forms.CharField(label='Description', widget=forms.Textarea)
    bot_catcher = forms.CharField(
        widget=forms.HiddenInput,
        required=False,
    )

    def clean_bot_catcher(self):
        if len(self.cleaned_data['bot_catcher']):
            raise forms.ValidationError('This is a bot')