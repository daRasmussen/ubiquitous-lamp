from django.test import SimpleTestCase
from django.urls import reverse, resolve
from main.views import index as main_view_index
from account.views import register_user as account_register_user
from conf.conf import Names


class TestUrls(SimpleTestCase):
    def test_index_url_is_resolved(self):
        url = reverse(Names.INDEX)
        self.assertEquals(resolve(url).func, main_view_index)

    def test_register_user_url_is_resolved(self):
        url = reverse(Names.REGISTER_USER)
        self.assertEquals(resolve(url).func, account_register_user)

    def test_lgoin_url_is_resolved(self):
        url = reverse(Names.LOGIN_USER)