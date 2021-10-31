from django.test import SimpleTestCase
from account.forms import SignUpForm

class TestForms(SimpleTestCase):
    def test_signup_form_valid_data(self):
        form = SignUpForm(data={
           "username": 'FAKES'
        })
        #self.assertTrue(from.is_valid())