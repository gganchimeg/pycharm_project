import time
from src.pages.credential_related.registration_page_child import PhoneRegistrationPage
from src.pages.login_page import LoginPage
from utilities.readProperties import ReadConfig
from utilities.helper_functions import string_to_list, otp_extraction


class TestRegistrationByPhone:
    baseURL = ReadConfig.get_application_url()
    email = ReadConfig.get_registration_phone()
    password = ReadConfig.get_registration_password()
    def test_register_by_phone(self, setup):
        """
            Completed
        :param setup:
        :return:
        """
        self.driver = setup  # setup dotroo browseroo zarlaad driver uusgesen
        self.driver.get(self.baseURL)
        # self.driver.maximize_window()
        self.driver.implicitly_wait(10)  # once

        self.startPage = LoginPage(self.driver)
        self.startPage.click_register_button()
        self.regPage = PhoneRegistrationPage(self.driver)

        self.regPage.set_email(self.email)
        self.regPage.set_password(self.password)
        self.regPage.set_password_duplicate(self.password)
        self.regPage.set_privacy_policy()
        otp_input_page = self.regPage.click_submit_button()
        time.sleep(15)   # sms irehiig huleene


        # ene heseg deer adb geer message ruuu handalt hiij OTP gee avna
        code = otp_extraction()
        otp_list = string_to_list(code)
        # otp fill in
        otp_input_page.set_digit_one(otp_list[0])
        otp_input_page.set_digit_two(otp_list[1])
        otp_input_page.set_digit_three(otp_list[2])
        otp_input_page.set_digit_four(otp_list[3])
        otp_input_page.set_digit_five(otp_list[4])
        otp_input_page.set_digit_six(otp_list[5])

        reg_successful_page = otp_input_page.click_submit_button()
        time.sleep(10)
        reg_successful_page.click_login_button()

        print("\ndone")


        self.driver.quit()











