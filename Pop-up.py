from LaunchDriver import Browser
from selenium.webdriver.common.by import By
import time

browser = Browser()
browser.get_url()
browser.driver.find_element(By.XPATH, "//*[@id='HTML9']/div[1]/button").click()
time.sleep(2)

browser.driver.switch_to.alert.accept()  # Closes alert button using ok

browser.driver.find_element(By.XPATH, "//*[@id='HTML9']/div[1]/button").click()
browser.driver.switch_to.alert.dismiss()  # Closes alert button using close
time.sleep(2)
browser.close_browser()
