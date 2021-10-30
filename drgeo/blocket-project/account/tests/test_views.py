from django.test import TestCase
from django.urls import reverse

from conf.conf import Names, Locations


class BaseTest(TestCase):
    def setUp(self):
        self.register_url = reverse(Names.REGISTER_USER)
        return super().setUp()


class RegisterTest(BaseTest):
    def test_view_register_user(self):
        res = self.client.get(self.register_url)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, Locations.REGISTER_USER)