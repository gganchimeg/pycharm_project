import pytest
import configparser
from src.pages.login_page import LoginPage
from utilities.readProperties import ReadConfig

@pytest.mark.first
def login_process(driver, usern, passw):
    baseURL = ReadConfig.getApplicationURL()
    driver.get(baseURL)
    loginPage = LoginPage(driver)

    # self.driver.maximize_window()
    driver.implicitly_wait(10)  # once

    loginPage.set_email(usern)   # username fill
    loginPage.set_password(passw) # password fill
    # loginPage.checkShowPassword()   # by choice
    print("click_submit_button")
    profile_selector_page = loginPage.click_submit_button()     # login page end, switching to profile selection page
    return profile_selector_page

@pytest.mark.second
def profile_selection_process(profile_selector_page):
    home_page = profile_selector_page.select_first_profile()
    # for now hardcoded to login into first profile
    return home_page
    # # self.driver.maximize_window()
    # driver.implicitly_wait(10)  # once
    # profileSelectionPage.
    # return homepage
    # time.sleep(10)
    # self.driver.quit()

def getOTP(otp):
    otp_list = [int(i) for i in str(otp)]
    return otp_list

def return_activation_link(email_address):
    # endeesee mailruugee nevtreed activation link deer dardag linkruuugee orno
    from utilities.gmail_check_api import main as gmailapi
    import re
    import time

    address = ""
    match = re.search(r'(.+)@', email_address)
    if match:
        address = match.group(1)
    else:
        print("Check this value!: ReadConfig.getRegistrationEmail()")

    prefix = r"C:\Users\ganchimeg.g\Local\PycharmProjects\pycharm_project\utilities"
    address = prefix + "\\" + address + ".json"
    print(address)
    activation_link = None
    while not activation_link:
        activation_link = gmailapi(address)
        time.sleep(40)
    return activation_link

def update_config_value(sec, opt, v):
    config = configparser.RawConfigParser()
    config.read("C:/Users/ganchimeg.g/Local/PycharmProjects/pycharm_project/configurations/config.ini")
    config.set(section=sec, option=opt, value=v)

    with open("C:/Users/ganchimeg.g/Local/PycharmProjects/pycharm_project/configurations/config.ini", 'w') as configfile:
        config.write(configfile)
