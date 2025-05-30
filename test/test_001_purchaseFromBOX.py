import time

from src.pages.payment_unitel0_phone_input_popup import PaymentUnitel0PhoneNumberInputPage
from utilities.helper_functions import login_process, string_to_list
from utilities.helper_functions import profile_selection_process
from utilities.readProperties import ReadConfig


#

class Test:
    baseURL = ReadConfig.get_application_url()
    # logger = LogGen.loggen() # for log
    username = ""
    password = ""

    def purchase_box_content(self, setup):
        """
        completed
        :param setup:
        :return:
        """

        # variables for just initial testing
        # will remove it later ----------------------------------------------
        purchase_pin = ReadConfig.get_purchase_pin()

        # -------------------------------------------------------------------
        # self.logger.info("/* test001_LoginByEmail started */")
        self.driver = setup  # setup dotroo browseroo zarlaad driver uusgesen
        self.driver.get(self.baseURL)
        # self.driver.maximize_window()
        self.driver.implicitly_wait(10)  # once

        # --------------------- general login process ---------------------
        profile_selector_page = login_process(self.driver, usern=self.username, passw=self.password)
        home_page = profile_selection_process(profile_selector_page)
        # --------------------- end -----------------

        # ---------  old code below
        box_page = home_page.click_navigation_box()
        content_info_page = box_page.click_crazyrich()
        time.sleep(2)
        payment_popup = content_info_page.click_rent_button()
        payment_options = payment_popup.click_rent_button()
        payment_options.click_default_payment()
        unitel0_popup = PaymentUnitel0PhoneNumberInputPage(self.driver)
        # default payment ni unitel-0 baih yum bol dugaar insert hiideg popup class init hiih hereg garch baina
        # odoohondoo shuud hardcode hiilee
        unitel0_popup.set_phone_number("86118529")
        verif_otp_popup = unitel0_popup.click_ok_button()

        # otp gee garaas avahnee
        verif_otp = string_to_list("")
        verif_otp = ''.join(map(str, verif_otp))
        # Unitel-0 uchraas end dugaar oruuldag line nemlee
        verif_otp_popup.set_verif_code(verif_otp)
        successful = verif_otp_popup.click_ok_button()

        successful.click_ok_button()





        #
        # # START entering the purchase pin ----------------------------------------------------
        # popupPage = PaymentPurchasePinInputPage(self.driver)
        # time.sleep(1)
        # popupPage.setDigitOne()
        # # time.sleep(1)
        # popupPage.setDigitTwo()
        # # time.sleep(1)
        # popupPage.setDigitThree()
        # # time.sleep(1)
        # popupPage.setDigitFour()
        # # time.sleep(2)
        # popupPage.clickSubmitButton()
        # # END entering the ppurchase pin ----------------------------------------------------

        print("sleeping\n")
        time.sleep(5)

        self.driver.quit()



