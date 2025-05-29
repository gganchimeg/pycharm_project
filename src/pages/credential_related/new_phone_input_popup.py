from src.pages.credential_related.new_user_data_input_page import NewDataInputPage
from src.pages.credential_related.update_phone_number_otp_input_page import UpdatePhoneNumberOTPInput


class NewPhoneInputPage(NewDataInputPage):

    def set_new_phone(self, p):
        self.current_pass_input_new_email.set_text(p)

    def set_new_phone_duplicate(self, p):
        self.confirm_new_email.set_text(p)

    def click_continue(self):
        self.continue_button.click()
        return UpdatePhoneNumberOTPInput(self.driver)

    def click_close(self):
        self.close.click()


