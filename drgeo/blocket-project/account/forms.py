from django import forms


class SignUpForm(forms.Form):
    email = forms.EmailField(max_length=60)
    username = forms.CharField(max_length=30)
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()