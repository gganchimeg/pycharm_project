from seleniumpagefactory.Pagefactory import PageFactory
from src.pages.contentInfoPage import ContentInfoPage

class BoxPage(PageFactory):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    locators = {
        'test_crazyrich': ('XPATH', "//body[1]/div[2]/div[1]/div[2]/div[1]/react-component[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[6]"),
        'test1': ("XPATH", "//body//div[@id='mosaic']//div[contains(@class,'main-list-with-info')]//div//div//div[1]//div[2]//div[2]//div[5]")
    }

    def click_crazyrich(self):
        self.test1.click()
        return ContentInfoPage(self.driver)
