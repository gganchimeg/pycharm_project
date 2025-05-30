
from seleniumpagefactory.Pagefactory import PageFactory

from src.pages.payment_options import PaymentOptionsPage
from src.pages.payment_unitel0_verification_code_popup import PaymentUnitel0VerifCodeInputPage


class PaymentUnitel0PhoneNumberInputPage(PageFactory):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    locators = {
    'input_box': ('XPATH', "//input[@id='input-mobile-phone']"),
    'close_button': ('XPATH', "//div[contains(@class,'ngdialog-message payment-options-modal center-item center-item-tv heavy-font-type')]//div[contains(@class,'tv-icon icon-exit close-payment-option-hover close-payment-button cursor-pointer delete-element-tv ng-scope')]"),
    'ok_button': ('XPATH', "//li[@ng-repeat='item in data']")
    }

    def set_phone_number(self, number):
        self.input_box.set_text(number)

    def click_ok_button(self):
        self.ok_button.click()
        return PaymentUnitel0VerifCodeInputPage(self.driver)

    def click_close_button(self):
        self.close_button.click()
        return PaymentOptionsPage(self.driver)

