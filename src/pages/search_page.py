from seleniumpagefactory.Pagefactory import PageFactory
from src.pages.contentInfoPage import ContentInfoPage
from src.pages.contentInfoPage_svod import ContentInfoPageSVOD
from src.pages.content_info_page_series import ContentInfoPageSeries
from src.pages.content_info_page_tvod import ContentInfoPageTVOD
from src.pages.navigation_box import BoxPage


class SearchPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'search_input': ('XPATH', "//input[@id='searchInput']"),
        'result_1': ('XPATH', "(//div[contains(@class,'container-collectionItem')])[1]")
    }

    def set_search_input(self, value):
        self.search_input.set_text(value)


    def click_result_svod(self):
        self.result_1.click()
        return ContentInfoPageSVOD(self.driver)

    def click_result_tvod(self):
        self.result_1.click()
        return ContentInfoPageTVOD(self.driver)

    def click_result_series(self):
        self.result_1.click()
        return ContentInfoPageSeries(self.driver)


    # def click_first_result(self):
    #     self.result_1.click()
    #     return

    def test(self):
        self.navigation_box.click()
        return BoxPage(self.driver)
