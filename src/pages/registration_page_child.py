from seleniumpagefactory.Pagefactory import PageFactory

from src.pages.registration_page import BaseRegistrationPage
from src.pages.registration_phone_otp_input_page import RegistrationPhoneOTPInput

class EmailRegistrationPage(BaseRegistrationPage, PageFactory):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(self.driver)

    def clickSubmitButton(self):
        super().clickSubmitButton()
        # return RegistrationEmailVerificationPage(self.driver)


class PhoneRegistrationPage(BaseRegistrationPage, PageFactory):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(self.driver)

    def clickSubmitButton(self):
        super().clickSubmitButton()
        return RegistrationPhoneOTPInput(self.driver)