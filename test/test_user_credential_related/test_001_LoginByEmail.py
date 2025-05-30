import time

from seleniumpagefactory.Pagefactory import ElementNotFoundException

from src.pages.login_page import LoginPage
from src.pages.profile_selection import ProfileSelectorPage
from utilities.readProperties import ReadConfig


# from seleniumwire import webdriver

class TestLoginByEmail:
    baseURL = ReadConfig.get_application_url()
    # logger = LogGen.loggen() # for log
    email = ReadConfig.get_user_email()
    # phone_number =  ReadConfig.getRegistrationPhone()
    password = ReadConfig.get_password()
    profilePin = ReadConfig.get_profile_pin()
    purchasePin = ReadConfig.get_purchase_pin()
    parentalPin = ReadConfig.get_parental_pin()

    def test_login_by_email(self, setup):
        """
            Completed
        """
        # self.logger.info("/* test001_LoginByEmail started */")
        self.driver = setup  # setup dotroo browseroo zarlaad driver uusgesen
        self.driver.get(self.baseURL)
        # self.driver.maximize_window()
        self.driver.implicitly_wait(10)  # once

        login_page = LoginPage(self.driver)
        login_page.set_email(self.email)
        login_page.set_password(self.password)
        login_page.click_submit_button()
        profile_selector_page = ProfileSelectorPage(self.driver)

        # try:
        #     print("1:", profile_selector_page.profile_1.is_displayed())
        #     print("1:", profile_selector_page.profile_1.is_enabled())
        #     profile_selector_page.profile_1.click()  # log in
        #     self.driver.quit()
        # except ElementNotFoundException:
        #     print("Element not found and it's not possible")
        #
        # try:
        #     print("2: ", profile_selector_page.profile_2.is_displayed())
        #     print("2: ", profile_selector_page.profile_2.is_enabled())
        #     profile_selector_page.profile_2.click()  # log in
        #     self.driver.quit()
        # except ElementNotFoundException:
        #     print("Element not found and it's new account")

        try:
            print("3: ", profile_selector_page.profile_3.is_displayed())
            print("3: ", profile_selector_page.profile_3.is_enabled())
            profile_selector_page.profile_3.click()  # log in
            self.driver.quit()
        except ElementNotFoundException:
            print("Element not found and there is only 1 acc")

        try:
            print("4: ", profile_selector_page.profile_4.is_displayed())
            print("4: ", profile_selector_page.profile_4.is_enabled())
            profile_selector_page.profile_4.click()  # log in
            self.driver.quit()
        except ElementNotFoundException:
            print("Element not found and there are only 2 accs")


        time.sleep(5)

        self.driver.quit()