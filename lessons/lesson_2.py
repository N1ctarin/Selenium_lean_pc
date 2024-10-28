from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)

pole = browser.find_element(By.ID, "answer")
pole.send_keys(y)

checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
checkbox.click()

radiobatton = browser.find_element(By.ID, "robotsRule")
radiobatton.click()

button_1 = browser.find_element(By.TAG_NAME, "button")
button_1.click()

sleep(20)

browser.quit()



