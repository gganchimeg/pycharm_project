import pytest
from src.pages.login_page import LoginPage
from src.pages.payment_fourdigit_popup import PaymentPurchasePinInputPage
from configparser import SafeConfigParser
import time
import json
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities.helper_functions import login_process
from utilities.helper_functions import profile_selection_process

class TestChangeEmail:
    configSet = SafeConfigParser()
    baseURL = ReadConfig.getApplicationURL()
    old_email = ReadConfig.getUseremail()
    new_email = ReadConfig.getUserNewemail()
    passw = ReadConfig.getPassword()


    def test_change_email(self, setup):
        self.configSet.set("commonInfo", "email", "ganchimegulti@gmail.com")
        # -------------------------------------------------------------------
        self.driver = setup  # setup dotroo browseroo zarlaad driver uusgesen
        self.driver.get(self.baseURL)
        # self.driver.maximize_window()
        self.driver.implicitly_wait(10)  # once
        # --------------------- general login process ---------------------
        response = login_process(self.driver, self.old_email, self.passw)
        homePage = profile_selection_process(response)
        # --------------------- end -----------------

        # ---------  old code below
        settingsPage = homePage.clickSettings
        contentInfoPage = boxPage.clickCrazyRich()
        time.sleep(2)
        paymentPopup = contentInfoPage.clickRentButton()
        paymentOptions = paymentPopup.clickRentButton()
        paymentOptions.clickDefaultPayment()

        # START entering the ppurchase pin ----------------------------------------------------
        popupPage = PaymentPurchasePinInputPage(self.driver)

        time.sleep(10)
        self.driver.quit()



