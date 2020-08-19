from LaunchDriver import Browser
from selenium.webdriver import ActionChains
import time

browser = Browser()
browser.get_url()
actions = ActionChains(browser.driver)

double_click = browser.driver.find_element_by_xpath("//*[@id='HTML10']/div[1]/button")
actions.double_click(double_click).perform()
time.sleep(5)
text_field = browser.driver.find_element_by_xpath("//*[@id='field2']").text
print(text_field)
browser.close_browser()
