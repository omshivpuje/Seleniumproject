from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Chrome driver
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://www.google.com/")
print(driver.title)
print(driver.current_url)

driver.find_element_by_xpath("//*[@id='gbw']/div/div/div[1]/div[1]/a").click()
print(driver.title)
print(driver.current_url)
time.sleep(5)
# driver.close()  # Closes the current focused browser tab
driver.quit()  # Closes all the tabs and browser
