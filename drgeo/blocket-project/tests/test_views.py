from django.test import TestCase, Client
from django.urls import reverse

from account.models import Account
from conf.conf import Names, Locations


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.index_url = reverse(Names.INDEX.name)
        self.fake_account = Account.objects.create(
            username="FAKE HELP",
            email="FAKERS@FAKES.se",
            password="FAKERS@FAKERS"""
        )

    def test_project_list_GET(self):
        res = self. client.get(self.index_url)

        self.assertEquals(res.status_code, 200)
        self.assertTemplateUsed(res, Locations.INDEX.name)
