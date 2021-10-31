from sqlite3 import IntegrityError

import faker.utils.loading
from django.db.models import QuerySet
from django.test import TestCase
from faker import Faker

from account.models import Account


class TestAccount(TestCase):
    _first = None

    def setUp(self):
        self.fake = Faker(["sv_SE"])
        """ Setup 30 fake accounts. """
        for _ in range(30):
            profile = self.fake.profile()
            if self._first is None:
                self._first = profile
            Account.objects.create(
                username=profile["username"],
                email=profile["mail"],
                password=self.fake.password(length=12)
            )

    def test_fake_account_created(self):
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
