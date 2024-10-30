from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

from lessons.lesson_2 import checkbox
from main import browser

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/execute_script.html"

browser = webdriver.Chrome()
browser.get(link)

x = browser.find_element(By.ID, "input_value").text
y = calc(x)

anser = browser.find_element(By.ID, "answer")
anser.send_keys(y)

submit = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true)", submit)

checkbox = browser.find_element(By.ID, "robotCheckbox")
checkbox.click()

radiobatton = browser.find_element(By.ID, "robotsRule")
radiobatton.click()

submit.click()

sleep(20)

browser.quit()
