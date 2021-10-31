from django.test import SimpleTestCase
from faker import Faker

from account.forms import SignUpForm


class TestForms(SimpleTestCase):
    profiles = []

    def setUp(self):
        self.fakers = [
            Faker(["sv_SE"]),
            Faker(["da_DK"]),
            Faker(["en_US"]),
            Faker(["bg_BG"]),
            Faker(["da_DK"]),
            Faker(["sv_SE"]),
            Faker(["bg_BG"]),
            Faker(["en_US"]),
        ]
        for fake in self.fakers:
            for _ in range(100):
                profile = fake.profile()
                self.profiles.append({
                    "username": profile["username"],
                    "email": profile["mail"],
                    "password": fake.password(length=12)
                })

    def test_signup_form_valid_data(self):
        for profile in self.profiles:
            assert SignUpForm(data={
                "email": profile["email"],
                "username": profile["username"],
                "password1": profile["password"],
                "password2": profile["password"]
            }).is_valid()

    def test_signup_form_no_data(self):
        form = SignUpForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)

    """ TODO: Add tests for validation, etc.. """