from django import forms
from .models import Users

from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']