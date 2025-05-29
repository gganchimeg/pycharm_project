from src.pages.credential_related.registration_successful_page import RegistrationSuccessfulPage
from src.pages.credential_related.six_digit_otp_input_page import SixDigitOTPInput


class RegistrationPhoneOTPInput(SixDigitOTPInput):

    def clickSubmitButton(self):
        self.submit_button.click()
        return RegistrationSuccessfulPage(self.driver)

    def clickBackButton(self):
        self.back_button.click()
    #      endees back hiiihed registration page garch irn gehdee inputuud ni
    #      already filled baih uchraas need to clear them first
    #      !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    # also login_page ees shuud registration_phone_otp_input_page ruu shijine
    #     return basereg(self.driver)   circular import
        pass


