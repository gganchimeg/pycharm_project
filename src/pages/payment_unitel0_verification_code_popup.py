
from seleniumpagefactory.Pagefactory import PageFactory
from src.pages.payment_fourdigit_popup import PaymentPurchasePinInputPage
from src.pages.payment_successful_popup import PurchaseSuccessfulPage
from utilities.readProperties import ReadConfig
from src.pages.payment_options import PaymentOptionsPage

class PaymentUnitel0VerifCodeInputPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
    'input_box': ('XPATH', "//input[@id='input-unitel-code']"),
    'close_button': ('XPATH', "//div[@class='payment-unitel-code-modal']//div[@class='tv-icon icon-exit close-payment-option-hover close-payment-button cursor-pointer delete-element-tv ng-scope']"),
    'ok_button': ('XPATH', "//li[contains(@ng-repeat,'item in data')]"),
    'resend': ('XPATH', "//span[contains(@class,'unitel-resend ng-scope')]")
    }

    def setVerifCode(self, code):
        self.input_box.set_text(code)

    def clickOkButton(self):
        self.ok_button.click()
        return PurchaseSuccessfulPage(self.driver)

    def clickCloseButton(self):
        self.close_button.click()
        return PaymentOptionsPage(self.driver)

    def clickResend(self):
        self.resend.click()

