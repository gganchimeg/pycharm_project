
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
import time
from selenium.webdriver.support.ui import Select

#----------------------------------------------------#
URL_g = "http://10.129.43.130:8082/client"
phoneNumber_g = "ganchimeg.g@unitel.mn"
password_g = "admin123"
#----------------------------------------------------#
driver = webdriver.Edge()
driver.get(URL_g)
driver.implicitly_wait(10)  # once
#----------------------------------------------------#

# time.sleep(2)
email_input = driver.find_element(By.XPATH, "//input[@id='userName']")
email_input.send_keys(phoneNumber_g)

password_input = driver.find_element(By.XPATH, "//input[@id='password']")
password_input.send_keys(password_g)

login_but = driver.find_element(By.XPATH, "//button[@type='submit']")
login_but.click()

customers_but = driver.find_element(By.XPATH, "//a[@id='customersMainButton']")
customers_but.click()

dropdown = driver.find_element(By.XPATH, "//a[normalize-space()='Name']")
dropdown.click()

id_list = driver.find_element(By.XPATH, "//span[normalize-space()='ID']")
id_list.click()

inputt = driver.find_element(By.XPATH, "//input[@id='accountSearchSearchInput']")
inputt.send_keys("90357")

search_but = driver.find_element(By.XPATH, "//span[@class='icon-search icon-small']")
search_but.click()

gaitai_error_popup = driver.find_element(By.XPATH, "//button[normalize-space()='OK']")
gaitai_error_popup.click()


devices = driver.find_element(By.XPATH, "//div[@class='categoryName ng-binding']")
devices.click()


x = 15
while x > 1:
    driver.implicitly_wait(10)  # once

    deletee = driver.find_element(By.XPATH, "//a[@class='icon-delete']")
    deletee.click()

    ok_button = driver.find_element(By.XPATH, "//button[normalize-space()='OK']")
    ok_button.click()
    time.sleep(1)
    sec_ok = driver.find_element(By.XPATH, "(//button[normalize-space()='OK'])[1]")
    sec_ok.click()

    error_exit = driver.find_element(By.XPATH, "//button[@class='primary-action-btn ng-binding']")
    error_exit.click()



    x = x - 1


getextended
