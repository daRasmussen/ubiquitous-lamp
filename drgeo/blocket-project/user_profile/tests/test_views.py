from django.test import TestCase, Client, TransactionTestCase
from django.urls import reverse
from faker import Faker

from account.models import Account
from addresses.models import Address
from conf.conf import Names, Locations


class BaseTest(TransactionTestCase):
    accounts = []

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
                account = Account.objects.create(
                    username=profile["username"],
                    email=profile["mail"],
                    password=fake.password(length=12)
                )
                account.save()
                address = Address.objects.create(
                    address=fake.street_address(),
                    building_number=fake.building_number(),
                    city=fake.city(),
                    country=fake.country(),
                    postcode=fake.postcode(),
                    account=Account.objects.get(username=profile["username"])
                )
                self.accounts.append({
                    "account": account,
                    "address": address
                })
        return super().setUp()


class RegisterTest(BaseTest):
    def test_view_update_account_GET(self):
        res = self.client.get(self.register_url)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, Locations.USER_PROFILE)

    def test_view_register_new_user_POST(self):
        for account in self.accounts:
            res = self.client.post(self.register_url, {
                "username":     account["account"]["username"],
                "email":        account["account"]["email"],
                "image":        account["account"]["email"],
                "first_name":   account["account"]["email"],
                "last_name":    account["account"]["email"],
                "phone":        account["account"]["email"],
                "about":        account["account"]["email"],
                "street":       account["address"]["email"],
                "postcode":     account["address"]["email"],
                "city":         account["address"]["email"],
                "country":      account["address"]["email"],
                "user":         Account.objects.get(username=account["account"]["username"])
            })
            """ Redirect """
            self.assertEquals(res.status_code, 302)
            assert Account.objects.count() != 0
            assert Address.objects.count() != 0

