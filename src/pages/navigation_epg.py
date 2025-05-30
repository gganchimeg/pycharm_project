from seleniumpagefactory.Pagefactory import PageFactory
from src.pages.contentInfoPage import ContentInfoPage

class GuidePage(PageFactory):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    locators = {
        'test': ('XPATH', "//body[1]/div[2]/div[1]/div[2]/div[1]/react-component[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[7]")
    }

    def test(self):
        self.test_crazyrich.click()
        return ContentInfoPage(self.driver)
