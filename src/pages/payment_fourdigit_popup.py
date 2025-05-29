from seleniumpagefactory.Pagefactory import PageFactory

from src.pages.payment_successful_popup import PurchaseSuccessfulPage
from utilities.readProperties import ReadConfig
from src.pages.payment_options import PaymentOptionsPage
# only for token payment, unitel payment
class PaymentPurchasePinInputPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
    'submit_button': ('XPATH', "//div[@class='button-hovered confirm-pin-button medium-font cursor-pointer language-unfocused medium-font-type ng-binding ng-scope']"),
    'close_button': ('XPATH', "//div[@class='tv-icon icon-exit close-payment-button cursor-pointer ng-scope']"),
    'digit_one': ('XPATH', "//input[@id='pin0']"),
    'digit_two': ('XPATH', "//input[@id='pin1']"),
    'digit_three': ('XPATH', "//input[@id='pin2']"),
    'digit_four': ('XPATH', "//input[@id='pin3']")
    }
    def set_digit_one(self, d):
        self.digit_one.set_text(d)

    def set_digit_two(self, d):
        self.digit_two.set_text(d)

    def set_digit_three(self, d):
        self.digit_three.set_text(d)

    def set_digit_four(self, d):
        self.digit_four.set_text(d)

    def click_close_button(self):
        self.close_button.click()
        # ymar2 caseuudees orjj irj bolohiig bodoh heregtei !!!!!!!!!!!!!!!!!!!!!!!!!
        # return PaymentOptionsPage(self.driver)

    def click_submit_button(self):
        self.submit_button.click()
        return PurchaseSuccessfulPage(self.driver)
