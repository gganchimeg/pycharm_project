from src.pages.profile_selection import ProfileSelectorPage
from src.pages.credential_related.reset_password_page import ResetPasswordPage
from seleniumpagefactory.Pagefactory import PageFactory
from src.pages.credential_related.registration_page import BaseRegistrationPage

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

    def set_email(self, email):
        self.email_input.set_text(email)

    def set_password(self, password):
        self.pass_input.set_text(password)

    def check_show_password(self):
        self.pass_show.click()

    def click_submit_button(self):
        self.submit_button.click()
        return ProfileSelectorPage(self.driver)

    def click_register_button(self):
        self.register_button.click()
        return BaseRegistrationPage(self.driver)
    #     eniiig garaas avaad goy hiiine odoohondoo hardcode hiiy

    def click_reset_password(self):
        self.forgot_password.click()
        return ResetPasswordPage(self.driver)



