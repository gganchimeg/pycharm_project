from seleniumpagefactory.Pagefactory import PageFactory
from src.pages.registration_successful_page import RegistrationSuccessfulPage
from typing_extensions import ParamSpec

from src.pages.new_password_input_popup import TestNewpasswordInputPage


class ResetPasswordPhoneOTPInput(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'digit_one': ('XPATH', "//input[@id='pin0']"),
        'digit_two': ('XPATH', "//input[@id='pin1']"),
        'digit_three': ('XPATH', "//input[@id='pin2']"),
        'digit_four': ('XPATH', "//input[@id='pin3']"),
        'digit_five': ('XPATH', "//input[@id='pin4']"),
        'digit_six': ('XPATH', "//input[@id='pin5']"),
        'submit_button': ('XPATH', "//div[@class='medium-font-type ng-binding']"),
        'back_button': ('XPATH', "//div[@class='icon-up-arrow back-arrow arrow-back-button cursor-pointer ng-scope']"),
        'send_again_link': ('XPATH', "//span[@class='highlightMessage medium-font-type cursor-pointer ng-binding ng-scope']")
    }

    def set_digit_one(self, digitone):
        self.digit_one.set_text(digitone)

    def set_digit_two(self, digittwo):
        self.digit_two.set_text(digittwo)

    def set_digit_three(self, digitthree):
        self.digit_three.set_text(digitthree)

    def set_digit_four(self, digitfour):
        self.digit_four.set_text(digitfour)

    def set_digit_five(self, digitfive):
        self.digit_five.set_text(digitfive)

    def set_digit_six(self, digitsix):
        self.digit_six.set_text(digitsix)

    def click_submit_button(self):
        self.submit_button.click()
        return TestNewpasswordInputPage(self.driver)

    def click_back_button(self):
        self.back_button.click()
    #      endees back hiiihed registration page garch irn gehdee inputuud ni
    #      already filled baih uchraas need to clear them first
    #      !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    # also login_page ees shuud registration_phone_otp_input_page ruu shijine
    #     return basereg(self.driver)   circular import
    def click_send_again_link(self):
        self.send_again_link.click()


