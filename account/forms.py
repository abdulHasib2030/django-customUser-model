from typing import Any
from account.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import authenticate

class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password1', 'password2']

class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self) -> dict[str, Any]:
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        user = authenticate(email = email, password= password)
        if not user:
            raise forms.ValidationError("Invalid email or password")
        return self.cleaned_data
