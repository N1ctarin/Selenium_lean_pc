from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import  os

from main import browser

link = "https://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

first_name = browser.find_element(By.NAME, "firstname")
first_name.send_keys("name")

last_name = browser.find_element(By.NAME, "lastname")
last_name.send_keys("surname")

email = browser.find_element(By.NAME, "email")
email.send_keys("test@email.com")

sub_file = browser.find_element(By.ID, "file")

current_dir = os.path.abspath(os.path.dirname(__file__))
ful_dir = os.path.join(current_dir, "ttt.txt")

sub_file.send_keys(ful_dir)

submit = browser.find_element(By.TAG_NAME, "button")
submit.click()

sleep(20)

browser.quit()

