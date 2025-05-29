
from src.pages.payment_fourdigit_popup import PaymentPurchasePinInputPage
import time

from src.pages.payment_unitel0_phone_input_popup import PaymentUnitel0PhoneNumberInputPage
from utilities.readProperties import ReadConfig
from utilities.helper_functions import login_process, string_to_list
from utilities.helper_functions import profile_selection_process

#

class Test:
    baseURL = ReadConfig.getApplicationURL()
    # logger = LogGen.loggen() # for log

    def purchaseBOXcontent(self, setup):
        '''
        completed
        :param setup:
        :return:
        '''

        # variables for just initial testing
        # will remove it later ----------------------------------------------
        purchasePin = ReadConfig.getPurchasePin()

        # -------------------------------------------------------------------
        # self.logger.info("/* test001_LoginByEmail started */")
        self.driver = setup  # setup dotroo browseroo zarlaad driver uusgesen
        self.driver.get(self.baseURL)
        # self.driver.maximize_window()
        self.driver.implicitly_wait(10)  # once

        # --------------------- general login process ---------------------
        profileSelectorPage = login_process(self.driver)
        homePage = profile_selection_process(profileSelectorPage)
        # --------------------- end -----------------

        # ---------  old code below
        boxPage = homePage.click_navigation_box()
        contentInfoPage = boxPage.clickCrazyRich()
        time.sleep(2)
        paymentPopup = contentInfoPage.clickRentButton()
        paymentOptions = paymentPopup.clickRentButton()
        paymentOptions.click_default_payment()
        unitel0_popup = PaymentUnitel0PhoneNumberInputPage(self.driver)
        # default payment ni unitel-0 baih yum bol dugaar insert hiideg popup class init hiih hereg garch baina
        # odoohondoo shuud hardcode hiilee
        unitel0_popup.setPhoneNumber("86118529")
        verif_otp_popup = unitel0_popup.clickOkButton()

        # otp gee garaas avahnee
        verif_otp = string_to_list()
        verif_otp = ''.join(map(str, verif_otp))
        # Unitel-0 uchraas end dugaar oruuldag line nemlee
        verif_otp_popup.setVerifCode(verif_otp)
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



