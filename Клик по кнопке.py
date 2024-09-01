from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
time.sleep(2) 

for _ in range(5):
    try:
        add_element_button = driver.find_element(By.XPATH, '//button[text()="Add Element"]')
        add_element_button.click()
        time.sleep(1) 
    except NoSuchElementException:
        print("Кнопка 'Add Element' больше не существует.")
        break

delete_buttons = driver.find_elements(By.XPATH, '//button[@class="btn-danger"]')

print(len(delete_buttons))