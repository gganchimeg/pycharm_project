from src.pages.contentInfoPage import ContentInfoPage
from src.pages.player import VideoPlayer


class ContentInfoPageSeries(ContentInfoPage):
    locators = {
        'season_1': ('XPATH', ""),
        'season_2': ('XPATH', ""),
        'season_3': ('XPATH', ""),
        'episode_1': ('XPATH', ""),
        'episode_2': ('XPATH', "")
    }

    def __init__(self, driver):
        super().__init__(driver)


    def click_play(self):
        super().get_button_1().click()
        return VideoPlayer(self.driver)

    def click_rent(self):
        super().get_button_1().click()

    def click_watch_later(self):
        super().get_button_2().click()

    def click_season_1(self):
        self.season_1.click()

    def click_episode_1(self):
        self.episode_1.click()





