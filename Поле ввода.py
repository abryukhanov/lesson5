from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/inputs")

input_field = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div/input')
input_field.send_keys('1000')
sleep (2)
input_field.clear()
sleep (2)
input_field.send_keys('999')
