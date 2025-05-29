
from seleniumpagefactory.Pagefactory import PageFactory
from utilities.readProperties import ReadConfig

class PaymentOptionsPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
    'default_payment': ('XPATH', "//div[@class='payment-options-text payment-options-text-default ']"),
    'close_button': ('XPATH', "//div[@class='payment-options-modal']//div[@class='tv-icon icon-exit close-payment-option-hover close-payment-button cursor-pointer delete-element-tv ng-scope']"),
    'other_options': ('XPATH', "//div[@class='dropdown-wrap']"),
    'payment_option_unitel': ('XPATH', "//img[@src='https://www.unitel.mn/looktv/icons/unitel.png']"),
    'payment_option_qpay': ('XPATH', "//body[1]/div[5]/div[2]/div[1]/div[1]/div[4]/linear-list[1]/ul[1]/ng-include[1]/div[2]/div[1]/react-component[1]/div[1]/div[3]/div[1]/div[1]"),
        'payment_option_qpay_khan': ('XPATH', "//body//div[@id='paymentoptions-dialog']//div[@class='dropdown-wrap']//div[@class='dropdown-wrap']//div[3]//div[2]"),
        'payment_option_qpay_mbank': ('XPATH', "//body[1]/div[5]/div[2]/div[1]/div[1]/div[4]/linear-list[1]/ul[1]/ng-include[1]/div[2]/div[1]/react-component[1]/div[1]/div[3]/div[10]/div[1]"),
    'payment_option_bankcard': ('XPATH', "//body[1]/div[5]/div[2]/div[1]/div[1]/div[4]/linear-list[1]/ul[1]/ng-include[1]/div[2]/div[1]/react-component[1]/div[1]/div[4]/div[1]/div[1]"),
        'payment_option_bankcard_saved': ('XPATH', "//span[@class='payment-options-subtitle']"),
        'payment_option_bankcard_add': ('XPATH', "//div[contains(text(),'Add card')]"),
    'payment_option_coupon': ('XPATH', "//div[contains(text(),'Coupon')]")
    }

    def click_default_payment(self):
        self.default_payment.click()

    def click_other_options(self):
        self.other_options.click()

    def click_close_button(self):
        self.close_button.click()

    def click_unitel_payment(self):
        self.payment_option_unitel.click()

    def click_bankcard_payment(self):
        self.payment_option_bankcard.click()

