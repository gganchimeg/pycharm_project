from seleniumpagefactory.Pagefactory import PageFactory
from utilities.readProperties import ReadConfig

class SuccessfulMessage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
    'ok_login_button': ('XPATH', "//div[@class='ellipsis ng-binding ng-scope']")
    }

    def click_ok_button(self):
        pass
