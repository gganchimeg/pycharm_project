from seleniumpagefactory.Pagefactory import PageFactory

from src.pages.change_password_successful_message import ChangePasswordSuccessfulPage
from src.pages.registration_successful_page import RegistrationSuccessfulPage


class TestNewpasswordInputPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'current_pass_input': ('XPATH', "//input[@id='email']"),
        'pass_input': ('XPATH', "//input[@id='password']"),
        'pass_input_duplicate': ('XPATH', "//input[@id='confirm-password']"),
        'continue_button': ('XPATH', "//div[@class='ellipsis vertical-center black-font-type login-button-text ng-binding ng-scope']"),
        'pass_show': ('XPATH', "//div[@ng-click='changeShowPassword()']"),
        'pass_show_duplicate': ('XPATH', "//div[@ng-click='changeShowNewPassword()']"),
        'close': ('XPATH', "//div[@class='tv-icon icon-exit close-login-button cursor-pointer ng-scope']")
    }
    def set_current_password(self, p):
        self.current_pass_input.set_text(p)

    def set_new_password(self, p):
        self.pass_input.set_text(p)

    def set_new_password_duplicate(self, p):
        self.pass_input_duplicate.set_text(p)

    def check_show_password(self):
        self.pass_show.click()

    def check_show_password_duplicate(self):
        self.pass_show_duplicate.click()

    def click_continue_fromforgotpassword(self):
        self.continue_button.click()
        return RegistrationSuccessfulPage(self.driver)

    def click_continue_fromsettings(self):
        self.continue_button.click()
        return ChangePasswordSuccessfulPage(self.driver)

    def click_close(self):
        self.close.click()


