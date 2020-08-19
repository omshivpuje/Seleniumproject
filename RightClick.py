from LaunchDriver import Browser
from selenium.webdriver import ActionChains
import time

browser = Browser()
browser.get_url()
actions = ActionChains(browser.driver)

button = browser.driver.find_element_by_xpath("button XPATH")

# Right Click actions using context_click
actions.context_click(button).perform()
