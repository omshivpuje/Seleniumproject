# How many links present
# Capture all links
# Click on the links

from LaunchDriver import Browser
from selenium.webdriver.common.by import By

browser = Browser()
browser.get_url("https://www.expedia.com/")
browser.driver.implicitly_wait(10)

links = browser.driver.find_element(By.TAG_NAME, "a")

flight_sitemap = browser.driver.find_element(By.LINK_TEXT, "Flights Sitemap")
print("Link is present", flight_sitemap.text)
[print(link.text) for link in links]
print("links present in a page", len(links))
browser.close_browser()
