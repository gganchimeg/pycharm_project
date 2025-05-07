
from seleniumpagefactory.Pagefactory import PageFactory
from utilities.readProperties import ReadConfig

class ChangePasswordSuccessfulPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
    'ok_button': ('XPATH', "//div[@class='ellipsis ng-binding ng-scope']")
    }

    def click_ok_button(self):
        self.ok_button.click()
        # login page ruu userne
