from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
browser.get("https://suninjuly.github.io/selects1.html")

num1 = browser.find_element(By.ID, "num1")
x = int(num1.text)
num2 = browser.find_element(By.ID, "num2")
y = int(num2.text)
summ = str(x+y)

select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_visible_text(summ)

but = browser.find_element(By.TAG_NAME, "button").click()

sleep(30)

browser.quit()