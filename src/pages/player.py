from seleniumpagefactory.Pagefactory import PageFactory
from src.pages.contentInfoPage import ContentInfoPage

class VideoPlayer(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'video_player': ('XPATH', "//div[@id='videoPlayer']"),
        'tv_rewind_button_fullOpacity': "(//div[@class='player-icon icon-10 tv-icon medium-margin-right cursor-pointer ng-scope'])[1]",
        'tv_ff_button_fullOpacity': "(//div[@class='player-icon icon-101 tv-icon medium-margin-right cursor-pointer ng-scope'])[1]",
        'player_rewind_button_noOpacity': ('XPATH', "(//div[@class='player-icon icon-10 tv-icon medium-margin-right cursor-pointer ng-scope no-opacity'])[1]"),
        'player_ff_button_noOpacity': ('XPATH', "(//div[@class='player-icon icon-101 tv-icon medium-margin-right cursor-pointer ng-scope no-opacity'])[1]"),

        # 'rewind_button': ('XPATH', "//div[@class='tv-icon icon-10 medium-margin-right cursor-pointer ng-scope']"),
        # 'ff_button': ('XPATH', "//div[@class='tv-icon icon-101 medium-margin-left cursor-pointer ng-scope']"),

        'tv_pause_button': ("XPATH", "//div[@class='tv-icon cursor-pointer ng-scope icon-pause no-opacity']"),
        'tv_pause_button_fullOpacity': ("XPATH", "//div[@class='tv-icon cursor-pointer ng-scope icon-pause']"),
        'player_pause_button': ("XPATH", "//div[@class='player-icon tv-icon center-item-tv icon-pause no-opacity']"),
        'player_pause_button_fullOpacity': ("XPATH", "//div[@class='player-icon tv-icon center-item-tv icon-pause']"),

        'zapper_arrow_left': ('XPATH', "//span[@class='tv-icon icon-up-arrow trickplay-left-arrow']"),
        'zapper_arrow_right': ('XPATH', "//span[@class='tv-icon icon-up-arrow trickplay-right-arrow']"),
        'time_elapsed': ('XPATH', "//div[@class='light-font-type primary-font-color unselectable-text banner-time-text-left ng-binding banner-time-text-live']"),
        'progress_bar': ('XPATH', "//progress-bar[@id='progress-bar']"),
        'progress_bar_outer': ('XPATH', "//progress-bar[@id='progress-bar']//div[@class='outer-progress-bar overflow-hidden unfocus-bg-color']"),
        'progress_bar_inner': ('XPATH', "//div[@class='inner-progres-bar focus-bg-color bottom-border-radius-middle-straight']"),
        'progress_bar_inner_secondary': ('XPATH', "//div[@class='inner-progres-bar focus-bg-color bottom-border-radius-middle-straight']"),
        'pending_time': ('XPATH', "//div[@class='light-font-type primary-font-color unselectable-text ng-binding banner-time-text-live banner-end-time-live']"),
        'full_screen': ('XPATH', "//div[@class='tv-icon icon-maximize delete-element-tv cursor-pointer full-screen-button-live']"),
        'close_button': ('XPATH', "//div[@class='tv-icon icon-exit exit-button cursor-pointer']"),
        'zapper_bottom_channel': ('XPATH', "//div[@class='zapper-upper-container zapper-bottom-container delete-element-pc ng-scope']"),
        'zapper_upper_channel': ('XPATH', "//div[@class='zapper-upper-container delete-element-pc ng-scope']"),
        'nowAndNext_current_icon_startOver': "//div[@class='tv-icon icon-restart white medium-small-font']",
        'nowAndNext_current': "(//li[@class='nowAndNext-item hovered-element nowAndNext-selected-margin now-and-next-bg tertiary-bg-color float-left unselectable-text cursor-pointer ng-scope'])[1]",
        'nowAndNext_future': "(//li[@class='nowAndNext-item hovered-element nowAndNext-selected-margin now-and-next-bg tertiary-bg-color float-left unselectable-text cursor-pointer ng-scope'])[2]",
        'icon_cc': "//i[@class='tv-icon icon-language']",
        'icon_settings': "//i[@class='tv-icon icon-settings']",
        'icon_heart_empty': "//i[@class='tv-icon icon-heart-empty']",
        'icon_heart_fill': "//i[@class='tv-icon icon-heart-fill']",
        'icon_startOver': "//i[@class='tv-icon icon-restart']",
        'icon_volume': "//i[@class='tv-icon icon-volume']",
        'icon_volume_slider': "//input[@type='range']"

    }
    def test(self):
        self.test1.click()
        return ContentInfoPage(self.driver)


# subtitle: "https://edge-strm-04.univision.mn/bpk-token/1aa@2jkhqpy4j3a4rnf5p4uvkuoa5ans0b2d2v32zsca/dash/TwilightSagaNewMoon_1745824093-textstream_eng=1000-1680000.dash"