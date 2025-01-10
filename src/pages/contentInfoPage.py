from seleniumpagefactory.Pagefactory import PageFactory
from src.pages.payment_popup import PaymentPage
class ContentInfoPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'rent_button': ('XPATH', "//div[@class='info-action-buttons ng-scope']//li[1]//div[1]")
    }

    def clickRentButton(self):
        self.rent_button.click()
        return PaymentPage(self.driver)
