import time
from utilities.readProperties import ReadConfig
from utilities.helper_functions import login_process, update_config_value, return_activation_link
from utilities.helper_functions import profile_selection_process


class TestUpdateEmailAddress:
    baseURL = ReadConfig.get_application_url()
    # logger = LogGen.loggen() # for log
    username = ReadConfig.get_username_for_login()
    current_password = ReadConfig.get_password()
    current_email = ReadConfig.get_user_email()
    new_email = ReadConfig.get_new_email()

    def test_update_email_address(self, setup):
        self.driver = setup  # setup dotroo browseroo zarlaad driver uusgesen
        self.driver.get(self.baseURL)
        # self.driver.maximize_window()
        self.driver.implicitly_wait(10)  # once
        # --------------------- general login process ---------------------
        profile_selector_page = login_process(self.driver, usern= self.username, passw=self.current_password)
        home_page = profile_selection_process(profile_selector_page)

        profile_config_page = home_page.click_navigation_settings()
        account_config_page = profile_config_page.click_acc_conf()


        enter_new_email = account_config_page.click_change_email()
        enter_new_email.set_new_email(self.new_email)
        enter_new_email.set_confirm_email(self.new_email)

        verif_email_sent_page = enter_new_email.click_continue()
        time.sleep(10)

        # mailruugee nevtreed activation link deer dardag linkruuugee orno
        activation_link = return_activation_link(self.new_email)
        print("link: ", activation_link)

        self.driver.get(activation_link)
        # self.driver.close()   #activationii tsonhiig haana

        time.sleep(5)

        verif_email_sent_page.click_ok_button()

        print('done')

        # updating the credentials in config
        update_config_value(sec="commonInfo", opt="email", v=self.new_email)
        update_config_value(sec="updateInfo", opt="email", v=self.current_email)

        self.driver.quit()



