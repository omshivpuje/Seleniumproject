from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://www.google.com/")
print(driver.title)
print(driver.current_url)
driver.close()