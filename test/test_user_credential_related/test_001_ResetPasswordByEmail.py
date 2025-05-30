from src.pages.credential_related.reset_password_by_email import ResetPasswordByEmailPage
from src.pages.login_page import LoginPage
from utilities.readProperties import ReadConfig
from utilities.helper_functions import update_config_value, return_activation_link, \
    extract_new_password_from_html_page


class TestResetPasswordByEmail:
    baseURL = ReadConfig.get_application_url()
    mail = ReadConfig.get_user_email()
    current_password = ReadConfig.get_password()
    def test_reset_password_by_email(self, setup):

        self.driver = setup  # setup dotroo browseroo zarlaad driver uusgesen
        self.driver.get(self.baseURL)
        # self.driver.maximize_window()
        self.driver.implicitly_wait(5)  # once

        self.startPage = LoginPage(self.driver)
        self.startPage.click_reset_password()
        reset_pass_page = ResetPasswordByEmailPage(self.driver)

        reset_pass_page.set_username(self.mail)
        verif_page = reset_pass_page.click_reset_button()


        # mailruugee nevtreed activation link deer dardag linkruuugee orno
        activation_link = return_activation_link(ReadConfig.get_registration_email())
        new_password = extract_new_password_from_html_page(activation_link)

        # open_link(self.driver, activation_link)  # to activate


        update_config_value("commonInfo", "password", new_password)
        update_config_value("updateInfo", "password", self.current_password)
        # current pass gesen variabled utgaa avtsan bsn solihoos umnu, but need to check

        self.driver.quit()











