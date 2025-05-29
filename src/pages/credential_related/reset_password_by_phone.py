
from src.pages.credential_related.reset_password_page import ResetPasswordPage
from src.pages.credential_related.reset_password_phone_otp_input_page import ResetPasswordPhoneOTPInput


class ResetPasswordByPhonePage(ResetPasswordPage):

    def click_reset_button(self):
        self.reset_password_button.click()
        return ResetPasswordPhoneOTPInput(self.driver)
