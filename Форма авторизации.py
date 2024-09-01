from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")

username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'username')))
password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password')))
username_field.send_keys('tomsmith')
password_field.send_keys('SuperSecretPassword!')

login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/form/button/i')))
login_button.click()


