from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            "required": "",
            "type": "text",
            "class": "form-control",
            "id": "floatingInput",
            "placeholder": "user",
        })
        self.fields["email"].widget.attrs.update({
            "required": "",
            "type": "email",
            "class": "form-control",
            "id": "floatingInput",
            "placeholder": "name@example.com",
        })
        self.fields["password1"].widget.attrs.update({
            "required": "",
            "type": "password",
            "class": "form-control",
            "id": "floatingInput",
            "placeholder": "Password",
        })
        self.fields["password2"].widget.attrs.update({
            "required": "",
            "type": "password",
            "class": "form-control",
            "id": "floatingInput",
            "placeholder": "Password",
        })

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2"
        ]