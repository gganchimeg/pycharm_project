import pytest
from src.pages.login_page import LoginPage
from src.pages.payment_fourdigit_popup import PaymentPurchasePinInputPage
from utilities.network_response import save_network_log
import time
import json
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities.helper_functions import login_process
from utilities.helper_functions import profile_selection_process

# for now it's just a script to test flows

class Test:
    baseURL = ReadConfig.getApplicationURL()
    # logger = LogGen.loggen() # for log

    def test(self, setup):

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
        response = login_process(self.driver)
        homePage = profile_selection_process(response)
        # --------------------- end -----------------




        # ---------  old code below
        boxPage = homePage.clickNavigationBox()
        contentInfoPage = boxPage.clickCrazyRich()
        time.sleep(2)
        paymentPopup = contentInfoPage.clickRentButton()
        paymentOptions = paymentPopup.clickRentButton()
        paymentOptions.clickDefaultPayment()

        # START entering the ppurchase pin ----------------------------------------------------
        popupPage = PaymentPurchasePinInputPage(self.driver)
        time.sleep(1)
        popupPage.setDigitOne()
        # time.sleep(1)
        popupPage.setDigitTwo()
        # time.sleep(1)
        popupPage.setDigitThree()
        # time.sleep(1)
        popupPage.setDigitFour()
        # time.sleep(2)
        popupPage.clickSubmitButton()
        # END entering the ppurchase pin ----------------------------------------------------


        time.sleep(10)
        self.driver.quit()



