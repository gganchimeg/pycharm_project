from seleniumpagefactory.Pagefactory import PageFactory
from src.pages.login_page import LoginPage


class RegistrationEmailVerificationPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'login_button': ('XPATH', "//div[@class='ellipsis vertical-center black-font-type login-button-text ng-binding ng-scope']"),
        'send_again_link': ('XPATH', "//span[@class='highlightMessage medium-font-type register-link ng-scope']")
    }

    def clickLoginButton(self):
        self.login_button.click()
        return LoginPage(self.driver)
    def clickSendAgainLink(self):
        self.send_again_link.click()
        return self


