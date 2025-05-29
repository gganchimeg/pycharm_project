from src.pages.credential_related.registration_page_child import EmailRegistrationPage
from src.pages.credential_related.registration_email_sent_page import RegistrationEmailVerificationPage
from src.pages.login_page import LoginPage
from utilities.helper_functions import return_activation_link
from utilities.readProperties import ReadConfig


class TestRegistrationByEmail:
    baseURL = ReadConfig.getApplicationURL()

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
        self.regPage.set_email(ReadConfig.getRegistrationEmail())
        self.regPage.set_password(ReadConfig.getRegistrationPassword())
        self.regPage.setPassword_duplicate(ReadConfig.getRegistrationPassword())
        self.regPage.setPrivacyPolicy()

        self.regPage.click_submit_button()
    #   circular importooso bolj endee init hiilee
        verif_page = RegistrationEmailVerificationPage(self.driver)

        # mailruugee nevtreed activation link deer dardag linkruuugee orno
        activation_link = return_activation_link(ReadConfig.getRegistrationEmail())
        self.driver.get(activation_link)
        self.driver.close()   #activationii tsonhiig haana

        # verif_page.clickSendAgainLink()


















        





