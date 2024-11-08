import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import math

from main import browser


@pytest.fixture(scope="session")
def load_config():
    with open('package.json', 'r') as config_file:
        config = json.load(config_file)
        return config


class TestLogin:
    @pytest.mark.parametrize("number", ["236896", "236897", "236898", "236899", "236903", "236904", "236905"])
    def test_authorization(self, browser, load_config, number):
        login_stepik = load_config['email']
        password_stepik = load_config['password']

        link = f"https://stepik.org/lesson/{number}/step/1"

        browser.get(link)
        browser.implicitly_wait(5)

        link_1 = browser.find_element(By.CSS_SELECTOR, ".navbar__auth_login")
        link_1.click()
        email = browser.find_element(By.ID, 'id_login_email')
        email.send_keys(login_stepik)
        password = browser.find_element(By.ID, 'id_login_password')
        password.send_keys(password_stepik)
        button_1 = browser.find_element(By.CSS_SELECTOR, "button_with-loader")
        button_1.click()
        time.sleep(4)
        answer = math.log(int(time.time()))

        pole_input = browser.find_element(By.CSS_SELECTOR, ".textarea")
        pole_input.click()
        pole_input.send_keys(answer)
        button_2 = browser.find_element(By.TAG_NAME, "button")
        button_2.click()
        time.sleep(5)

