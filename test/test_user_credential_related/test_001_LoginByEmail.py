from logging import exception

from seleniumpagefactory.Pagefactory import ElementNotFoundException

from src.pages.login_page import LoginPage
from src.pages.profile_selection import ProfileSelectorPage
import time
from utilities.readProperties import ReadConfig


# from seleniumwire import webdriver

class TestLoginByEmail:
    baseURL = ReadConfig.getApplicationURL()
    # logger = LogGen.loggen() # for log
    email = ReadConfig.getUseremail()
    # phone_number =  ReadConfig.getRegistrationPhone()
    password = ReadConfig.getPassword()
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
        profileSelectorPage = ProfileSelectorPage(self.driver)

        # try:
        #     print("1: ", profileSelectorPage.profile_1.is_displayed())
        #     print("1: ", profileSelectorPage.profile_1.is_enabled())
        #     profileSelectorPage.profile_1.click()  # log in
        #     self.driver.quit()
        # except ElementNotFoundException:
        #     print("Element not found and it's not possible")
        #
        # try:
        #     print("2: ", profileSelectorPage.profile_2.is_displayed())
        #     print("2: ", profileSelectorPage.profile_2.is_enabled())
        #     profileSelectorPage.profile_2.click()  # log in
        #     self.driver.quit()
        # except ElementNotFoundException:
        #     print("Element not found and it's new account")

        try:
            print("3: ", profileSelectorPage.profile_3.is_displayed())
            print("3: ", profileSelectorPage.profile_3.is_enabled())
            profileSelectorPage.profile_3.click()  # log in
            self.driver.quit()
        except ElementNotFoundException:
            print("Element not found and there is only 1 acc")

        try:
            print("4: ", profileSelectorPage.profile_4.is_displayed())
            print("4: ", profileSelectorPage.profile_4.is_enabled())
            profileSelectorPage.profile_4.click()  # log in
            self.driver.quit()
        except ElementNotFoundException:
            print("Element not found and there are only 2 accs")


        time.sleep(5)

        self.driver.quit()