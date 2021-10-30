from django.test import TestCase
from django.urls import reverse


class BaseTest(TestCase):
    def setUp(self):
        self.register_url = reverse('register')
        return super().setUp()


class RegisterTest(BaseTest):
    def test_can_view_page_correctly(self):
        res = self.client.get(self.register_url)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'account/register_user')
