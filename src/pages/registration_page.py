from seleniumpagefactory.Pagefactory import PageFactory

class BaseRegistrationPage(PageFactory):
    def __init__(self, driver):
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

    def setEmail(self, email):
        self.email_input.set_text(email)

    def setPhone(self, phone):
        self.email_input.set_text(phone)

    def setPassword(self, password):
        self.pass_input.set_text(password)

    def setPassword_duplicate(self, password):
        self.pass_input_duplicate.set_text(password)

    def checkShowPassword(self):
        self.pass_show.click()

    def checkShowPassword_duplicate(self):
        self.pass_show_duplicate.click()

    def setPrivacyPolicy(self):
        self.policy_check.click()

    def clickSubmitButton(self):
        self.register_confirm_button.click()

    def closeWindow(self):
        self.close.click()

class EmailRegistrationConfirmationPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'confirm_button': ('XPATH', "(//li[@class='button-vertical-container horizontal-center popup-button-vertical-item small-font wrap cursor-pointer rounded-input-40 ng-scope no-bg basic-border button-bg-color popup-button-vertical-item-bg'])[1]"),
        'back_button': ('XPATH', "//div[@class='tv-icon icon-up-arrow back-arrow back-login-button cursor-pointer ng-scope']"),
        'send_again': ('XPATH', "//span[@class='highlightMessage medium-font-type register-link ng-scope']")
    }

    def clickConfirmButton(self):
        self.confirm_button.click()
    def clickBack(self):
        self.back_button.click()
    def clickSendAgain(self):
        self.send_again.click()

class PhoneRegistrationOTPPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'email_input': ('XPATH', "//input[@id='email']"),
        'pass_input': ('XPATH', "//input[@id='password']"),
        'pass_input_duplicate': ('XPATH', "//input[@id='confirm-password']"),
        'close': ('XPATH', "//div[@class='tv-icon icon-exit close-login-button cursor-pointer ng-scope']")
    }

    def setEmail(self, email):
        self.email_input.set_text(email)

    def setPhone(self, phone):
        self.email_input.set_text(phone)

    def setPassword(self, password):
        self.pass_input.set_text(password)



