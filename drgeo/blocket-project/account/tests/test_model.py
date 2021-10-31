from sqlite3 import IntegrityError

from django.test import TestCase
from faker import Faker

from account.models import Account


class TestAccount(TestCase):
    _first = None

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
                if self._first is None:
                    self._first = profile
                a = Account.objects.create(
                    username=profile["username"],
                    email=profile["mail"],
                    password=fake.password(length=12)
                )
                a.save()

    def test_fake_account_created(self):
        assert Account.objects.count() == 120
        assert self._first
        assert isinstance(self._first, dict)

    def test_accounts_created(self):
        for account in Account.objects.all():
            assert account
            assert account.email
            assert account.username
            assert account.password
            assert account.is_active
            assert account.date_joined
            assert account.is_staff is False
            assert account.is_superuser is False
            assert account.phone == ""
            assert account.first_name == ""
            assert account.last_name == ""
            assert account.image

    def test_accounts_update(self):
        for fake in self.fakers[::-1]:
            for account in Account.objects.all():
                new_username = fake.profile()["username"]
                if not Account.objects.filter(username=new_username):
                    assert Account.objects.filter(id=account.id).update(username=new_username)

    def test_accounts_delete(self):
        for fake in self.fakers:
            for account in Account.objects.all():
                entry = Account.objects.get(username=account.username)
                assert entry.delete()