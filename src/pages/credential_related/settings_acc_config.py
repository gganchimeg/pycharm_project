from seleniumpagefactory.Pagefactory import PageFactory
from src.pages.credential_related.change_email_input_confirmation import ChangeEmailInput
from src.pages.credential_related.change_password_newpassword_input_popup import ChangePasswordNewpasswordInputPage
from src.pages.credential_related.new_phone_input_popup import NewPhoneInputPage


class SettingsAccConfigPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'change_password': ('XPATH', "/html[1]/body[1]/div[2]/div[1]/div[3]/div[2]/settings-account[1]/div[1]/div[1]/div[4]/div[1]/linear-list[1]/ul[1]/ng-include[1]/div[1]/div[1]/div[1]/linear-list[1]/ul[1]/ng-include[1]/div[1]/span[2]"),
        'change_email': ('XPATH', "/html[1]/body[1]/div[2]/div[1]/div[3]/div[2]/settings-account[1]/div[1]/div[1]/div[4]/div[1]/linear-list[1]/ul[1]/ng-include[1]/div[2]/div[1]/div[1]/linear-list[1]/ul[1]/ng-include[1]/div[1]/span[2]"),
        'change_phone': ('XPATH', "/html[1]/body[1]/div[2]/div[1]/div[3]/div[2]/settings-account[1]/div[1]/div[1]/div[4]/div[1]/linear-list[1]/ul[1]/ng-include[1]/div[3]/div[1]/div[1]/linear-list[1]/ul[1]/ng-include[1]/div[1]/span[2]"),
        'change_par_pin': ('XPATH', "/html[1]/body[1]/div[2]/div[1]/div[3]/div[2]/settings-account[1]/div[1]/div[1]/div[4]/div[1]/linear-list[1]/ul[1]/ng-include[1]/div[4]/div[2]/div[1]/linear-list[1]/ul[1]/ng-include[1]/div[1]/span[2]")
    }

    def click_change_email(self):
        self.change_email.click()
        return ChangeEmailInput(self.driver)

    def click_change_password(self):
        self.change_password.click()
        return ChangePasswordNewpasswordInputPage(self.driver)

    def click_change_phone(self):
        self.change_phone.click()
        return NewPhoneInputPage(self.driver)




