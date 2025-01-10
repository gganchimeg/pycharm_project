import pytest
from src.pages.login_page import LoginPage
from utilities.readProperties import ReadConfig

@pytest.mark.first
def login_process(driver):
    baseURL = ReadConfig.getApplicationURL()
    driver.get(baseURL)
    loginPage = LoginPage(driver)

    # self.driver.maximize_window()
    driver.implicitly_wait(10)  # once

    loginPage.setEmail(ReadConfig.getUseremail())   # username fill
    loginPage.setPassword(ReadConfig.getPassword()) # password fill
    # loginPage.checkShowPassword()   # by choice
    profileSelectorPage = loginPage.clickSubmitButton()     # login page end, switching to profile selection page
    return profileSelectorPage

@pytest.mark.second
def profile_selection_process(profileSelectorPage):
    homePage = profileSelectorPage.select_first_profile()
    return homePage


    # # self.driver.maximize_window()
    # driver.implicitly_wait(10)  # once
    #
    # profileSelectionPage.
    # return homepage
    #
    # time.sleep(10)
    # self.driver.quit()
