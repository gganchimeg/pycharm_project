from src.pages.registration_page_phone import PhoneRegistrationPage
from src.pages.login_page import LoginPage
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
        # ene neg hardcoded yumiig arilgah
        self.regPage.setEmail("89988218")
        self.regPage.setPassword("Ganchimeg.g\n")
        self.regPage.setPassword_duplicate("Ganchimeg.g\n")
        self.regPage.setPrivacyPolicy()
        otpInputPage = self.regPage.clickSubmitButton()

        time.sleep(2)
        # garaas avah neg yum hiine
        otp = input("Enter the OTP")
        otp_list = [int(i) for i in str(otp)]

        otpInputPage.setDigitOne(otp_list[0])
        otpInputPage.setDigitTwo(otp_list[1])
        otpInputPage.setDigitThree(otp_list[2])
        otpInputPage.setDigitFour(otp_list[3])
        otpInputPage.setDigitFive(otp_list[4])
        otpInputPage.setDigitSix(otp_list[5])

        otpInputPage.clickSubmitButton()

        time.sleep(5)
        self.driver.quit()











