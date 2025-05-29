
from src.pages.credential_related.successful_message_popup import SuccessfulMessage

class ResetPasswordSuccessfulPage(SuccessfulMessage):

    def click_ok_button(self):
        self.ok_button.click()
        # login page ruu userne, returnhiih geheer circular import bolchood bna