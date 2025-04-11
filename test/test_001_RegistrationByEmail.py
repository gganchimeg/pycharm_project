from src.pages.registration_page_phone import EmailRegistrationPage
from src.pages.login_page import LoginPage
from utilities.helper_functions import getOTP
import time
from utilities.readProperties import ReadConfig


class TestRegistrationByEmail:
    baseURL = ReadConfig.getApplicationURL()

    def test_register_by_email(self, setup):
        self.driver = setup  # setup dotroo browseroo zarlaad driver uusgesen
        self.driver.get(self.baseURL)
        # self.driver.maximize_window()
        self.driver.implicitly_wait(10)  # once

        self.startPage = LoginPage(self.driver)
        self.startPage.clickRegisterButton()
        self.regPage = EmailRegistrationPage(self.driver)

        self.regPage.setEmail(ReadConfig.getRegistrationEmail())
        self.regPage.setPassword(ReadConfig.getRegistrationPassword())
        self.regPage.setPassword_duplicate(ReadConfig.getRegistrationPassword())
        self.regPage.setPrivacyPolicy()

        regEmailSentPage = self.regPage.clickSubmitButton()
    # otp = getOTP()
    # if       confirm logic bichne

        self.driver.quit()
















        





