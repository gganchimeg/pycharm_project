
from seleniumpagefactory.Pagefactory import PageFactory
from src.pages.payment_fourdigit_popup import PaymentPurchasePinInputPage
from src.pages.payment_unitel0_verification_code_popup import PaymentUnitel0VerifCodeInputPage
from utilities.readProperties import ReadConfig
from src.pages.payment_options import PaymentOptionsPage

class PaymentUnitel0PhoneNumberInputPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
    'input_box': ('XPATH', "//input[@id='input-mobile-phone']"),
    'close_button': ('XPATH', "//div[contains(@class,'ngdialog-message payment-options-modal center-item center-item-tv heavy-font-type')]//div[contains(@class,'tv-icon icon-exit close-payment-option-hover close-payment-button cursor-pointer delete-element-tv ng-scope')]"),
    'ok_button': ('XPATH', "//li[@ng-repeat='item in data']")
    }

    def setPhoneNumber(self, number):
        self.input_box.set_text(number)

    def clickOkButton(self):
        self.ok_button.click()
        return PaymentUnitel0VerifCodeInputPage(self.driver)

    def clickCloseButton(self):
        self.close_button.click()
        return PaymentOptionsPage(self.driver)

