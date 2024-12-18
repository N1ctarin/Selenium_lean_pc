from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")
    button_1 = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert button_1.is_displayed()
