from django import forms

from account.models import Account


class ProfileForm(forms.Form):
    username = forms.CharField(max_length=60)
    email = forms.EmailField(max_length=60)
    password = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    phone = forms.CharField(max_length=30)
    image = forms.ImageField()
    about = forms.CharField(max_length=300)

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
        }),
        self.fields["password"].widget.attrs.update({
            "type": "password",
            "class": "form-control",
            "id": "password",
            "placeholder": "super-secret-password"
        })
        self.fields["first_name"].widget.attrs.update({
            "required": "",
            "type": "text",
            "class": "form-control",
            "id": "username",
            "placeholder": "Username"
        })
        self.fields["last_name"].widget.attrs.update({
            "required": "",
            "type": "text",
            "class": "form-control",
            "id": "username",
            "placeholder": "Username"
        })
        self.fields["phone"].widget.attrs.update({
            "required": "",
            "type": "text",
            "class": "form-control",
            "id": "username",
            "placeholder": "Username"
        })
        self.fields["about"].widget.attrs.update({
            "required": "",
            "type": "text",
            "class": "form-control",
            "id": "username",
            "placeholder": "Username"
        })
        self.fields["image"].widget.attrs.update({
            "required": "",
            "type": "image",
            "class": "form-control",
            "id": "username",
            "placeholder": "Username"
        })

        class Meta:
            model = Account
            fields = [
                "username",
                "email",
                "password",
                "last_name",
                "first_name",
                "phone",
                "about",
                "image",
            ]