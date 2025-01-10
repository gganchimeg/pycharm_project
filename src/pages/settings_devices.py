from seleniumpagefactory.Pagefactory import PageFactory
from src.pages.navigation_box import BoxPage

class SettingsDevicesPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'test': ('XPATH', "//div[@class='menu-view ng-scope']//div[3]//div[1]")
    }

    def test(self):
        self.navigation_box.click()
        return BoxPage(self.driver)
