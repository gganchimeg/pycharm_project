from seleniumpagefactory.Pagefactory import PageFactory


class SuccessfulMessage(PageFactory):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    locators = {
    'ok_login_button': ('XPATH', "//div[@class='ellipsis ng-binding ng-scope']")
    }

    def click_ok_button(self):
        pass
