import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By

from account.models import Account


class TestLogin(StaticLiveServerTestCase):
    """
        Numbers of profiles times number of fakers.
        MAX - 30
    """
    created_users = []
    NUMBER_OF_PROFILES = 1

    def setUp(self):
        self.browser = webdriver.Chrome('chromedriver')
        a = Account.objects.create(
            username="a",
            email="a@a.se",
            password="password"
        )
        a.save()

        print(a.password)

        #self.fakers = [
        #    Faker(["sv_SE"]),
        #    Faker(["da_DK"]),
        #    Faker(["en_US"]),
        #    Faker(["bg_BG"])
        #]
        #for fake in self.fakers:
        #    for _ in range(self.NUMBER_OF_PROFILES):
        #        profile = fake.profile()
        #        username = profile["username"]
        #        email = profile["mail"]
        #        password = fake.password(length=12)
        #        a = Account.objects.create(
        #            username=username,
        #            email=email,
        #            password=password
        #        )
        #        self.created_users.append({
        #            "email": email,
        #            "password": password,
        #        })
        #        a.save()

    def tearDown(self):
        self.browser.close()

    def test_login_known(self):
        self.browser.get(self.live_server_url + "/login")
        self.assert_el_and_send_to_id('email', "a@a.se")
        self.assert_el_and_send_to_id('password', "a")
        # self.assert_submit_and_click()
        # self.assert_find_alert_success()
        time.sleep(100)

    def test_login(self):
        for user in self.created_users:
            self.browser.get(self.live_server_url + "/login")
            self.assert_el_and_send_to_id('email', user["email"])
            self.assert_el_and_send_to_id('password', user["password"])
            self.assert_submit_and_click()
            self.assert_find_alert_success()
            # print("account: ", Account.objects.get(email=user["email"]))
            # print("temp", user['email'], user["password"])
            # time.sleep(10)

    def assert_find_alert_success(self):
        message = self.browser.find_element(By.CLASS_NAME, "alert-success")
        assert message

    def assert_submit_and_click(self):
        submit = self.browser.find_element(By.NAME, 'submit')
        assert submit
        submit.click()

    def assert_el_and_send_to_id(self, el_id, value):
        el = self.browser.find_element(By.ID, el_id)
        assert el
        el.send_keys(value)
