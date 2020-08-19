from LaunchDriver import Browser
from selenium.webdriver import ActionChains
import time

browser = Browser()
browser.get_url()
actions = ActionChains(browser.driver)

source = browser.driver.find_element_by_xpath("//*[@id='draggable']")
target = browser.driver.find_element_by_xpath("//*[@id='droppable']")
actions.drag_and_drop(source, target).perform()
time.sleep(5)
print(target.text)
browser.close_browser()
