from django import forms

from account.models import Account


class SignUpForm(forms.Form):
    email = forms.EmailField(max_length=60)
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            "required": "",
            "type": "text",
            "class": "form-control",
            "id": "username",
            "placeholder": "Username"
        })
        self.fields["email"].widget.attrs.update({
            "type": "email",
            "class": "form-control",
            "id": "email",
            "placeholder": "you@example.com",
        })
        self.fields["password"].widget.attrs.update({
            "type": "password",
            "class": "form-control",
            "id": "password",
            "placeholder": "super-secret-password"
        })

        class Meta:
            model = Account
            fields = [
                "username",
                "email",
                "password"
            ]


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=60)
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update({
            "required": "",
            "type": "text",
            "class": "form-control",
            "id": "email",
            "placeholder": "email"
        })

        self.fields["password"].widget.attrs.update({
            "type": "password",
            "class": "form-control",
            "id": "password",
            "placeholder": "super-secret-password"
        })

        class Meta:
            model = Account
            fields = [
                "email",
                "password"
            ]
