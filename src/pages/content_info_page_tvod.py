from seleniumpagefactory.Pagefactory import PageFactory

from src.pages.contentInfoPage import ContentInfoPage
from src.pages.payment_popup import PaymentPage
from src.pages.player import VideoPlayer


class ContentInfoPageTVOD(ContentInfoPage):

    def __init__(self, driver):
        super().__init__(driver)

    def click_play(self):
        super().get_button_1().click()

    def click_rent(self):
        super().get_button_1().click()

    def click_trailer(self):
        super().get_button_2().click()
        return VideoPlayer(self.driver)

    def click_watchLater(self):
        super().get_button_3().click()



