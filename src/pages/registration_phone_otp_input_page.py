from seleniumpagefactory.Pagefactory import PageFactory
from src.pages.registration_successful_page import RegistrationSuccessfulPage
from typing_extensions import ParamSpec


class RegistrationPhoneOTPInput(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'digit_one': ('XPATH', "//input[@id='pin0']"),
        'digit_two': ('XPATH', "//input[@id='pin1']"),
        'digit_three': ('XPATH', "//input[@id='pin2']"),
        'digit_four': ('XPATH', "//input[@id='pin3']"),
        'digit_five': ('XPATH', "//input[@id='pin4']"),
        'digit_six': ('XPATH', "//input[@id='pin5']"),
        'submit_button': ('XPATH', "//div[@class='pin-confirm medium-font language-unfocused setting-element-hovered cursor-pointer']"),
        'back_button': ('XPATH', "//div[@class='icon-up-arrow back-arrow arrow-back-button cursor-pointer ng-scope']"),
        'send_again_link': ('XPATH', "//span[@class='highlightMessage medium-font-type cursor-pointer ng-binding ng-scope']")
    }

    def setDigitOne(self, digitone):
        self.digit_one.set_text(digitone)

    def setDigitTwo(self, digittwo):
        self.digit_two.set_text(digittwo)

    def setDigitThree(self, digitthree):
        self.digit_three.set_text(digitthree)

    def setDigitFour(self, digitfour):
        self.digit_four.set_text(digitfour)

    def setDigitFive(self, digitfive):
        self.digit_five.set_text(digitfive)

    def setDigitSix(self, digitsix):
        self.digit_six.set_text(digitsix)

    def clickSubmitButton(self):
        self.submit_button.click()
        return RegistrationSuccessfulPage(self.driver)

    def clickBackButton(self):
        self.back_button.click()
    #      endees back hiiihed registration page garch irn gehdee inputuud ni
    #      already filled baih uchraas need to clear them first
    #      !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    # also login_page ees shuud registration_phone_otp_input_page ruu shijine
    #     return basereg(self.driver)   circular import
        pass
    def clickSendAgainLink(self):
        self.send_again_link.click()
        return self


