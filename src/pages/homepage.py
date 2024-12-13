from seleniumpagefactory.Pagefactory import PageFactory

class HomePage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'email_input': ('XPATH', "//input[@id='email']"),
        'pass_input': ('XPATH', "//input[@id='password']"),
        'close': ('XPATH', "//div[@class='tv-icon icon-exit close-login-button cursor-pointer ng-scope']")
    }

    def fill_email_input(self):
        self.email_input.set_text('ganchimeg.ganbaatarr@gmail.com\n')

    def fill_pass_input(self):
        self.pass_input.set_text("Ganchimeg.g\n")
        self.pass_input_duplicate.set_text("Ganchimeg.g\n")

    def check_show_password(self):
        self.pass_show.click()