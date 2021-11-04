from django.test import TestCase
from faker import Faker

from account.models import Account
from addresses.models import Address


class TestAddress(TestCase):
    def setUp(self):
        self.fakers = [
            Faker(["sv_SE"]),
            Faker(["da_DK"]),
            Faker(["en_US"]),
            Faker(["bg_BG"])
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
                a = Address.objects.create(
                    address=fake.street_address(),
                    building_number=fake.building_number(),
                    city=fake.city(),
                    country=fake.country(),
                    postcode=fake.postcode(),
                    account=Account.objects.get(username=profile["username"])
                )
                a.save()

    def test_fake_address_created(self):
        assert Address.objects.count() == 120

    def test_address_created(self):
        for address in Address.objects.all():
            assert address
            assert address.address
            assert address.building_number
            assert address.city
            assert address.country
            assert address.postcode
            assert address.account
