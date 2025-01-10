from seleniumpagefactory.Pagefactory import PageFactory
from src.pages.contentInfoPage import ContentInfoPage

class SearchPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'search_input': ('XPATH', "//div[@class='menu-view ng-scope']//div[3]//div[1]")
    }

    def test(self):
        self.navigation_box.click()
        return BoxPage(self.driver)
