from seleniumpagefactory.Pagefactory import PageFactory


class NewDataInputPage(PageFactory):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    locators = {
        'current_pass_input_new_email': ('XPATH', "//input[@id='email']"),
        'confirm_new_email': ('XPATH', "//input[@id='confirm-email']"),
        'pass_input': ('XPATH', "//input[@id='password']"),
        'pass_input_duplicate': ('XPATH', "//input[@id='confirm-password']"),
        'continue_button': ('XPATH', "//div[@class='ellipsis vertical-center black-font-type login-button-text ng-binding ng-scope']"),
        'pass_show': ('XPATH', "//div[@ng-click='changeShowPassword()']"),
        'pass_show_duplicate': ('XPATH', "//div[@ng-click='changeShowNewPassword()']"),
        'close': ('XPATH', "//div[@class='tv-icon icon-exit close-login-button cursor-pointer ng-scope']")
    }

    def check_show_password(self):
        self.pass_show.click()

    def check_show_password_duplicate(self):
        self.pass_show_duplicate.click()

    def click_continue(self):
        pass

    def click_close(self):
        pass


