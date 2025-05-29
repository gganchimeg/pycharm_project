from src.pages.credential_related.successful_message_popup import SuccessfulMessage


class ChangePasswordSuccessfulPage(SuccessfulMessage):

    def click_ok_button(self):
        self.ok_login_button.click()
        # login page ruu userne, returnhiih geheer circular import bolchood bna
