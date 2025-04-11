from src.pages.registration_page_phone import PhoneRegistrationPage
from src.pages.login_page import LoginPage
from utilities.helper_functions import getOTP
import time
from utilities.readProperties import ReadConfig


class TestRegistrationByPhone:
    baseURL = ReadConfig.getApplicationURL()

    def test_register_by_phone(self, setup):
        self.driver = setup  # setup dotroo browseroo zarlaad driver uusgesen
        self.driver.get(self.baseURL)
        # self.driver.maximize_window()
        self.driver.implicitly_wait(10)  # once

        self.startPage = LoginPage(self.driver)
        self.startPage.clickRegisterButton()
        self.regPage = PhoneRegistrationPage(self.driver)

        self.regPage.setEmail(ReadConfig.getRegistrationPhone())
        self.regPage.setPassword(ReadConfig.getRegistrationPassword())
        self.regPage.setPassword_duplicate(ReadConfig.getRegistrationPassword())
        self.regPage.setPrivacyPolicy()
        otpInputPage = self.regPage.clickSubmitButton()

        time.sleep(2)

        otp = getOTP()   # list butsaana

        otpInputPage.setDigitOne(otp[0])
        otpInputPage.setDigitTwo(otp[1])
        otpInputPage.setDigitThree(otp[2])
        otpInputPage.setDigitFour(otp[3])
        otpInputPage.setDigitFive(otp[4])
        otpInputPage.setDigitSix(otp[5])
        otpInputPage.clickSubmitButton()

        time.sleep(5)
        self.driver.quit()











