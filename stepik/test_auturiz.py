import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import math




@pytest.fixture(scope="session")
def load_config():
    with open('package.json', 'r') as config_file:
        config = json.load(config_file)
        return config

class TestLogin:
    def test_authorization(self, browser, load_config):
        login_stepik = load_config['email']
        password_stepik = load_config['password']

        link = "https://stepik.org/lesson/236895/step/1"

        browser.get(link)
        browser.implicitly_wait(5)

        link_1 = browser.find_element(By.ID, "ember457")
        link_1.click()
        email = browser.find_element(By.ID, 'id_login_email')
        email.send_keys(login_stepik)
        password = browser.find_element(By.ID, 'id_login_password')
        password.send_keys(password_stepik)
        button_1 = browser.find_element(By.CLASS_NAME, 'button_with-loader')
        button_1.click()

        answer = math.log(int(time.time()))

        pole_input = browser.find_element(By.TAG_NAME, 'textarea')
        pole_input.send_keys(answer)
        button_2 = browser.find_element(By.CLASS_NAME, 'submit-submission')
        button_2.click()
        time.sleep(5)

