from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/dynamicid")


for _ in range(3):
    blue_button = driver.find_element(By.CSS_SELECTOR, 'button.btn-primary')
    blue_button.click()
    sleep (10)