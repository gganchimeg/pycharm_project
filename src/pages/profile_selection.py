from seleniumpagefactory.Pagefactory import PageFactory
from src.pages.home_page import HomePage

class ProfileSelectorPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'profile1': ('XPATH', "//body[1]/div[2]/div[4]/linear-list[1]/ul[1]/ng-include[1]/li[1]/div[1]/img[1]"),
        'profile2': ('XPATH', "//body[1]/div[2]/div[4]/linear-list[1]/ul[1]/ng-include[1]/li[2]/div[1]/img[1]"),
        'profile3': ('XPATH', "//body[1]/div[2]/div[4]/linear-list[1]/ul[1]/ng-include[1]/li[3]/div[1]/img[1]"),
        'profile4': ('XPATH', "//body[1]/div[2]/div[4]/linear-list[1]/ul[1]/ng-include[1]/li[4]/div[1]/img[1]"),
        'profile5': ('XPATH', "//body[1]/div[2]/div[4]/linear-list[1]/ul[1]/ng-include[1]/li[5]/div[1]/img[1]"),
        # .......?????????not visible in ui add box
        'profile_add': ('XPATH', "//span[@class='light-font-type profile-item-add-plus-text profile-add-text ng-scope']"),
        'check_profile': ('XPATH', "//div[@class='profile-image profile-image-add']"),
        'check_add_button': ('XPATH', "//div[@class='profile-image']")
    }

    def select_first_profile(self):
        self.profile1.click()
        return HomePage(self.driver)

    def select_second_profile(self):
        self.profile2.click()

    def select_third_profile(self):
        self.profile3.click()

    def select_fourth_profile(self):
        self.profile4.click()

    def select_fifth_profile(self):
        self.profile5.click()

    def select_add_profile(self):
        self.profile_add.click()

