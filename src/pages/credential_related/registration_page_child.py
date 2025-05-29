from src.pages.credential_related.registration_page import BaseRegistrationPage
from src.pages.credential_related.registration_phone_otp_input_page import RegistrationPhoneOTPInput

class EmailRegistrationPage(BaseRegistrationPage):

    def clickSubmitButton(self):
        super().clickSubmitButton()
        # return RegistrationEmailVerificationPage(self.driver)


class PhoneRegistrationPage(BaseRegistrationPage):

    def clickSubmitButton(self):
        super().clickSubmitButton()
        return RegistrationPhoneOTPInput(self.driver)