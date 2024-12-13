from seleniumpagefactory.Pagefactory import PageFactory

class ForgotPasswordPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'email_input': ('XPATH', "//input[@id='email']"),
        'reset_password_button': ('XPATH', "(//li[@class='button-vertical-container horizontal-center popup-button-vertical-item small-font wrap cursor-pointer rounded-input-40 ng-scope no-bg basic-border popup-button-vertical-item-bg'])[1]"),
        'cancel_button': ('XPATH', "//div[normalize-space()='Cancel']")
    }

    def fill_email_input(self, email):
        self.email_input.set_text(email+'\n')

    def click_reset_button(self):
        self.reset_password_button.click()

    def click_cancel_button(self):
        self.cancel_button.click()


