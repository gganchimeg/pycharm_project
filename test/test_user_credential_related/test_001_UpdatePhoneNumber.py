import time
from utilities.readProperties import ReadConfig
from utilities.helper_functions import login_process, update_config_value, string_to_list, otp_extraction
from utilities.helper_functions import profile_selection_process


class TestUpdatePhoneNumber:
    baseURL = ReadConfig.getApplicationURL()
    # logger = LogGen.loggen() # for log
    username = ReadConfig.getUsernameForLogin()
    current_password = ReadConfig.getPassword()
    current_phone = ReadConfig.getPhoneNumber()
    new_phone = ReadConfig.getUpdatePhoneNumber()

    def test_update_phone_number(self, setup):
        self.driver = setup  # setup dotroo browseroo zarlaad driver uusgesen
        self.driver.get(self.baseURL)
        # self.driver.maximize_window()
        self.driver.implicitly_wait(10)  # once
        # --------------------- general login process ---------------------
        profile_selector_page = login_process(self.driver, usern= self.username, passw=self.current_password)
        home_page = profile_selection_process(profile_selector_page)

        profile_config_page = home_page.click_navigation_settings()
        account_config_page = profile_config_page.click_acc_conf()


        enter_new_phonenumber = account_config_page.click_change_phone()
        enter_new_phonenumber.set_new_phone(self.new_phone)
        enter_new_phonenumber.set_new_phone_duplicate(self.new_phone)
        enter_otp_page = enter_new_phonenumber.click_continue()
        time.sleep(10)
        # ene heseg deer adb geer message ruuu handalt hiij OTP gee avna
        code = otp_extraction()
        otp_list = string_to_list(code)
        # otp fill in
        enter_otp_page.set_digit_one(otp_list[0])
        enter_otp_page.set_digit_two(otp_list[1])
        enter_otp_page.set_digit_three(otp_list[2])
        enter_otp_page.set_digit_four(otp_list[3])
        enter_otp_page.set_digit_five(otp_list[4])
        enter_otp_page.set_digit_six(otp_list[5])

        update_successful_page = enter_otp_page.click_submit_button()

        time.sleep(5)

        update_successful_page.click_ok_button()

        print('done')

        # updating the credentials in config
        update_config_value(sec="commonInfo", opt="phone", v=self.new_phone)
        update_config_value(sec="updateInfo", opt="phone", v=self.current_phone)

        self.driver.quit()



