from seleniumpagefactory.Pagefactory import PageFactory
from src.pages.contentInfoPage import ContentInfoPage

class BoxPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'test_crazyrich': ('XPATH', "//body[1]/div[2]/div[1]/div[2]/div[1]/react-component[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[6]")
    }

    def clickCrazyRich(self):
        self.test_crazyrich.click()
        return ContentInfoPage(self.driver)
