import form as form
from django.contrib.auth.forms import UserCreationForm
from django import forms

from accounts.models import UserProfile
from core.BootstrapFormMixin import BootstrapFormMixin


class SignUpForm(UserCreationForm, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setup_form()


class UserProfileImageForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_picture',)
