from seleniumpagefactory.Pagefactory import PageFactory


class EmailSentPopup(PageFactory):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    locators = {
        'ok_button': ('XPATH', "//div[@class='ellipsis ng-binding ng-scope']"),
        'send_again_link': ('XPATH', "//span[@ng-click='resendMail()']")
    }

    def click_ok_button(self):
        self.ok_button.click()
        # return LoginPage(self.driver)
    def click_send_again_link(self):
        self.send_again_link.click()
        # return self


