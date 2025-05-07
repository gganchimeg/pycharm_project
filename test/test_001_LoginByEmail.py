import pytest
from src.pages.login_page import LoginPage
from src.pages.payment_fourdigit_popup import PaymentPurchasePinInputPage
from src.pages.profile_selection import ProfileSelectorPage
from src.pages.registration_email_sent_page import RegistrationEmailVerificationPage
from src.pages.registration_page_child import EmailRegistrationPage
from utilities.network_response import save_network_log
import time
import json
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
# from seleniumwire import webdriver

class TestLoginByEmail:
    baseURL = ReadConfig.getApplicationURL()
    # logger = LogGen.loggen() # for log
    email = ReadConfig.getUseremail()
    phone_number =  ReadConfig.getRegistrationPhone()
    password = ReadConfig.getPassword1()
    profilePin = ReadConfig.getProfilePin()
    purchasePin = ReadConfig.getPurchasePin()
    parentalPin = ReadConfig.getParentalPin()

    def test_login_by_email(self, setup):
        """
            Completed
        """
        # self.logger.info("/* test001_LoginByEmail started */")
        self.driver = setup  # setup dotroo browseroo zarlaad driver uusgesen
        self.driver.get(self.baseURL)
        # self.driver.maximize_window()
        self.driver.implicitly_wait(10)  # once

        loginPage = LoginPage(self.driver)
        loginPage.set_email(self.email)
        loginPage.set_password(self.password)
        loginPage.click_submit_button()
        self.profileSelectorPage = ProfileSelectorPage(self.driver)
        time.sleep(3)

        self.driver.quit()