from seleniumpagefactory.Pagefactory import PageFactory
from src.pages.contentInfoPage import ContentInfoPage
from src.pages.player import VideoPlayer


class TvPage(PageFactory):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    locators = {
        'test': ('XPATH', "//body[1]/div[2]/div[1]/div[2]/div[1]/react-component[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[7]"),
        'HBO': ('XPATH', "//body[1]/div[2]/div[1]/div[2]/div[1]/react-component[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]")
    }

    def click_hbo(self):
        self.HBO.click()
        return VideoPlayer(self.driver)

    def test(self):
        self.test_crazyrich.click()
        return ContentInfoPage(self.driver)
