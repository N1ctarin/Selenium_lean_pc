from time import sleep

from selenium import webdriver
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ES
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get(link)

pr = WebDriverWait(browser, 12).until(ES.text_to_be_present_in_element((By.ID, "price"), "$100"))
button = browser.find_element(By.ID, "book")
button.click()

x = int(browser.find_element(By.ID, "input_value").text)
y = calc(x)

anser = browser.find_element(By.ID, "answer")
anser.send_keys(y)

button_2 = browser.find_element(By.ID, "solve")
button_2.click()

print(browser.switch_to.alert.text)
browser.quit()


