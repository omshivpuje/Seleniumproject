from LaunchDriver import Browser
from selenium.webdriver.common.keys import Keys

import time

browser = Browser()
browser.get_url()
ele = browser.driver.find_element_by_name("q")
print(ele.is_displayed())
print(ele.is_enabled())
ele.send_keys("Welcome")
browser.driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[3]/center/input[1]").click()
browser.close_browser()

# ele.is_displayed()  # To check the status if the element is displayed or not
# ele.is_enabled()    # To check the status if the element is enabled or not
# ele.is_selected()   # To check the status of the element if it is selected or not (Used at radio buttons)
