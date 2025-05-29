import subprocess
from datetime import datetime, timedelta
from telnetlib import EC

import pytest, time, re
import requests
import configparser

from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from src.pages.login_page import LoginPage
from utilities.readProperties import ReadConfig

# @pytest.mark.first
def login_process(driver, usern, passw):
    baseURL = ReadConfig.getApplicationURL()
    driver.get(baseURL)
    loginPage = LoginPage(driver)

    # self.driver.maximize_window()
    driver.implicitly_wait(10)  # once

    loginPage.set_email(usern)   # username fill
    loginPage.set_password(passw) # password fill
    # loginPage.checkShowPassword()   # by choice
    time.sleep(5)

    profile_selector_page = loginPage.click_submit_button()     # login page end, switching to profile selection page
    print("clicked submit button")
    return profile_selector_page

# @pytest.mark.second
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

def string_to_list(s):
    list = [int(i) for i in str(s)]
    return list

def extract_new_password_from_html_page(url):
    body = requests.get(url).text
    if not body:
        return "No <body> tag found."
    print("body:  ", body)
    pattern = r': (.*?)(?=\.)'

    match = re.search(pattern, body)
    if match:
        return match.group(1).strip()
    else:
        return("No match found.")

def return_activation_link(email_address):
    # endeesee mailruugee nevtreed activation link deer dardag linkruuugee orno
    from utilities.gmail_check_api import main as gmailapi

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

def open_link(d, link):
    d.get(link)
    time.sleep(4)
    # d.quit()


def update_config_value(sec, opt, v):
    config = configparser.RawConfigParser()
    config.read("C:/Users/ganchimeg.g/Local/PycharmProjects/pycharm_project/configurations/config.ini")
    config.set(section=sec, option=opt, value=v)

    with open("C:/Users/ganchimeg.g/Local/PycharmProjects/pycharm_project/configurations/config.ini", 'w') as configfile:
        config.write(configfile)


def otp_extraction():
    epoch_time_5_minutes_before = (int((datetime.now() - timedelta(seconds=20)).timestamp()) * 1000)
    print("epoch time: ",epoch_time_5_minutes_before)
    adb_query = f"content query --uri content://sms/inbox --projection body --where 'date>{epoch_time_5_minutes_before} AND address=\"1474\"' --sort \"date\""

    try:
        result = subprocess.run(["adb","shell", adb_query],
                                capture_output=True,
                                encoding="UTF-8",
                                check=True)

        result = result.stdout.strip().split('\n')[-1]
        print("result: ", result)
        # code extract
        pattern = r".*: .*: (.*)"
        match = re.search(pattern, result)
        if match:
            extracted_value = match.group(1)
            print(extracted_value)
            return int(extracted_value)

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        print(f"Error output: {e.stderr}")
        return e.stderr


def latesttest_response(d):
# file ruu bichih
    with open("response_test.log", "ab") as f:
        # while True:  test purpose
        del d.requests

        time.sleep(60)
        for request in d.requests:
            # print(len(self.driver.requests))
            if request.response and request.response.status_code != 200:
                # print(f"\n--- Request: {request.method} {request.url} ---")
                # print(f"Status: {request.response.status_code}")

                url = request.url
                statuscode = request.response.status_code
                f.write(str(statuscode).encode())
                f.write(" ".encode())
                f.write(url.encode())
                f.write("\n".encode())

# -------------------------------------------------------------------
