from seleniumpagefactory.Pagefactory import PageFactory
# from src.pages.registration_successful_page import RegistrationSuccessfulPage
# from src.pages.registration_page import BaseRegistrationPage
# from src.pages.login_page import LoginPage
# from typing_extensions import ParamSpec


class RegistrationEmailVerificationPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'login_button': ('XPATH', "//div[@class='ellipsis vertical-center black-font-type login-button-text ng-binding ng-scope']"),
        'send_again_link': ('XPATH', "//span[@class='highlightMessage medium-font-type register-link ng-scope']")
    }


    def clickLoginButton(self):
        # self.login_button.click()
        # return LoginPage(self.driver) due to circular import
        pass
    def clickSendAgainLink(self):
        self.send_again_link.click()
        return self


