from utilities.helper_functions import profile_selection_process, login_process, update_config_value
from utilities.readProperties import ReadConfig


class TestChangePassword:
    baseURL = ReadConfig.get_application_url()
    # logger = LogGen.loggen() # for log
    username = ReadConfig.get_username_for_login()
    current_password = ReadConfig.get_password()
    new_password = ReadConfig.get_update_password()

    def test_change_password(self, setup):
        self.driver = setup  # setup dotroo browseroo zarlaad driver uusgesen
        self.driver.get(self.baseURL)
        # self.driver.maximize_window()
        self.driver.implicitly_wait(10)  # once
        # --------------------- general login process ---------------------
        profile_selector_page = login_process(self.driver, usern= self.username, passw=self.current_password)
        home_page = profile_selection_process(profile_selector_page)

        profile_config_page = home_page.click_navigation_settings()
        account_config_page = profile_config_page.click_acc_conf()
        enter_new_password_popup = account_config_page.click_change_password()
        # fill out section
        enter_new_password_popup.set_current_password(self.current_password)
        enter_new_password_popup.set_new_password(self.new_password)
        enter_new_password_popup.set_new_password_duplicate(self.new_password)
        enter_new_password_popup.check_show_password()
        success_page = enter_new_password_popup.click_continue_fromsettings()
        success_page.click_ok_button()

        print('done')

        update_config_value(sec="commonInfo", opt="password", v=self.new_password)
        update_config_value(sec="updateInfo", opt="password", v=self.current_password)

        self.driver.quit()



