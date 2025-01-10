
from seleniumpagefactory.Pagefactory import PageFactory
from utilities.readProperties import ReadConfig
from src.pages.payment_options import PaymentOptionsPage

class PaymentPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
    'rent_button': ('XPATH', "//div[@class='button-hovered rent-movie-button medium-font cursor-pointer medium-font-type ng-binding']"),
    'close_button': ('XPATH', "//div[@class='tv-icon icon-exit close-payment-option-hover close-payment-button cursor-pointer delete-element-tv ng-scope']")
    }

    def clickRentButton(self):
        self.rent_button.click()
        return PaymentOptionsPage(self.driver)
