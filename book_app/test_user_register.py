from django.conf import settings
from django.contrib.auth.models import User
from django.test import LiveServerTestCase
from selenium import webdriver

class HostTest(LiveServerTestCase):
    def testHomePage(self):
        driver = webdriver.Chrome()

        driver.get('http://127.0.0.1:8000/accounts/login/')
        assert "Login Page Selenium!" in driver.title