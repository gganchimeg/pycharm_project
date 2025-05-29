import time
from src.pages.payment_fourdigit_popup import PaymentPurchasePinInputPage
from utilities.readProperties import ReadConfig
from utilities.helper_functions import login_process, string_to_list
from utilities.helper_functions import profile_selection_process

class TestPurchaseVODUnitel1:
    baseURL = ReadConfig.getApplicationURL()
    # logger = LogGen.loggen() # for log
    purchase_pin = ReadConfig.getPurchasePin()
    username = ReadConfig.getPhoneNumber()
    password = ReadConfig.getPassword()

    def test_purchase_vod_unitel1(self, setup):
        '''
        completed
        :param setup:
        :return:
        '''

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

        box_page = home_page.click_navigation_box()
        content_info_page = box_page.clickCrazyRich()
        time.sleep(2)
        payment_popup = content_info_page.clickRentButton()
        payment_options = payment_popup.clickRentButton()
        payment_options.click_other_options()
        time.sleep(1)
        enter_otp_page = payment_options.click_unitel_payment()

        # entering the purchase pin ----------------------------------------------------
        l = string_to_list(self.purchase_pin)
        enter_purchase_pin_popup = PaymentPurchasePinInputPage(self.driver)
        time.sleep(1)
        enter_purchase_pin_popup.set_digit_one(l[0])
        # time.sleep(1)
        enter_purchase_pin_popup.set_digit_two(l[1])
        # time.sleep(1)
        enter_purchase_pin_popup.set_digit_three(l[2])
        # time.sleep(1)
        enter_purchase_pin_popup.set_digit_four(l[3])
        time.sleep(2)
        successful_page = enter_purchase_pin_popup.click_submit_button()

        print("done\n")
        time.sleep(5)
        successful_page.click_ok_button()
        self.driver.quit()



