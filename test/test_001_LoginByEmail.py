import pytest
from src.pages.login_page import LoginPage
from src.pages.payment_fourdigit_popup import PaymentPurchasePinInputPage
from utilities.network_response import save_network_log
import time
import json
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
# from seleniumwire import webdriver

# for now it's just a script to test flows

class TestLoginByEmail:
    baseURL = ReadConfig.getApplicationURL()
    # logger = LogGen.loggen() # for log

    def test_login_by_email(self, setup):
        # variables for just initial testing
        # will remove it later ----------------------------------------------
        purchasePin = ReadConfig.getPurchasePin()

        # -------------------------------------------------------------------
        # self.logger.info("/* test001_LoginByEmail started */")
        self.driver = setup  # setup dotroo browseroo zarlaad driver uusgesen
        self.driver.get(self.baseURL)
        # self.driver.maximize_window()
        self.driver.implicitly_wait(10)  # once


        self.loginPage = LoginPage(self.driver)
        # self.logger.info("/* Filling out credentials */")
        self.loginPage.setEmail(ReadConfig.getUseremail())
        self.loginPage.setPassword(ReadConfig.getPassword1())
        self.loginPage.checkShowPassword()
        self.profileSelectorPage = self.loginPage.clickSubmitButton()

        self.driver.quit()



