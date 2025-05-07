from seleniumpagefactory.Pagefactory import PageFactory
from src.pages.navigation_box import BoxPage
from src.pages.settings_profile_config import SettingsProfileConfigPage


class HomePage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'navigation_box': ('XPATH', "//div[@class='menu-view ng-scope']//div[3]//div[1]"),
        'navigation_settings': ('XPATH', "//div[@class='menu-font-size menu-item-icon-topbar menu-item-right-topbar icon-settings']")
    }

    def click_navigation_box(self):
        self.navigation_box.click()
        return BoxPage(self.driver)

    def click_navigation_settings(self):
        self.navigation_settings.click()
        return SettingsProfileConfigPage(self.driver)
