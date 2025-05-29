from src.pages.credential_related.change_password_successful_message import ChangePasswordSuccessfulPage
from src.pages.credential_related.six_digit_otp_input_page import SixDigitOTPInput


class UpdatePhoneNumberOTPInput(SixDigitOTPInput):

    def click_submit_button(self):
        self.submit_button.click()
        return ChangePasswordSuccessfulPage(self.driver)

    def click_back_button(self):
        self.back_button.click()
    #      endees back hiiihed registration page garch irn gehdee inputuud ni
    #      already filled baih uchraas need to clear them first
    #      !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    # also login_page ees shuud registration_phone_otp_input_page ruu shijine
    #     return basereg(self.driver)   circular import

