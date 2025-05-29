from src.pages.credential_related.change_email_sent_page import ChangeEmailVerificationPage
from src.pages.credential_related.new_user_data_input_page import NewDataInputPage
# from src.pages.settings_acc_config import SettingsAccConfigPage


class ChangeEmailInput(NewDataInputPage):

    def set_new_email(self, e):
        self.current_pass_input_new_email.set_text(e)

    def set_confirm_email(self, e):
        self.confirm_new_email.set_text(e)

    def click_continue(self):
        self.continue_button.click()
        return ChangeEmailVerificationPage(self.driver)

    def click_close(self):
        self.close.click()
        # return SettingsAccConfigPage(self.driver)


