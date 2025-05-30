from seleniumpagefactory.Pagefactory import PageFactory
class BaseRegistrationPage(PageFactory):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    locators = {
        'email_input': ('XPATH', "//input[@id='email']"),
        'pass_input': ('XPATH', "//input[@id='password']"),
        'pass_input_duplicate': ('XPATH', "//input[@id='confirm-password']"),
        'policy_check': ('XPATH', "//input[@id='checkbox']"),
        'register_confirm_button': ('XPATH', "//div[@class='ellipsis vertical-center black-font-type login-button-text ng-binding ng-scope']"),
        'pass_show': ('XPATH', "//div[@ng-click='changeShowPassword()']"),
        'pass_show_duplicate': ('XPATH', "//div[@ng-click='changeShowNewPassword()']"),
        'privacy_policy_link': ('XPATH', "//span[@class='register-link ng-scope']"),
        'close': ('XPATH', "//div[@class='tv-icon icon-exit close-login-button cursor-pointer ng-scope']")
    }

    def set_email(self, email):
        self.email_input.set_text(email)

    def set_phone(self, phone):
        self.email_input.set_text(phone)

    def set_password(self, password):
        self.pass_input.set_text(password)

    def set_password_duplicate(self, password):
        self.pass_input_duplicate.set_text(password)

    def check_show_password(self):
        self.pass_show.click()

    def check_show_password_duplicate(self):
        self.pass_show_duplicate.click()

    def set_privacy_policy(self):
        self.policy_check.click()

    def click_submit_button(self):
        self.register_confirm_button.click()

    def click_close_button(self):
        self.close.click()


