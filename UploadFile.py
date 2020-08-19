from LaunchDriver import Browser
import time

browser = Browser()
browser.get_url()

browser.driver.switch_to.frame(0)
upload = browser.driver.find_element_by_id("RESULT_FileUpload-10")
browser.driver.execute_script("arguments[0].scrollIntoView()", upload)

upload.send_keys("E://Images//PicsArt//IMG_20160408_005217.jpg")
time.sleep(10)
print(browser.driver.find_element_by_partial_link_text(".jpg").text)
browser.close_browser()
