from src.pages.credential_related.registration_page import BaseRegistrationPage
from src.pages.credential_related.registration_phone_otp_input_page import RegistrationPhoneOTPInput

class EmailRegistrationPage(BaseRegistrationPage):

    def click_submit_button(self):
        super().click_submit_button()
        # return RegistrationEmailVerificationPage(self.driver)


class PhoneRegistrationPage(BaseRegistrationPage):

    def click_submit_button(self):
        super().click_submit_button()
        return RegistrationPhoneOTPInput(self.driver)