from src.pages.registration_page import BaseRegistrationPage, EmailRegistrationConfirmationPage
from src.pages.login_page import LoginPage
from src.pages.registration_page import PhoneRegistrationOTPPage
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
        self.startPage.click_register_button()
        self.regPage = BaseRegistrationPage(self.driver)

        self.regPage.setEmail("89988218")
        self.regPage.setPassword("Ganchimeg.g\n")
        self.regPage.setPassword_duplicate("Ganchimeg.g\n")
        self.regPage.setPrivacyPolicy()
        self.regPage.clickSubmitButton()
        # burtguuleh continue

        self.emailSentPage = EmailRegistrationConfirmationPage(self.driver)
        # self.emailSentPage.clickConfirmButton()
        # self.emailSentPage.clickSendAgain()
        # self.emailSentPage.clickBack()

        time.sleep(10)
        self.driver.quit()
#       register amjilttai bol hereglegchid medegdehgui
#       shuud nevtrehee daraad tsaashaa yvna











