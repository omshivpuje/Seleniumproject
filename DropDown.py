# 1. Select one option
# 2. capture options from drop down
# 3. count how many option present

from LaunchDriver import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

browser = Browser()
browser.get_url()

browser.driver.find_element(By.CLASS_NAME, "uitk-button-text").click()
drp = Select(browser.driver.find_element(By.ID, "flight"))

# Below are the three approaches to select an option in drop down box
# drp.select_by_index(2)
# drp.select_by_value("Radio-2")
# drp.select_by_visible_text("Morning")

# Count number of options
print(len(drp.options))

# Capture all the options and print
all_options = drp.options
[print(val.text) for val in all_options]

drp.select_by_index(2)
