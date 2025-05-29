
from src.pages.credential_related.change_password_successful_message import ChangePasswordSuccessfulPage
from src.pages.credential_related.new_user_data_input_page import NewDataInputPage


# from src.pages.settings_acc_config import SettingsAccConfigPage


class ChangePasswordNewpasswordInputPage(NewDataInputPage):

    def set_current_password(self, p):
        self.current_pass_input_new_email.set_text(p)

    def set_new_password(self, p):
        self.pass_input.set_text(p)

    def set_new_password_duplicate(self, p):
        self.pass_input_duplicate.set_text(p)

    def click_continue(self):
        self.continue_button.click()
        return ChangePasswordSuccessfulPage(self.driver)

    def click_close(self):
        self.close.click()
        # return SettingsAccConfigPage(self.driver)


