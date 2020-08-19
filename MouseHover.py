# Mouse hover actions
# Class used - ActionChains from selenium.webdriver

from selenium.webdriver import ActionChains
from LaunchDriver import Browser

browser = Browser()
browser.get_url()
actions = ActionChains(browser.driver)

# Get the element locators by XPATH and use move_to_element() and complete the actions using perform.
element = browser.driver.find_element_by_xpath("Element XPATH")
actions.move_to_element(element).click().perform()
