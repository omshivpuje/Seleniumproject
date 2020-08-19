from LaunchDriver import Browser
import time

browser = Browser()
browser.get_url()

browser.driver.switch_to.frame(0)
upload = browser.driver.find_element_by_id("RESULT_FileUpload-10")
