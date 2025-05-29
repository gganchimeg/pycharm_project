from seleniumpagefactory.Pagefactory import PageFactory

class PurchaseSuccessfulPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'ok_button': ('XPATH', "//div[@id='paymentsucessful-dialog']//li[1]"),
        'close_button': ('XPATH', "//div[contains(@ng-click,'closePopUp()')]")
    }

    def click_ok_button(self):
        self.ok_button.click()

    def click_close_button(self):
        self.close_button.click()




