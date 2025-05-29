from src.pages.credential_related.new_user_data_input_page import NewDataInputPage


class ResetPasswordNewpasswordInputPage(NewDataInputPage):

    def set_current_password(self, p):
        self.current_pass_input_new_email.set_text(p)

    def set_new_password(self, p):
        self.pass_input.set_text(p)

    def set_new_password_duplicate(self, p):
        self.pass_input_duplicate.set_text(p)

    def click_continue(self):
        self.continue_button.click()
        return (self.driver)

    def click_close(self):
        self.close.click()
        # return ????/


