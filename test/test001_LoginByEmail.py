import pytest

from src.pages.login_page import LoginPage
from utilities.network_response import save_network_log
import time
import json
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
# from seleniumwire import webdriver



class TestLoginByEmail:
    baseURL = ReadConfig.getApplicationURL()
    # logger = LogGen.loggen() # for log

    def test_login_by_email(self, setup):
        # self.logger.info("/* test001_LoginByEmail started */")
        self.driver = setup  # setup dotroo browseroo zarlaad driver uusgesen
        self.driver.get(self.baseURL)
        # self.driver.maximize_window()
        self.driver.implicitly_wait(10)  # once


        self.loginPage = LoginPage(self.driver)
        # self.logger.info("/* Filling out credentials */")
        self.loginPage.setEmail(ReadConfig.getUseremail())
        self.loginPage.setPassword(ReadConfig.getPassword())
        self.loginPage.checkShowPassword()
        self.loginPage.clickSubmitButton()

        # page_source = self.driver.page_source
        # print(page_source)
        # Iterate through captured requests
        save_network_log(self.driver, "./utilities/network_response.txt", "a")

        # with open("/utilities/network_response.py", 'a') as file:
        #     for request in self.driver.requests:
        #         if request.url == "https://staging.looktv.mn/Login" and request.response.status_code == 200:
        #             # file.write(f"URL: {request.url}\n")
        #             # file.write(f"Response Status: {request.response.status_code}\n")
        #             # file.write(f"Response Body: {request.response.body}\n\n")
        #             json_response = json.loads(request.response.body)
        #             success_string = json_response['response']['status']
        #             if success_string == "SUCCESS":
        #                 print("Login success")
        #             else:
        #                 pytest.fail("Login failed")
        #                 break
        #             # file.write(json_response)
        #             #
        #
        # file.close()

        time.sleep(10)
        self.driver.quit()
#       register amjilttai bol hereglegchid medegdehgui
#       shuud nevtrehee daraad tsaashaa yvna




