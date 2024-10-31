from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button_1 = browser.find_element(By.TAG_NAME, "button")
button_1.click()

browser.switch_to.window(browser.window_handles[1])

x = int(browser.find_element(By.ID, "input_value").text)
y = calc(x)

anser = browser.find_element(By.ID, "answer")
anser.send_keys(y)

button_2 = browser.find_element(By.TAG_NAME, "button")
button_2.click()

q = browser.switch_to.alert.text
print(q)

browser.quit()