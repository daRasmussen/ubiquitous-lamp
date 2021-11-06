import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestIndex(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('chromedriver')

    def tearDown(self):
        self.browser.close()

    def test_profile_link_text(self):
        self.browser.get(self.live_server_url)
        assert self.browser.find_element(By.LINK_TEXT, "Profile")
