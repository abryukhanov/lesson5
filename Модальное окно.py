from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/entry_ad")

sleep(2)

close_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[3]')
close_button.click()