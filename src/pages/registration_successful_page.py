from seleniumpagefactory.Pagefactory import PageFactory


class RegistrationSuccessfulPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'login_button': ('XPATH', "//div[@class='ellipsis vertical-center black-font-type login-button-text ng-binding ng-scope']")
    }

    def clickLoginButton(self):
        # self.login_button.click()
        # return LoginPage(self.driver)
        pass



