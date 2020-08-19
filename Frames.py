from LaunchDriver import Browser
from selenium.webdriver.common.by import By
import time

browser = Browser()
browser.get_url()

browser.driver.switch_to.frame("form1434677811")
browser.driver.find_element_by_link_text("Software Testing Tutorials").click()
