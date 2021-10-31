import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By

from account.models import Account


class TestProjectListPage(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('chromedriver')

    def tearDown(self):
        self.browser.close()

    def test_index(self):
        self.browser.get(self.live_server_url)
        # time.sleep(20)
        # profile = self.browser.find_element_by_class_name("profile")
        profile = self.browser.find_element(By.LINK_TEXT, "Profile")
        assert profile
