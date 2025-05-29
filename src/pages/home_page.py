import time

from seleniumpagefactory.Pagefactory import PageFactory
from src.pages.navigation_box import BoxPage
from src.pages.navigation_tv import TvPage
from src.pages.player import VideoPlayer
from src.pages.search_page import SearchPage
from src.pages.settings_profile_config import SettingsProfileConfigPage


class HomePage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'navigation_box': ('XPATH', "//div[@class='menu-view ng-scope']//div[3]//div[1]"),
        'navigation_settings': ('XPATH', "//div[@class='menu-font-size menu-item-icon-topbar menu-item-right-topbar icon-settings']"),
        # 'navigation_settings': ('XPATH', "(//div[contains(@class,'menu-font-size menu-item-icon-topbar')])[7]"),
        'navigation_tv': ('XPATH', "(//div[@class='menu-font-size menu-item-icon-topbar '])[2]"),
        'favorite_channel_25': ('XPATH', "(//div[@class='primary-font-color live-item secondary-bg-color book-font-type wrap float-left mouse-over-border cursor-pointer'])[2]"),
        'navigation_search': ('XPATH', "//div[contains(@class,'menu-font-size menu-item-icon-topbar menu-item-right-topbar icon-search')]"),
        # 'navigation_search': ('XPATH', "(//div[contains(@class,'menu-font-size menu-item-icon-topbar')])[6]"),
        'navigation_filter': ('XPATH', "//div[contains(@class,'menu-font-size menu-item-icon-topbar menu-item-right-topbar icon-filters')]"),
        # 'navigation_filter': ('XPATH', "(//div[contains(@class,'menu-font-size menu-item-icon-topbar')])[5]"),
        'navigation_guide': ('XPATH', "(//div[contains(@class,'menu-font-size menu-item-icon-topbar')])[4]"),
    }

    def click_navigation_box(self):
        self.navigation_box.click()
        return BoxPage(self.driver)

    def click_navigation_tv(self):
        self.navigation_tv.click()
        time.sleep(3)
        self.navigation_tv.click()

        print("clicking TV")
        return TvPage(self.driver)

    def click_fav_channels_25(self):
        self.favorite_channel_25.click()
        print("opening v player")
        return VideoPlayer(self.driver)

    def click_navigation_settings(self):
        self.navigation_settings.click()
        return SettingsProfileConfigPage(self.driver)

    def click_navigation_search(self):
        self.navigation_search.click()
        print("\nopening search page")
        return SearchPage(self.driver)
