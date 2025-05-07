from seleniumpagefactory.Pagefactory import PageFactory

class RegistrationSuccessfulPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'login_button': ('XPATH', "//div[@class='ellipsis ng-binding ng-scope']")
    }

    def clickLoginButton(self):
        self.login_button.click()
        print('erasing loginpage return value due to circular import')
        # return LoginPage(self.driver)



