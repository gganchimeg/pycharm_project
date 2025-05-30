from seleniumpagefactory.Pagefactory import PageFactory


class SixDigitOTPInput(PageFactory):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    locators = {
        'digit_one': ('XPATH', "//input[@id='pin0']"),
        'digit_two': ('XPATH', "//input[@id='pin1']"),
        'digit_three': ('XPATH', "//input[@id='pin2']"),
        'digit_four': ('XPATH', "//input[@id='pin3']"),
        'digit_five': ('XPATH', "//input[@id='pin4']"),
        'digit_six': ('XPATH', "//input[@id='pin5']"),
        'submit_button': ('XPATH', "//div[@class='medium-font-type ng-binding']"),
        'back_button': ('XPATH', "//div[@class='icon-up-arrow back-arrow arrow-back-button cursor-pointer ng-scope']"),
        'send_again_link': ('XPATH', "//span[@class='highlightMessage medium-font-type cursor-pointer ng-binding ng-scope']")
    }

    def set_digit_one(self, digitone):
        self.digit_one.set_text(digitone)

    def set_digit_two(self, digittwo):
        self.digit_two.set_text(digittwo)

    def set_digit_three(self, digitthree):
        self.digit_three.set_text(digitthree)

    def set_digit_four(self, digitfour):
        self.digit_four.set_text(digitfour)

    def set_digit_five(self, digitfive):
        self.digit_five.set_text(digitfive)

    def set_digit_six(self, digitsix):
        self.digit_six.set_text(digitsix)

    def click_send_again_link(self):
        self.send_again_link.click()

    def click_submit_button(self):
        pass
    
    def click_back_button(self):
        pass

