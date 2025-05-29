
from src.pages.credential_related.reset_password_by_email_sent_page import ResetPasswordByEmailVerificationPage
from src.pages.credential_related.reset_password_page import ResetPasswordPage


class ResetPasswordByEmailPage(ResetPasswordPage):

    def click_reset_button(self):
        self.reset_password_button.click()
        return ResetPasswordByEmailVerificationPage(self.driver)
