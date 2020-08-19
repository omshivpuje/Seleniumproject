from LaunchDriver import Browser
from selenium.webdriver.common.by import By

browser = Browser()
browser.get_url()

currentWindow = browser.driver.window_handles
print(currentWindow)

