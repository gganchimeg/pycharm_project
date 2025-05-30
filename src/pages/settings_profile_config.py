from seleniumpagefactory.Pagefactory import PageFactory
from src.pages.credential_related.settings_acc_config import SettingsAccConfigPage


class SettingsProfileConfigPage(PageFactory):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    locators = {
        'account_conf': ('XPATH', "/html[1]/body[1]/div[2]/div[1]/div[3]/div[1]/react-component[1]/div[1]/div[1]/div[2]/div[1]/span[1]")
    }

    def click_acc_conf(self):
        self.account_conf.click()
        return SettingsAccConfigPage(self.driver)
