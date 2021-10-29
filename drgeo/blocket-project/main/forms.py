from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class CustomUserCreationForm(forms.Form):
    username = forms.CharField(label="Enter your Username.", min_length=4, max_length=40)
    email = forms.EmailField(label="Enter your email.")
    password = forms.CharField(label="Enter password", widget=forms.PasswordInput)
    confirm = forms.CharField(label="Confirm password", widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        filter_out_username = User.objects.filter(username=username)
        if filter_out_username.count():
            raise ValidationError("Username already exists.")
        return username

