from seleniumpagefactory.Pagefactory import PageFactory
from src.pages.navigation_box import BoxPage

class HomePage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'navigation_box': ('XPATH', "//div[@class='menu-view ng-scope']//div[3]//div[1]")
    }

    def clickNavigationBox(self):
        self.navigation_box.click()
        return BoxPage(self.driver)
