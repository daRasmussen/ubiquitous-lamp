from django.test import SimpleTestCase
from django.urls import reverse, resolve
from main.views import index as main_view_index
from conf.conf import Names, Locations


class TestUrls(SimpleTestCase):
    def test_index_url_is_resolved(self):
        url = reverse(Names.INDEX)
        self.assertEquals(resolve(url).func, main_view_index)
