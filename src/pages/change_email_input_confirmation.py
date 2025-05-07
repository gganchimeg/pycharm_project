from seleniumpagefactory.Pagefactory import PageFactory


class ChangeEmailInput(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'new_email': ('XPATH', "//div[@ng-if='(!showInputNewPassword || registerNewUserOpen) && !registerTermsOpen && !registerConfOpen']"),
        'confirm_new_email': ('XPATH', "//div[@ng-if='(!showInputNewPassword || registerNewUserOpen) && !registerTermsOpen && !registerConfOpen && changeEmailUsername']"),
        'close_button': ('XPATH', "//div[@class='tv-icon icon-exit close-login-button cursor-pointer ng-scope']"),
        'save_button': ('XPATH', "//div[@class='ellipsis vertical-center black-font-type login-button-text ng-binding ng-scope']")
    }

    def set_new_email(self, e):
        self.new_email.set_text(e)

    def set_confirm_new_email(self, e):
        self.confirm_new_email.set_text(e)



