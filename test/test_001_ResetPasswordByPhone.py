import time
from src.pages.reset_password_page import ResetPasswordPage
from src.pages.login_page import LoginPage
from utilities.readProperties import ReadConfig
from test.otp_extraction import otp_extraction
from utilities.helper_functions import getOTP, update_config_value

class TestResetPasswordByPhone:
    baseURL = ReadConfig.getApplicationURL()
    phone = ReadConfig.getPhoneNumber()
    current_password = ReadConfig.getPassword()
    new_password = ReadConfig.getUpdatePassword()
    def test_reset_password_by_phone(self, setup):
        '''
        Completed
        :param setup:
        :return:
        '''
        self.driver = setup  # setup dotroo browseroo zarlaad driver uusgesen
        self.driver.get(self.baseURL)
        # self.driver.maximize_window()
        self.driver.implicitly_wait(5)  # once

        self.startPage = LoginPage(self.driver)
        self.startPage.click_reset_password()
        reset_pass_page = ResetPasswordPage(self.driver)

        reset_pass_page.set_username(self.phone)
        otp_input_page = reset_pass_page.click_reset_button()
        time.sleep(20)   # otp irehiig huleene

        # ene heseg deer adb geer message ruuu handalt hiij OTP gee avna
        code = otp_extraction()
        print(code)
        otp_list = getOTP(code)
        print("list: ", otp_list)
        print("otp extracted")
        # otp fill in
        otp_input_page.set_digit_one(otp_list[0])
        otp_input_page.set_digit_two(otp_list[1])
        otp_input_page.set_digit_three(otp_list[2])
        otp_input_page.set_digit_four(otp_list[3])
        otp_input_page.set_digit_five(otp_list[4])
        otp_input_page.set_digit_six(otp_list[5])
        print("otp filled in")

        enter_new_pass_page = otp_input_page.click_submit_button()
        print("opening new pass page")
        time.sleep(5)
        # enter new password
        enter_new_pass_page.set_new_password(self.new_password)
        enter_new_pass_page.set_new_password_duplicate(self.new_password)
        reg_successful_page = enter_new_pass_page.click_continue_fromforgotpassword()
        # reg_successful_page.clickLoginButton()
        print("\ndone")


        update_config_value("commonInfo", "password", self.new_password)
        update_config_value("updateInfo", "password", self.current_password)
        # current pass gesen variabled utgaa avtsan bsn solihoos umnu, but need to check

        self.driver.quit()











