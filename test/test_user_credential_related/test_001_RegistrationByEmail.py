from src.pages.credential_related.registration_page_child import EmailRegistrationPage
from src.pages.credential_related.registration_email_sent_page import RegistrationEmailVerificationPage
from src.pages.login_page import LoginPage
from utilities.helper_functions import return_activation_link
from utilities.readProperties import ReadConfig


class TestRegistrationByEmail:
    baseURL = ReadConfig.get_application_url()
    activation_link = None

    def test_register_by_email(self, setup):
        """
            Completed
        """
        self.driver = setup  # setup dotroo browseroo zarlaad driver uusgesen
        self.driver.get(self.baseURL)
        # self.driver.maximize_window()
        self.driver.implicitly_wait(10)  # once

        self.startPage = LoginPage(self.driver)
        self.startPage.click_register_button()
        self.regPage = EmailRegistrationPage(self.driver)
        # fill in process
        self.regPage.set_email(ReadConfig.get_registration_email())
        self.regPage.set_password(ReadConfig.get_registration_password())
        self.regPage.set_password_duplicate(ReadConfig.get_registration_password())
        self.regPage.set_privacy_policy()

        self.regPage.click_submit_button()
    #   circular importooso bolj endee init hiilee
        verif_page = RegistrationEmailVerificationPage(self.driver)

        # mailruugee nevtreed activation link deer dardag linkruuugee orno
        self.activation_link = return_activation_link(ReadConfig.get_registration_email())
        while self.activation_link is None:
            verif_page.clickSendAgainLink()
            self.activation_link = return_activation_link(ReadConfig.get_registration_email())
        #  double check hiih edit hiisnees hoish run hiij uzeegui
        self.driver.get(self.activation_link)
        self.driver.close()   #activationii tsonhiig haana






















        





