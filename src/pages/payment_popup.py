from cProfile import Profile
from src.pages.profile_selection import ProfileSelectorPage
from src.pages.registration_page import BaseRegistrationPage
from src.pages.forgot_password_page import ForgotPasswordPage
from seleniumpagefactory.Pagefactory import PageFactory
from utilities.readProperties import ReadConfig

class PaymentPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
    'rent_button': ('XPATH', "//div[@class='button-hovered rent-movie-button medium-font cursor-pointer medium-font-type ng-binding']"),
    'close_button': ('XPATH', "//div[@class='tv-icon icon-exit close-payment-option-hover close-payment-button cursor-pointer delete-element-tv ng-scope']")
    }

    def clickRentButton(self):
        self.submit_button.click()
        return ProfileSelectorPage(self.driver)

    def clickCloseButton(self):
        self.register_button.click()
        return BaseRegistrationPage(self.driver)