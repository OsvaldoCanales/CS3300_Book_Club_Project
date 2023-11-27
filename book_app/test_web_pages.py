from django.conf import settings
from django.contrib.auth.models import User
from django.test import LiveServerTestCase

# Selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 

#This tests if the title contains the correct title
#First selenium test run through
class HostTest(LiveServerTestCase):
    def testHomePage(self):
        # Use ChromeDriverManager to automatically download and install the ChromeDriver
        chrome_path = ChromeDriverManager().install()

        # Use the Chrome service with the executable path
        chrome_service = ChromeService(chrome_path)

        # Create a Chrome WebDriver instance with the service
        driver = webdriver.Chrome(service=chrome_service)

        # Navigate to the login page
        driver.get(self.live_server_url + '/accounts/login/')

        # Check if the title contains the expected text
        assert "The Scholar Ship" in driver.title

        # Close the browser window
        driver.quit()

#Test to see if regististration works correctly
class RegistrationTest(LiveServerTestCase):
    def setUp(self):
         # Use ChromeDriverManager to automatically download and install the ChromeDriver
        chrome_path = ChromeDriverManager().install()

        # Use the Chrome service with the executable path
        chrome_service = ChromeService(chrome_path)

        # Create a Chrome WebDriver instance with the service
        self.driver = webdriver.Chrome(service=chrome_service)

        

    def tearDown(self):
        self.driver.quit()

    def testUserRegistration(self):
        # Navigate to the registration page
        self.driver.get(self.live_server_url + '/accounts/register/')

        # Fill out the registration form with valid information
        self.driver.find_element(By.ID, 'id_username').send_keys('testuser')
        self.driver.find_element(By.ID, 'id_email').send_keys('testuser@example.com')
        self.driver.find_element(By.ID, 'id_password1').send_keys('strongpassword123')
        self.driver.find_element(By.ID, 'id_password2').send_keys('strongpassword123')

        # Submit the registration form
        submit_button = WebDriverWait(self.driver, 2).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))
        )
    
        submit_button.click()

         # Check if the user is redirected to the expected page after registration
        self.assertEqual(self.driver.current_url, self.live_server_url + '/accounts/login/')

         # Optional: This checks to see if a success message is displayed on the page
        success_message = WebDriverWait(self.driver, 2).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.alert-success'))
        ).text

        self.assertIn('successfully registered', success_message)