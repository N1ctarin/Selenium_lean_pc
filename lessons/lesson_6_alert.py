from time import sleep
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

from main import browser

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button_1 = browser.find_element(By.TAG_NAME, "button")
button_1.click()

alert = browser.switch_to.alert
alert.accept()

x = browser.find_element(By.ID, "input_value").text
y = calc(x)

anser = browser.find_element(By.ID, "answer")
anser.send_keys(y)

submit = browser.find_element(By.TAG_NAME, "button")
submit.click()

print(browser.switch_to.alert.text)

browser.quit()