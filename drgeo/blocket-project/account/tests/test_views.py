from django.test import TestCase, Client, TransactionTestCase
from django.urls import reverse
from faker import Faker

from account.models import Account
from conf.conf import Names, Locations


class BaseTest(TransactionTestCase):
    profiles = []

    def setUp(self):
        self.client = Client()
        self.register_url = reverse(Names.REGISTER_USER)
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
            for _ in range(30):
                profile = fake.profile()
                self.profiles.append({
                    "username": profile["username"],
                    "email": profile["mail"],
                    "password": fake.password(length=12)
                })
        return super().setUp()


class RegisterTest(BaseTest):
    def test_view_register_user_GET(self):
        res = self.client.get(self.register_url)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, Locations.REGISTER_USER)

    def test_view_register_new_user_POST(self):
        for profile in self.profiles:
            res = self.client.post(self.register_url, {
                "username": profile["username"],
                "email": profile["email"],
                "password": profile["password"]
            })
            """ Redirect """
            self.assertEquals(res.status_code, 302)
            """ TODO: Assert that user has been created. """
            assert Account.objects.count() != 0

    """ Assert that users are in db. """
    #def test_view_register_confirm_users_created(self):
    #        for profile in self.profiles:
    #            assert Account.objects.get(username=profile["username"])
    #            assert Account.objects.get(email=profile["email"])

    """ TODO: Create test for error handling. """
