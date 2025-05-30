from seleniumpagefactory.Pagefactory import PageFactory


class ContentInfoPage(PageFactory):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    locators = {
        'button_1': ('XPATH', "//div[@class='info-action-buttons ng-scope']//li[1]"),
        'button_2': ('XPATH', "//div[@class='info-action-buttons ng-scope']//li[2]"),
        'button_3': ('XPATH', "//div[@class='info-action-buttons ng-scope']//li[3]"),
        'related_content_list': ('XPATH', "")
    }

    def get_button_1(self):
        return self.button_1
    def get_button_2(self):
        return self.button_2
    def get_button_3(self):
        return self.button_3
