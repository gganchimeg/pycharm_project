from seleniumpagefactory.Pagefactory import PageFactory
from src.pages.reset_password_phone_otp_input_page import ResetPasswordPhoneOTPInput


class ResetPasswordPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'email_input': ('XPATH', "//input[@id='email']"),
        'reset_password_button': ('XPATH', "(//li[@class='button-vertical-container horizontal-center popup-button-vertical-item small-font wrap cursor-pointer rounded-input-40 ng-scope no-bg basic-border popup-button-vertical-item-bg'])[1]"),
        'cancel_button': ('XPATH', "//div[normalize-space()='Cancel']")
    }

    def set_username(self, p):
        self.email_input.set_text(p)

    def click_reset_button(self):
        self.reset_password_button.click()
        return ResetPasswordPhoneOTPInput(self.driver)

    def click_cancel_button(self):
        self.cancel_button.click()


