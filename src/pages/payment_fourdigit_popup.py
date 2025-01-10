from seleniumpagefactory.Pagefactory import PageFactory
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
    def setDigitOne(self):
        self.digit_one.set_text(9)
        # inputBox = self.digit_one.click()
        # inputBox.sendKeys("9")

    def setDigitTwo(self):
        self.digit_two.set_text(9)
        # inputBox = self.digit_two.click()
        # inputBox.sendKeys("9")

    def setDigitThree(self):
        self.digit_three.set_text(9)

        # inputBox = self.digit_three.click()
        # inputBox.sendKeys("9")

    def setDigitFour(self):
        self.digit_four.set_text(9)

        # inputBox = self.digit_four.click()
        # inputBox.sendKeys("9")

    def clickCloseButton(self):
        self.close_button.click()
        # ymar2 caseuudees orjj irj bolohiig bodoh heregtei !!!!!!!!!!!!!!!!!!!!!!!!!
        # return PaymentOptionsPage(self.driver)

    def clickSubmitButton(self):
        self.submit_button.click()
        # return PaymentOptionsPage(self.driver)
