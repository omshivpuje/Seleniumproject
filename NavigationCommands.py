from LaunchDriver import Browser
import time

def printTitle():
    time.sleep(5)
    print(browser.driver.title)

browser = Browser()
browser.get_url()
browser.get_url("https://www.facebook.com/")
browser.driver.back()
printTitle()
browser.driver.forward()
printTitle()
browser.close_browser()

# to go back - driver.back()
# to go forward - driver.forward()