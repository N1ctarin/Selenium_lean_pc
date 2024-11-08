import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import json

@pytest.fixture(scope="session")
def load_config():
    with open('package.json', 'r') as config_file:
        config = json.load(config_file)
        return config

class TestLogin:
    def test_authorization(self, browser, load_config):
        login_stepik = load_config['email']
        password_stepik = load_config['password']

        link = "https://stepik.org/catalog?auth=login"
        browser.get(link)
        email = browser.find_element(By.ID, 'id_login_email')
        email.send_keys(login_stepik)
        password = browser.find_element(By.ID, 'id_login_password')
        password.send_keys(password_stepik)
        button_1 = browser.find_element(By.TAG_NAME, 'Войти')
        button_1.click()
        time.sleep(3)

        browser.get("https://stepik.org/lesson/236895/step/1")

