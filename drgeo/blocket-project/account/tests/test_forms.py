from django.test import SimpleTestCase

from account.forms import SignUpForm


class TestForms(SimpleTestCase):
    def test_signup_form_valid_data(self):
        form = SignUpForm(data={
            "email": "user@blocket.se",
            "username": "user",
            "password1": "password",
            "password2": "password"
        })
        self.assertTrue(form.is_valid())

    def test_signup_form_no_data(self):
        form = SignUpForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)