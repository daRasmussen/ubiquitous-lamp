import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By

from account.models import Account

""" TODO: Add tests for messages. """


class TestProjectListPage(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('chromedriver')
        self.fakers = [
            Faker(["sv_SE"]),
            Faker(["da_DK"]),
            Faker(["en_US"]),
            Faker(["bg_BG"])
        ]

    def tearDown(self):
        self.browser.close()

    def test_index(self):
        self.browser.get(self.live_server_url)
        assert self.browser.find_element(By.LINK_TEXT, "Profile")

    def test_register_valid_user(self, user="username", mail="user@email.se", secret="password"):
        self.browser.get(self.live_server_url + "/register_user")
        username = self.browser.find_element(By.ID, "username")
        assert username
        username.send_keys(user)
        email = self.browser.find_element(By.ID, "email")
        assert email
        email.send_keys(mail)
        password = self.browser.find_element(By.ID, "password")
        assert password
        password.send_keys(secret)
        submit = self.browser.find_element(By.NAME, "submit")
        assert submit
        submit.click()
        assert self.browser.current_url == self.live_server_url + '/'
        message = self.browser.find_element(By.CLASS_NAME, "alert-success")
        assert message

    def test_register_multiple_user(self):
        for fake in self.fakers:
            for _ in range(30):
                profile = fake.profile()
                self.test_register_valid_user(
                    user=profile["username"],
                    mail=profile["mail"],
                    secret=fake.password(length=12)
                )
