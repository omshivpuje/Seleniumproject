from LaunchDriver import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import time

browser = Browser()


def find_element_by_id(id):
    return browser.driver.find_element(By.ID, id)


browser.get_url("https://www.expedia.com/")
browser.driver.implicitly_wait(10)
find_element_by_id("tab-flight-tab-hp").click()  # Flights button
find_element_by_id("flight-type-one-way-label-hp-flight").click()
find_element_by_id("flight-origin-hp-flight").send_keys("MAA")
time.sleep(2)
find_element_by_id("flight-destination-hp-flight").send_keys("Pune")
time.sleep(2)
find_element_by_id("flight-departing-single-hp-flight").clear()
find_element_by_id("flight-departing-single-hp-flight").send_keys("07/11/2020")
browser.driver.find_element(By.XPATH, "//*[@id='flight-departing-wrapper-single-hp-flight']/div/div[2]/div[1]/button").click()
time.sleep(2)
browser.driver.find_element(By.XPATH, "//*[@id='gcw-flights-form-hp-flight']/div[8]/label/button").click()
wait = WebDriverWait(browser.driver, 10)
one_stop = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='stopFilter_stops-1']")))
one_stop.click()
time.sleep(5)
browser.close_browser()
