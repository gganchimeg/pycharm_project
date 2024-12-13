from cProfile import Profile
from src.pages.profile_selection import ProfileSelectorPage
from src.pages.registration_page import BaseRegistrationPage
from src.pages.forgot_password_page import ForgotPasswordPage
from seleniumpagefactory.Pagefactory import PageFactory
from utilities.readProperties import ReadConfig

class LoginPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
    'email_input': ('XPATH', "//input[@id='email']"),
    'pass_input': ('XPATH', "//input[@id='password']"),
    'submit_button': ('XPATH', "//div[@class='ellipsis vertical-center black-font-type login-button-text ng-binding ng-scope']"),
    'register_button': ('XPATH', "//div[@class='button-vertical-container basic-border horizontal-center popup-button-vertical-item small-font login-sign-up-button cursor-pointer delete-element-tv wrap']"),
    'forgot_password': ('XPATH', "//div[@class='medium-font-type login-forget-password small-font ng-scope']"),
    'pass_show': ('XPATH', "//div[@class='login-icon vertical-center tv-icon medium-font login-eye-icon primary-font-color cursor-pointer icon-eye-on']")
    }

    def setEmail(self, email):
        self.email_input.set_text(email + '\n')

    def setPassword(self, password):
        self.pass_input.set_text(password + '\n')

    def checkShowPassword(self):
        self.pass_show.click()

    def clickSubmitButton(self):
        self.submit_button.click()
        return ProfileSelectorPage(self.driver)

    def clickRegisterButton(self):
        self.register_button.click()
        return BaseRegistrationPage(self.driver)

    def clickForgotPassword(self):
        self.forgot_password.click()
        return ForgotPasswordPage(self.driver)



