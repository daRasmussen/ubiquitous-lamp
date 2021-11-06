import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestProjectListPage(StaticLiveServerTestCase):
    profiles = []
    # max 30
    NUMBER_OF_PROFILES = 1

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
        # time.sleep(10)

    def test_register_valid_user(self, user="username", mail="user@email.se", secret="password"):
        self.browser.get(self.live_server_url + "/register_user")
        self.assert_el_and_send_to_id('username', user)
        self.assert_el_and_send_to_id('email', mail)
        self.assert_el_and_send_to_id('password', secret)
        self.assert_submit_and_click()
        assert self.browser.current_url == self.live_server_url + '/'
        self.assert_find_alert_success()

    def test_register_multiple_user(self):
        for fake in self.fakers:
            for _ in range(self.NUMBER_OF_PROFILES):
                profile = fake.profile()
                username = profile["username"]
                email = profile["mail"]
                password = fake.password(length=12)

                self.test_register_valid_user(
                    user=username,
                    mail=email,
                    secret=password
                )
                self.profiles.append({
                    "username": username,
                    "email": email,
                    "password": password,
                    "first_name": profile["name"].split(" ")[0],
                    "last_name": profile["name"].split(" ")[1],
                    "phone": fake.phone_number(),
                    "about": profile["website"][0]
                })

    def assert_find_alert_success(self):
        message = self.browser.find_element(By.CLASS_NAME, "alert-success")
        assert message

    def assert_submit_and_click(self, ):
        submit = self.browser.find_element(By.NAME, 'submit')
        assert submit
        submit.click()

    def assert_el_and_send_to_id(self, el_id, value):
        el = self.browser.find_element(By.ID, el_id)
        assert el
        el.send_keys(value)

    def test_update_valid_user(self, profile):
        self.browser.get(self.live_server_url + "/profile")
        self.assert_el_and_send_to_id("username", profile["username"])
        self.assert_el_and_send_to_id("email", profile["email"])
        self.assert_el_and_send_to_id("first_name", profile["first_name"])
        self.assert_el_and_send_to_id("last_name", profile["last_name"])
        self.assert_el_and_send_to_id("phone", profile["phone"])
        self.assert_el_and_send_to_id("about", profile["about"])

    def test_update_multiple_user(self):
        for profile in self.profiles:
            self.browser.get(self.live_server_url + "/login")
            email = self.browser.find_element(By.ID, "email")
            assert email
            email.send_keys(profile["email"])
            password = self.browser.find_element(By.ID, "password")
            assert password
            password.send_keys(profile["email"])
            fake = self.fakers[0]
            profile = fake.profile()
            self.test_update_valid_user(
                profile={
                    "user": profile["username"],
                    "mail": profile["mail"],
                    "secret": profile["password"],
                    "first_name": profile["first_name"],
                    "last_name": profile["last_name"],
                    "phone": profile["phone"],
                    "about": profile["about"]
                }
            )
