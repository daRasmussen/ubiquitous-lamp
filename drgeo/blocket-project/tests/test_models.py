from django.test import TestCase

from account.models import Account


class TestModels(TestCase):
    def setUp(self):
        self.project1 = Account.objects.create(
            name="",
        )

    def test_accout_has_uuid_on_create(self):
        self.assertEqual(self.project1.slug, 'uuid')