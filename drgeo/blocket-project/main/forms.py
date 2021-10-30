from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.views.generic import FormView

from main.models import Profile


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


class CustomUserChangeForm(UserChangeForm):
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
        self.fields["first_name"].widget.attrs.update({
            "type": "text",
            "class": "form-control",
            "id": "firstName"
        })
        self.fields["last_name"].widget.attrs.update({
            "type": "text",
            "class": "form-control",
            "id": "lastName"
        })

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
        ]


class CustomProfileCreationForm(FormView):
    class Meta:
        model = Profile
        fields = [
            "image",
            "phone",
            "url",
        ]


class CustomProfileChangeForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["phone"].widget.attrs.update({
            "type": "text"
        })
        self.fields["image"].widget.attrs.update({
            "type": "image"
        })
        self.fields["url"].widget.attrs.update({
            "type": "text"
        })

    class Meta:
        model: Profile
        fields = [
            "phone"
            "image",
            "url"
        ]