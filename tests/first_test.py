from idlelib.iomenu import encoding
from idlelib.run import interruptable

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions import action_builder

# failed with class
# class First:
#   def __init__(self, dc):
#     self.desired_cap = dc
#     self.desired_capabilities = UiAutomator2Options().load_capabilities(self.desired_cap)
#     self.driver = webdriver.Remote(command_executor="http://127.0.0.1:4723", options=self.desired_capabilities)
#     self.email_insert = ""
#     self.pass_insert = ""
#     self.login_button = ""
#   def collect_elms(self):
#     self.email_insert = self.driver.find_element(by=AppiumBy.XPATH,
#                                                  value='//android.widget.EditText[@resource-id="net.giitd.looktv.main:id/etUser"]')
#     self.pass_insert = self.driver.find_element(by=AppiumBy.XPATH,
#                                                 value='//android.widget.EditText[@resource-id="net.giitd.looktv.main:id/etPassword"]')
#     self.login_button = self.driver.find_element(by=AppiumBy.XPATH,
#                                                  value='//android.widget.Button[@resource-id="net.giitd.looktv.main:id/btLogin"]')
#
#   def login(self):
#     self.email_insert.click()
#     self.email_insert.send_keys("89988218")
#
#     self.pass_insert.click()
#     self.pass_insert.send_keys("G.Ganchimeg")
#
#     self.login_button.click()
#   def profile_selector(self):
#     pass
#
#   def play_from_con_watch(self):
#     pass


if __name__ == '__main__':
  desired_cap = dict(
    platformName="Android",
    deviceName="1a7617340601",
    app="C:/Users/ganchimeg.g/Documents/univision-apk/252.apk",
    appPackage="",
    appActivity="",
    #   net.giitd.looktv.main/com.omtv.activities.SplashActivity
    noreset= "true"
  )

  desired_capabilities = UiAutomator2Options().load_capabilities(desired_cap)
  driver = webdriver.Remote(command_executor="http://127.0.0.1:4723", options=desired_capabilities)
  driver.implicitly_wait(5)
  email_insert = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="net.giitd.looktv.main:id/etUser"]')
  pass_insert = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="net.giitd.looktv.main:id/etPassword"]')
  login_button = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@resource-id="net.giitd.looktv.main:id/btLogin"]')

  # login section
  driver.implicitly_wait(5)
  email_insert.click()
  email_insert.send_keys("89988218")
  pass_insert.click()
  pass_insert.send_keys("G.Ganchimeg")
  login_button.click()

  # profile selection

  profile1 = driver.find_element(by=AppiumBy.ID, value='net.giitd.looktv.main:id/image_profile')
  profile1.click()

  # play live tv
  menu_live = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@content-desc="TV"]')
  menu_live.click()




  # scrolling
  # tv_scroll = driver.find_element(by=AppiumBy.XPATH, value='// androidx.viewpager.widget.ViewPager[ @ resource - id = "net.giitd.looktv.main:id/view_pager"]')
  # tv_scroll.
  screen_size = driver.get_window_size()
  start_x = screen_size['width']/2
  start_y = screen_size['height']*0.8
  end_y = screen_size['height']*0.1

  actions = ActionChains(driver)
  pointer = PointerInput(interaction.POINTER_TOUCH, 'finger')
  action_builder = ActionBuilder(driver, mouse=pointer)

  action_builder.pointer_action.move_to_location(x=int(start_x), y=int(start_y))
  action_builder.pointer_action.pointer_down()
  action_builder.pointer_action.move_to_location(x=int(start_x), y=int(end_y))
  action_builder.pointer_action.pointer_up()

  actions.w3c_actions = action_builder
  actions.perform()








  central_tv = driver.find_element(by=AppiumBy.XPATH, value='(//android.widget.LinearLayout[@resource-id="net.giitd.looktv.main:id/channel_root"])[3]/android.widget.LinearLayout')
  central_tv.click()

  #
  # print(driver.get_)
  # tv8 = driver.find_element(AppiumBy.XPATH, value='(//android.widget.LinearLayout[@resource-id="net.giitd.looktv.main:id/channel_root"])[4]')
  # tv8.click()
  # driver.implicitly_wait(3)
  page_source = driver.page_source
  with open('page_source.xml', 'w', encoding='utf-8') as f:
    f.write(page_source)
  with open('page_source.html', 'w', encoding='utf-8') as f:
    f.write(page_source)
  driver.wait_activity()












